# -*- coding: utf-8 -*-
"""dump.json と訳ファイルから、カード用のデータ (units.json) を作る。

  python3 extract.py --dump ../dump.json --list
  python3 extract.py --dump ../dump.json --set daughters_of_khaine -o units.json

カードの組 (set) はファクション単位 (md の warscrolls と同じく Spearhead 版と
グランドアライアンスは除く) と Spearhead 単位 (spearhead_<slug>)。

日本語は official_translations/ (公式訳) → own_translations/ (独自訳) の順に引き、
独自訳から来たものには own=True を付ける (カードに「独自訳」バッジ)。引き方 (キーの候補の順) は
md 生成と同じ .claude/skills/_lib/aos_translations.py の規則。translation_notes.json の
status=open の注は、当たった訳のキーとフィールドごとに fix (訂正) と note (理由) として持たせる。
"""
import argparse, collections, importlib.util, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILLS = os.path.join(REPO, '.claude', 'skills')
sys.path.insert(0, os.path.join(SKILLS, '_lib'))
import aos_translations as T  # noqa: E402


def load_module(skill, filename):
    spec = importlib.util.spec_from_file_location(filename[:-3], os.path.join(SKILLS, skill, 'scripts', filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Layers:
    """1 ファクション分の訳 (公式訳・独自訳) と訳注。"""

    def __init__(self, base, faction):
        self.slug = T.slugify(faction)
        load = lambda layer: (json.load(open(p, encoding='utf-8'))
                              if os.path.exists(p := os.path.join(base, layer, '%s.json' % self.slug)) else {})
        self.official, self.own = load('official_translations'), load('own_translations')
        p = os.path.join(base, 'translation_notes.json')
        notes = json.load(open(p, encoding='utf-8')).get('notes', []) if os.path.exists(p) else []
        self.notes = [n for n in notes if n.get('status') == 'open' and n.get('faction') == self.slug]

    def get(self, section, keys):
        """(値, 独自訳か, 当たったキー)。無ければ (None, False, None)。"""
        for k in keys:
            v = (self.official.get(section) or {}).get(k)
            if v:
                return v, False, k
            v = (self.own.get(section) or {}).get(k)
            if v:
                return v, True, k
        return None, False, None

    def faction_name(self):
        return self.official.get('faction_name') or self.own.get('faction_name')

    def fixes(self, section, key, field=None):
        """[(誤訳箇所, 修正後), ...] と [理由, ...]。"""
        pairs, reasons = [], []
        for n in self.notes:
            if n['tr_section'] != section or n['tr_key'] != key or (field and n.get('tr_field') != field):
                continue
            f = n.get('fix_ja')
            if isinstance(f, str):
                pairs.append((n['ja'], f))
            elif isinstance(f, dict):
                pairs += list(f.items())
            if n['note'] not in reasons:
                reasons.append(n['note'])
        return pairs, reasons


class Dump:
    def __init__(self, path):
        raw = json.load(open(path, encoding='utf-8'))
        self.path = path
        self.base = os.path.dirname(os.path.abspath(path))
        self.d = raw['data']
        self.data_version = raw.get('metadata', {}).get('data_version')
        d = self.d
        by = lambda t, k: collections.defaultdict(list, {})
        self.W = collections.defaultdict(list)
        for x in d['warscroll_weapon']:
            self.W[x['warscrollId']].append(x)
        self.A = collections.defaultdict(list)
        for x in d['warscroll_ability']:
            self.A[x['warscrollId']].append(x)
        wa = {x['id']: x['name'] for x in d['weapon_ability']}
        self.WA = collections.defaultdict(list)
        for x in sorted(d['warscroll_weapon_weapon_ability'], key=lambda x: x.get('displayOrder') or 0):
            if x['weaponAbilityId'] in wa:
                self.WA[x['warscrollWeaponId']].append(wa[x['weaponAbilityId']])
        kw = {k['id']: k['name'] for k in d['keyword']}
        self.AK = collections.defaultdict(list)
        for x in d['warscroll_ability_keyword']:
            self.AK[x['warscrollAbilityId']].append(kw.get(x['keywordId']))
        ta = {x['id']: x for x in d['terrain_ability']}
        self.TA = collections.defaultdict(list)
        for x in sorted(d['warscroll_terrain_ability'], key=lambda x: x.get('displayOrder') or 0):
            if x['terrainAbilityId'] in ta:
                self.TA[x['warscrollId']].append(ta[x['terrainAbilityId']])
        self.ADD = collections.defaultdict(list)
        for x in d['warscroll_additional_characteristic']:
            self.ADD[x['warscrollId']].append(x)
        self.RO = collections.defaultdict(list)
        for x in sorted(d['warscroll_regiment_option'], key=lambda x: x.get('displayOrder') or 0):
            if not x.get('hiddenFromReference'):
                self.RO[x['warscrollId']].append(x)

    # ---------- 組 (set) の一覧 ----------
    def sets(self):
        d = self.d
        fk = {f['id']: f['name'] for f in d['faction_keyword']}
        ws = {w['id']: w for w in d['warscroll']}
        members = collections.defaultdict(list)
        for x in d['warscroll_faction_keyword']:
            w = ws.get(x['warscrollId'])
            if w and not w.get('isSpearhead'):
                members[x['factionKeywordId']].append(w)
        out = []
        for fid, lst in members.items():
            name = fk[fid]
            if name.startswith('Grand Alliance'):
                continue
            out.append({'slug': T.slugify(name), 'kind': 'faction', 'faction': name, 'title': name,
                        'units': sorted(lst, key=lambda w: (w['name'], w.get('subname') or ''))})
        for sp in load_module('extract-spearheads', 'extract_spearheads.py').collect_spearheads(d):
            if not sp['units']:
                continue
            out.append({'slug': 'spearhead_' + T.slugify(sp['name']), 'kind': 'spearhead', 'faction': sp['faction'],
                        'title': sp['name'],
                        'units': sorted(sp['units'], key=lambda w: (w['name'], w.get('subname') or ''))})
        return sorted(out, key=lambda s: (s['kind'] != 'faction', s['slug']))

    # ---------- 1 組分 ----------
    def build(self, s):
        L = Layers(self.base, s['faction'])
        alliance = None
        for w in s['units']:
            for k in (w.get('referenceKeywords') or '').split(','):
                if k.strip() in ('Order', 'Chaos', 'Death', 'Destruction'):
                    alliance = k.strip()
        title_ja, _, _ = L.get('group_names', [s['title']]) if s['kind'] == 'spearhead' else (None, 0, 0)
        meta = {'slug': s['slug'], 'kind': s['kind'], 'faction_en': s['faction'], 'faction_ja': L.faction_name(),
                'faction_slug': L.slug, 'alliance': alliance, 'title_en': s['title'], 'title_ja': title_ja,
                'data_version': self.data_version}
        return {'meta': meta, 'units': [self.unit(w, L) for w in s['units']]}

    @staticmethod
    def pair(L, section, keys, en):
        """名前の日英: {ja, en, own, fix, note}。ja が無ければ英語を ja に入れ en は空 (英語のみ)。"""
        ja, own, k = L.get(section, keys)
        fix, note = L.fixes(section, k) if k else ([], [])
        if ja and ja != en:
            return {'ja': ja, 'en': en, 'own': own, 'fix': fix, 'note': note}
        return {'ja': en, 'en': '', 'own': False, 'fix': [], 'note': []}

    def unit(self, w, L):
        name, sub = w['name'], w.get('subname')
        sp = bool(w.get('isSpearhead'))
        nm = self.pair(L, 'unit_names', [name], name)
        if sub:
            nm['ja'] += '、' + sub if nm['en'] else ', ' + sub
            if nm['en']:
                nm['en'] += ', ' + sub
        weapons = {'ranged': [], 'melee': []}
        for x in self.W[w['id']]:
            p = self.pair(L, 'weapon_names', ['%s|%s' % (name, x['name']), x['name']], x['name'])
            if x.get('battleDamaged'):
                p['ja'] += '（戦傷時）'
                if p['en']:
                    p['en'] += ' (battle damaged)'
            ab_en = self.WA[x['id']]
            ab_ja = [L.get('weapon_ability_names', [a])[0] or a for a in ab_en]
            vals = [x.get('attacks'), x.get('hit'), x.get('wound'), x.get('rend'), x.get('damage')]
            if x.get('type') == 'ranged':
                vals = [x.get('range')] + vals
            row = dict(p, v=[v if v not in (None, '') else '-' for v in vals],
                       abil_ja=ab_ja if ab_ja != ab_en else [], abil_en=ab_en)
            weapons['ranged' if x.get('type') == 'ranged' else 'melee'].append(row)
        abilities = [self.ability(a, L, name, sp, [k for k in self.AK[a['id']] if k]) for a in self.A[w['id']]]
        terrain = []
        for t in self.TA[w['id']]:
            it = self.ability({'name': t['name'], 'effect': t.get('rules')}, L, name, sp, [])
            terrain.append(it)
        kws = []
        kfix = {}
        for k in [k.strip() for k in (w.get('referenceKeywords') or '').split(',') if k.strip()]:
            ja, own, key = L.get('keyword_names', ['%s|%s' % (name, k), k])
            kws.append([ja or k, k if ja and ja != k else ''])
            if key:
                pairs, _ = L.fixes('keyword_names', key)
                if pairs:
                    kfix[k] = pairs
        wg_ja, _, wg_key = L.get('wargear_option_texts', [name])
        return {
            'id': w['id'], 'name': nm, 'legends': bool(w.get('isLegends')), 'spearhead': sp,
            'stats': [['移動力', 'Move', w.get('move')], ['体力', 'Health', w.get('health')],
                      ['防御力', 'Save', w.get('save')], ['確保力', 'Control', w.get('control')]],
            'ward': w.get('wardSave'),
            'additional': [[c['name'], c['value']] for c in self.ADD[w['id']]],
            'points': w.get('points'), 'models': w.get('modelCount'), 'base': w.get('baseSize'),
            'reinforce': not w.get('cannotBeReinforced'),
            'ranged': weapons['ranged'], 'melee': weapons['melee'],
            'abilities': abilities, 'terrain': terrain,
            'keywords': kws, 'keyword_fix': kfix,
            'regiment': [r.get('optionText') or '' for r in self.RO[w['id']]],
            'notes_en': w.get('notes') or '',
            'wargear': {'ja': wg_ja or '', 'en': w.get('wargearOptionsText') or '',
                        'fix': L.fixes('wargear_option_texts', wg_key)[0] if wg_key else []}
                       if w.get('wargearOptionsText') else None,
        }

    def ability(self, a, L, unit, sp, kw_en):
        en = a['name']
        nm = self.pair(L, 'ability_names', ['%s|%s' % (unit, en), en], en)
        tx, own, key = L.get('ability_texts', T.Translations.text_keys(en, unit, sp))
        tx = tx or {}
        fields = {}
        for f, src in (('timing', 'phaseDetails'), ('used_by', 'usedBy'), ('declare', 'declare'), ('effect', 'effect')):
            e = a.get(src) or (a.get('additionalRulesText') if f == 'effect' else None) or ''
            fields[f] = {'ja': tx.get(f) or '', 'en': e}
            if key:
                fields[f]['fix'] = L.fixes('ability_texts', key, f)[0]
        notes = L.fixes('ability_texts', key)[1] if key else []
        return {'name': nm, 'fields': fields, 'own': own if tx else False,
                'kw_ja': tx.get('keywords') or '', 'kw_en': ', '.join(kw_en),
                'cast': a.get('castingValue'), 'cp': a.get('cpCost'), 'note': notes + nm['note']}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dump', default=os.path.join(REPO, 'dump.json'))
    ap.add_argument('--set', help='組のスラッグ (部分一致)')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('-o', '--out', default='units.json')
    a = ap.parse_args()
    dd = Dump(a.dump)
    sets = dd.sets()
    if a.list or not a.set:
        for s in sets:
            print('%-48s %4d  %s' % (s['slug'], len(s['units']), s['kind']))
        return
    hit = [s for s in sets if s['slug'] == a.set] or [s for s in sets if a.set.lower() in s['slug']]
    if len(hit) != 1:
        raise SystemExit('組が一意に決まりません: %s (%s)' % (a.set, ', '.join(s['slug'] for s in hit[:8]) or '該当なし'))
    data = dd.build(hit[0])
    json.dump(data, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%s: %d ユニット' % (a.out, len(data['units'])))


if __name__ == '__main__':
    main()
