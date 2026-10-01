# -*- coding: utf-8 -*-
"""ファクションごとの配色 (40k の cards/factions.py に当たる)。

キーは md・訳ファイルと同じファクションのスラッグ (Daughters of Khaine → daughters_of_khaine)。
colors は (濃・中・明) の 3 色で、パネル色や罫線色は build.py がここから計算する。
未登録のファクションはグランドアライアンスの色、それも分からなければグレーになる。
日本語名は official_translations/<slug>.json の faction_name から引く。
"""

FACTIONS = {
    'daughters_of_khaine': {'colors': ('#3a0d16', '#7d1626', '#d94a5a')},
}

# グランドアライアンス (warscroll の referenceKeywords に出る語) ごとの既定色
ALLIANCE = {
    'Order': ('#13294b', '#2c5a8f', '#7fb2e5'),
    'Chaos': ('#2b0f0f', '#6b1d1d', '#d0583b'),
    'Death': ('#1c1f24', '#3d4a52', '#8fb5b0'),
    'Destruction': ('#1f2a0e', '#4a6420', '#a8c95a'),
}
DEFAULT = ('#1f2a24', '#3f5a4c', '#9cc3a8')


def colors(slug, alliance=None):
    f = FACTIONS.get(slug)
    if f:
        return f['colors']
    return ALLIANCE.get(alliance or '', DEFAULT)
