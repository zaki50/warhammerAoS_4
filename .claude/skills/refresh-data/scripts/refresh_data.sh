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
#   refresh_data.sh --no-cards      # ウォースクロールカード (cards/) の再生成を省く
set -euo pipefail

# --- リポジトリルートを自身の位置から導出 ---
#     .claude/skills/refresh-data/scripts/refresh_data.sh → 4 階層上が repo root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
cd "$ROOT"

FETCH=1; REGEN=1; CARDS=1; SERIAL=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-fetch)   FETCH=0; shift;;
    --fetch-only) REGEN=0; shift;;
    --no-cards)   CARDS=0; shift;;
    -s|--serial)  SERIAL="$2"; shift 2;;
    -h|--help)    sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
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

# --- 訳注 (translation_notes.json) を新しい dump.json と訳ファイルに照合して状態を更新 ---
echo "=== 訳注の照合 (translation-notes) ==="
python3 .claude/skills/translation-notes/scripts/translation_notes.py check --dump dump.json --update \
  | sed 's/^/  /' || echo "  NG(tn)"

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

# --- 6. データ改訂なし (抽出日のみの差分) なら自動で元に戻す ---
# 条件: git 管理下で、dump.json が HEAD から不変 (= data_version も不変) かつ
# 生成物の変更行がすべて出典行 (抽出日) / dump.meta.json の extractedAt のみで、
# 新規・削除ファイルが無い場合に限り、生成物一式を HEAD に戻す。
GEN_PATHS=(warscrolls faction_rules battle_tactics.md spearheads dump.json dump.meta.json)
if git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
   && git diff --quiet -- dump.json 2>/dev/null \
   && [[ -z "$(git status --porcelain -- "${GEN_PATHS[@]}" | grep -v '^ M ' || true)" ]]; then
  # 変更行は '+'/'-' で始まる行のうち、ファイル見出しの '+++ '/'--- ' を除いたもの。
  # 箇条書きの行は '+- **…**' のように 2 文字目も '-' になるので、2 文字目では除外しない
  CHANGED="$(git diff -U0 -- "${GEN_PATHS[@]}" | grep -E '^[+-]' | grep -vE '^(\+\+\+|---) ' || true)"
  NON_PROV="$(printf '%s\n' "$CHANGED" \
      | grep -vE '^[+-](出典: Warhammer Age of Sigmar 公式アプリ|  "extractedAt": )' \
      | grep -v '^$' || true)"
  if [[ -n "$CHANGED" && -z "$NON_PROV" ]]; then
    git checkout -- "${GEN_PATHS[@]}"
    echo "=== データ改訂なし (抽出日のみの差分) のため生成物を元に戻しました ==="
  fi
fi

# --- 7. 参照されなくなった訳の確認 (列挙のみ。失敗扱いにはしない) ---
echo "=== 訳ファイルの確認 (check-translations) ==="
python3 .claude/skills/check-translations/scripts/check_translations.py --dump dump.json \
  | sed 's/^/  /' || echo "  NG(ct)"

# --- 8. ウォースクロールカード (cards/。HTML と Dropbox の PDF) ---
if [[ $CARDS -eq 1 ]]; then
  echo "=== ウォースクロールカード (cards/make.py --all) ==="
  python3 cards/make.py --all 2>&1 | tail -2 | sed 's/^/  /' || echo "  NG(cards)"
  python3 cards/make.py --check 2>&1 | tail -1 | sed 's/^/  /' || echo "  NG(cards check)"
fi

echo "=== 完了 ==="
