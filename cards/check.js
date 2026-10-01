// カードがはみ出していないかを確認する。
//   node check.js <書籍ディレクトリ>/cards.html [...]
//   node check.js --all            # cards/*/cards.html と cards_a5.html をまとめて
// はみ出しが 0 なら終了コード 0。CI 的に使える。
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');

(async () => {
  let files = process.argv.slice(2);
  if (files[0] === '--all' || files.length === 0) {
    const root = __dirname;
    files = fs.readdirSync(root)
      .flatMap(d => ['cards.html', 'cards_a5.html'].map(f => path.join(root, d, f)))
      .filter(f => fs.existsSync(f));
  }
  const b = await chromium.launch();
  const p = await b.newPage();
  let ng = 0;
  for (const f of files) {
    await p.goto('file://' + path.resolve(f), { waitUntil: 'networkidle' });
    await p.waitForFunction("document.body.dataset.ready==='1'", { timeout: 300000 });
    const r = await p.evaluate(() => {
      const over = []; let spill = 0, cards = 0, small = [];
      document.querySelectorAll('.card').forEach(c => {
        if (c.classList.contains('blank')) return;
        if (c.classList.contains('front')) cards++;
        const nm = c.querySelector('.hname') ? c.querySelector('.hname').childNodes[0].textContent : '?';
        c.querySelectorAll('.card.front > .body > .colL, .card.front > .body > .colR, .card.back .cols > .colL, .card.back .cols > .colR')
          .forEach(e => {
            if (e.scrollHeight - e.clientHeight > 1) over.push(nm);
            const fs2 = parseFloat(e.style.fontSize) || 2.5;
            if (fs2 / 2.5 < 0.7) small.push(nm + '(' + Math.round(fs2 / 2.5 * 100) + '%)');
          });
        if (c.querySelector('.spill')) spill++;
      });
      return { over, spill, cards, small };
    });
    const name = path.basename(path.dirname(f))
      + (path.basename(f) === 'cards_a5.html' ? ' (A5)' : '');
    if (r.over.length) ng++;
    console.log(`${name.padEnd(40)} ${String(r.cards).padStart(4)}枚  裏送り${String(r.spill).padStart(2)}` +
      (r.over.length ? `  はみ出し ${r.over.length}: ${r.over.slice(0, 5).join(', ')}` : '') +
      (r.small.length ? `  極小 ${r.small.slice(0, 3).join(', ')}` : ''));
  }
  await b.close();
  if (ng) { console.log(`\nはみ出しのある書籍: ${ng}`); process.exit(1); }
  console.log('\nはみ出しなし');
})();
