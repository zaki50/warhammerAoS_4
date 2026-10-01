# -*- coding: utf-8 -*-
"""dump.json からウォースクロールカードの PDF までを一気に作る (40k の cards/make.py に合わせた使い方)。

  python3 make.py daughters_of_khaine        # 組 (ファクション / spearhead_<名前>) のスラッグ。部分一致可
  python3 make.py khainite_shadow_coven       # Spearhead
  python3 make.py --list                      # 組の一覧
  python3 make.py daughters_of_khaine --notes # 誤訳の理由を注記として出す
  python3 make.py daughters_of_khaine --no-pdf
  python3 make.py daughters_of_khaine --no-a5 # A4 2面付けだけ
  python3 make.py --all                       # 全部の組を一括生成
  python3 make.py --check                     # はみ出し確認 (node check.js --all)

units.json と cards.html / cards_a5.html は このスクリプトと同じ場所の <スラッグ>/ 以下に置く。
PDF は印刷して使うものなので Dropbox に書き出す (--pdf-dir か環境変数 AOS_CARDS_PDF_DIR で変えられる)。
1 組につき <スラッグ>_cards.pdf (A4 に2枚) と、A5 横1枚ずつの <スラッグ>_cards_a5_front.pdf / _back.pdf。
"""
import argparse, glob, json, os, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
PDF_DIR = os.environ.get('AOS_CARDS_PDF_DIR') or os.path.expanduser(
    '~/Library/CloudStorage/Dropbox/2_Warhammer/AoS 4版/original_cards')


def node_env():
    """Playwright が通常の require で見つからなければ npx のキャッシュを NODE_PATH で見せる。無ければ None。"""
    env = dict(os.environ)
    if subprocess.run(['node', '-e', "require('playwright')"], env=env, capture_output=True).returncode == 0:
        return env
    for c in sorted(glob.glob(os.path.expanduser('~/.npm/_npx/*/node_modules/playwright')),
                    key=os.path.getmtime, reverse=True):
        e = dict(env, NODE_PATH=os.path.dirname(c) + (os.pathsep + env['NODE_PATH'] if env.get('NODE_PATH') else ''))
        if subprocess.run(['node', '-e', "require('playwright')"], env=e, capture_output=True).returncode == 0:
            return e
    return None


def node(*args):
    env = node_env()
    if env is None:
        print('Playwright が見つからないため PDF 化をスキップします (npm i playwright か npx playwright install chromium)',
              file=sys.stderr)
        return False
    return subprocess.run(['node'] + list(args), env=env).returncode == 0


def write_set(dd, s, notes, no_a5):
    import build as B
    data = dd.build(s)
    d = os.path.join(HERE, s['slug'])
    os.makedirs(d, exist_ok=True)
    json.dump(data, open(os.path.join(d, 'units.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(d, 'cards.html'), 'w', encoding='utf-8').write(B.Cards(data, show_notes=notes).html())
    if not no_a5:
        open(os.path.join(d, 'cards_a5.html'), 'w', encoding='utf-8').write(B.Cards(data, show_notes=notes, a5=True).html())
    return d, data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target', nargs='?')
    ap.add_argument('--dump', default=os.path.join(REPO, 'dump.json'))
    ap.add_argument('--notes', action='store_true', help='誤訳の理由を注記として出す')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--no-pdf', action='store_true')
    ap.add_argument('--no-a5', action='store_true', help='A5 横 1 面付け (cards_a5) を作らない')
    ap.add_argument('--pdf-dir', default=PDF_DIR, help='PDF の出力先 (既定: %(default)s)')
    ap.add_argument('--check', action='store_true', help='はみ出し確認 (check.js --all)')
    a = ap.parse_args()

    if a.check:
        sys.exit(0 if node(os.path.join(HERE, 'check.js'), '--all') else 1)
    import extract, build as B
    dd = extract.Dump(a.dump)
    sets = dd.sets()
    if a.list or not (a.target or a.all):
        for s in sets:
            print('%-48s %4d  %s' % (s['slug'], len(s['units']), s['kind']))
        return
    if a.all:
        todo = sets
    else:
        todo = [s for s in sets if s['slug'] == a.target] or [s for s in sets if a.target.lower() in s['slug']]
        if len(todo) != 1:
            raise SystemExit('組が一意に決まりません: %s (%s)' % (a.target, ', '.join(s['slug'] for s in todo[:8]) or '該当なし'))
    for s in todo:
        d, data = write_set(dd, s, a.notes, a.no_a5)
        m = data['meta']
        print('%-48s %4d ユニット / %s' % (s['slug'], len(data['units']), m.get('title_ja') or m.get('faction_ja') or m['title_en']))
    for old in dict.fromkeys(B.Cards.unmatched):
        print('警告: 訂正の誤訳箇所が本文に見つからない: %s' % old, file=sys.stderr)
    if a.no_pdf:
        return
    os.makedirs(a.pdf_dir, exist_ok=True)
    if a.all:
        node(os.path.join(HERE, 'render_all.js'), HERE, a.pdf_dir)
    else:
        d = os.path.join(HERE, todo[0]['slug'])
        for suf, extra in (('', []),) + ((('_a5', ['--sides']),) if not a.no_a5 else ()):
            node(os.path.join(HERE, 'render.js'), os.path.join(d, 'cards%s.html' % suf),
                 os.path.join(a.pdf_dir, '%s_cards%s.pdf' % (todo[0]['slug'], suf)), *extra)


if __name__ == '__main__':
    main()
