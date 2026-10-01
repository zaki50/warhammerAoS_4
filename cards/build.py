# -*- coding: utf-8 -*-
"""units.json からウォースクロールカードの HTML を組み立てる (40k の cards/build.py に合わせた表示)。

  python3 build.py units.json -o cards.html [--notes] [--a5]

- 名前・本文は日英併記 (日本語の下／後ろに英語をグレーの小さい字で)。日本語訳が無い項目は英語だけ
- 誤訳・誤植 (translation_notes.json の status=open) は取り消し線＋修正語 (オレンジ)。
  --notes を付けると、その下に「訳注：理由」も出す
- 独自訳 (own_translations/) から来た本文には「独自訳」バッジ
- --a5 は A5 横・1 ページ 1 枚 (表・裏が交互)。既定は A4 縦に 2 枚
"""
import argparse, html, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '.claude', 'skills', 'translation-notes', 'scripts'))
import factions as FX  # noqa: E402
from translation_notes import fix_parts  # noqa: E402

E = lambda s: html.escape(s or '')


# ---------- 配色 (40k と同じ計算) ----------
def _hex(c):
    c = c.lstrip('#')
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _mix(a, b, t):
    ra, rb = _hex(a), _hex(b)
    return '#%02x%02x%02x' % tuple(round(ra[i] + (rb[i] - ra[i]) * t) for i in range(3))


def palette(colors):
    dk, mid, lt = colors
    return {'dk': dk, 'dk2': _mix(dk, mid, .55), 'mid': mid, 'lt': lt,
            'line': _mix(mid, '#ffffff', .55), 'panel': _mix(mid, '#ffffff', .92),
            'row': _mix(mid, '#ffffff', .85), 'en': _mix(dk, '#ffffff', .3)}


def clean(t):
    t = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), t or '')
    t = t.replace('*', '')   # 元データの強調・斜体記号 (Markdown) は表示しない
    return re.sub(r'\s+', ' ', t).strip()


class Cards:
    def __init__(self, data, show_notes=False, a5=False):
        self.units = data['units']
        self.meta = data['meta']
        self.show_notes = show_notes
        self.a5 = a5

    # --- 既知の誤訳を取り消し線＋修正語にする (40k の Cards.fix と同じ) ---
    unmatched = []   # 本文に当たらなかった訂正 (誤訳箇所)。build 後に警告として出す

    @staticmethod
    def fix(t, pairs):
        t = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), t or '')
        t = re.sub(r'\*{3}', '**', t)
        t = re.sub(r'[ \t]{2,}', ' ', t).strip().replace('**', '\x01')
        t = E(t)
        for old, new in pairs or []:
            parts = fix_parts(clean(old), clean(new))
            tol = lambda x: '\x01?'.join(re.escape(ch) for ch in E(x))
            body = [p for p in parts if p[0] != 'ins']
            # 区間の境目に太字の記号 (\x01) があっても当たるよう、境目ごとに (\x01?) を挟んで拾い直す
            m = re.search('(\x01?)'.join('(%s)' % tol(x) for _, x in body), t)
            if m:
                out, gi, first = '', 1, True
                for kind, x in parts:
                    if kind == 'ins':
                        out += '<ins>%s</ins>' % E(x)
                    else:
                        if not first:
                            out += m.group(gi); gi += 1   # 境目の太字記号
                        first = False
                        g = m.group(gi); gi += 1
                        out += ('<s>%s</s>' % g) if kind == 'del' else g
                t = t[:m.start()] + out + t[m.end():]
            else:
                Cards.unmatched.append(old)
        parts = t.split('\x01')
        t = ''.join(p + ('<b>' if i % 2 == 0 else '</b>') for i, p in enumerate(parts[:-1])) + parts[-1]
        return re.sub(r'\s*\n\s*', '<br>', t)

    def note_lines(self, notes):
        if not self.show_notes:
            return ''
        return ''.join('<p class="note"><b>訳注：</b>%s</p>' % E(clean(n)) for n in notes if n)

    @staticmethod
    def own(flag):
        return '<span class="own">独自訳</span>' if flag else ''

    # ---------- 名前 ----------
    def name_html(self, p, sep=' '):
        """{ja, en, fix} を「日本語 (英語)」で。en が無ければ英語だけ。"""
        ja = self.fix(p['ja'], p.get('fix'))
        return ja + ('%s<span class="en-n">%s</span>' % (sep, E(p['en'])) if p.get('en') else '')

    # ---------- ステータス ----------
    def stats_block(self, u):
        boxes = ''.join('<div class="st"><span class="sl">%s<i>%s</i></span><span class="sv">%s</span></div>'
                        % (ja, en, E(str(v) if v is not None else '-')) for ja, en, v in u['stats'])
        add = ''.join('<div class="st"><span class="sl">%s</span><span class="sv">%s</span></div>'
                      % (E(n), E(str(v))) for n, v in u['additional'])
        ward = ('<div class="inv"><span>加護<i>Ward</i></span><b>%s</b></div>' % E(u['ward'])) if u['ward'] else ''
        return '<div class="stats">%s%s%s</div>' % (boxes, add, ward)

    # ---------- 武器表 ----------
    WEP_R = [('射程', 'Rng'), ('回数', 'Atk'), ('ヒット', 'Hit'), ('ウーンズ', 'Wnd'), ('貫通', 'Rnd'), ('ダメージ', 'Dmg')]
    WEP_M = WEP_R[1:]

    @staticmethod
    def _abil(lst, br):
        return ('<span class="wa">%s%s%s</span>'
                % (br[0], E('、'.join(lst)) if br[0] == '［' else E(', '.join(lst)), br[1])) if lst else ''

    def weapon_table(self, title, title_en, icon, rows, heads):
        if not rows:
            return ''
        th = ''.join('<th>%s<i>%s</i></th>' % (ja, en) for ja, en in heads)
        tr = []
        for r in rows:
            nm = self.fix(r['ja'], r.get('fix')) + self._abil(r.get('abil_ja') or r.get('abil_en'), '［］' if r.get('abil_ja') else '[]')
            if r.get('en') or r.get('abil_ja'):
                nm += '<span class="en-n">%s%s</span>' % (E(r.get('en')), self._abil(r.get('abil_en') if r.get('abil_ja') else [], '[]'))
            tr.append('<tr><td class="wn">%s</td>%s</tr>' % (nm, ''.join('<td>%s</td>' % E(str(v)) for v in r['v'])))
        return ('<table class="wt"><thead><tr><th class="wh"><span class="wi">%s</span>%s<i>%s</i></th>%s</tr></thead>'
                '<tbody>%s</tbody></table>' % (icon, title, title_en, th, ''.join(tr)))

    def weapon_notes(self, u):
        seen, out = set(), []
        for r in u['ranged'] + u['melee']:
            for n in r.get('note') or []:
                if n not in seen:
                    seen.add(n); out.append(n)
        return ('<div class="wrules">%s</div>' % self.note_lines(out)) if (out and self.show_notes) else ''

    # ---------- アビリティ ----------
    LABEL = {'used_by': ('使用者', 'Used By'), 'declare': ('宣言', 'Declare'), 'effect': ('効果', 'Effect')}

    def render_ability(self, a):
        f = a['fields']
        ja_any = any(f[k]['ja'] for k in f)
        tags = []
        tm = f['timing']['ja'] or f['timing']['en']
        if tm:
            tags.append(E(tm))
        if a.get('cast'):
            tags.append('詠唱/祈願値 %s' % E(str(a['cast'])))
        if a.get('cp'):
            tags.append('CP %s' % E(str(a['cp'])))
        kw = a['kw_ja'] or a['kw_en']
        head = ('<p class="ab abh"><b>%s：</b>%s<span class="tmg">%s</span>%s</p>'
                % (self.name_html(a['name']), self.own(a.get('own')), ' / '.join(tags),
                   ('<span class="akw">［%s］</span>' % E(kw)) if kw else ''))
        body = []
        for k in ('used_by', 'declare', 'effect'):
            src = f[k]['ja'] or (f[k]['en'] if not ja_any else '')
            if src:
                body.append('<p class="ab"><span class="lbl">%s：</span>%s</p>'
                            % (self.LABEL[k][0], self.fix(src, f[k].get('fix'))))
        en = ''
        if ja_any:
            parts = [f['timing']['en']] if f['timing']['en'] else []
            parts += ['%s: %s' % (self.LABEL[k][1], clean(f[k]['en'])) for k in ('used_by', 'declare', 'effect') if f[k]['en']]
            if a['kw_en'] and a['kw_ja']:
                parts.append('Keywords: %s' % a['kw_en'])
            en = '<p class="en-b">%s</p>' % E(' ／ '.join(parts))
        return '<div class="abgrp">%s%s%s%s</div>' % (head, ''.join(body), en, self.note_lines(a.get('note')))

    @staticmethod
    def panel(title, title_en, inner, pid='', cls=''):
        if not inner:
            return ''
        t = '%s<i>%s</i>' % (title, title_en) if title_en else title
        return ('<div class="panel%s"%s><div class="ph">%s</div><div class="pc">%s</div></div>'
                % (' ' + cls if cls else '', ' id="%s"' % pid if pid else '', t, inner))

    # ---------- フッタ ----------
    BADGE = ('<svg viewBox="0 0 64 64"><path d="M32 3 60 32 32 61 4 32Z" fill="none" stroke="var(--dk)" stroke-width="3"/>'
             '<path d="M32 9 55 32 32 55 9 32Z" fill="var(--dk)"/>'
             '<path d="M32 16 40 32 32 48 24 32Z" fill="var(--lt)"/></svg>')

    def kwlist(self, u):
        fx = u.get('keyword_fix') or {}
        return '、'.join(('%s(%s)' % (self.fix(a, fx.get(b)), E(b.upper()))) if b else self.fix(a, fx.get(a))
                        for a, b in u['keywords'])

    def footer(self, u):
        fja, fen = self.meta.get('faction_ja'), self.meta.get('faction_en') or ''
        fname = ('%s (%s)' % (fja, fen.upper())) if fja else fen.upper()
        return ('<div class="foot"><div class="kw"><b>キーワード / Keywords：</b>%s</div>'
                '<div class="badge">%s</div>'
                '<div class="fkw"><b>陣営 / Faction：</b><br><span>%s</span></div></div>'
                % (self.kwlist(u), self.BADGE, E(fname)))

    def header(self, u, sub='', corner=''):
        s = '<div class="hsub">%s</div>' % sub if sub else ''
        c = '<div class="hcorner">%s</div>' % corner if corner else ''
        tags = []
        if u.get('legends'):
            tags.append('レジェンド<i>Legends</i>')
        if u.get('spearhead'):
            tags.append('スピアヘッド<i>Spearhead</i>')
        lg = ''.join('<div class="hlgd">%s</div>' % t for t in tags)
        nm = u['name']
        en = '<span class="en">%s</span>' % E(nm['en']) if nm.get('en') else ''
        return ('<div class="head"><div class="hname">%s%s</div>%s<div class="htags">%s</div>%s</div>'
                % (self.fix(nm['ja'], nm.get('fix')), en, s, lg, c))

    # ---------- 背景 (完成見本写真の透かし) ----------
    BANNER_DIR = os.path.join(HERE, 'bannerImages', 'wm')

    def banner(self, u):
        fn = (u.get('id') or '') + '.jpg'
        if u.get('id') and os.path.exists(os.path.join(self.BANNER_DIR, fn)):
            return '<div class="bg" style="background-image:url(../bannerImages/wm/%s)"></div>' % E(fn)
        return ''

    # ---------- 表面・裏面 ----------
    def front(self, u, i):
        left = (self.weapon_table('遠隔武器', 'Ranged Weapons', '◈', u['ranged'], self.WEP_R) +
                self.weapon_table('近接武器', 'Melee Weapons', '⚔', u['melee'], self.WEP_M) +
                self.weapon_notes(u))
        if not left:
            left = '<p class="none">武器なし / No weapons</p>'
        right = self.panel('アビリティ', 'Abilities', ''.join(self.render_ability(a) for a in u['abilities']), 'ab%d' % i)
        return ('<div class="card front" data-i="%d">%s%s%s<div class="body">'
                '<div class="colL fit">%s</div><div class="colR">%s</div></div>%s</div>'
                % (i, self.banner(u), self.header(u), self.stats_block(u), left, right, self.footer(u)))

    def back(self, u, i):
        info = []
        if u['points'] is not None:
            info.append('<b>ポイント：</b>%spt' % E(str(u['points'])))
        if u['models'] is not None:
            info.append('<b>モデル数：</b>%s' % E(str(u['models'])))
        if u['base']:
            info.append('<b>ベースサイズ：</b>%s' % E(u['base']))
        if not u['reinforce']:
            info.append('<b>増援不可</b>')
        sub = '　/　'.join(info)

        wg = ''
        if u.get('wargear'):
            w = u['wargear']
            wg = ('<p class="ab">%s</p>' % self.fix(w['ja'] or w['en'], w.get('fix') if w['ja'] else None)) + \
                 ('<p class="en-b">%s</p>' % E(clean(w['en'])) if w['ja'] else '')
        reg = ''.join('<li>%s</li>' % E(clean(r)) for r in u['regiment'] if r)
        reg = '<ul class="bul">%s</ul>' % reg if reg else ''
        notes = '<p class="ab">%s</p>' % E(clean(u['notes_en'])) if u['notes_en'] else ''
        terrain = ''.join(self.render_ability(t) for t in u['terrain'])

        spill = ('<div class="panel spill" id="sp%d"><div class="ph">アビリティ（つづき）'
                 '<i>Abilities (cont.)</i></div><div class="pc" id="spc%d"></div></div>' % (i, i))
        memo = '<div class="memo"><div class="memoh">メモ / MEMO</div>%s</div>' % ('<div class="memol"></div>' * 6)
        return ('<div class="card back" data-i="%d">%s<div class="body body2"><div class="cols fit">'
                '<div class="colL">%s%s%s</div><div class="colR">%s%s</div></div>%s</div>%s</div>'
                % (i, self.header(u, sub, 'data_version %s' % E(str(self.meta.get('data_version', '')))),
                   self.panel('装備オプション', 'Wargear Options', wg, cls='wargear'),
                   self.panel('地形ルール', 'Terrain Rules', terrain), spill,
                   self.panel('連隊オプション', 'Regiment Options', reg, cls='movable'),
                   self.panel('備考', 'Notes', notes, cls='movable'),
                   memo, self.footer(u)))

    # ---------- 全体 ----------
    def html(self):
        pages = []
        if self.a5:
            for i, u in enumerate(self.units):
                pages.append('<div class="sheet">%s</div>' % self.front(u, i))
                pages.append('<div class="sheet">%s</div>' % self.back(u, i))
        else:
            for k in range(0, len(self.units), 2):
                pair = self.units[k:k + 2]
                f = ''.join(self.front(u, k + j) for j, u in enumerate(pair))
                b = ''.join(self.back(u, k + j) for j, u in enumerate(pair))
                if len(pair) == 1:
                    f += '<div class="card blank"></div>'; b += '<div class="card blank"></div>'
                pages.append('<div class="sheet">%s</div>' % f)
                pages.append('<div class="sheet">%s</div>' % b)
        css = open(os.path.join(HERE, 'card.css'), encoding='utf-8').read()
        pal = palette(FX.colors(self.meta.get('faction_slug'), self.meta.get('alliance')))
        css += '\n:root{%s}\n' % ''.join('--%s:%s;' % (k, v) for k, v in pal.items())
        if self.a5:
            css += ('\n@page{size:A5 landscape;margin:0;}\n.sheet{width:210mm;height:148mm;}\n'
                    '.card{height:148mm;}\n.card:first-child::after{content:none;}\n')
        script = open(os.path.join(HERE, 'fit.js'), encoding='utf-8').read()
        m = self.meta
        title = '%s ウォースクロールカード' % (m.get('title_ja') or m.get('faction_ja') or m.get('title_en'))
        return ('<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><title>%s</title>'
                '<style>%s</style></head><body>%s<script>%s</script></body></html>'
                % (E(title), css, ''.join(pages), script))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('units', nargs='?', default='units.json')
    ap.add_argument('-o', '--out', default='cards.html')
    ap.add_argument('--notes', action='store_true', help='誤訳の理由を注記として表示する')
    ap.add_argument('--a5', action='store_true', help='A5 横・1ページ1枚で組む (既定は A4 縦に2枚)')
    a = ap.parse_args()
    c = Cards(json.load(open(a.units, encoding='utf-8')), show_notes=a.notes, a5=a.a5)
    open(a.out, 'w', encoding='utf-8').write(c.html())
    print('%s: %d ユニット' % (a.out, len(c.units)))
    for old in dict.fromkeys(Cards.unmatched):
        print('警告: 訂正の誤訳箇所が本文に見つからない: %s' % old, file=sys.stderr)


if __name__ == '__main__':
    main()
