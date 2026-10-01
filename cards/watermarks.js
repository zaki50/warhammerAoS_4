// bannerImages/*.jpg から、カードの背景にそのまま敷ける「透かし画像」を作る。
//   node watermarks.js [bannerImages ディレクトリ] [--opacity 0.5] [--crop-left 0.15]
//                        [--shift-down 15] [--no-fade] [--placeholder-min 4]
//                        [--only <id の一部>[,...]] [--force]
//
// CSS の opacity / mask で薄くすると PDF に透明度が残り、ビューアによっては
// (macOS のプレビュー等) 背景が表示されない。そこで白地に薄く重ねた状態と
// 上端のフェードを画像そのものに焼き込み、不透明な JPEG として書き出す。
// 出力は <bannerImages>/wm/<元のファイル名>。
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), crypto = require('crypto');

const argv = process.argv.slice(2);
// 値を取るオプション。この直後の引数はディレクトリ指定と間違えないようにする
const VALUE_FLAGS = new Set(['--opacity', '--crop-left', '--shift-down', '--placeholder-min', '--only']);
const opt = n => { const i = argv.indexOf(n); return i < 0 ? null : argv[i + 1]; };
const positional = argv.filter((a, i) => !a.startsWith('--') && !VALUE_FLAGS.has(argv[i - 1]));
const SRC = path.resolve(positional[0] || path.join(__dirname, 'bannerImages'));
const OPACITY = parseFloat(opt('--opacity') || '0.5');
// AoS の bannerImage (1024×500) はモデルが中央にあるので、既定では左端を切り落とさない
// (40k の元画像は左に余白が多いので 40k 側の既定は 0.15)
const CROP_LEFT = parseFloat(opt('--crop-left') || '0');
// 画像をカード上で何 mm 下げるか。画像は下端合わせなので、下端をそのぶん切り落とすと
// 中身全体が下へ移動し、上に白い余白ができる。フェードは下で計算し直すので、
// これまで白く飛んでいた画像の上のほう (顔など) が見えるようになる
const SHIFT_DOWN_MM = parseFloat(opt('--shift-down') || '15');
const FORCE = argv.includes('--force');
const NO_FADE = argv.includes('--no-fade');   // 上端のフェードを付けない (一様な濃さ)
// 試すとき用: ファイル名に含まれるものだけ作る (カンマ区切りで複数指定できる)
const ONLY = (opt('--only') || '').split(',').map(x => x.trim()).filter(Boolean);
// カード上で画像は下端合わせ・幅いっぱい (background-size:100% auto) に置かれる。
// 画像の上端がそのまま横一直線の境目になってしまうので、そこだけ短く白へ溶かす。
// 既定の切り抜きだと画像の上端はカード上端から約 42mm なので、40mm〜55mm を指定すると
// 上端から 13mm ほどのフェードになる (40mm は画像より上なので実質は上端から始まる)。
// 切り抜き方で画像の縦横比が変わるので、フェード位置は毎回そこから計算する。
const CARD_W = 210, CARD_H = 148, FADE_TOP_MM = 40, FADE_END_MM = 55;

// 名前の違う PLACEHOLDER_MIN ユニット以上が同じ画像を使っていたら、それはその
// ユニットの写真ではなく書籍共通の代用画像 (扉絵)。背景にすると書籍じゅうのカードが
// 同じ絵になってしまうので使わない。Imperial Armour や Legends で多い。
// 書籍はまたいで数える (タイタン系のように同じ扉絵が 2 冊に分かれている例があるため)。
// 本物の写真を誤って落とさないよう、しきい値は高め (4) にしてある
// (CP 版とコデックス版で同じ写真を使っている正常なケースは 2 なので巻き込まない)。
const PLACEHOLDER_MIN = parseInt(opt('--placeholder-min') || '4', 10);
function placeholders(dir) {
  const ix = path.join(dir, 'index.json');
  if (!fs.existsSync(ix)) return new Set();
  const images = JSON.parse(fs.readFileSync(ix, 'utf8')).images || {};
  const byHash = new Map();
  for (const v of Object.values(images)) {
    const p = path.join(dir, v.file);
    if (!fs.existsSync(p)) continue;
    const h = crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
    if (!byHash.has(h)) byHash.set(h, []);
    byHash.get(h).push(v);
  }
  const out = new Set();
  for (const v of byHash.values()) {
    const names = new Set(v.map(x => x.name_en));
    if (names.size >= PLACEHOLDER_MIN) v.forEach(x => out.add(x.file));
  }
  return out;
}

(async () => {
  const out = path.join(SRC, 'wm');
  fs.mkdirSync(out, { recursive: true });
  const skip = placeholders(SRC);
  const files = fs.readdirSync(SRC)
    .filter(f => /\.(jpg|jpeg|png|webp)$/i.test(f)
      && (!ONLY.length || ONLY.some(o => f.includes(o))));
  // 代用画像だと分かったものは、以前に作った透かしがあれば消しておく
  let removed = 0;
  for (const f of files) {
    if (!skip.has(f)) continue;
    const dst = path.join(out, f.replace(/\.(png|webp)$/i, '.jpg'));
    if (fs.existsSync(dst)) { fs.unlinkSync(dst); removed++; }
  }
  console.log(`代用画像 ${skip.size} 件は背景に使わない${removed ? ` (作成済みの ${removed} 件を削除)` : ''}`);
  // file:// の画像を canvas に読み込むので file アクセスを許可する
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage();
  await p.goto('file://' + path.join(SRC, 'index.json'));
  let done = 0, made = 0;
  for (const f of files) {
    const dst = path.join(out, f.replace(/\.(png|webp)$/i, '.jpg'));
    done++;
    if (skip.has(f)) continue;
    if (fs.existsSync(dst) && !FORCE) continue;
    const data = await p.evaluate(async ([name, alpha, crop, shiftMM, cardW, cardH, fadeTop, fadeEnd]) => {
      const img = new Image();
      img.src = './' + name;
      await img.decode();
      const sx = Math.round(img.naturalWidth * crop);
      const w = img.naturalWidth - sx;
      // 下端を shiftMM 相当だけ切り落とす = カード上で中身がそのぶん下がる
      const sh = Math.min(Math.round(shiftMM * w / cardW), img.naturalHeight - 1);
      const c = document.createElement('canvas');
      c.width = w; c.height = img.naturalHeight - sh;
      const x = c.getContext('2d');
      x.fillStyle = '#fff'; x.fillRect(0, 0, c.width, c.height);
      x.globalAlpha = alpha;
      x.drawImage(img, sx, 0, c.width, c.height, 0, 0, c.width, c.height);
      x.globalAlpha = 1;
      if (fadeEnd > 0) {
        // カード上での見え方からフェードの位置を割り出す (画像は幅いっぱい・下端合わせ)
        const hMM = cardW * c.height / c.width, topMM = cardH - hMM;
        const clamp = v => Math.min(1, Math.max(0, v));
        const f0 = clamp((fadeTop - topMM) / hMM), f1 = clamp((fadeEnd - topMM) / hMM);
        const g = x.createLinearGradient(0, 0, 0, c.height);
        g.addColorStop(0, '#fff');
        g.addColorStop(f0, '#fff');
        g.addColorStop(Math.max(f1, f0 + 0.001), 'rgba(255,255,255,0)');
        x.fillStyle = g; x.fillRect(0, 0, c.width, c.height);
      }
      return c.toDataURL('image/jpeg', 0.85).split(',')[1];
    }, [f, OPACITY, CROP_LEFT, SHIFT_DOWN_MM, CARD_W, CARD_H, FADE_TOP_MM, NO_FADE ? 0 : FADE_END_MM]);
    fs.writeFileSync(dst, Buffer.from(data, 'base64'));
    made++;
    if (made % 100 === 0) console.log(`  ${done}/${files.length}`);
  }
  await b.close();
  const size = fs.readdirSync(out).reduce((s, f) => s + fs.statSync(path.join(out, f)).size, 0);
  console.log(`透かし画像 ${made} 件作成 / 合計 ${fs.readdirSync(out).length} 件 ${(size / 1e6).toFixed(0)}MB → ${out}`);
})();
