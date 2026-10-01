# official_translations — 公式訳

GW が出している日本語版の資料（バトルプロフィール、陣営パック、バトルトーム等）に載っている
**公式訳**を、ファクションごとに `official_translations/<ファクションslug>.json` に書く。
ファイルは取り込んだファクションの分だけ置く（無いファクションはこの層をスキップするだけ）。

AoS の dump.json には日本語が一切入っていない（40k 版と違い `localisations` が無い）ので、
md に出る日本語はすべてこのフォルダと `own_translations/` から来る。

## 使われ方

`extract-warscrolls` / `extract-faction-rules` / `extract-spearheads` が md を生成するとき、
名前を次の順で引く（読み込みと照合は `.claude/skills/_lib/aos_translations.py` が共通で行う）。

1. **`official_translations/<slug>.json`（このフォルダ）** … 公式訳
2. **`own_translations/<slug>.json`** … 1 に無いものだけ。独自訳
3. どちらにも無ければ英語のまま

見つかった場合、`{日本語名}({英語名})` で出す（例: `## ウィッチアエルフ(Witch Aelves)`）。

| セクション | 当たる場所 |
|---|---|
| `unit_names` | ウォースクロールの見出し、Spearhead の編成一覧とユニット詳細の見出し |
| `weapon_names` | 射撃武器・近接武器の表の武器名（戦傷時プロファイルは訳の後ろに「（戦傷時）」） |
| `ability_names` | アビリティ名。ウォースクロールのアビリティと地形ルール、ファクションルール（バトル特性・バトルフォーメーション・英雄特性・神器・その他の強化・ロアの呪文/祈祷/顕現）、Spearhead のバトル特性・レジメントアビリティ・強化 |

アビリティ・武器の本文（宣言・効果）や、グループ名（フォーメーション名・ロア名など）は今は訳さない。

- `<slug>` は md のファイル名と同じファクションのスラッグ（`Daughters of Khaine` → `daughters_of_khaine`）
- **他ファクションのファイルは参照しない**（同じ英語名でも資料ごとに訳が違うことがあり、
  訳を直したときの影響をそのファクションの md に閉じるため）。陣営をまたぐユニットも各ファイルに持つ
- グランドアライアンス（`grand_alliance_order` 等）やアーミー・オブ・リナウンの md は、
  それぞれのスラッグのファイルが無ければ英語のまま

## ファイルの形

```json
{
 "_faction": "ドーター・オヴ・カイン (Daughters of Khaine)",
 "_source": "バトルプロフィール ドーター・オヴ・カイン 2026年4月",
 "_notes": ["表記ゆれなど、取り込み時の判断のメモ"],
 "unit_names":    { "Witch Aelves": "ウィッチアエルフ" },
 "weapon_names":  { "Sciansá": "…", "Witch Aelves|Sciansá": "…" },
 "ability_names": { "Frenzied Fervour": "…", "Blessings of Khaine": "…" }
}
```

| キー | 内容 |
|---|---|
| `unit_names` | `{英語名: 日本語名}`。ウォースクロール名（`warscroll.name`）。サブネームは含めない |
| `weapon_names` | `{英語名: 日本語名}`。武器名（`warscroll_weapon.name`） |
| `ability_names` | `{英語名: 日本語名}`。アビリティ名（`warscroll_ability` / `ability` / `battle_formation_rule` / `lore_ability` / `terrain_ability` の `name`） |

- 武器名とアビリティ名は `"ユニット英語名|名前"` をキーにすると**そのユニットにだけ**当たる
  （同じ英語名でもユニットごとに訳が違う場合に使う）。ユニット指定のキーが先に引かれ、
  無ければ名前だけのキーを引く。ユニットに属さないファクションルールのアビリティ
  （バトル特性など）は名前だけのキーでしか引かれない
- キーは dump.json の名前と**完全一致**（`’` と `'`、`-` と `‑` も区別する）。
  禍事版の `Scourge of Ghyran Bloodwrack Shrine`（コロン無し）と `Scourge of Aqshy: Khainite Shadowstalkers`
  （コロン有り）のように、dump.json 上の表記そのままにする
- Spearhead 版は通常版と同じ英語名なので、同じキーで両方に当たる
- `_` で始まるキーはメモ用で読み飛ばされる
- 資料内で表記が揺れている場合は、ユニット名の欄（名前欄・見出し）を採用し、`_notes` に残す

## 取り込み元

`~/Dropbox/2_Warhammer/AoS 4版/` の日本語版 PDF と、同じ名前に `(英語)` が付いた英語版 PDF を
突き合わせる。`pdftotext -layout` と `pdftotext -raw` の両方で抽出して、行の折り返しで名前が
切れていないか確かめる。

| ファクション | 取り込んだ資料 | 件数 |
|---|---|---:|
| ドーター・オヴ・カイン | バトルプロフィール 2026年4月、陣営パック 2025年10月、スピアヘッド 2 冊、グューラン／アキュシーの禍事、バトルトーム・サプリメント | ユニット名 29、武器名 30、アビリティ名 66 |

拾えなかったものは各ファイルの `_pending` に一覧で残す（書籍スキャンなどから補う）。

### 取り込みのコツ（DoK で分かったこと）

- `pdftotext -raw` だと武器表が 1 行 1 武器で日英同順に並ぶので、能力値の並びが一致する行どうしを対応付けられる。
  アビリティは「名前：本文」の見出しが日英同順に並ぶ（英語は `NAME:` の大文字）
- 日本語版の**ウォースクロールの表題は装飾フォントでテキスト抽出が文字化けする**。表題やルビ付きの見出しは
  `pdftoppm -r 200 -x … -y … -W … -H …` で切り出した画像を目で読む
- 陣営パックは新バトルトームより前の版のことがある。現行の dump.json と英語名が一致するものだけ採る
- 同じ英語でも資料・ページで訳が揺れることがある（表題と本文、ユニットごとの武器名など）。
  どちらを採ったかは `_notes` に残し、場所ごとに訳を変える必要があれば `ユニット|名前` のキーを使う

## 参照されなくなった訳の確認

dump.json の更新でユニット・武器・アビリティが消えたり改名されたりすると、キーだけが残る。
`check-translations` スキルで列挙できる（`refresh-data` の最後にも自動で走る）。

```bash
python3 .claude/skills/check-translations/scripts/check_translations.py --dump dump.json
```

バトルプロフィールに載らないもの（マニフェステーション、Legends、新しい禍事版など）は
英語のまま残る。陣営パックやバトルトームから取り込むときは `_source` に追記する。
