// PDF の書き出し。sides が真なら、表 (奇数ページ) と裏 (偶数ページ) を別ファイルにする。
const path = require('path');

async function writePdf(page, out, sides) {
  const opt = { preferCSSPageSize: true, printBackground: true };
  if (!sides) {
    await page.pdf({ path: out, ...opt });
    return [out];
  }
  const n = await page.evaluate(() => document.querySelectorAll('.sheet').length);
  const base = out.replace(/\.pdf$/, '');
  const range = start => {
    const a = [];
    for (let i = start; i <= n; i += 2) a.push(i);
    return a.join(',');
  };
  const files = [];
  for (const [suf, start] of [['_front', 1], ['_back', 2]]) {
    const f = base + suf + '.pdf';
    await page.pdf({ path: f, pageRanges: range(start), ...opt });
    files.push(f);
  }
  return files;
}

module.exports = { writePdf };
