# own_translations — 独自訳

公式の日本語訳が見つからないものに当てる**独自訳**を、ファクションごとに
`own_translations/<ファクションslug>.json` に書く。形は `official_translations/` と同じ
（`unit_names` など）。

- `official_translations/` に同じキーがあれば、そちらが優先される（独自訳は公式訳の穴埋め）
- 公式訳が後から見つかったら、`official_translations/` に移してここからは消す
- 他ファクションのファイルは参照しない

詳しい仕組みと書き方は `official_translations/README.md` を参照。

現在、独自訳のファイルは無い。
