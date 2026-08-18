#!/usr/bin/env bash
# Warhammer Age of Sigmar データ一括更新スクリプト。
# 接続端末から dump.json を取り直し(fetch-dump)、warscrolls / faction_rules
# (ファクション単位) / battle_tactics.md / spearheads を再生成する。
#
# 使い方:
#   refresh_data.sh                 # dump.json 取得 + 全 .md 再生成 (既定)
#   refresh_data.sh --no-fetch      # dump.json 取得をスキップし再生成のみ
#   refresh_data.sh --fetch-only    # dump.json 取得のみ (再生成しない)
#   refresh_data.sh -s <serial>     # fetch-dump に adb serial を渡す (端末が複数のとき)
set -euo pipefail

# --- リポジトリルートを自身の位置から導出 ---
#     .claude/skills/refresh-data/scripts/refresh_data.sh → 4 階層上が repo root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
cd "$ROOT"

FETCH=1; REGEN=1; SERIAL=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-fetch)   FETCH=0; shift;;
    --fetch-only) REGEN=0; shift;;
    -s|--serial)  SERIAL="$2"; shift 2;;
    -h|--help)    sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "不明な引数: $1" >&2; exit 1;;
  esac
done

FETCH_SH=.claude/skills/fetch-dump/scripts/fetch_dump.sh
WS=.claude/skills/extract-warscrolls/scripts/extract_warscrolls.py
FR=.claude/skills/extract-faction-rules/scripts/extract_faction_rules.py
BT=.claude/skills/extract-battle-tactics/scripts/extract_battle_tactics.py
SP=.claude/skills/extract-spearheads/scripts/extract_spearheads.py

# --- 1. dump.json 取得 ---
if [[ $FETCH -eq 1 ]]; then
  echo "=== dump.json 取得 (fetch-dump) ==="
  if [[ -n "$SERIAL" ]]; then
    bash "$FETCH_SH" -o dump.json -s "$SERIAL"
  else
    bash "$FETCH_SH" -o dump.json
  fi
  echo
fi

if [[ $REGEN -eq 0 ]]; then
  echo "=== 完了 (fetch-only) ==="
  exit 0
fi

if [[ ! -f dump.json ]]; then
  echo "dump.json がありません。--no-fetch を外して取得するか、fetch-dump を先に実行してください。" >&2
  exit 1
fi

# いずれもファクション/Spearhead 別のファイル構造のため、消えた項目が残らないよう
# ディレクトリをクリアしてから再生成する

# --- 2. warscrolls (ファクション単位, クリア再生成) ---
echo "=== warscrolls (クリア再生成) ==="
rm -rf warscrolls
python3 "$WS" --dump dump.json --all >/dev/null || echo "  NG(ws)"
echo "  files: $(find warscrolls -name '*.md' | wc -l | tr -d ' ')"

# --- 3. faction_rules (ファクション単位, クリア再生成) ---
echo "=== faction_rules (クリア再生成) ==="
rm -rf faction_rules
python3 "$FR" --dump dump.json --all >/dev/null || echo "  NG(fr)"
echo "  files: $(find faction_rules -name '*.md' | wc -l | tr -d ' ')"

# --- 4. battle_tactics.md (単一ファイル) ---
echo "=== battle_tactics.md ==="
python3 "$BT" --dump dump.json -o battle_tactics.md >/dev/null || echo "  NG(bt)"

# --- 5. spearheads (全一括, クリア再生成) ---
echo "=== spearheads (クリア再生成) ==="
rm -rf spearheads
python3 "$SP" --dump dump.json >/dev/null || echo "  NG(sp)"
echo "  files: $(find spearheads -name '*.md' | wc -l | tr -d ' ')"

echo "=== 完了 ==="
