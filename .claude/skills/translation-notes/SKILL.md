---
name: translation-notes
description: official_translations/ の公式訳（書籍などから書き写した日本語）の既知の誤訳・誤植を translation_notes.json で管理し、md 生成時に本文中で「~~誤~~==正==」の形に訂正する。新しい誤訳を登録したい、データ更新後に誤訳が残っているか確認したい、resolved になった注を整理したい、といった依頼で使う。「訳注を追加して」「誤訳の訂正を登録して」「translation_notes.json を更新して」など。40k リポジトリの translation-notes と同じ考え方。
---

# 訳注（既知の誤訳・誤植）管理スキル

AoS の md に出る日本語は、すべて `official_translations/` / `own_translations/` から来る（dump.json に日本語は無い）。
公式訳は書籍どおりに載せる方針なので、書籍の誤訳・誤植は訳ファイルでは直さず、リポジトリ直下の
`translation_notes.json` に訳注として登録する。抽出スクリプト（extract-warscrolls / extract-faction-rules /
extract-spearheads）は生成時にこのファイルを読み、`status: open` の項目の `fix_ja` を本文中に書き込む
（40k の extract-core-rules と同じ表記。取り消し線が誤り、ハイライトが訂正）。

```
- 効果: …戦場に配置されていた場合、自軍は追加で==D==3再集結ポイントを得る。
**キーワード:** 歩兵、~~豪傑~~==豪傑（1/10）==、旗手（1/10）、…
```

共通部分が短い訂正は全体を差し替えて見せる。本文の `**` は残す。訂正文が無い注や、訂正箇所が本文に
見つからなかった注だけは、従来どおり該当箇所の直後に `> [!warning] 訳注` のコールアウト（説明と訂正）として出す
（アビリティは字下げしてその項目の下、武器名は武器表の後、キーワードはキーワード行の後）。
訂正を探す範囲は、アビリティならそのアビリティの行、武器名は武器表、キーワードはキーワード行、装備オプション（`wargear_option_texts`）はその行に限る。

## データ形式

```json
{
 "checked_data_version": 483,
 "notes": [
  {
   "faction": "daughters_of_khaine",          // 訳ファイル official_translations/<faction>.json
   "tr_section": "ability_texts",             // 訳ファイルのセクション
   "tr_key": "Icon of Slaughter",             // 訳ファイルのキー（"ユニット|名前" や "Spearhead|…" もそのまま）
   "tr_field": "effect",                      // ability_texts のフィールド（名前だけのセクションは null）
   "table": "warscroll_ability",              // 英語側の dump.json テーブル
   "id": "df187102-…",                         // 英語側のレコード id
   "en_field": "effect",                      // 英語側のフィールド
   "name": "Icon of Slaughter",               // 目印（英語名）
   "ja": "自軍は追加で3再集結ポイントを得る",     // 誤訳を特定する日本語の部分文字列
   "en": "you receive D3 additional rally points", // 対応する英語の部分文字列
   "note": "英語版は「…」。日本語版（書籍 p.62）の「…」は誤り。",  // 理由（カードの --notes、訂正できないときの md の訳注）
   "issue": "A. 数値の誤り",                   // 分類
   "status": "open",                          // open | resolved | en_changed | missing
   "since": 483,                              // 登録時の data_version
   "fix_ja": {"追加で3再集結ポイント": "追加でD3再集結ポイント"}  // 訂正（下記）
  }
 ]
}
```

### `fix_ja` — 訂正データ（必ず併せて登録する）

- 文字列 … `ja` をその文字列に置き換える
- オブジェクト `{誤訳箇所: 修正後}` … 複数箇所、または `ja` とは別の範囲を置き換えるとき
- md では本文中の誤訳箇所が `~~誤~~==正==` になる（照合は `**` と空白を無視）。訳ファイルの本文自体は書籍どおりのまま

照合は `**`・HTML の除去、NFKC、空白の畳み込み、引用符の統一のうえで**部分一致**。`check` は `open` の項目について
`fix_ja` のキーが本文に残っているかも確認し、無ければ警告する。

## 使い方

```bash
TN=.claude/skills/translation-notes/scripts/translation_notes.py

python3 $TN check --dump dump.json            # 状態が変わる項目を表示（変化ありなら終了コード 3）
python3 $TN check --dump dump.json --update   # 結果を translation_notes.json に書き戻す（refresh-data が自動で実行）
python3 $TN list --dump dump.json             # 登録済みの一覧
```

## 状態の意味

| status | 意味 | 生成時 |
|---|---|---|
| `open` | 訳ファイルに `ja`、dump.json に `en` が残っている（誤訳が残っている） | 本文を訂正する |
| `resolved` | 訳ファイルの日本語が変わった（新しい版の書籍で直ったなど。`resolved_in` に data_version） | 出さない |
| `en_changed` | 英語側が変わった。注の前提を見直す | 出さない |
| `missing` | 訳ファイルのキー／フィールド、または dump.json のレコードが無い | 出さない |

## 新しい注の追加手順

1. 誤訳・誤植の箇所を確認する（書籍のスキャン、`official_translations/<faction>.json` の該当キー）
2. dump.json で英語のレコード（table / id / フィールド）と、誤訳箇所を一意に特定できる `ja` / `en` の部分文字列を決める
3. `translation_notes.json` の `notes` に 1 件追加し（**`fix_ja` も入れる**）、`check` で `open` になることを確認する
4. `refresh-data --no-fetch` などで再生成し、該当 md の本文に `~~誤~~==正==` が入る（`> [!warning] 訳注` に回っていない）ことを確認する

訳ファイルの本文は書籍どおりのまま触らない（訳注で訂正する）。
