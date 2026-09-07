#!/usr/bin/env bash
# Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) の base.apk を
# 接続済み Android 端末から取得し、assets/dump.json を取り出してプロジェクトへ保存する。
#
# 使い方:
#   fetch_dump.sh [-o <出力先 dump.json>] [-s <adb serial>] [--keep-apk]
#
# 既定の出力先はカレントディレクトリの ./dump.json
set -euo pipefail

PKG="com.gamesworkshop.aos4"
OUT="./dump.json"
SERIAL=""
KEEP_APK=0
TMPDIR="$(mktemp -d)"
trap '[[ $KEEP_APK -eq 0 ]] && rm -rf "$TMPDIR"' EXIT

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output) OUT="$2"; shift 2;;
    -s|--serial) SERIAL="$2"; shift 2;;
    --keep-apk)  KEEP_APK=1; shift;;
    --pkg)       PKG="$2"; shift 2;;
    -h|--help)   sed -n '2,12p' "$0"; exit 0;;
    *) echo "不明な引数: $1" >&2; exit 1;;
  esac
done

ADB=(adb)
[[ -n "$SERIAL" ]] && ADB=(adb -s "$SERIAL")

# 1. 端末接続確認
if ! "${ADB[@]}" get-state >/dev/null 2>&1; then
  echo "エラー: Android 端末が接続されていません (adb get-state 失敗)。" >&2
  echo "  端末を USB 接続し、USB デバッグを有効化してください。" >&2
  exit 1
fi

# 2. アプリのインストール確認
if ! "${ADB[@]}" shell pm path "$PKG" >/dev/null 2>&1; then
  echo "エラー: パッケージ $PKG が端末にインストールされていません。" >&2
  exit 1
fi

# 3. base.apk のパスを取得
# grep/head でパイプを早期に閉じると上流が SIGPIPE で死に、pipefail のせいで
# スクリプトごと落ちる (rc=141) ため、一度変数に受けてから探す。
PM_OUT="$("${ADB[@]}" shell pm path "$PKG" | tr -d '\r')"
APK_PATH=""
while IFS= read -r line; do
  if [[ "$line" == *base.apk ]]; then APK_PATH="${line#package:}"; break; fi
done <<< "$PM_OUT"
if [[ -z "$APK_PATH" ]]; then
  echo "エラー: base.apk のパスを取得できませんでした。" >&2
  exit 1
fi
echo "base.apk: $APK_PATH"

# 4. APK を pull
LOCAL_APK="$TMPDIR/base.apk"
"${ADB[@]}" pull "$APK_PATH" "$LOCAL_APK" >/dev/null
echo "pulled: $(du -h "$LOCAL_APK" | cut -f1)"

# 5. assets/dump.json を展開
unzip -o "$LOCAL_APK" assets/dump.json -d "$TMPDIR/extract" >/dev/null
SRC="$TMPDIR/extract/assets/dump.json"
if [[ ! -f "$SRC" ]]; then
  echo "エラー: APK 内に assets/dump.json が見つかりませんでした。" >&2
  exit 1
fi

# 6. 出力先へコピー
OUT_DIR="$(dirname "$OUT")"
[[ -n "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"
cp "$SRC" "$OUT"

# 7. data_version を表示
VER="$(python3 -c "import json,sys; print(json.load(open('$OUT')).get('metadata',{}).get('data_version'))" 2>/dev/null || echo '?')"
echo "saved: $OUT ($(du -h "$OUT" | cut -f1), data_version $VER)"

# 8. 抽出元のバージョン情報をサイドカー <dump>.meta.json に記録
# grep -m1 / head -1 でパイプを早期に閉じると tr が SIGPIPE で死に、
# pipefail のせいでスクリプトごと落ちる。一度変数に受けて bash の正規表現で拾う。
DUMPSYS="$("${ADB[@]}" shell dumpsys package "$PKG" 2>/dev/null | tr -d '\r')"
VNAME=""; VCODE=""
# 不一致時は && リスト全体が rc=1 になる。set -e では落ちない (AND-OR リストの
# 最後以外のコマンドの失敗は対象外) が、行の並び替えでこれが最終文になると
# スクリプトの終了ステータスが 1 になるため || true で固定しておく。
[[ "$DUMPSYS" =~ versionName=([^[:space:]]+) ]] && VNAME="${BASH_REMATCH[1]}" || true
[[ "$DUMPSYS" =~ versionCode=([0-9]+) ]] && VCODE="${BASH_REMATCH[1]}" || true
SERIAL_ID="$("${ADB[@]}" get-serialno 2>/dev/null | tr -d '\r')"
DEVMODEL="$("${ADB[@]}" shell getprop ro.product.model 2>/dev/null | tr -d '\r')"
NOW="$(date +%Y-%m-%dT%H:%M:%S%z)"
META="${OUT%.json}.meta.json"
python3 - "$META" "$PKG" "$VNAME" "$VCODE" "$VER" "$NOW" "$DEVMODEL" "$SERIAL_ID" << 'PY'
import json, sys
meta_path, pkg, vname, vcode, dver, now, model, serial = sys.argv[1:9]
def num(x):
    try: return int(x)
    except: return x or None
json.dump({
    "package": pkg,
    "appName": "Warhammer Age of Sigmar",
    "versionName": vname or None,
    "versionCode": num(vcode),
    "dataVersion": num(dver),
    "extractedAt": now,
    "device": ("%s (%s)" % (model, serial)).strip() if (model or serial) else None,
}, open(meta_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("meta saved: %s (v%s build %s)" % (meta_path, vname, vcode))
PY
[[ $KEEP_APK -eq 1 ]] && echo "APK 保持: $LOCAL_APK"
exit 0
