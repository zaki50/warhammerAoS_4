"""md 生成で使う日本語訳 (official_translations/ と own_translations/) の読み込みと照合。

extract-warscrolls / extract-faction-rules / extract-spearheads が共通で使い、
check-translations は LOOKUPS に記録されたキーから未使用の訳を判定する。

訳ファイル: <dump.json と同じディレクトリ>/{official,own}_translations/<ファクションslug>.json
  {"unit_names": {...}, "weapon_names": {...}, "ability_names": {...}, "ability_texts": {...}}
  キーは英語名、または "ユニット英語名|英語名" (そのユニットにだけ当たる。武器・アビリティのみ)。
  ability_texts はさらに "Spearhead|ユニット英語名|英語名" / "Spearhead|英語名" で Spearhead 版にだけ当てられる。
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

    def text(self, en, unit=None, spearhead=False):
        """アビリティ本文の訳 ({timing, declare, effect, keywords} の dict) か None。
        具体的なキーから順に引く: Spearhead|ユニット|名前 → Spearhead|名前 → ユニット|名前 → 名前。"""
        keys = []
        if spearhead:
            keys.append("Spearhead|%s|%s" % (unit, en) if unit else "Spearhead|%s" % en)
        if unit:
            keys.append("%s|%s" % (unit, en))
        keys.append(en)
        for i, k in enumerate(keys):
            v = self._get("ability_texts", k)
            if v:
                for rest in keys[i + 1:]:
                    SHADOWED.add((self.base, self.slug, "ability_texts", rest))
                return v
        return None
