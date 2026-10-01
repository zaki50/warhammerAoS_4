#!/usr/bin/env python3
"""translation_notes.json（公式訳の既知の誤訳・誤植）を、訳ファイルと dump.json に照合する。

各注は、日本語の場所（official_translations/<faction>.json の tr_section / tr_key / tr_field）と、
英語の場所（dump.json の table / id / en_field）を持つ。照合では

  - 訳ファイルのその場所に ja（誤訳箇所）が残っているか
  - dump.json のそのレコードに en が残っているか

を見て status を決める（HTML と ** の除去・NFKC・空白の畳み込み・引用符の統一のうえで部分一致）。

使い方:
  python3 translation_notes.py check --dump dump.json            # 状態が変わる項目を表示（変化ありなら終了コード 3）
  python3 translation_notes.py check --dump dump.json --update   # 結果を translation_notes.json に書き戻す
  python3 translation_notes.py list
"""
import argparse, json, os, re, sys, unicodedata

STATUSES = ("open", "resolved", "en_changed", "missing")


def norm(s):
    s = re.sub(r"<[^>]+>", "", s or "").replace("**", "")
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", "", s)


def notes_path(dump_path):
    return os.path.join(os.path.dirname(os.path.abspath(dump_path)), "translation_notes.json")


def ja_text(base, n):
    """注が指す日本語の文字列。見つからなければ None。"""
    p = os.path.join(base, "official_translations", "%s.json" % n["faction"])
    if not os.path.exists(p):
        return None
    v = (json.load(open(p, encoding="utf-8")).get(n["tr_section"]) or {}).get(n["tr_key"])
    if isinstance(v, dict):
        v = v.get(n.get("tr_field"))
    return v if isinstance(v, str) else None


def en_text(d, n):
    for x in d.get(n["table"], []):
        if x.get("id") == n["id"]:
            v = x.get(n["en_field"])
            return v if isinstance(v, str) else ""
    return None


def judge(base, d, n):
    ja, en = ja_text(base, n), en_text(d, n)
    if ja is None or en is None:
        return "missing", []
    warns = []
    if n.get("en") and norm(n["en"]) not in norm(en):
        status = "en_changed"
    elif n.get("ja") and norm(n["ja"]) not in norm(ja):
        status = "resolved"
    else:
        status = "open"
    fix = n.get("fix_ja")
    if status == "open" and isinstance(fix, dict):
        for k in fix:
            if norm(k) not in norm(ja):
                warns.append("fix_ja のキー「%s」が本文に無い" % k)
    return status, warns


def cmd_check(args):
    raw = json.load(open(args.dump, encoding="utf-8"))
    d, dv = raw["data"], raw.get("metadata", {}).get("data_version")
    path = notes_path(args.dump)
    doc = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(args.dump))
    changed = 0
    for n in doc["notes"]:
        status, warns = judge(base, d, n)
        for w in warns:
            print("警告: %s (%s): %s" % (n["name"], n["tr_key"], w))
        if status != n.get("status"):
            changed += 1
            print("%s: %s → %s" % (n["name"], n.get("status"), status))
            if args.update:
                n["status"] = status
                if status == "resolved":
                    n["resolved_in"] = dv
                else:
                    n.pop("resolved_in", None)
    counts = {s: sum(1 for n in doc["notes"] if (n.get("status") if args.update else judge(base, d, n)[0]) == s)
              for s in STATUSES}
    print("訳注 %d 件: %s" % (len(doc["notes"]), ", ".join("%s %d" % (k, v) for k, v in counts.items() if v)))
    if args.update:
        doc["checked_data_version"] = dv
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
    if changed and not args.update:
        sys.exit(3)


def cmd_list(args):
    doc = json.load(open(notes_path(args.dump), encoding="utf-8"))
    for n in doc["notes"]:
        print("[%s] %s / %s %s: %s" % (n.get("status"), n["faction"], n["tr_section"], n["tr_key"], n["note"]))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--dump", default="dump.json")
    c.add_argument("--update", action="store_true")
    l = sub.add_parser("list")
    l.add_argument("--dump", default="dump.json")
    args = ap.parse_args()
    (cmd_check if args.cmd == "check" else cmd_list)(args)


if __name__ == "__main__":
    main()
