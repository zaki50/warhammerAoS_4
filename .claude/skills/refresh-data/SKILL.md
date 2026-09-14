---
name: refresh-data
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) のデータを丸ごと最新化する。接続済み Android 端末から dump.json を取り直し(fetch-dump)、warscrolls / faction_rules（ファクション単位）/ battle_tactics.md / spearheads を一括再生成する。「dump.json を更新して .md を作り直して」「データを最新化して全部再生成して」「アプリのデータ更新を反映して」といった、取得と全再生成をまとめて行いたい依頼で使う。
---

# データ一括更新スキル

接続済み Android 端末から最新の `dump.json` を取得し、その内容で全 Markdown
（ウォースクロール・ファクションルール [いずれもファクション単位]・
バトルタクティックカード・Spearhead）を一括再生成する。個別スキル
（`fetch-dump` / `extract-*`）を一つ一つ回す代わりに、アプリのバージョンアップ時などに
「取得 → 全再生成」をワンショットで実行するためのスキル。

## 前提

- `fetch-dump` スキルと同じ（`adb`・`unzip`・`python3`）。
- **取得には AVD 名 `Warhammer_tablet_35` のエミュレータを使い、実行前にエミュレータ内の
  Play ストアで公式アプリを最新に更新する**（詳細は `fetch-dump` スキルの前提を参照）。
  他の端末も接続されている場合は `-s <エミュレータの serial>` を付けて実行する。
- 再生成のみ（`--no-fetch`）なら端末接続は不要で、既存の `dump.json` を使う。

## 使い方

スクリプト: `scripts/refresh_data.sh`

```bash
SKILL=.claude/skills/refresh-data/scripts/refresh_data.sh

# 既定: dump.json 取得 + 全 .md 再生成
bash $SKILL

# 既存の dump.json を使い、再生成のみ（端末不要）
bash $SKILL --no-fetch

# dump.json の取得だけ（再生成しない = fetch-dump と同等）
bash $SKILL --fetch-only

# 端末が複数接続されているとき、adb serial を指定
bash $SKILL -s 46221FDAP000JD
```

### オプション

- `--no-fetch` … dump.json の取得をスキップし、既存 `dump.json` から再生成のみ行う
- `--fetch-only` … dump.json の取得だけ行い、再生成しない
- `-s, --serial <serial>` … `fetch-dump` に渡す adb serial（端末が複数のとき）

## 処理内容

1. **dump.json 取得**（既定）… `fetch-dump` を呼び、`dump.json` と `dump.meta.json` を更新
2. **warscrolls** … `--all` で一括再生成（Grand Alliance 除外・Spearhead 版除外）。
   ファクション別ファイルのため、削除された項目が残らないよう `warscrolls/` を
   **クリアしてから**再生成
3. **faction_rules** … `--all` で一括再生成。同様に `faction_rules/` をクリアしてから再生成
4. **battle_tactics.md** … 単一ファイルを上書き再生成
5. **spearheads** … 全一括再生成。ファクション別ディレクトリ構造のため、
   `spearheads/` をクリアしてから再生成
6. **データ改訂なしの自動復元** … git 管理下で `dump.json` が HEAD から不変
   （= data_version も不変）かつ、生成物の変更行がすべて出典行（抽出日）と
   `dump.meta.json` の `extractedAt` のみで、新規・削除ファイルも無い場合は、
   生成物一式を自動で `git checkout` して元に戻す
   （抽出日だけの無意味な差分をコミット候補に残さないため）。
   出典行以外の変更が 1 行でもあれば何も戻さない。

AoS の dump.json は英語のみのため、40k 版のような言語方針（`--lang`）は無い。

## 生成後の確認

再生成後、`git status` の差分がバージョン更新・データ改訂に沿ったものか確認する。
「表示順序以外の実質変化」を見たい場合は、各 .md の行を `sort -u` で集合化して
バージョン行（`data_version` 等）を除外した diff を取ると、並び替えだけの差分と
データ改訂（ポイント・アビリティ本文・新規フォーメーション等）を切り分けられる。

## 関連スキル

このスキルは以下を内部で呼び出す。個別に実行したい場合はそれぞれを直接使う:

- `fetch-dump` … dump.json 取得のみ
- `extract-warscrolls` … ウォースクロール（ファクション単位）
- `extract-faction-rules` … ファクションルール（ファクション単位）
- `extract-battle-tactics` … バトルタクティックカード（単一ファイル）
- `extract-spearheads` … Spearhead（全一括）
