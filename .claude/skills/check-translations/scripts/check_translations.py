#!/usr/bin/env python3
"""official_translations/ と own_translations/ の訳のうち、md 生成で参照されなくなったものを列挙する。

判定は生成規則を複製せず、extract-warscrolls / extract-faction-rules / extract-spearheads の
build 関数で全 md をメモリ上に生成し (ファイルは書かない)、そのとき実際に照合されたキー
(aos_translations.LOOKUPS) と各訳ファイルのキーを突き合わせる。生成側に新しい訳の当て先を
足しても、この判定は自動的に追随する。

報告する項目:
  - 該当ファクションが無いファイル (ファイル名のスラッグに一致するファクションが dump.json に無い)
  - 名前が dump.json に無いキー (削除・改名)
  - 名前はあるが、そのファクションの md では引かれないキー (他ファクションへの移動など)
  - 公式訳に同じキーがあるため使われない独自訳

使い方:
  python3 check_translations.py --dump dump.json
  python3 check_translations.py --dump dump.json --fail   # 見つかったら終了コード 1
"""
import argparse, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(SKILLS, "_lib"))
import aos_translations as T  # noqa: E402


def load_module(skill, filename):
    path = os.path.join(SKILLS, skill, "scripts", filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def generate_all(dump_path, raw):
    """全 md をメモリ上で生成して、照合されたキーを T.LOOKUPS に貯める。"""
    d = raw["data"]
    ws_mod = load_module("extract-warscrolls", "extract_warscrolls.py")
    fr_mod = load_module("extract-faction-rules", "extract_faction_rules.py")
    sp_mod = load_module("extract-spearheads", "extract_spearheads.py")

    with_ws = {x["factionKeywordId"] for x in d["warscroll_faction_keyword"]}
    for f in d["faction_keyword"]:
        if f["id"] in with_ws:
            ws_mod.build(dump_path, f["id"], raw)
    for fid in fr_mod.factions_with_rules(d):
        fr_mod.build(dump_path, fid, raw)

    ix = sp_mod.build_indexes(d)
    ab_by_group = {}
    for a in d["ability"]:
        ab_by_group.setdefault(a.get("abilityGroupId"), []).append(a)
    for sp in sp_mod.collect_spearheads(d):
        sp_mod.build_one(dump_path, sp, d, ix, raw.get("metadata", {}).get("data_version"),
                         ab_by_group)


def known_names(d):
    """セクションごとの、dump.json に存在する英語名の集合。"""
    abilities = set()
    for t in ("warscroll_ability", "ability", "battle_formation_rule", "lore_ability",
              "terrain_ability"):
        abilities |= {x["name"] for x in d.get(t, []) if x.get("name")}
    keywords = {k["name"] for k in d.get("keyword", [])}
    for w in d["warscroll"]:
        keywords |= {k.strip() for k in (w.get("referenceKeywords") or "").split(",") if k.strip()}
    groups = {x["name"] for t in ("ability_group", "battle_formation", "lore") for x in d.get(t, [])}
    groups |= {re.sub(r"^Spearhead( Battlepack)?:\s*", "", p["name"]) for p in d["publication"]}
    return {
        "unit_names": {w["name"] for w in d["warscroll"]},
        "weapon_names": {x["name"] for x in d["warscroll_weapon"]},
        "ability_names": abilities,
        "ability_texts": abilities,
        "keyword_names": keywords,
        "weapon_ability_names": {x["name"] for x in d.get("weapon_ability", [])},
        "group_names": groups,
        "group_texts": groups,
        "wargear_option_texts": {w["name"] for w in d["warscroll"]},
    }


def check(dump_path, raw):
    d = raw["data"]
    base = os.path.dirname(os.path.abspath(dump_path))
    generate_all(dump_path, raw)
    looked = {(s, sec, k) for b, s, sec, k in T.LOOKUPS if b == base}
    shadowed = {(s, sec, k) for b, s, sec, k in T.SHADOWED if b == base}
    faction_slugs = {T.slugify(f["name"]) for f in d["faction_keyword"]}
    names = known_names(d)
    unit_set = names["unit_names"]

    tables = {}
    for layer in T.LAYERS:
        ldir = os.path.join(base, layer)
        if not os.path.isdir(ldir):
            continue
        for fn in sorted(os.listdir(ldir)):
            if fn.endswith(".json") and not fn.startswith("_"):
                tables[(layer, fn[:-5])] = json.load(open(os.path.join(ldir, fn), encoding="utf-8"))

    problems = []
    for (layer, slug), t in sorted(tables.items()):
        rel = "%s/%s.json" % (layer, slug)
        if slug not in faction_slugs:
            problems.append((rel, None, None, "ファイル名に一致するファクションが dump.json に無い"))
            continue
        official = tables.get(("official_translations", slug), {})
        for sec in T.SECTIONS:
            for key in sorted(k for k in (t.get(sec) or {}) if not k.startswith("_")):
                if (slug, sec, key) in looked:
                    if layer == "own_translations" and (official.get(sec) or {}).get(key):
                        problems.append((rel, sec, key, "公式訳に同じキーがあるので使われない"))
                    continue
                unit, _, name = key.rpartition("|")
                if unit == "Spearhead" or unit.startswith("Spearhead|"):
                    unit = unit[len("Spearhead"):].lstrip("|")
                if (slug, sec, key) in shadowed:
                    why = "出てくる箇所がすべて、より具体的なキー（「ユニット|%s」や「Spearhead|…」）で上書きされていて使われない" % key
                elif unit and unit not in unit_set:
                    why = "ユニット「%s」が dump.json に無い（削除・改名）" % unit
                elif name not in names[sec]:
                    why = "dump.json にこの名前が無い（削除・改名）"
                elif unit:
                    why = "このファクションの md で、ユニット「%s」にこの名前が出ない" % unit
                else:
                    why = "このファクションの md に出ない（他ファクションへの移動など）"
                problems.append((rel, sec, key, why))
    return problems, len(tables)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="dump.json のパス (訳フォルダはこれと同じディレクトリ)")
    ap.add_argument("--fail", action="store_true", help="未使用の訳があれば終了コード 1")
    args = ap.parse_args()

    raw = json.load(open(args.dump, encoding="utf-8"))
    problems, nfiles = check(args.dump, raw)
    if not problems:
        print("未使用の訳はありません（訳ファイル %d 件）" % nfiles)
        return
    print("未使用の訳: %d 件（訳ファイル %d 件中）" % (len(problems), nfiles))
    cur = None
    for rel, sec, key, why in problems:
        if rel != cur:
            print("\n%s" % rel)
            cur = rel
        if key is None:
            print("  - %s" % why)
        else:
            print("  - [%s] %s: %s" % (sec, key, why))
    if args.fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
