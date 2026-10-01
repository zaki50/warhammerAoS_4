#!/usr/bin/env python3
"""Warhammer Age of Sigmar 公式アプリの dump.json からファクションルールを抽出する。

指定ファクション (faction_keyword) の以下を Markdown 化する:
  - バトル特性 (ability_group.abilityGroupType == battleTraits)
  - バトルフォーメーション (battle_formation + battle_formation_rule)
  - 英雄特性 (heroicTraits) / アーティファクト・オブ・パワー (artefactsOfPower)
  - その他の強化 (otherEnhancements)
  - ロア (lore + lore_ability: 呪文・祈祷・顕現)

使い方:
  # ファクションルールを持つファクション一覧
  python3 extract_faction_rules.py --dump dump.json --list

  # ファクション名(部分一致)で抽出。
  # 既定で faction_rules/<ファクション>_faction_rules.md に保存される
  python3 extract_faction_rules.py --dump dump.json --faction "Skaven"

  # id 直接指定 / 全ファクション一括
  python3 extract_faction_rules.py --dump dump.json --faction-id fc32e7a5-...
  python3 extract_faction_rules.py --dump dump.json --all

dump.json は英語のみ。入手方法は fetch-dump スキルを参照。
"""
import json, re, argparse, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_lib"))
from aos_translations import Translations  # noqa: E402

GROUP_SECTIONS = [
    ("battleTraits", "戦闘特性"),
    ("heroicTraits", "英雄特性"),
    ("artefactsOfPower", "神器"),
    ("otherEnhancements", "その他の強化"),
]


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


def slugify(en):
    return re.sub(r"[^a-z0-9]+", "_", (en or "").lower()).strip("_")


def render_ability(a, indent="  ", tr=None):
    """ability / battle_formation_rule / lore_ability を共通の箇条書きで描画。"""
    lines = []
    head = "- **%s**" % (tr.ability(a.get("name")) if tr else a.get("name"))
    tx = (tr.text(a.get("name")) if tr else None) or {}
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
    return lines


def spearhead_pub_ids(d):
    """Spearhead 収録の publication id 集合。"""
    return {p["id"] for p in d["publication"]
            if p.get("spearheadName") or p.get("publicationType") == "spearhead"}


def group_pubs(d):
    """ability_group id -> [publication id...]"""
    r = {}
    for x in d["ability_group_publication"]:
        r.setdefault(x["abilityGroupId"], []).append(x["publicationId"])
    return r


def faction_groups(d, fid):
    """factionId が一致する ability_group を type 別に返す。
    Spearhead 収録グループは除外する (extract-spearheads の担当)。"""
    sp = spearhead_pub_ids(d)
    gp = group_pubs(d)
    r = {}
    for g in d["ability_group"]:
        if g.get("factionId") == fid and g.get("abilityGroupType"):
            pubs = gp.get(g["id"], [])
            if pubs and all(p in sp for p in pubs):
                continue
            r.setdefault(g["abilityGroupType"], []).append(g)
    return r


def build(dump_path, fid, raw):
    d = raw["data"]
    data_version = raw.get("metadata", {}).get("data_version")
    fk = {f["id"]: f for f in d["faction_keyword"]}
    fname = fk.get(fid, {}).get("name") or fid
    tr = Translations(dump_path, fname)

    ab_by_group = {}
    for a in d["ability"]:
        ab_by_group.setdefault(a.get("abilityGroupId"), []).append(a)
    for v in ab_by_group.values():
        v.sort(key=lambda x: x.get("displayOrder") or 0)
    bfr_by_bf = {}
    for r in d["battle_formation_rule"]:
        bfr_by_bf.setdefault(r["battleFormationId"], []).append(r)
    la_by_lore = {}
    for a in d["lore_ability"]:
        la_by_lore.setdefault(a["loreId"], []).append(a)
    groups = faction_groups(d, fid)
    gp = group_pubs(d)
    pubs = {p["id"]: p for p in d["publication"]}

    def pub_suffix(gid):
        names = [pubs[p]["name"] for p in gp.get(gid, []) if p in pubs]
        return "（出典: %s）" % ", ".join(names) if names else ""

    out = []
    out.append("# %s ファクションルール\n" % tr.faction(fname))
    out.append(provenance(dump_path, data_version))
    n_items = 0

    def emit_groups(gtype, title):
        nonlocal n_items
        gs = groups.get(gtype, [])
        if not gs:
            return
        out.append("\n## %s\n" % title)
        for g in sorted(gs, key=lambda x: x["name"]):
            legends = " (Legends)" if g.get("isLegends") else ""
            out.append("\n### %s%s%s\n" % (tr.group(g["name"]), legends, pub_suffix(g["id"])))
            if g.get("restrictionText"):
                out.append("%s\n" % clean(tr.group_text(g["name"], g["restrictionText"])))
            for a in ab_by_group.get(g["id"], []):
                out.extend(render_ability(a, tr=tr))
                n_items += 1

    emit_groups("battleTraits", "戦闘特性")

    bfs = [b for b in d["battle_formation"] if b.get("factionId") == fid]
    if bfs:
        out.append("\n## 戦闘陣形\n")
        for b in sorted(bfs, key=lambda x: x["name"]):
            tags = []
            if b.get("points"):
                tags.append("%spt" % b["points"])
            if b.get("isLegends"):
                tags.append("Legends")
            out.append("\n### %s%s\n" % (tr.group(b["name"]),
                                         "（%s）" % ", ".join(tags) if tags else ""))
            for r in bfr_by_bf.get(b["id"], []):
                out.extend(render_ability(r, tr=tr))
                n_items += 1

    for gtype, title in GROUP_SECTIONS[1:]:
        emit_groups(gtype, title)

    lores = [l for l in d["lore"] if l.get("factionId") == fid]
    if lores:
        out.append("\n## 伝承（呪文・奇蹟・顕現）\n")
        for l in sorted(lores, key=lambda x: x["name"]):
            pts = "（%spt）" % l["points"] if l.get("points") else ""
            out.append("\n### %s%s\n" % (tr.group(l["name"]), pts))
            if l.get("restrictionText"):
                out.append("%s\n" % clean(tr.group_text(l["name"], l["restrictionText"])))
            for a in sorted(la_by_lore.get(l["id"], []),
                            key=lambda x: (x.get("castingValue") or 0, x["name"])):
                out.extend(render_ability(a, tr=tr))
                n_items += 1

    return "\n".join(out) + "\n", n_items, fname


def factions_with_rules(d):
    """ファクションルールを持つ faction id -> (formations, groups, lores) 件数。"""
    r = {}
    def bump(fid, i):
        if fid:
            r.setdefault(fid, [0, 0, 0])[i] += 1
    for b in d["battle_formation"]:
        bump(b.get("factionId"), 0)
    for g in d["ability_group"]:
        if g.get("abilityGroupType") in dict(GROUP_SECTIONS):
            bump(g.get("factionId"), 1)
    for l in d["lore"]:
        bump(l.get("factionId"), 2)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="dump.json のパス")
    ap.add_argument("--faction", help="ファクション名 (部分一致)")
    ap.add_argument("--faction-id", help="faction id を直接指定")
    ap.add_argument("--all", action="store_true", help="全ファクション一括生成")
    ap.add_argument("-o", "--output",
                    help="出力ファイル名。ディレクトリを含まない場合は --outdir 配下に保存")
    ap.add_argument("--outdir", default="faction_rules",
                    help="出力先ディレクトリ (既定 faction_rules)")
    ap.add_argument("--stdout", action="store_true",
                    help="ファイルに保存せず標準出力へ (--all とは併用不可)")
    ap.add_argument("--list", action="store_true",
                    help="ファクションルールを持つファクション一覧を表示")
    args = ap.parse_args()

    raw = json.load(open(args.dump, encoding="utf-8"))
    d = raw["data"]
    fk = {f["id"]: f for f in d["faction_keyword"]}
    withrules = factions_with_rules(d)

    if args.list:
        rows = [(fk[fid]["name"], fid, c) for fid, c in withrules.items() if fid in fk]
        print("%-45s %4s %4s %4s" % ("faction", "編成", "特性", "ロア"))
        for nm, fid, (nf, ng, nl) in sorted(rows):
            print("%-45s %4d %4d %4d  %s" % (nm, nf, ng, nl, fid))
        return

    if args.all:
        if args.stdout:
            ap.error("--all と --stdout は併用できません")
        os.makedirs(args.outdir, exist_ok=True)
        written = 0
        for fid in sorted(withrules, key=lambda i: fk.get(i, {}).get("name", "")):
            if fid not in fk:
                continue
            md, n, fname = build(args.dump, fid, raw)
            if n == 0:
                continue
            out_path = os.path.join(args.outdir, "%s_faction_rules.md" % slugify(fname))
            open(out_path, "w", encoding="utf-8").write(md)
            print("written %d rules for '%s' -> %s" % (n, fname, out_path))
            written += 1
        print("done: %d factions" % written)
        return

    fid = args.faction_id
    if not fid:
        if not args.faction:
            ap.error("--faction か --faction-id か --all のいずれかが必要です")
        q = args.faction.lower()
        cands = [(f["name"], f["id"]) for f in d["faction_keyword"]
                 if q in f["name"].lower()]
        exact = [(nm, i) for nm, i in cands if nm.lower() == q]
        if len(exact) == 1:
            fid = exact[0][1]
        elif not cands:
            print("該当ファクションなし: %s" % args.faction, file=sys.stderr)
            sys.exit(1)
        elif len(cands) > 1:
            print("複数候補に一致。--faction-id で指定してください:", file=sys.stderr)
            for nm, i in sorted(cands):
                print("  %-45s %s" % (nm, i), file=sys.stderr)
            sys.exit(1)
        else:
            fid = cands[0][1]

    md, n, fname = build(args.dump, fid, raw)
    if n == 0:
        print("'%s' にはファクションルールがありません。--list で確認してください。"
              % fname, file=sys.stderr)
        sys.exit(1)

    if args.stdout:
        sys.stdout.write(md)
        return
    if args.output:
        out_path = args.output
        if os.path.dirname(out_path) == "":
            out_path = os.path.join(args.outdir, out_path)
    else:
        out_path = os.path.join(args.outdir, "%s_faction_rules.md" % slugify(fname))
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(md)
    print("written %d rules for '%s' -> %s" % (n, fname, out_path))


if __name__ == "__main__":
    main()
