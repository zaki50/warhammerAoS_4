#!/usr/bin/env python3
"""Warhammer Age of Sigmar 公式アプリの dump.json からウォースクロールを抽出する。

抽出単位は **faction_keyword**（ファクション: Stormcast Eternals / Skaven 等。
グランドアライアンスやアーミー・オブ・リナウンも同テーブルに含まれる）。
ウォースクロールは warscroll_faction_keyword でファクションに M:N で紐づく。

使い方:
  # ファクション一覧を表示 (ウォースクロールを持つもののみ、件数付き)
  python3 extract_warscrolls.py --dump dump.json --list

  # ファクション名（部分一致・大文字小文字無視）で抽出。
  # 既定で warscrolls/<ファクション>_warscrolls.md に保存される
  python3 extract_warscrolls.py --dump dump.json --faction "Ogor Mawtribes"

  # faction id を直接指定
  python3 extract_warscrolls.py --dump dump.json --faction-id 08135df6-...

  # 全ファクションを一括生成 (warscrolls/ 配下。Grand Alliance は除外)
  python3 extract_warscrolls.py --dump dump.json --all

  # Spearhead 版ウォースクロールも含める (既定は除外)
  python3 extract_warscrolls.py --dump dump.json --faction "Skaven" --include-spearhead

dump.json は英語のみ（localisations 無し）。入手方法は fetch-dump スキルを参照。
"""
import json, re, argparse, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_lib"))
from aos_translations import Translations, slugify  # noqa: E402


def provenance(dump_path, data_version=None):
    """出典文字列を生成。<dump>.meta.json (fetch-dump 生成) があれば
    アプリ版・抽出日時も含める。"""
    meta = {}
    mpath = (dump_path[:-5] + ".meta.json") if dump_path.endswith(".json") \
        else (dump_path + ".meta.json")
    if os.path.exists(mpath):
        try:
            meta = json.load(open(mpath, encoding="utf-8"))
        except Exception:
            meta = {}
    pkg = meta.get("package") or "com.gamesworkshop.aos4"
    parts = ["出典: Warhammer Age of Sigmar 公式アプリ (%s)" % pkg]
    if meta.get("versionName"):
        vc = " build %s" % meta["versionCode"] if meta.get("versionCode") else ""
        parts.append("アプリ版 %s%s" % (meta["versionName"], vc))
    dv = data_version if data_version is not None else meta.get("dataVersion")
    if dv is not None:
        parts.append("dump.json data_version %s" % dv)
    if meta.get("extractedAt"):
        parts.append("抽出 %s" % str(meta["extractedAt"])[:10])
    return " / ".join(parts) + "\n"


def clean(t):
    """複数行テキストを 1 行に平坦化する（箇条書きの • はそのまま残る）。"""
    return re.sub(r"\s*\n\s*", " ", t or "").strip()


def cell(t):
    return clean(t).replace("|", "\\|") or "-"


def build_indexes(d):
    """warscroll 描画に必要なインデックス群を構築する。"""
    def by(t, key):
        r = {}
        for x in d.get(t, []):
            r.setdefault(x[key], []).append(x)
        return r
    ix = {
        "weapons_by_ws": by("warscroll_weapon", "warscrollId"),
        "abilities_by_ws": by("warscroll_ability", "warscrollId"),
        "addchar_by_ws": by("warscroll_additional_characteristic", "warscrollId"),
        "regopt_by_ws": by("warscroll_regiment_option", "warscrollId"),
        "terrainab_by_ws": by("warscroll_terrain_ability", "warscrollId"),
        "wwa_by_weapon": by("warscroll_weapon_weapon_ability", "warscrollWeaponId"),
        "wakw_by_ability": by("warscroll_ability_keyword", "warscrollAbilityId"),
        "weapon_ability": {x["id"]: x for x in d.get("weapon_ability", [])},
        "terrain_ability": {x["id"]: x for x in d.get("terrain_ability", [])},
        "keyword": {x["id"]: x["name"] for x in d.get("keyword", [])},
    }
    return ix


def render_ability_lines(a, kw_names=None, indent="  ", tr=None, unit=None, spearhead=False):
    """warscroll_ability / lore_ability 相当の 1 アビリティを箇条書きで描画。
    本文の訳 (ability_texts) があれば、タイミング・宣言・効果・キーワードをそれで置き換える。"""
    lines = []
    name = tr.ability(a.get("name"), unit) if tr else a.get("name")
    tx = (tr.text(a.get("name"), unit, spearhead) if tr else None) or {}
    head = "- **%s**" % name
    tags = []
    if tx.get("timing") or a.get("phaseDetails"):
        tags.append(tx.get("timing") or a["phaseDetails"])
    if a.get("castingValue"):
        tags.append("詠唱/詠誦値 %s" % a["castingValue"])
    if a.get("cpCost"):
        tags.append("CP %s" % a["cpCost"])
    if a.get("cost"):
        tags.append("コスト %s" % a["cost"])
    if tags:
        head += "（%s）" % " / ".join(tags)
    if tx.get("keywords"):
        head += " ［%s］" % tx["keywords"]
    elif kw_names:
        head += " ［%s］" % ", ".join(kw_names)
    lines.append(head)
    used_by = tx.get("used_by") or a.get("usedBy")
    declare = tx.get("declare") or a.get("declare")
    effect = tx.get("effect") or a.get("effect")
    if used_by:
        lines.append("%s- 使用者: %s" % (indent, clean(used_by)))
    if declare:
        lines.append("%s- 宣言: %s" % (indent, clean(declare)))
    if effect:
        lines.append("%s- 効果: %s" % (indent, clean(effect)))
    # 宣言/効果を持たないパッシブ等は補足テキストで代替
    if not declare and not effect:
        for k in ("additionalRulesText", "subsectionRulesText"):
            if a.get(k):
                lines.append("%s- %s" % (indent, clean(a[k])))
                break
    keys_name = ["%s|%s" % (unit, a.get("name")), a.get("name")] if unit else [a.get("name")]
    if tr:
        notes = tr.fix_lines(lines, "ability_texts", tr.text_keys(a.get("name"), unit, spearhead), indent)
        notes += tr.fix_lines(lines, "ability_names", keys_name, indent)
        lines += notes
    return lines


def render_warscroll(w, ix, out, tr, show_points=True):
    """1 ウォースクロールを Markdown で out(list) に追記する。"""
    wid = w["id"]
    unit = w["name"]
    name = tr.unit(w)
    flags = []
    if w.get("isLegends"):
        flags.append("Legends")
    if w.get("isSpearhead"):
        flags.append("Spearhead")
    out.append("\n---\n\n## %s%s\n" % (name, " (%s)" % ", ".join(flags) if flags else ""))

    info = []
    if show_points and w.get("points") is not None:
        info.append("**ポイント:** %spt" % w["points"])
    if w.get("modelCount") is not None:
        info.append("**モデル数:** %s" % w["modelCount"])
    if w.get("baseSize"):
        info.append("**ベースサイズ:** %s" % w["baseSize"])
    if info:
        out.append(" / ".join(info) + "\n")
    if w.get("cannotBeReinforced"):
        out.append("**増援不可**\n")

    # ステータス (Move/Health/Save/Control + Ward)
    ward = w.get("wardSave")
    cols = ["移動力", "体力", "防御力", "確保力"] + (["加護"] if ward else [])
    vals = [w.get("move"), w.get("health"), w.get("save"), w.get("control")] \
        + ([ward] if ward else [])
    out.append("**ステータス:**\n")
    out.append("| " + " | ".join(cols) + " |")
    out.append("|" + "---|" * len(cols))
    out.append("| " + " | ".join(str(v) if v is not None else "-" for v in vals) + " |")
    for ac in ix["addchar_by_ws"].get(wid, []):
        out.append("\n**%s:** %s" % (ac["name"], ac["value"]))

    # 武器 (射撃 → 近接)。battleDamaged は戦傷時プロファイル
    def wab_names(weapon):
        rows = sorted(ix["wwa_by_weapon"].get(weapon["id"], []),
                      key=lambda x: x.get("displayOrder") or 0)
        return [tr.weapon_ability(ix["weapon_ability"][r["weaponAbilityId"]]["name"])
                for r in rows if r["weaponAbilityId"] in ix["weapon_ability"]]

    weapons = ix["weapons_by_ws"].get(wid, [])
    ranged = [x for x in weapons if x.get("type") == "ranged"]
    melee = [x for x in weapons if x.get("type") != "ranged"]
    wstart = len(out)
    if ranged:
        out.append("\n**遠隔武器:**\n")
        out.append("| 武器 | 射程 | 回数 | ヒット | ウーンズ | 貫通 | ダメージ | アビリティ |")
        out.append("|---|---|---|---|---|---|---|---|")
        for x in ranged:
            nm = tr.weapon(x["name"], unit) + ("（戦傷時）" if x.get("battleDamaged") else "")
            out.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
                cell(nm), cell(x.get("range")), cell(x.get("attacks")),
                cell(x.get("hit")), cell(x.get("wound")), cell(x.get("rend")),
                cell(x.get("damage")), cell(", ".join(wab_names(x)) or "-")))
    if melee:
        out.append("\n**近接武器:**\n")
        out.append("| 武器 | 回数 | ヒット | ウーンズ | 貫通 | ダメージ | アビリティ |")
        out.append("|---|---|---|---|---|---|---|")
        for x in melee:
            nm = tr.weapon(x["name"], unit) + ("（戦傷時）" if x.get("battleDamaged") else "")
            out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
                cell(nm), cell(x.get("attacks")), cell(x.get("hit")),
                cell(x.get("wound")), cell(x.get("rend")),
                cell(x.get("damage")), cell(", ".join(wab_names(x)) or "-")))

    wnotes, wlines = [], out[wstart:]
    for name in dict.fromkeys(x["name"] for x in ranged + melee):
        for l in tr.fix_lines(wlines, "weapon_names", ["%s|%s" % (unit, name), name]):
            if l not in wnotes:
                wnotes.append(l)
    out[wstart:] = wlines
    if wnotes:
        out.append("")
        out.extend(wnotes)

    abilities = ix["abilities_by_ws"].get(wid, [])
    if abilities:
        out.append("\n**アビリティ:**\n")
        for a in abilities:
            kws = [ix["keyword"].get(r["keywordId"])
                   for r in ix["wakw_by_ability"].get(a["id"], [])]
            out.extend(render_ability_lines(a, [k for k in kws if k], tr=tr, unit=unit,
                                            spearhead=bool(w.get("isSpearhead"))))

    # 地形ウォースクロールの地形ルール
    tas = sorted(ix["terrainab_by_ws"].get(wid, []),
                 key=lambda x: x.get("displayOrder") or 0)
    if tas:
        out.append("\n**地形ルール:**\n")
        for r in tas:
            ta = ix["terrain_ability"].get(r["terrainAbilityId"])
            if ta:
                tx = tr.text(ta["name"], unit) or {}
                out.append("- **%s:** %s" % (tr.ability(ta["name"], unit),
                                             clean(tx.get("effect") or ta.get("rules"))))

    # 編成 (レジメントに加えられるユニット)
    ropts = [r for r in sorted(ix["regopt_by_ws"].get(wid, []),
                               key=lambda x: x.get("displayOrder") or 0)
             if not r.get("hiddenFromReference")]
    if ropts:
        out.append("\n**連隊オプション:**\n")
        for r in ropts:
            out.append("- %s" % clean(r.get("optionText") or ""))

    if w.get("wargearOptionsText"):
        out.append("\n**装備オプション:** %s" % clean(tr.wargear_text(unit, w["wargearOptionsText"])))
        wline = out[-1:]
        wgnotes = tr.fix_lines(wline, "wargear_option_texts", [unit])
        out[-1:] = wline
        if wgnotes:
            out.append("")
            out.extend(wgnotes)
    if w.get("referenceKeywords"):
        out.append("\n**キーワード:** %s" % tr.keywords(w["referenceKeywords"], unit))
        knotes, kline = [], out[-1:]
        for k in [k.strip() for k in w["referenceKeywords"].split(",") if k.strip()]:
            knotes += tr.fix_lines(kline, "keyword_names", ["%s|%s" % (unit, k), k])
        out[-1:] = kline
        if knotes:
            out.append("")
            out.extend(knotes)
    if w.get("notes"):
        out.append("\n**ノート:** %s" % clean(w["notes"]))


def faction_warscrolls(d, faction_id, include_spearhead=False):
    ws = {w["id"]: w for w in d["warscroll"]}
    ids = [x["warscrollId"] for x in d["warscroll_faction_keyword"]
           if x["factionKeywordId"] == faction_id]
    rows = [ws[i] for i in ids if i in ws]
    total = len(rows)
    if not include_spearhead:
        rows = [w for w in rows if not w.get("isSpearhead")]
    rows.sort(key=lambda w: (w["name"], w.get("subname") or ""))
    return rows, total


def build(dump_path, faction_id, raw, include_spearhead=False):
    d = raw["data"]
    data_version = raw.get("metadata", {}).get("data_version")
    fk = {f["id"]: f for f in d["faction_keyword"]}
    fname = fk.get(faction_id, {}).get("name") or faction_id
    rows, total = faction_warscrolls(d, faction_id, include_spearhead)
    ix = build_indexes(d)
    tr = Translations(dump_path, fname)

    out = []
    out.append("# %s ウォースクロール一覧\n" % tr.faction(fname))
    out.append(provenance(dump_path, data_version))
    note = "" if include_spearhead else \
        "（Spearhead 版 %d 件は除外。--include-spearhead で含められる）" % (total - len(rows))
    out.append("全%d ウォースクロール%s\n" % (len(rows), note))
    for w in rows:
        render_warscroll(w, ix, out, tr)
    return "\n".join(out) + "\n", len(rows), fname


def list_factions(d):
    cnt = {}
    for x in d["warscroll_faction_keyword"]:
        cnt[x["factionKeywordId"]] = cnt.get(x["factionKeywordId"], 0) + 1
    rows = [(f["name"], f["id"], cnt.get(f["id"], 0)) for f in d["faction_keyword"]
            if cnt.get(f["id"], 0) > 0]
    for nm, fid, n in sorted(rows):
        print("%-45s %4d  %s" % (nm, n, fid))


def resolve_faction(d, ap, args):
    if args.faction_id:
        return args.faction_id
    if not args.faction:
        ap.error("--faction か --faction-id か --all のいずれかが必要です")
    q = args.faction.lower()
    cands = [(f["name"], f["id"]) for f in d["faction_keyword"]
             if q in f["name"].lower()]
    exact = [(nm, fid) for nm, fid in cands if nm.lower() == q]
    if len(exact) == 1:
        return exact[0][1]
    if not cands:
        print("該当ファクションなし: %s" % args.faction, file=sys.stderr)
        sys.exit(1)
    if len(cands) > 1:
        print("複数候補に一致。--faction-id で指定してください:", file=sys.stderr)
        for nm, fid in sorted(cands):
            print("  %-45s %s" % (nm, fid), file=sys.stderr)
        sys.exit(1)
    return cands[0][1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="dump.json のパス")
    ap.add_argument("--faction", help="ファクション名 (部分一致)")
    ap.add_argument("--faction-id", help="faction id を直接指定")
    ap.add_argument("--all", action="store_true",
                    help="全ファクションを一括生成 (Grand Alliance は除外)")
    ap.add_argument("--include-spearhead", action="store_true",
                    help="Spearhead 版ウォースクロールも含める")
    ap.add_argument("-o", "--output",
                    help="出力ファイル名。ディレクトリを含まない場合は --outdir 配下に保存")
    ap.add_argument("--outdir", default="warscrolls",
                    help="出力先ディレクトリ (既定 warscrolls)")
    ap.add_argument("--stdout", action="store_true",
                    help="ファイルに保存せず標準出力へ (--all とは併用不可)")
    ap.add_argument("--list", action="store_true",
                    help="ファクション一覧を表示 (ウォースクロールを持つもののみ)")
    args = ap.parse_args()

    raw = json.load(open(args.dump, encoding="utf-8"))
    d = raw["data"]

    if args.list:
        list_factions(d)
        return

    if args.all:
        if args.stdout:
            ap.error("--all と --stdout は併用できません")
        cnt = {}
        for x in d["warscroll_faction_keyword"]:
            cnt[x["factionKeywordId"]] = cnt.get(x["factionKeywordId"], 0) + 1
        os.makedirs(args.outdir, exist_ok=True)
        written = 0
        for f in sorted(d["faction_keyword"], key=lambda x: x["name"]):
            if cnt.get(f["id"], 0) == 0 or f["name"].startswith("Grand Alliance"):
                continue
            md, n, fname = build(args.dump, f["id"], raw, args.include_spearhead)
            if n == 0:
                continue
            out_path = os.path.join(args.outdir, "%s_warscrolls.md" % slugify(fname))
            open(out_path, "w", encoding="utf-8").write(md)
            print("written %d warscrolls for '%s' -> %s" % (n, fname, out_path))
            written += 1
        print("done: %d factions" % written)
        return

    fid = resolve_faction(d, ap, args)
    md, n, fname = build(args.dump, fid, raw, args.include_spearhead)

    if args.stdout:
        sys.stdout.write(md)
        return
    if args.output:
        out_path = args.output
        if os.path.dirname(out_path) == "":
            out_path = os.path.join(args.outdir, out_path)
    else:
        out_path = os.path.join(args.outdir, "%s_warscrolls.md" % slugify(fname))
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(md)
    print("written %d warscrolls for '%s' -> %s" % (n, fname, out_path))


if __name__ == "__main__":
    main()
