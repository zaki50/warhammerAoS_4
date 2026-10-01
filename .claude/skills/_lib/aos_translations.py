"""md 生成で使う日本語訳 (official_translations/ と own_translations/) の読み込みと照合。

extract-warscrolls / extract-faction-rules / extract-spearheads が共通で使い、
check-translations は LOOKUPS に記録されたキーから未使用の訳を判定する。

訳ファイル: <dump.json と同じディレクトリ>/{official,own}_translations/<ファクションslug>.json
  {"unit_names": {...}, "weapon_names": {...}, "ability_names": {...}, "ability_texts": {...}}
  キーは英語名、または "ユニット英語名|英語名" (そのユニットにだけ当たる。武器・アビリティのみ)。
  ability_texts はウォースクロールのアビリティを "ユニット英語名|英語名" で持つ (名前だけのキーには落ちない)。
  名前だけのキーはファクションルールのアビリティ用。"Spearhead|…" を前に付けると Spearhead 版にだけ当たる。
  keyword_names (ユニットのキーワード) / weapon_ability_names (武器アビリティ) / group_names (アビリティグループ・
  戦闘陣形・伝承・Spearhead の名前) / group_texts (グループの前置き文) は英語名がキー。
  "faction_name" はファクション名の日本語 (文字列)。
公式訳が独自訳より優先。他ファクションのファイルは参照しない。
"""
import json, os, re

LAYERS = ("official_translations", "own_translations")
SECTIONS = ("unit_names", "weapon_names", "ability_names", "ability_texts",
            "keyword_names", "weapon_ability_names", "group_names", "group_texts",
            "wargear_option_texts")
# ability_texts の値で使うフィールド (いずれも省略可。省略したものは英語のまま)
TEXT_FIELDS = ("timing", "used_by", "declare", "effect", "keywords")

_notes_cache = {}


def _load_notes(base):
    """<base>/translation_notes.json の status=open の注 (無ければ空)。"""
    if base not in _notes_cache:
        p = os.path.join(base, "translation_notes.json")
        notes = json.load(open(p, encoding="utf-8")).get("notes", []) if os.path.exists(p) else []
        _notes_cache[base] = [n for n in notes if n.get("status") == "open"]
    return _notes_cache[base]


def _plain(s):
    return (s or "").replace("**", "")


def fix_pairs(n):
    """注の fix_ja を [(誤訳箇所, 修正後), ...] にする。fix_ja が文字列なら ja 全体の差し替え。"""
    fix = n.get("fix_ja")
    if isinstance(fix, str):
        return [(_plain(n.get("ja")), _plain(fix))]
    if isinstance(fix, dict):
        return [(_plain(a), _plain(b)) for a, b in fix.items()]
    return []


def fix_parts(old, new):
    """訂正 old → new を [(keep|del|ins, 文字列), ...] に分ける (translation-notes の fix_parts と同じ)。"""
    if not new:
        return [("del", old)]
    if not old:
        return [("ins", new)]
    if old == new:
        return [("keep", old)]
    head = 0
    while head < len(old) and head < len(new) and old[head] == new[head]:
        head += 1
    tail = 0
    while (tail < len(old) - head and tail < len(new) - head
           and old[len(old) - 1 - tail] == new[len(new) - 1 - tail]):
        tail += 1
    if head or tail:
        mid = fix_parts(old[head:len(old) - tail], new[head:len(new) - tail])
        return (([("keep", old[:head])] if head else []) + mid
                + ([("keep", old[len(old) - tail:])] if tail else []))
    i = old.find(new)
    if i >= 0:
        return ([("del", old[:i])] if old[:i] else []) + [("keep", new)] + \
               ([("del", old[i + len(new):])] if old[i + len(new):] else [])
    j = new.find(old)
    if j >= 0:
        return ([("ins", new[:j])] if new[:j] else []) + [("keep", old)] + \
               ([("ins", new[j + len(old):])] if new[j + len(old):] else [])
    return [("del", old), ("ins", new)]


def _loose_pattern(old):
    """誤訳箇所を、Markdown 化した本文 (太字記号や空白が挟まる) から探す正規表現。"""
    return re.compile(r"(?:\*\*|\s)*".join(re.escape(ch) for ch in old if not ch.isspace()))


_MARKUP = re.compile(r"(?:\*\*|\s)*")


def _render_fix(old, new, matched):
    """本文中の一致箇所 matched (old に太字記号・空白が挟まったもの) を「~~誤~~==正==」に書き換える。
    matched 側の太字記号は残す (落とすと前後の ** と対がずれる)。"""
    parts = fix_parts(old, new)
    # 共通部分がごくわずかなら、細切れにせず全体を差し替えて見せる
    kept = sum(len(t) for k, t in parts if k == "keep")
    if 0 < kept < max(4, 0.3 * len(old)):
        parts = [("del", old), ("ins", new)]
    out, pos = [], 0
    for kind, txt in parts:
        if kind == "ins":
            out.append("==%s==" % txt)
            continue
        m = _MARKUP.match(matched, pos)
        out.append(matched[pos:m.end()])
        pos = start = m.end()
        n = len([c for c in txt if not c.isspace()])
        while n:
            pos = _MARKUP.match(matched, pos).end() if pos > start else pos
            pos += 1
            n -= 1
        seg = matched[start:pos]
        out.append(seg if kind == "keep" else "~~%s~~" % seg)
    out.append(matched[pos:])
    return "".join(out)


# 照合を試みた (base, slug, section, key) の記録。check-translations が使う
LOOKUPS = set()
# "ユニット|名前" が当たったため照合されなかった "名前" の記録 (同じ形)
SHADOWED = set()
_cache = {}


def slugify(en):
    return re.sub(r"[^a-z0-9]+", "_", (en or "").lower()).strip("_")


def _load_layer(base, layer, slug):
    p = os.path.join(base, layer, "%s.json" % slug)
    if p not in _cache:
        _cache[p] = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    return _cache[p]


def pair(ja, en):
    """{日本語}({英語}) 表記。訳が無い (または英語と同じ) なら英語のみ。"""
    return "%s(%s)" % (ja, en) if ja and ja != en else en


class Translations:
    def __init__(self, dump_path, faction_name):
        self.base = os.path.dirname(os.path.abspath(dump_path))
        self.slug = slugify(faction_name)
        self.official = _load_layer(self.base, "official_translations", self.slug)
        self.own = _load_layer(self.base, "own_translations", self.slug)

    def _get(self, section, key):
        LOOKUPS.add((self.base, self.slug, section, key))
        for t in (self.official, self.own):
            v = (t.get(section) or {}).get(key)
            if v:
                return v
        return None

    def _scoped(self, section, en, unit):
        """"ユニット|名前" を先に、無ければ "名前" を引く。"""
        if unit:
            v = self._get(section, "%s|%s" % (unit, en))
            if v:
                SHADOWED.add((self.base, self.slug, section, en))
                return v
        return self._get(section, en)

    def unit(self, w):
        """ウォースクロールの見出し名。サブネームは英語のまま後ろに付ける。"""
        sub = (", %s" % w["subname"]) if w.get("subname") else ""
        ja = self._get("unit_names", w["name"])
        return pair(ja + sub if ja else None, w["name"] + sub)

    def weapon(self, en, unit=None):
        return pair(self._scoped("weapon_names", en, unit), en)

    def ability(self, en, unit=None):
        return pair(self._scoped("ability_names", en, unit), en)

    def keyword(self, en, unit=None):
        """キーワードの日本語か None。"""
        return self._scoped("keyword_names", en, unit)

    def keywords(self, csv, unit=None):
        """"Hero, Infantry, ..." を書籍と同じ「、」区切りの日本語にし、元の英語を括弧で添える。
        1 つも訳が無ければ英語のまま。"""
        toks = [k.strip() for k in (csv or "").split(",") if k.strip()]
        jas = [self.keyword(k, unit) for k in toks]
        if not any(jas):
            return ", ".join(toks)
        return "%s（%s）" % ("、".join(j or k for j, k in zip(jas, toks)), ", ".join(toks))

    def weapon_ability(self, en):
        return pair(self._get("weapon_ability_names", en), en)

    def wargear_text(self, unit, text):
        """ウォースクロールの装備オプション文 (wargearOptionsText)。キーはユニット英語名。"""
        return self._get("wargear_option_texts", unit) or text

    def group(self, en):
        """アビリティグループ・戦闘陣形・伝承・Spearhead の名前。"""
        return pair(self._get("group_names", en), en)

    def group_text(self, en, text):
        """グループの前置き文 (restrictionText)。訳が無ければ英語のまま。"""
        return self._get("group_texts", en) or text

    def faction(self, en):
        v = self.official.get("faction_name") or self.own.get("faction_name")
        return pair(v, en)

    @staticmethod
    def text_keys(en, unit=None, spearhead=False):
        """ability_texts を引くキーの候補 (具体的なものから順)。"""
        if unit:
            # ウォースクロールのアビリティはユニット指定のキーだけで引く。名前だけのキーに落とすと、
            # 同じ名前で中身の違う別ユニット (Legends・禍事版) やファクションルールの本文が当たってしまう
            return (["Spearhead|%s|%s" % (unit, en)] if spearhead else []) + ["%s|%s" % (unit, en)]
        return (["Spearhead|%s" % en] if spearhead else []) + [en]

    def _hit_notes(self, section, keys):
        """translation_notes.json の open な注のうち、このファクションの section の keys に当たるもの。
        keys は引く順の候補で、実際に訳が当たったキーの注だけを返す (同じ文面の注は 1 つにまとめる)。"""
        used = next((k for k in keys
                     if (self.official.get(section) or {}).get(k) or (self.own.get(section) or {}).get(k)), None)
        if used is None:
            return []
        out, seen = [], set()
        for n in _load_notes(self.base):
            if (n.get("faction") == self.slug and n.get("tr_section") == section
                    and n.get("tr_key") == used and n["note"] not in seen):
                seen.add(n["note"])
                out.append(n)
        return out

    def fix_lines(self, lines, section, keys, indent=""):
        """当たった注の fix_ja を、描画済みの行 lines (その場で書き換える) に「~~誤~~==正==」の形で
        書き込む (40k の extract-core-rules と同じ表記)。訂正文が無い注・本文に見つからなかった訂正は
        訳注のコールアウト行にして返す。"""
        rest = []
        for n in self._hit_notes(section, keys):
            ok = False
            for old, new in fix_pairs(n):
                pat = _loose_pattern(old)
                for i, l in enumerate(lines):
                    m = pat.search(l)
                    if m:
                        lines[i] = l[:m.start()] + _render_fix(old, new, m.group(0)) + l[m.end():]
                        ok = True
                        break
            if not ok:
                rest.append(n)
        out = []
        for n in rest:
            body = n["note"]
            pairs = fix_pairs(n)
            if pairs:
                body += " 訂正: " + "、".join("「%s」→「%s」" % (a, b) for a, b in pairs)
            out += ["%s> [!warning] 訳注" % indent, "%s> %s" % (indent, body)]
        return out

    def text(self, en, unit=None, spearhead=False):
        """アビリティ本文の訳 ({timing, declare, effect, keywords} の dict) か None。
        ユニットのアビリティは Spearhead|ユニット|名前 → ユニット|名前、ファクションルールの
        アビリティ (unit=None) は Spearhead|名前 → 名前 の順に引く。"""
        keys = self.text_keys(en, unit, spearhead)
        for i, k in enumerate(keys):
            v = self._get("ability_texts", k)
            if v:
                for rest in keys[i + 1:]:
                    SHADOWED.add((self.base, self.slug, "ability_texts", rest))
                return v
        return None
