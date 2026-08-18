---
name: extract-warscrolls
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の dump.json からウォースクロール（ステータス・武器・アビリティ・キーワード・ポイント・レジメントオプション）をファクション単位で抽出し Markdown 出力する。「○○のウォースクロールを取得して」「スケイヴン/ストームキャスト等のユニットデータを出して」「dump.json から抽出して」といった依頼で使う。40k の extract-datasheets に相当。
---

# ウォースクロール抽出スキル

Warhammer Age of Sigmar 公式アプリ `com.gamesworkshop.aos4` に同梱された全ウォースクロールの
ルール DB（`assets/dump.json`）から、指定ファクションのウォースクロールを抽出して Markdown 化する。

## 抽出単位: faction_keyword（ファクション）

ウォースクロールは `warscroll_faction_keyword` でファクションに M:N で紐づく。
`faction_keyword` にはアーミー（Skaven 等）のほか、グランドアライアンス
（Grand Alliance Order/Chaos/Death/Destruction）やアーミー・オブ・リナウン等の
グルーピングも含まれる。`--list` で件数付き一覧を確認できる。

## データソース

データは APK 内 `assets/dump.json`（約11MB, トップ階層 `metadata` / `data`）に格納されている。
プロジェクトルートの `dump.json` を使う。無い・古い場合は `fetch-dump` スキルで端末から取得する。

**dump.json は英語のみ**（40k 版と異なり `localisations` を持たない）。`--lang` オプションは無い。

## 使い方

スクリプト: `scripts/extract_warscrolls.py`（依存は Python 3 標準ライブラリのみ）

```bash
SKILL=.claude/skills/extract-warscrolls/scripts/extract_warscrolls.py

# 1. ファクション一覧（ウォースクロールを持つもののみ、件数 + id）
python3 $SKILL --dump dump.json --list

# 2. ファクション名（部分一致・大小無視）で抽出。
#    既定で warscrolls/<ファクション>_warscrolls.md に保存される
python3 $SKILL --dump dump.json --faction "Ogor Mawtribes"

# 3. id を直接指定（名前が複数候補に一致する場合）
python3 $SKILL --dump dump.json --faction-id 08135df6-633c-4d58-9adb-7d4b8563b0da

# 4. 全ファクションを warscrolls/ 配下に一括生成（Grand Alliance は除外）
python3 $SKILL --dump dump.json --all

# 5. Spearhead 版ウォースクロールも含める（既定は除外）
python3 $SKILL --dump dump.json --faction "Skaven" --include-spearhead
```

### 出力先

- 既定で **`warscrolls` ディレクトリ**に `<ファクション名のスラッグ>_warscrolls.md` として保存する
  （ディレクトリは自動作成）。
- `-o <ファイル名>` … ファイル名のみなら `warscrolls/` 配下に保存。`-o path/to/x.md` のように
  ディレクトリを含めるとその場所に保存（明示指定が優先。`--all` とは併用不可）。
- `--outdir <dir>` … 保存先ディレクトリを変更（既定 `warscrolls`）。
- `--stdout` … ファイルに保存せず標準出力へ（`--all` とは併用不可）。

## 出力内容（ウォースクロールごと）

ポイント・モデル数・ベースサイズ / ステータス (Move Health Save Control + Ward) /
追加特性（Relentless Discipline 等）/ 射撃・近接武器プロファイル
(A Hit Wnd Rnd D + 武器アビリティ) / アビリティ（フェイズ・宣言・効果・詠唱値・キーワード）/
地形ルール（ファクションテレイン）/ レジメントオプション / キーワード / ノート。

- 戦傷時（battle damaged）プロファイルの武器は「（戦傷時）」を付記。
- Legends / Spearhead 版は見出しに付記。

## 注意点

- **Spearhead 版ウォースクロールは既定で除外**する（Spearhead モード専用の別プロファイル。
  `isSpearhead` フラグで区別され、`extract-spearheads` スキルが担当）。
  含めたい場合は `--include-spearhead`。
- `--all` はグランドアライアンス（Grand Alliance ~）を除外する（下位ファクションと重複するため）。
  必要なら `--faction "Grand Alliance Death"` のように個別指定で抽出できる。
- キーワードは 40k と異なりユニット単位（`warscroll.referenceKeywords`）で、モデル別の差異は無い。
- データ版は出力ヘッダの `data_version` で確認できる（取得時点 466）。

## dump.json のスキーマ要点

`data` 直下は 70 テーブル（リスト）。ウォースクロール組み立てに使う主なもの:

- `warscroll` … 本体。ステータス（`move/health/save/control/wardSave`）・`points`・
  `modelCount`・`baseSize`・`referenceKeywords`・`isSpearhead`・`isLegends` をインラインで持つ。
- `warscroll_faction_keyword` / `faction_keyword` … ファクション紐付け（M:N）。
- `warscroll_weapon` … 武器（`type`: ranged/melee, `attacks/hit/wound/rend/damage`）。
  `warscroll_weapon_weapon_ability` + `weapon_ability` で Crit (Mortal) 等の武器アビリティ。
- `warscroll_ability` … アビリティ（`phaseDetails/declare/effect/castingValue/cpCost`）。
  `warscroll_ability_keyword` + `keyword` でアビリティのキーワード（Spell 等）。
- `warscroll_additional_characteristic` … 追加特性。
- `warscroll_regiment_option` … レジメント編成オプション（`optionText` が表示用文字列）。
- `warscroll_terrain_ability` + `terrain_ability` … ファクションテレインの地形ルール。
- `warscroll_publication` / `publication` … 収録書籍（M:N）。

他にも `battle_formation`, `ability_group`, `lore`, `battle_tactic` 等が同じ JSON に
含まれる（`extract-faction-rules` / `extract-battle-tactics` / `extract-spearheads` が担当）。

## 関連スキル

- `fetch-dump` … dump.json を端末から取得・更新
- `extract-faction-rules` … バトル特性・フォーメーション・強化・ロア
- `extract-battle-tactics` … バトルタクティックカード
- `extract-spearheads` … Spearhead（固定編成モード）
