---
name: extract-core-rules
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の dump.json からコアルールと上級ルール（最新の General's Handbook のもの）の全文を 1 本の Markdown (core_rules.md) に書き出す。英語は dump.json、日本語は公式 PDF から書き写した official_translations/core_rules.json を当て、日英併記にする。「コアルールを再生成して」「core_rules.md を作り直して」「コアルールで○○のルールを調べて」「コアルールの訳を足して」といった依頼で使う。40k の extract-core-rules に相当。
---

# コアルール抽出スキル

`core_rules.md` を `dump.json` から生成する。AoS の dump.json は英語だけなので、日本語は公式 PDF
（コアルール、ルール・アップデート）から書き写した `official_translations/core_rules.json` を当てる。

## データの構造

- `publication` … `Core Rules` と、いちばん新しい `General's Handbook YYYY-YY: Advanced Rules`
- `rule_section`（章。`parentId` で入れ子、`displayOrder` 順）→ `rule_container`（節）→
  `rule_container_component`（本文。`text` / `boxedText` / `textBold` / `textItalic` / `header` / `accordion` /
  `bullets`（本文は `bullet_point`）/ `ability`（`ability` を参照）/ `image`）
- アプリの本文には追加・エラッタが**反映済み**。章末の「Addenda, Errata and FAQs」はその一覧と FAQ

## 使い方

```bash
SKILL=.claude/skills/extract-core-rules/scripts/extract_core_rules.py
python3 $SKILL --dump dump.json                  # core_rules.md
python3 $SKILL --dump dump.json --check          # 訳なし・英語が改訂された訳・未使用の訳
python3 $SKILL --dump dump.json --lookups x.json # 訳の当て先（英語と en_hash つき）
```

`refresh-data` からも呼ばれる。

## 訳ファイル `official_translations/core_rules.json`

```json
{
 "titles": {"5.1 Keywords": "5.1 キーワード"},
 "texts": {"<段落または箇条書きの id>": {"at": "5.0 Abilities > 5.1 Keywords", "en_hash": "1a2b3c4d", "ja": "…"}},
 "abilities": {"<ability の id>": {"at": "…", "en_hash": "…", "name": "…", "timing": "…", "used_by": "…",
                                   "declare": "…", "effect": "…", "keywords": "…", "lore": "…"}}
}
```

- `en_hash` は訳したときの英語のハッシュ（`--lookups` に出る値）。**アプリの改訂で英語が変わった訳は使わず英語で出し**、
  `--check`（と `check-translations`）に「英語が改訂された」として出る。新しい日本語を確かめてから `ja` と `en_hash` を直す
- 書き写す文は紙面どおり。段落の区切りは `\n\n`、箇条書きの行は `• `、太字は `**…**`
- 上級ルールは毎年の General's Handbook で改訂される。日本語版の資料が無い段落は訳を置かず、英語のまま出す
- 誤訳・誤植は `translation_notes.json` に `faction: "core_rules"` で登録する
  （`tr_section` は `texts`（`tr_field: "ja"`）か `abilities`（`tr_field` は欄名）、`tr_key` は id、
  `table` は `rule_container_component`（`textContent`）/ `bullet_point`（`text`）/ `ability`）。本文中に `~~誤~~==正==` で出る

## 出力の形

- `## コアルール` → `### 章` → `#### 5.0 アビリティ(Abilities)` → `##### 5.1 キーワード(Keywords)`
- 本文は日本語、英語は `> [!quote]- EN`（折りたたみ）。日本語が無いものは英語だけ
- アビリティと赤枠（boxedText）は引用枠（`>`）。図は `![代替文](url)`
