---
name: extract-spearheads
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の dump.json から Spearhead 情報（固定編成のユニット詳細・バトル特性・レジメントアビリティ・強化）を抽出し、ファクション別に Markdown 出力する。「Spearhead を抽出して」「○○のスピアヘッドを出して」といった依頼で使う。40k の extract-combat-patrols に相当。
---

# Spearhead 抽出スキル

Warhammer Age of Sigmar 公式アプリ `com.gamesworkshop.aos4` 同梱の `assets/dump.json` から、
各 **Spearhead**（固定編成の小規模ゲームモード。40k の Combat Patrol 相当）の情報を抽出し、
ファクションごとのディレクトリに 1 Spearhead 1 ファイルで保存する。

## データソース

プロジェクトルートの `dump.json` を使う。無い・古い場合は `fetch-dump` スキルで端末から取得する。
**dump.json は英語のみ**（`--lang` オプションは無い）。

## 使い方

スクリプト: `scripts/extract_spearheads.py`（Python 3 標準ライブラリのみ）

```bash
SKILL=.claude/skills/extract-spearheads/scripts/extract_spearheads.py

# 一覧表示(ファクション名 + Spearhead 名 + ユニット数)
python3 $SKILL --dump dump.json --list

# 全 Spearhead を spearheads/ 配下に出力(既定)
python3 $SKILL --dump dump.json

# ファクションで絞り込み
python3 $SKILL --dump dump.json --faction "Skaven"
python3 $SKILL --dump dump.json --faction-id fc32e7a5-c952-430a-bcda-9aba4195c181

# 出力先を変更
python3 $SKILL --dump dump.json --outdir sp
```

## 出力

- **出力先**: 既定で `spearheads/<ファクション名>/<Spearhead 名>.md`
  （ディレクトリは自動作成。ファイル/フォルダ名の `/` 等は `-` に置換）。
- `--outdir <dir>` で保存先ディレクトリを変更。

### 各ファイルの内容

1. **編成** … 収録ユニットの一覧（モデル数付き）
2. **ユニット詳細** … 各ユニットの Spearhead 版ウォースクロール
   （ステータス・武器・アビリティ・キーワード。固定編成のためポイントは無い）
3. **バトル特性** … その Spearhead 固有のバトル特性（存在する場合）
4. **レジメントアビリティ** … ターンごとに 1 つ選ぶアビリティ（4 種）
5. **強化** … ジェネラルに与える強化（4 種）

## 補足

- Spearhead は publication（`spearheadName` 持ち / 名前が "Spearhead: ..."）として表現され、
  ユニットは `warscroll_publication` 経由の `isSpearhead == true` なウォースクロール、
  各種アビリティは `ability_group_publication` 経由の `ability_group`
  （`battleTraits` / `regimentAbilities` / `spearheadEnhancements`）が紐づく。
- アーミーに属さないシーズン Battlepack（Fire and Jade / Sand and Bone 等の
  コアアビリティ・地形ルール・レリック）は `spearheads/共通ルール/` 配下に出力する。
- 通常モードのウォースクロールは `extract-warscrolls`、ファクションルールは
  `extract-faction-rules`、dump 取得は `fetch-dump`。
