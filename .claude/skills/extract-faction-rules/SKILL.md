---
name: extract-faction-rules
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の dump.json からファクションルール（バトル特性・バトルフォーメーション・英雄特性・アーティファクト・その他の強化・ロア）をファクション単位で抽出し Markdown 出力する。「○○のバトル特性を取得して」「スケイヴンのフォーメーションを出して」「アーティファクト/呪文ロア一覧を抽出して」といった依頼で使う。40k の extract-detachment-rules に相当。
---

# ファクションルール抽出スキル

Warhammer Age of Sigmar 公式アプリ `com.gamesworkshop.aos4` 同梱の `assets/dump.json` から、
指定ファクションのアーミールール一式を抽出して Markdown 化する。

## 出力内容

ファクションごとに以下のセクションを出力する（存在するもののみ）:

1. **バトル特性** … `ability_group` (`abilityGroupType == battleTraits`)
2. **バトルフォーメーション** … `battle_formation` + `battle_formation_rule`
   （40k のデタッチメントに相当。ポイント付きのものはポイントを付記）
3. **英雄特性** … `heroicTraits`
4. **アーティファクト・オブ・パワー** … `artefactsOfPower`
5. **その他の強化** … `otherEnhancements`（Moulder Mutations 等）
6. **ロア（呪文・祈祷・顕現）** … `lore` + `lore_ability`（詠唱/詠誦値・ポイント付き）

各アビリティはフェイズ・宣言・効果・ポイント・詠唱値付きの箇条書き。
同名グループ（版違い等）を区別できるよう、グループ見出しに出典書籍を付記する。

## データソース

プロジェクトルートの `dump.json` を使う。無い・古い場合は `fetch-dump` スキルで端末から取得する。
**dump.json は英語のみ**（`--lang` オプションは無い）。

## 使い方

スクリプト: `scripts/extract_faction_rules.py`（Python 3 標準ライブラリのみ）

```bash
SKILL=.claude/skills/extract-faction-rules/scripts/extract_faction_rules.py

# ファクションルールを持つファクション一覧（フォーメーション/特性グループ/ロアの件数付き）
python3 $SKILL --dump dump.json --list

# ファクション名(部分一致)で抽出。
# 既定で faction_rules/<ファクション>_faction_rules.md に保存される
python3 $SKILL --dump dump.json --faction "Skaven"

# id 直接指定 / 全ファクション一括
python3 $SKILL --dump dump.json --faction-id fc32e7a5-c952-430a-bcda-9aba4195c181
python3 $SKILL --dump dump.json --all
```

### 出力先

- 既定で **`faction_rules` ディレクトリ**に `<ファクション名のスラッグ>_faction_rules.md` として保存。
- `-o <ファイル名>` … ファイル名のみなら `faction_rules/` 配下、パス付きならその場所に保存。
- `--outdir <dir>` … 保存先ディレクトリを変更（既定 `faction_rules`）。
- `--stdout` … 標準出力へ（`--all` とは併用不可）。

## 注意点

- **Spearhead 収録のグループは除外**する（`ability_group_publication` の紐付け先が
  Spearhead 出版物のもの。`extract-spearheads` スキルが担当）。
- `abilityGroupType` が未設定のグループ（Unbind 等の汎用コアアビリティ、約50件）は
  ファクションに属さないため対象外。
- **レジメント・オブ・リナウン**（`abilityGroupType == regimentOfRenown`）は
  ファクション横断の別概念のため、このスキルでは出力しない。
- ウォースクロールは `extract-warscrolls`、バトルタクティックは `extract-battle-tactics`。
