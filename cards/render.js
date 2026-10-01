// cards.html を PDF に書き出す:  node render.js cards.html cards.pdf [--sides]
// 複数まとめて出すなら make.py --all（ブラウザを1つ使い回すのでこちらが速い）
//
// --sides を付けると、1ページ1枚で表・裏が交互に並ぶ HTML (cards_a5.html) を
// 奇数ページ = 表面、偶数ページ = 裏面 の 2 ファイルに分けて書き出す
// (out が cards_a5.pdf なら cards_a5_front.pdf / cards_a5_back.pdf)。片面印刷しか
// できないプリンタで、表を刷ってから紙を戻して裏を刷るための出力。
const { chromium } = require('playwright');
const path = require('path');
const { writePdf } = require('./pdf_sides');
(async () => {
  const args = process.argv.slice(2).filter(a => a !== '--sides');
  const sides = process.argv.includes('--sides');
  const src = path.resolve(args[0] || 'cards.html');
  const out = path.resolve(args[1] || 'cards.pdf');
  const b = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.waitForFunction("document.body.dataset.ready==='1'", { timeout: 300000 });
  for (const f of await writePdf(p, out, sides)) console.log(f);
  await b.close();
})();
