#!/usr/bin/env python3
"""Warhammer Age of Sigmar 公式アプリの dump.json から Spearhead 情報を抽出する。

Spearhead は固定編成の小規模ゲームモード (40k の Combat Patrol 相当)。
各 Spearhead は publication (name が "Spearhead: ..." / spearheadName 持ち) として
表現され、以下が紐づく:
  - 収録ユニット: warscroll_publication 経由の isSpearhead なウォースクロール
  - バトル特性 / レジメントアビリティ / 強化:
    ability_group_publication 経由の ability_group
    (battleTraits / regimentAbilities / spearheadEnhancements)

使い方:
  # 一覧表示 (ファクション名 + Spearhead 名)
  python3 extract_spearheads.py --dump dump.json --list

  # 全 Spearhead を spearheads/ 配下に出力 (既定)
  python3 extract_spearheads.py --dump dump.json

  # ファクションで絞り込み
  python3 extract_spearheads.py --dump dump.json --faction "Skaven"
  python3 extract_spearheads.py --dump dump.json --faction-id fc32e7a5-...

  # 出力先を変更
  python3 extract_spearheads.py --dump dump.json --outdir sp

出力: spearheads/<ファクション名>/<Spearhead 名>.md (1 Spearhead 1 ファイル)。
dump.json は英語のみ。入手方法は fetch-dump スキルを参照。
"""
import json, re, argparse, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_lib"))
from aos_translations import Translations  # noqa: E402


def provenance(dump_path, data_version=None):
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
    return re.sub(r"\s*\n\s*", " ", t or "").strip()


def cell(t):
    return clean(t).replace("|", "\\|") or "-"


def safe_name(n):
    return re.sub(r"[/\\:*?\"<>|]", "-", n).strip()


# ---- ウォースクロール描画 (extract-warscrolls と同等の表記) ----

def build_indexes(d):
    def by(t, key):
        r = {}
        for x in d.get(t, []):
            r.setdefault(x[key], []).append(x)
        return r
    return {
        "weapons_by_ws": by("warscroll_weapon", "warscrollId"),
        "abilities_by_ws": by("warscroll_ability", "warscrollId"),
        "addchar_by_ws": by("warscroll_additional_characteristic", "warscrollId"),
        "wwa_by_weapon": by("warscroll_weapon_weapon_ability", "warscrollWeaponId"),
        "wakw_by_ability": by("warscroll_ability_keyword", "warscrollAbilityId"),
        "weapon_ability": {x["id"]: x for x in d.get("weapon_ability", [])},
        "keyword": {x["id"]: x["name"] for x in d.get("keyword", [])},
    }


def render_ability_lines(a, kw_names=None, indent="  ", tr=None, unit=None, spearhead=False):
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
    if a.get("points"):
        tags.append("%spt" % a["points"])
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


def render_warscroll(w, ix, out, tr):
    wid = w["id"]
    unit = w["name"]
    out.append("\n### %s\n" % tr.unit(w))

    info = []
    if w.get("modelCount") is not None:
        info.append("**モデル数:** %s" % w["modelCount"])
    if w.get("baseSize"):
        info.append("**ベースサイズ:** %s" % w["baseSize"])
    if info:
        out.append(" / ".join(info) + "\n")

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
                                            spearhead=True))

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


# ---- Spearhead の列挙と描画 ----

GROUP_SECTION = [
    ("battleTraits", "戦闘特性"),
    ("regimentAbilities", "連隊アビリティ"),
    ("spearheadEnhancements", "強化"),
]


def collect_spearheads(d):
    """Spearhead publication ごとに {pub, faction, warscrolls, groups} を返す。"""
    pubs = {p["id"]: p for p in d["publication"]}
    fk = {f["id"]: f["name"] for f in d["faction_keyword"]}
    ws = {w["id"]: w for w in d["warscroll"]}
    wp = {}
    for x in d["warscroll_publication"]:
        wp.setdefault(x["publicationId"], []).append(x["warscrollId"])
    gp = {}
    for x in d["ability_group_publication"]:
        gp.setdefault(x["publicationId"], []).append(x["abilityGroupId"])
    ag = {g["id"]: g for g in d["ability_group"]}

    sp_ids = [p["id"] for p in d["publication"]
              if p.get("spearheadName") or p.get("publicationType") == "spearhead"
              or p["name"].startswith("Spearhead:")]
    result = []
    for pid in sp_ids:
        p = pubs[pid]
        units = [ws[i] for i in wp.get(pid, [])
                 if i in ws and ws[i].get("isSpearhead")]
        groups = [ag[i] for i in gp.get(pid, []) if i in ag]
        if not units and not groups:
            continue  # Spearhead Doubles 等のルールのみの出版物は対象外
        faction = fk.get(p.get("factionKeywordId"))
        if not faction:
            for g in groups:
                if g.get("factionId") in fk:
                    faction = fk[g["factionId"]]
                    break
        name = re.sub(r"^Spearhead( Battlepack)?:\s*", "", p["name"])
        # アーミーに属さないシーズン Battlepack 等は共通ルールとして分類する
        result.append({"pub": p, "name": name, "faction": faction or "共通ルール",
                       "units": units, "groups": groups})
    result.sort(key=lambda x: (x["faction"], x["name"]))
    return result


def build_one(dump_path, sp, d, ix, data_version, ab_by_group):
    out = []
    tr = Translations(dump_path, sp["faction"])
    out.append("# Spearhead: %s（%s）\n" % (tr.group(sp["name"]), tr.faction(sp["faction"])))
    out.append(provenance(dump_path, data_version))

    units = sorted(sp["units"], key=lambda w: (w["name"], w.get("subname") or ""))
    if units:
        out.append("\n## 編成\n")
        for w in units:
            mc = w.get("modelCount")
            out.append("- %s%s" % (tr.unit(w), "（%s体）" % mc if mc else ""))
        out.append("\n## ユニット詳細\n")
        for w in units:
            render_warscroll(w, ix, out, tr)

    order = {t: i for i, (t, _) in enumerate(GROUP_SECTION)}
    titles = dict(GROUP_SECTION)
    for g in sorted(sp["groups"],
                    key=lambda g: order.get(g.get("abilityGroupType"), 9)):
        title = titles.get(g.get("abilityGroupType"))
        out.append("\n## %s\n" % ("%s（%s）" % (title, g["name"]) if title
                                  else g["name"]))
        if g.get("restrictionText"):
            out.append("%s\n" % clean(tr.group_text(g["name"], g["restrictionText"])))
        for a in ab_by_group.get(g["id"], []):
            out.extend(render_ability_lines(a, tr=tr, spearhead=True))
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="dump.json のパス")
    ap.add_argument("--faction", help="ファクション名で絞り込み (部分一致)")
    ap.add_argument("--faction-id", help="faction id で絞り込み")
    ap.add_argument("--outdir", default="spearheads",
                    help="出力先ディレクトリ (既定 spearheads)")
    ap.add_argument("--list", action="store_true",
                    help="一覧表示 (ファクション名 + Spearhead 名)")
    args = ap.parse_args()

    raw = json.load(open(args.dump, encoding="utf-8"))
    d = raw["data"]
    data_version = raw.get("metadata", {}).get("data_version")
    sps = collect_spearheads(d)

    if args.faction_id:
        fk = {f["id"]: f["name"] for f in d["faction_keyword"]}
        nm = fk.get(args.faction_id)
        sps = [s for s in sps if s["faction"] == nm]
    elif args.faction:
        q = args.faction.lower()
        sps = [s for s in sps if q in s["faction"].lower()]
    if not sps:
        print("該当する Spearhead がありません。--list で確認してください。",
              file=sys.stderr)
        sys.exit(1)

    if args.list:
        for s in sps:
            print("%-30s %s (%d units)" % (s["faction"], s["name"], len(s["units"])))
        return

    ix = build_indexes(d)
    ab_by_group = {}
    for a in d["ability"]:
        ab_by_group.setdefault(a.get("abilityGroupId"), []).append(a)
    for v in ab_by_group.values():
        v.sort(key=lambda x: x.get("displayOrder") or 0)

    for s in sps:
        md = build_one(args.dump, s, d, ix, data_version, ab_by_group)
        fdir = os.path.join(args.outdir, safe_name(s["faction"]))
        os.makedirs(fdir, exist_ok=True)
        out_path = os.path.join(fdir, "%s.md" % safe_name(s["name"]))
        open(out_path, "w", encoding="utf-8").write(md)
        print("written %s" % out_path)
    print("done: %d spearheads" % len(sps))


if __name__ == "__main__":
    main()
