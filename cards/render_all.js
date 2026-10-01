// cards/*/cards.html と cards_a5.html をまとめて PDF 化する（ブラウザを1つ使い回すので速い）。
// A5 のほうは片面印刷用に表 (_front) と裏 (_back) を別ファイルで出す。
//   node render_all.js [cards ディレクトリ] [PDF の出力先]
// 出力先を指定すると、そこに <書籍スラッグ>_cards*.pdf をまとめて置く。
// 省略すると従来どおり各書籍のディレクトリに書き出す。通常は make.py --all から呼ばれる。
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const { writePdf } = require('./pdf_sides');

(async () => {
  const root = path.resolve(process.argv[2] || __dirname);
  const outDir = process.argv[3] ? path.resolve(process.argv[3]) : null;
  if (outDir) fs.mkdirSync(outDir, { recursive: true });
  const dirs = fs.readdirSync(root).filter(d => fs.existsSync(path.join(root, d, 'cards.html')));
  const b = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const p = await b.newPage();
  for (const d of dirs) {
    // cards.html (A4 2面付け) と cards_a5.html (A5 1面付け・表裏を別ファイルに) を PDF にする
    for (const [suf, sides] of [['', false], ['_a5', true]]) {
      const src = path.join(root, d, 'cards' + suf + '.html');
      if (!fs.existsSync(src)) continue;
      await p.goto('file://' + src, { waitUntil: 'networkidle' });
      await p.waitForFunction("document.body.dataset.ready==='1'", { timeout: 300000 });
      const out = outDir ? path.join(outDir, d + '_cards' + suf + '.pdf')
                         : path.join(root, d, d + '_cards' + suf + '.pdf');
      for (const f of await writePdf(p, out, sides)) console.log(f);
    }
  }
  await b.close();
})();
