---
name: fetch-dump
description: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の base.apk を接続済み Android 端末から取得し、同梱の assets/dump.json を取り出してプロジェクトに保存する。「dump.json を取得して」「最新のデータに更新して」「APK からデータを取り直して」といった依頼や、他の抽出スキル(extract-warscrolls / extract-faction-rules / extract-battle-tactics / extract-spearheads)を使う前に dump.json が無い・古い場合に使う。
---

# dump.json 取得スキル

Warhammer Age of Sigmar 公式アプリ `com.gamesworkshop.aos4` の `base.apk` を接続済み Android 端末から
取得し、APK 内 `assets/dump.json`（全ファクションのルール・ワースクロール DB、約11MB）を
取り出してプロジェクトに保存する。`extract-*` 系スキルの入力となる `dump.json` を用意・更新するためのスキル。

## 前提

- macOS / Linux 等で `adb`・`unzip`・`python3` が使えること。
- **取得には AVD 名 `Warhammer_tablet_35`（表示名 "Warhammer tablet 35"）のエミュレータを使う**
  （実機ではなくこのエミュレータを使うのが本プロジェクトの運用）。
  起動していなければ `emulator -avd Warhammer_tablet_35` で起動し、
  `adb -s <serial> emu avd name` で AVD 名を確認できる。
- **取得の前に、エミュレータ内の Play ストアで公式アプリを最新に更新**してから実行する
  （Play の UI 操作には Mobile MCP を優先して使う）。
- 他の端末・エミュレータも接続されている場合は `-s <serial>` で対象を指定する。
- アプリのデータ領域 `/data/data/...` は root 不可・デバッグ不可で直接読めないが、
  APK 同梱の JSON に全データが入っているためそれを使う。
- `assets/dump.json` は base.apk にのみ含まれ、split（言語・ABI・xxhdpi 等）には含まれない。

## 使い方

スクリプト: `scripts/fetch_dump.sh`

```bash
SKILL=.claude/skills/fetch-dump/scripts/fetch_dump.sh

# 既定: ./dump.json に保存
bash $SKILL

# 出力先を指定
bash $SKILL -o dump.json

# 複数端末が接続されている場合は serial を指定
bash $SKILL -s 46221FDAP000JD

# pull した base.apk を残す（デバッグ用）
bash $SKILL --keep-apk
```

### オプション

- `-o, --output <path>` … 保存先（既定 `./dump.json`、親ディレクトリは自動作成）
- `-s, --serial <serial>` … 対象端末の adb serial（端末が複数のとき）
- `--keep-apk` … 取得した base.apk を一時ディレクトリに残す
- `--pkg <package>` … 対象パッケージ名を変更（既定 `com.gamesworkshop.aos4`）

## 処理の流れ

1. `adb get-state` で端末接続を確認
2. `adb shell pm path <pkg>` でインストール確認 & base.apk のパス取得
3. `adb pull` で base.apk を一時取得
4. `unzip` で `assets/dump.json` を展開
5. 出力先へコピーし、`metadata.data_version` を表示
6. 抽出元のバージョン情報をサイドカー `<dump>.meta.json` に記録
   （`versionName` / `versionCode` / `dataVersion` / `extractedAt` / `device`）

## サイドカー `dump.meta.json`

`dump.json` と同じディレクトリに `dump.meta.json` を出力する。抽出系スキル
（extract-warscrolls / extract-faction-rules / extract-battle-tactics /
extract-spearheads）はこのファイルを読み、各 .md の「出典」行にアプリ版
（versionName/versionCode）・data_version・抽出日を記載する。サイドカーが無い場合は
`dump.json` の `data_version` のみを記載する。

## 関連スキル

取得した `dump.json` を入力に以下で抽出する:

- `extract-warscrolls` … ウォースクロール（ユニットデータ）
- `extract-faction-rules` … バトル特性・フォーメーション・強化・ロア
- `extract-battle-tactics` … バトルタクティックカード
- `extract-spearheads` … Spearhead（固定編成モード）

## トラブルシューティング

- **「Android 端末が接続されていません」**: USB 接続・USB デバッグ・端末側の許可ダイアログを確認。
  `adb devices -l` を実行して `device` 状態か確認する。
- **「パッケージが見つかりません」**: アプリ未インストール。別アプリの場合は `--pkg` を指定。
  端末上のパッケージは `adb shell pm list packages | grep gamesworkshop` で確認。
- **「assets/dump.json が見つかりません」**: アプリのバージョンによって構成が変わった可能性。
  `unzip -l base.apk | grep -i assets` で同梱物を確認する。
