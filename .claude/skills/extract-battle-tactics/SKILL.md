---
name: extract-battle-tactics
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の dump.json からマッチプレイのバトルタクティックカード（General's Handbook）を抽出し Markdown 出力する。「バトルタクティックを取得して」「バトルタクティックカード一覧を出して」といった依頼で使う。AoS 4版に策略(ストラタジェム)は無く、40k の extract-stratagems に最も近い汎用戦術要素として本スキルが対応する。
---

# バトルタクティックカード抽出スキル

Warhammer Age of Sigmar 公式アプリ `com.gamesworkshop.aos4` 同梱の `assets/dump.json` から、
マッチプレイ（General's Handbook バトルパック）の**バトルタクティックカード**を抽出して
Markdown 化する。

AoS 4版には 40k の策略（ストラタジェム）に当たるものが無い。ファクション固有の
「使い所のあるアビリティ」はウォースクロール／ファクションルール側に統合されており、
汎用の戦術選択肢はこのバトルタクティックカードが担う。

## 出力内容

バトルパック（General's Handbook）ごとに、各カードについて:

- **カード効果**（`rulesText`: カード全体に適用されるセットアップ・特殊ルール）
- **3 種のバトルタクティック**（Strike / Affray / Domination、各 VP と達成条件）

## データソース

プロジェクトルートの `dump.json` を使う。無い・古い場合は `fetch-dump` スキルで端末から取得する。
**dump.json は英語のみ**（`--lang` オプションは無い）。

## 使い方

スクリプト: `scripts/extract_battle_tactics.py`（Python 3 標準ライブラリのみ）

```bash
SKILL=.claude/skills/extract-battle-tactics/scripts/extract_battle_tactics.py

# 既定: ./battle_tactics.md に保存
python3 $SKILL --dump dump.json

# 出力先を指定 / 標準出力へ
python3 $SKILL --dump dump.json -o out/battle_tactics.md
python3 $SKILL --dump dump.json --stdout
```

## 注意点

- カードはファクションに紐づかない汎用要素のため、出力は 1 ファイル（既定 12 カード）。
- データ構造: `battle_tactic_card`（`battlepackId` で `battlepack` = GHB に紐づく）
  ↔ `battle_tactic`（`battleTacticCardId`、`battleTacticType`: strike/affray/domination、
  `victoryPoints`）。
- 関連スキル: ウォースクロール `extract-warscrolls` / ファクションルール
  `extract-faction-rules` / Spearhead `extract-spearheads` / dump 取得 `fetch-dump`。
