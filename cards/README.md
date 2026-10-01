# ウォースクロールカード生成

公式アプリのデータ（リポジトリ直下の `dump.json`）と日本語訳（`official_translations/` / `own_translations/`）、
訳注（`translation_notes.json`）から、A5 横のウォースクロールカードを両面印刷用の PDF にする。
warhammer40k_11 の `cards/`（データシートカード）と同じ作り・同じ表示規則にしてある。`warscrolls/*.md` は経由しない。

用紙に合わせて 2 種類の PDF を出す。**A4 縦に2枚**（刷ってから切る）と、**A5 横に1枚**（表面だけ・裏面だけの 2 ファイル）。

## クイックスタート

```sh
cd cards
python3 make.py daughters_of_khaine          # 組のスラッグ（部分一致可）
python3 make.py khainite_shadow_coven         # Spearhead の組は spearhead_<名前>
python3 make.py --list                        # 組の一覧（ファクション 84、Spearhead 52）
python3 make.py --all                         # 全部の組を一括生成
python3 make.py daughters_of_khaine --notes   # 誤訳の訂正箇所に理由の注記を付ける
python3 make.py daughters_of_khaine --no-pdf  # HTML まで（Node/Playwright が無い環境用）
python3 make.py daughters_of_khaine --no-a5   # A4 2面付けだけ
python3 make.py --check                       # はみ出し確認（= node check.js --all、0 なら終了コード 0）
```

組（set）の単位は md と同じ。**ファクション**ごと（Spearhead 版とグランドアライアンスは除く）と、**Spearhead** ごと。

出力は 2 か所に分かれる。

| 場所 | ファイル | 中身 |
|---|---|---|
| `cards/<スラッグ>/`（リポジトリ内） | `units.json` / `cards.html` / `cards_a5.html` | 抽出したデータと HTML |
| Dropbox `2_Warhammer/AoS 4版/original_cards/` | `<スラッグ>_cards.pdf` | A4 縦・1ページに2枚 |
| 同上 | `<スラッグ>_cards_a5_front.pdf` / `_back.pdf` | A5 横・1ページ1枚、表面だけ／裏面だけ |

PDF の出力先は `--pdf-dir` か環境変数 `AOS_CARDS_PDF_DIR` で変えられる。

## ユニット画像（表面の背景）

40k と同じく、表面にユニットの完成見本写真を薄く敷く（`dump.json` の `warscroll.bannerImage`）。

```sh
python3 cards/fetch_images.py     # 元画像を cards/bannerImages/ に取得（約 1,300 件）
node cards/watermarks.js          # 白地に薄く焼き込んだ透かし版を wm/ に作る
```

`cards/bannerImages/wm/<warscroll id>.jpg` が無いユニットは背景なしで組まれる。画像は GW の著作物なので
リポジトリには入れない（`.gitignore`）。透かしのオプションは 40k の `cards/README.md` と同じ。ただし AoS の画像（1024×500）はモデルが中央にあるので、
`--crop-left` の既定は 0（40k は 0.15）。

## 印刷方法

40k と同じ。A4 版は **A4 縦・長辺とじ**の両面印刷で、中央の破線で切ると A5 横が 2 枚。
A5 版は `_front.pdf` を刷ってから紙を戻して `_back.pdf` を刷る（片面印刷のプリンタ向け）。いずれも等倍で印刷する。

## カードの内容

**表面** — ユニット名（日本語＋英語）／能力値（移動力・体力・防御力・確保力、加護、追加特性）／遠隔武器・近接武器
（武器アビリティを ［クリティカル（致命的）］ のように併記）／アビリティ（タイミング・キーワード・使用者・宣言・効果）／キーワード

**裏面** — 右上に生成に使った dump.json の `data_version`／ポイント・モデル数・ベースサイズ・増援不可／装備オプション／
地形ルール／アビリティ（つづき）／連隊オプション／備考／メモ欄

表面に入りきらないアビリティは、末尾から裏面の「アビリティ（つづき）」へ送る（`fit.js`）。

## 日英の併記・訳注・独自訳（40k と同じ規則）

- 名前は「日本語 英語」（英語はグレーの小さい字）、本文は日本語の下に英語。日本語訳の無い項目は英語だけ
- 訳は md と同じ順で引く（`official_translations/` → `own_translations/`、キーの候補の順は
  `.claude/skills/_lib/aos_translations.py`）。**他ファクションのファイルは参照しない**
- `translation_notes.json` の `status: open` の注は、該当箇所を ~~取り消し線~~ ＋ 修正語（オレンジ）で表示する。
  理由の注記は既定では出さず、`--notes` で表示する
- 独自訳（`own_translations/`）から来た本文にはオレンジの**独自訳**バッジ（ユニット名には付けない）
- キーワードは「日本語(英語の大文字)」。Legends / Spearhead 版は名前欄の右端にタグ
- 訂正の誤訳箇所が本文に見つからないときは、`make.py` / `build.py` が警告を出す

ファクションルール（戦闘特性・戦闘陣形・神器・伝承など）はカードには載せない（md の `faction_rules/` を参照）。

## ファイル構成

| ファイル | 役割 |
|---|---|
| `make.py` | 一括実行の入口 |
| `extract.py` | `dump.json` と訳ファイル・訳注 → `units.json` |
| `build.py` | `units.json` → `cards.html`（レイアウト、訳注の訂正表示、独自訳バッジ） |
| `factions.py` | ファクションごとの配色（未登録はグランドアライアンスの色） |
| `card.css` / `fit.js` / `render.js` / `render_all.js` / `pdf_sides.js` / `check.js` / `watermarks.js` / `fetch_images.py` | 40k から流用（AoS 用の追加は `card.css` の末尾と `fetch_images.py` の対象テーブル） |

**git に入れるのは `units.json` / `cards.html` / `cards_a5.html` とスクリプトだけ。** PDF と画像は `.gitignore`。

**Playwright の場所**: `make.py` は `require('playwright')` が通らないとき `~/.npm/_npx/*/node_modules/playwright` を
探して `NODE_PATH` に足す（`node render_all.js` などを直接叩くときは自分で `NODE_PATH` を通す）。
