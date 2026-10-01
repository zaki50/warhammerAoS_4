# -*- coding: utf-8 -*-
"""dump.json の warscroll.bannerImage を全部ダウンロードして cards/bannerImages/ に置く (40k から流用)。

  python3 fetch_images.py                 # 未取得のぶんだけ取る (再実行で続きから)
  python3 fetch_images.py --field rowImage --out rowImages
  python3 fetch_images.py --force         # 既にあるファイルも取り直す

保存名は warscroll の id (<uuid>.jpg)。どのユニットのものかは同じフォルダの
index.json を見る。画像は Games Workshop のもので容量も大きい (banner で約260MB)
ため、リポジトリには入れない (.gitignore 済み)。
"""
import argparse, json, os, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EXT = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp', 'image/gif': '.gif'}


def targets(dump, field):
    d = json.load(open(dump, encoding='utf-8'))['data']
    pub = {p['id']: p['name'] for p in d['publication']}
    wp = {}
    for x in d['warscroll_publication']:
        wp.setdefault(x['warscrollId'], pub.get(x['publicationId'], ''))
    out = []
    for r in d['warscroll']:
        if not r.get(field):
            continue
        out.append({'id': r['id'], 'url': r[field], 'name_en': r['name'], 'name_ja': '',
                    'publication': wp.get(r['id'], '')})
    return out


def fetch(t, outdir, force):
    hit = [f for f in os.listdir(outdir) if f.startswith(t['id'] + '.')]
    if hit and not force:
        return hit[0], None
    req = urllib.request.Request(t['url'], headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read()
            ext = EXT.get(r.headers.get('Content-Type', '').split(';')[0].strip(), '.bin')
    except (urllib.error.URLError, OSError) as e:
        return None, '%s %s: %s' % (t['id'], t['name_en'], e)
    fn = t['id'] + ext
    open(os.path.join(outdir, fn), 'wb').write(body)
    return fn, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dump', default=os.path.join(REPO, 'dump.json'))
    ap.add_argument('--field', default='bannerImage', help='bannerImage (既定) / rowImage')
    ap.add_argument('--out', help='保存先 (既定: cards/<field の複数形>)')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--workers', type=int, default=8)
    a = ap.parse_args()

    outdir = a.out or os.path.join(HERE, a.field.replace('Image', 'Images'))
    if not os.path.isabs(outdir):
        outdir = os.path.join(HERE, outdir)
    os.makedirs(outdir, exist_ok=True)

    ts = targets(a.dump, a.field)
    print('%s: %d 件 → %s' % (a.field, len(ts), outdir))
    index, errs, done = {}, [], 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for t, (fn, err) in zip(ts, ex.map(lambda t: fetch(t, outdir, a.force), ts)):
            done += 1
            if err:
                errs.append(err)
            else:
                index[t['id']] = {'file': fn, 'name_en': t['name_en'], 'name_ja': t['name_ja'],
                                  'publication': t['publication'], 'url': t['url']}
            if done % 100 == 0 or done == len(ts):
                print('  %d/%d' % (done, len(ts)), flush=True)

    json.dump({'_doc': 'warscroll id → 画像ファイル。python3 cards/fetch_images.py で作る',
               'field': a.field, 'images': index},
              open(os.path.join(outdir, 'index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    total = sum(os.path.getsize(os.path.join(outdir, f)) for f in os.listdir(outdir))
    print('保存 %d 件 / 失敗 %d 件 / 合計 %.0fMB' % (len(index), len(errs), total / 1e6))
    for e in errs[:20]:
        print('  NG', e, file=sys.stderr)
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
