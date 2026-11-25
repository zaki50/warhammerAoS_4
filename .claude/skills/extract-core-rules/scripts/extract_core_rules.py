#!/usr/bin/env python3
"""公式アプリの dump.json からコアルールと上級ルールを 1 本の Markdown (core_rules.md) に書き出す。

章 (rule_section) → 節 (rule_container) → 本文 (rule_container_component) をアプリの並び順のまま出力する。
英語は dump.json、日本語は official_translations/core_rules.json (公式 PDF からの書き写し) から引く。
訳があるものは日本語を本文に、英語を折りたたみ (> [!quote]- EN) に、訳が無いものは英語をそのまま出す。

訳は英語のハッシュ (en_hash) と組で持つ。アプリの改訂で英語が変わった訳は使わず (英語で出し)、
--check で「古くなった訳」として列挙する。

使い方:
  python3 extract_core_rules.py --dump dump.json               # ./core_rules.md
  python3 extract_core_rules.py --dump dump.json --stdout
  python3 extract_core_rules.py --dump dump.json --check        # 訳の抜け・古い訳・未使用の訳
  python3 extract_core_rules.py --dump dump.json --lookups x.json   # 訳の当て先 (英語つき) を書き出す
"""
import argparse, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "_lib"))
import aos_translations as T  # noqa: E402

TR_NAME = "core_rules"
# (publication 名の条件, md の見出し)。上級ルールは最新の General's Handbook のもの (displayOrder・名前の降順) を使う
CORE = "Core Rules"
ADVANCED = re.compile(r"^General's Handbook (\d{4}-\d{2}): Advanced Rules$")
ABILITY_FIELDS = (("timing", "phaseDetails", "タイミング"), ("used_by", "usedBy", "使用者"),
                  ("declare", "declare", "宣言"), ("effect", "effect", "効果"))


def en_hash(s):
    return hashlib.sha1(re.sub(r"\s+", " ", s or "").strip().encode()).hexdigest()[:8]


def provenance(dump_path, data_version):
    meta = {}
    mpath = dump_path[:-5] + ".meta.json" if dump_path.endswith(".json") else dump_path + ".meta.json"
    if os.path.exists(mpath):
        meta = json.load(open(mpath, encoding="utf-8"))
    parts = ["出典: Warhammer Age of Sigmar 公式アプリ (%s)" % (meta.get("package") or "com.gamesworkshop.aos4")]
    if meta.get("versionName"):
        parts.append("アプリ版 %s%s" % (meta["versionName"],
                                     " build %s" % meta["versionCode"] if meta.get("versionCode") else ""))
    if data_version is not None:
        parts.append("dump.json data_version %s" % data_version)
    if meta.get("extractedAt"):
        parts.append("抽出 %s" % str(meta["extractedAt"])[:10])
    return " / ".join(parts)


class Core:
    def __init__(self, dump_path, raw):
        self.dump_path, self.raw = dump_path, raw
        self.base = os.path.dirname(os.path.abspath(dump_path))
        d = self.d = raw["data"]
        p = os.path.join(self.base, "official_translations", TR_NAME + ".json")
        self.tr = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
        self.notes = [n for n in T._load_notes(self.base) if n.get("faction") == TR_NAME]
        self.by_parent, self.containers, self.components, self.bullets = {}, {}, {}, {}
        for s in d["rule_section"]:
            self.by_parent.setdefault(s.get("parentId") or s.get("publicationId"), []).append(s)
        for c in d["rule_container"]:
            self.containers.setdefault(c["ruleSectionId"], []).append(c)
        for x in d["rule_container_component"]:
            self.components.setdefault(x["ruleContainerId"], []).append(x)
        for b in d["bullet_point"]:
            self.bullets.setdefault(b["ruleContainerComponentId"], []).append(b)
        for t in (self.by_parent, self.containers, self.components, self.bullets):
            for v in t.values():
                v.sort(key=lambda x: (x.get("displayOrder") or 0, x["id"]))
        self.abilities = {a["id"]: a for a in d["ability"]}
        kw = {k["id"]: k["name"] for k in d["keyword"]}
        self.ab_kw = {}
        for x in d["ability_keyword"]:
            self.ab_kw.setdefault(x["abilityId"], []).append(kw.get(x["keywordId"], "?"))
        self.used, self.stale, self.missing, self.lookups = set(), [], [], []
        self.hits = self.total = 0

    # --- 訳 ---
    def publications(self):
        core = [p for p in self.d["publication"] if p["name"] == CORE]
        adv = sorted((p for p in self.d["publication"] if ADVANCED.match(p["name"])),
                     key=lambda p: p["name"], reverse=True)[:1]
        return core + adv

    def name(self, sec, en, at):
        """見出し・図の小見出しなど、英語の文字列そのものをキーに引く。"""
        en = (en or "").strip()
        if not en:
            return None
        self.lookups.append(dict(section=sec, key=en, at=at, en=en))
        self.total += 1
        v = (self.tr.get(sec) or {}).get(en)
        self.used.add((sec, en))
        if v:
            self.hits += 1
            return v
        self.missing.append((sec, en, at))
        return None

    def text(self, key, en, at, table, field):
        """本文。texts[<id>] = {"at","en_hash","ja"}。英語が変わっていたら使わない。"""
        if not (en or "").strip():
            return None
        self.lookups.append(dict(section="texts", key=key, at=at, en=en, en_hash=en_hash(en)))
        self.total += 1
        self.used.add(("texts", key))
        v = (self.tr.get("texts") or {}).get(key)
        if not v:
            self.missing.append(("texts", key, at))
            return None
        if v.get("en_hash") != en_hash(en):
            self.stale.append(("texts", key, at))
            return None
        self.hits += 1
        return self.fix(v["ja"], "texts", key, "ja")

    def ability(self, a, at):
        en = {k: a.get(f) for k, f, _ in ABILITY_FIELDS}
        en.update(name=a["name"], lore=a.get("lore"), keywords=", ".join(self.ab_kw.get(a["id"], [])) or None)
        h = en_hash("\n".join("%s=%s" % (k, en[k] or "") for k in sorted(en) if k != "lore"))
        self.lookups.append(dict(section="abilities", key=a["id"], at=at, en=en, en_hash=h))
        self.total += 1
        self.used.add(("abilities", a["id"]))
        v = (self.tr.get("abilities") or {}).get(a["id"])
        if not v:
            self.missing.append(("abilities", a["id"], at))
            v = {}
        elif v.get("en_hash") != h:
            self.stale.append(("abilities", a["id"], at))
            v = {}
        else:
            self.hits += 1
            v = {k: self.fix(x, "abilities", a["id"], k) if isinstance(x, str) else x for k, x in v.items()}
        return en, v

    def fix(self, ja, sec, key, field):
        """訳注 (translation_notes.json の faction=core_rules) の訂正を ~~誤~~==正== の形で書き込む。"""
        for n in self.notes:
            if n["tr_section"] != sec or n["tr_key"] != key or n.get("tr_field") != field:
                continue
            for old, new in T.fix_pairs(n):
                m = T._loose_pattern(old).search(ja) if old else None
                if m:
                    ja = ja[:m.start()] + T._render_fix(old, new, m.group(0)) + ja[m.end():]
        return ja

    # --- 出力 ---
    @staticmethod
    def md(t):
        """本文を Markdown に。• 行は箇条書き、空行は段落。"""
        t = (t or "").replace("\xa0", " ").replace(" ", " ").strip()
        t = re.sub(r"\*{3}(\s*)", r"***\1", t)
        out, prev_list = [], False
        for ln in re.split(r"\n+", t):
            ln = ln.strip()
            if not ln:
                continue
            ln = re.sub(r"^\*\*\s*([•‣◆])\s*", r"\1 **", ln)
            if ln.startswith("* "):      # 注の「* …」を箇条書きにしない
                ln = "\\" + ln
            m = re.match(r"^[•‣◆]\s*(.*)$", ln)
            n = re.match(r"^\d+\.\s+", ln)
            is_list = bool(m or n)
            if out and not (is_list and prev_list):
                out.append("")
            out.append("- " + m.group(1) if m else ln)
            prev_list = is_list
        return "\n".join(out)

    @staticmethod
    def quote_en(t):
        return "> [!quote]- EN\n" + "\n".join(("> " + ln).rstrip() for ln in t.split("\n"))

    def both(self, ja, en, wrap=None):
        """日本語 + 折りたたみ英語。日本語が無ければ英語だけ。"""
        w = wrap or (lambda s: s)
        if not ja:
            return [w(self.md(en)), ""]
        return [w(self.md(ja)), "", self.quote_en(self.md(en)), ""]

    @staticmethod
    def boxed(s):
        return "\n".join(("> " + ln).rstrip() for ln in s.split("\n"))

    def render_ability(self, a, at):
        en, ja = self.ability(a, at)
        cost = ""
        if a.get("cpCost"):
            cost = "｜%s CP" % a["cpCost"]
        elif a.get("cost"):
            cost = "｜%s" % a["cost"]

        def block(v, labels, named):
            ls = ["**%s**（%s%s）" % (named, self.inline(v.get("timing")) or "", cost)]
            if v.get("lore"):
                ls.append("*%s*" % self.inline(v["lore"]))
            for k, _, lab in ABILITY_FIELDS[1:]:
                if v.get(k):
                    body = self.md(v[k])
                    first, _, rest = body.partition("\n")
                    ls.append("- **%s:** %s" % (labels[k], first))
                    ls += [("  " + x).rstrip() for x in rest.split("\n")] if rest else []
            if v.get("keywords"):
                ls.append("- **%s:** %s" % (labels["keywords"], v["keywords"]))
            return "\n".join(ls[:1] + [""] + (ls[1:2] + [""] if v.get("lore") else []) + ls[2 if v.get("lore") else 1:])

        JA = {k: lab for k, _, lab in ABILITY_FIELDS}
        JA["keywords"] = "キーワード"
        EN = dict(used_by="Used By", declare="Declare", effect="Effect", keywords="Keywords")
        if not ja:
            return [self.boxed(block(en, JA, a["name"])), ""]
        named = T.pair(ja.get("name"), a["name"])
        merged = {k: ja.get(k) or (en.get(k) if k != "lore" else None) for k in en}
        return [self.boxed(block(merged, JA, named)), "", self.quote_en(block(en, EN, a["name"])), ""]

    @staticmethod
    def inline(t):
        return re.sub(r"\s*\n\s*", " ", (t or "").replace("\xa0", " ")).strip()

    @classmethod
    def item(cls, pad, t):
        """箇条書き 1 項目。項目の中の「• …」は入れ子の箇条書きにする。"""
        head, *subs = re.split(r"\n\s*[•‣◆]\s*", (t or "").strip())
        return "\n".join(["%s- %s" % (pad, cls.inline(head))] +
                         ["%s  - %s" % (pad, cls.inline(x)) for x in subs])

    def render_component(self, x, at):
        kind, en = x["contentType"], x.get("textContent")
        key, loc = x["id"], at
        out = []
        if kind == "image":
            if x.get("imageUrl"):
                alt = re.sub(r"[\[\]]", "", self.inline(x.get("altText"))) or "図"
                out += ["![%s](%s)" % (alt, x["imageUrl"]), ""]
            return out
        if kind == "ability" and x.get("abilityId"):
            return self.render_ability(self.abilities[x["abilityId"]], loc)
        if kind == "bullets":
            ja_l, en_l, all_ja = [], [], True
            for b in self.bullets.get(key, []):
                ja = self.text(b["id"], b["text"], loc, "bullet_point", "text")
                pad = "  " * (b.get("indent") or 0)
                ja_l.append(self.item(pad, ja or b["text"]))
                en_l.append(self.item(pad, b["text"]))
                all_ja &= bool(ja)
            if not ja_l:
                return []
            if ja_l == en_l:
                return ["\n".join(en_l), ""]
            return ["\n".join(ja_l), "", self.quote_en("\n".join(en_l)), ""]
        if x.get("title"):
            t = self.name("titles", x["title"], loc)
            out += ["##### %s" % self.heading(t, x["title"]), ""]
            loc = x["title"]
        ja = self.text(key, en, loc, "rule_container_component", "textContent")
        if kind == "header":
            out += ["**%s**" % T.pair(ja, self.inline(en)), ""]
        elif kind == "textItalic":
            cap = lambda s: "*%s*" % self.inline(s).strip("*")
            out += [cap(ja or en), ""] + (["", self.quote_en(self.inline(en)), ""] if ja else [])
        elif kind == "boxedText":
            out += self.both(ja, en, self.boxed)
        elif kind == "textBold":
            b = lambda s: "**%s**" % self.inline(s).replace("**", "")
            out += [b(ja or en), ""] + ([self.quote_en(self.inline(en)), ""] if ja else [])
        elif en:
            out += self.both(ja, en)
        return out

    @staticmethod
    def heading(ja, en):
        """「5.1 キーワード(Keywords)」の形。英語側の番号は日本語側にもあれば省く。"""
        en = en.strip()
        if not ja:
            return en
        m = re.match(r"^([\d.]+)\s+(.*)$", en)
        if m and ja.startswith(m.group(1)):
            return "%s(%s)" % (ja, m.group(2))
        return "%s(%s)" % (ja, en)

    def build(self):
        meta = self.raw.get("metadata", {})
        out, toc = [], []
        for pub in self.publications():
            title = "コアルール(Core Rules)" if pub["name"] == CORE else \
                "上級ルール %s(Advanced Rules)" % ADVANCED.match(pub["name"]).group(1)
            out += ["## %s" % title, ""]
            toc.append("- [[#%s]]" % title)
            for s in self.by_parent.get(pub["id"], []):
                self.section(s, 3, out, toc, pub)
        head = ["# ウォーハンマー エイジ・オヴ・シグマー コアルール（4版）", "",
                provenance(self.dump_path, meta.get("data_version")), "",
                "公式アプリ同梱の `dump.json` にあるコアルールと上級ルール（最新の General's Handbook のもの）を、"
                "アプリの並び順のまま書き出したもの。追加・エラッタは本文に反映済みで、章末の「Addenda, Errata and FAQs」は"
                "その一覧。日本語は公式 PDF（コアルール、ルール・アップデート）の文を "
                "`official_translations/core_rules.json` から引き、英語は折りたたみ（`[!quote]- EN`）で併記する。"
                "日本語が無い、または英語が改訂されて日本語が古くなった箇所は英語のまま出す。"
                "既知の誤訳は本文中に `~~誤~~==正==` の形で訂正する。", "", "## 目次", ""]
        return re.sub(r"\n{3,}", "\n\n", "\n".join(head + toc + [""] + out)).rstrip() + "\n"

    def section(self, s, level, out, toc, pub):
        name = s["name"].strip()
        ja = self.name("titles", name, pub["name"])
        h = self.heading(ja, name)
        out += ["%s %s" % ("#" * level, h), ""]
        toc.append("%s- [[#%s]]" % ("  " * (level - 2), h))
        conts = self.containers.get(s["id"], [])
        num = re.compile(r"^[\d.]+\s+")
        for c in conts:
            title = (c.get("title") or "").strip()
            at = title or name
            if title and num.sub("", title).lower() != num.sub("", name).lower():
                t = self.name("titles", title, name)
                out += ["%s %s" % ("#" * min(level + 1, 5), self.heading(t, title)), ""]
            if c.get("subtitle"):
                out += ["*%s*" % self.inline(c["subtitle"]), ""]
            where = "%s > %s" % (name, at) if at != name else name
            for x in self.components.get(c["id"], []):
                out += self.render_component(x, where)
        for ch in self.by_parent.get(s["id"], []):
            self.section(ch, level + 1, out, toc, pub)

    def unused(self):
        out = []
        for sec in ("titles", "texts", "abilities"):
            for k in (self.tr.get(sec) or {}):
                if not k.startswith("_") and (sec, k) not in self.used:
                    out.append((sec, k))
        return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True)
    ap.add_argument("-o", "--output", default="core_rules.md")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--check", action="store_true", help="訳の抜け・古い訳・未使用の訳を表示 (md は書かない)")
    ap.add_argument("--lookups", help="訳の当て先を JSON に書き出す (md は書かない)")
    args = ap.parse_args()
    core = Core(args.dump, json.load(open(args.dump, encoding="utf-8")))
    md = core.build()
    if args.lookups:
        json.dump(core.lookups, open(args.lookups, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("%d 件 -> %s" % (len(core.lookups), args.lookups))
    elif args.check:
        for sec, k, at in core.missing:
            print("訳なし [%s] %s (%s)" % (sec, k, at))
        for sec, k, at in core.stale:
            print("英語が改訂された [%s] %s (%s)" % (sec, k, at))
        for sec, k in core.unused():
            print("未使用 [%s] %s" % (sec, k))
        print("訳 %d / %d、訳なし %d、古い訳 %d、未使用 %d" % (
            core.hits, core.total, len(core.missing), len(core.stale), len(core.unused())))
    elif args.stdout:
        sys.stdout.write(md)
    else:
        open(args.output, "w", encoding="utf-8").write(md)
        print("written %s (訳 %d / %d、古い訳 %d)" % (args.output, core.hits, core.total, len(core.stale)))


if __name__ == "__main__":
    main()
