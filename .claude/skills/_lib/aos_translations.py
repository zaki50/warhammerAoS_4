"""md 生成で使う日本語訳 (official_translations/ と own_translations/) の読み込みと照合。

extract-warscrolls / extract-faction-rules / extract-spearheads が共通で使い、
check-translations は LOOKUPS に記録されたキーから未使用の訳を判定する。

訳ファイル: <dump.json と同じディレクトリ>/{official,own}_translations/<ファクションslug>.json
  {"unit_names": {...}, "weapon_names": {...}, "ability_names": {...}}
  キーは英語名、または "ユニット英語名|英語名" (そのユニットにだけ当たる。武器・アビリティのみ)。
公式訳が独自訳より優先。他ファクションのファイルは参照しない。
"""
import json, os, re

LAYERS = ("official_translations", "own_translations")
SECTIONS = ("unit_names", "weapon_names", "ability_names")

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
