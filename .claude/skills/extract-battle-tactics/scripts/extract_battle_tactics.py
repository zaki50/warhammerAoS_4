#!/usr/bin/env python3
"""Warhammer Age of Sigmar 公式アプリの dump.json からバトルタクティックカードを抽出する。

AoS 4版に策略(ストラタジェム)は無く、マッチプレイ(General's Handbook)の
バトルタクティックカードが最も近い汎用の戦術要素。各カードはカード効果
(rulesText)と 3 種のバトルタクティック (Strike / Affray / Domination) を持つ。

使い方:
  # 既定: ./battle_tactics.md に保存
  python3 extract_battle_tactics.py --dump dump.json

  # 出力先を指定 / 標準出力へ
  python3 extract_battle_tactics.py --dump dump.json -o out/battle_tactics.md
  python3 extract_battle_tactics.py --dump dump.json --stdout

dump.json は英語のみ。入手方法は fetch-dump スキルを参照。
"""
import json, re, argparse, sys, os

TYPE_LABEL = {"strike": "Strike", "affray": "Affray", "domination": "Domination"}


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


def build(dump_path, raw):
    d = raw["data"]
    data_version = raw.get("metadata", {}).get("data_version")
    packs = {b["id"]: b for b in d.get("battlepack", [])}
    tactics_by_card = {}
    for t in d["battle_tactic"]:
        tactics_by_card.setdefault(t.get("battleTacticCardId"), []).append(t)

    cards_by_pack = {}
    for c in d["battle_tactic_card"]:
        cards_by_pack.setdefault(c.get("battlepackId"), []).append(c)

    out = []
    out.append("# バトルタクティックカード一覧\n")
    out.append(provenance(dump_path, data_version))
    n = 0
    order = {"strike": 0, "affray": 1, "domination": 2}
    for pid in sorted(cards_by_pack,
                      key=lambda i: packs.get(i, {}).get("name") or ""):
        pname = packs.get(pid, {}).get("name")
        if pname:
            out.append("\n## %s\n" % pname)
        for c in sorted(cards_by_pack[pid], key=lambda x: x["name"]):
            out.append("\n### %s\n" % c["name"])
            if c.get("rulesText"):
                out.append("**カード効果:** %s\n" % clean(c["rulesText"]))
            for t in sorted(tactics_by_card.get(c["id"], []),
                            key=lambda x: order.get(x.get("battleTacticType"), 9)):
                label = TYPE_LABEL.get(t.get("battleTacticType"),
                                       t.get("battleTacticType") or "")
                vp = "、%sVP" % t["victoryPoints"] if t.get("victoryPoints") else ""
                out.append("- **%s**（%s%s）: %s" % (
                    t["name"], label, vp, clean(t.get("rulesText"))))
            n += 1
    # カードに紐づかないバトルタクティックがあれば漏らさず出力する
    orphans = tactics_by_card.get(None, [])
    if orphans:
        out.append("\n## その他のバトルタクティック\n")
        for t in sorted(orphans, key=lambda x: x["name"]):
            out.append("- **%s**: %s" % (t["name"], clean(t.get("rulesText"))))
    return "\n".join(out) + "\n", n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="dump.json のパス")
    ap.add_argument("-o", "--output", default="battle_tactics.md",
                    help="出力ファイル (既定 ./battle_tactics.md)")
    ap.add_argument("--stdout", action="store_true",
                    help="ファイルに保存せず標準出力へ")
    args = ap.parse_args()

    raw = json.load(open(args.dump, encoding="utf-8"))
    md, n = build(args.dump, raw)
    if args.stdout:
        sys.stdout.write(md)
        return
    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    open(args.output, "w", encoding="utf-8").write(md)
    print("written %d battle tactic cards -> %s" % (n, args.output))


if __name__ == "__main__":
    main()
