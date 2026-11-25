# ウォーハンマー エイジ・オヴ・シグマー コアルール（4版）

出典: Warhammer Age of Sigmar 公式アプリ (com.gamesworkshop.aos4) / アプリ版 1.40.0 build 91 / dump.json data_version 499 / 抽出 2026-11-19

公式アプリ同梱の `dump.json` にあるコアルールと上級ルール（最新の General's Handbook のもの）を、アプリの並び順のまま書き出したもの。追加・エラッタは本文に反映済みで、章末の「Addenda, Errata and FAQs」はその一覧。日本語は公式 PDF（コアルール、ルール・アップデート）の文を `official_translations/core_rules.json` から引き、英語は折りたたみ（`[!quote]- EN`）で併記する。日本語が無い、または英語が改訂されて日本語が古くなった箇所は英語のまま出す。既知の誤訳は本文中に `~~誤~~==正==` の形で訂正する。

## 目次

- [[#コアルール(Core Rules)]]
  - [[#コアルール 1.0 - 7.0(Core Rules 1.0 - 7.0)]]
    - [[#1.0 基本概念(Core Concepts)]]
    - [[#2.0 戦いの道具(Tools of War)]]
    - [[#3.0 陣営(Factions)]]
    - [[#4.0 ウォースクロール(Warscrolls)]]
    - [[#5.0 アビリティ(Abilities)]]
    - [[#6.0 視認(Visibility)]]
    - [[#7.0 近接範囲(Combat Range)]]
  - [[#バトルの設定 8.0 - 10.1(Setting up for Battle 8.0 - 10.1)]]
    - [[#8.0 アーミー(The Armies)]]
    - [[#9.0 バトルプラン(Battleplans)]]
    - [[#10.0 初期配置フェイズ(The Deployment Phase)]]
  - [[#バトル 11.0 - 14.4(The Battle 11.0 - 14.4)]]
    - [[#11.0 バトル手順(Battle Sequence)]]
    - [[#12.0 バトルラウンドの開始時(Start of Battle Round)]]
    - [[#13.0 ターンのフェイズ(Turn Phases)]]
    - [[#14.0 共通コアアビリティ(Universal Core Abilities)]]
  - [[#移動 15.0 - 15.5(Movement 15.0 - 15.5)]]
    - [[#15.0 移動(Movement)]]
  - [[#攻撃 16.0 - 18.4(Attacking 16.0 - 18.4)]]
    - [[#16.0 攻撃対象の選択(Picking Targets)]]
    - [[#17.0 攻撃手順(The Attack Sequence)]]
    - [[#18.0 ダメージ手順(The Damage Sequence)]]
    - [[#攻撃の図解(Attacking Diagram)]]
    - [[#攻撃の使用例(Attacking Example)]]
  - [[#スペシャルルール 19.0 - 30.0(Special Rules 19.0 - 30.0)]]
    - [[#19.0 先手効果と後手効果(STRIKE-FIRST and STRIKE-LAST)]]
    - [[#20.0 武器アビリティ(Weapon Abilities)]]
    - [[#21.0 回復(Healing)]]
    - [[#22.0 兵の復帰と追加(Returning and Adding Models)]]
    - [[#23.0 トークン(Tokens)]]
    - [[#24.0 ユニットの配置(Setting up Units)]]
    - [[#25.0 護られし英雄(Guarded Heroes)]]
    - [[#26.0 ランダム能力値(Random Characteristics)]]
    - [[#27.0 修正の順序(Modifier Order)]]
    - [[#28.0 上級アビリティのルール(Advanced Ability Rules)]]
    - [[#29.0 両立しないルール(Contradictory Rules)]]
    - [[#30.0 効果の順序(Order of Effects)]]
  - [[#ターン終了 31.0 - 33.0(End of Turn 31.0 - 33.0)]]
    - [[#31.0 ターン終了時の概要(End of Turn Overview)]]
    - [[#32.0 作戦目標(Objectives)]]
    - [[#33.0 バトルラウンドの終了時(End of Battle Round)]]
  - [[#補遺、エラッタ、多く寄せられた質問(Addenda, Errata and FAQs)]]
    - [[#補遺(Addenda)]]
    - [[#エラッタ(Errata)]]
    - [[#多く寄せられた質問(Frequently Asked Questions)]]
- [[#上級ルール 2026-27(Advanced Rules)]]
  - [[#上級ルール 2026-27(Advanced Rules 2026-27)]]
  - [[#指揮アビリティ 2026-27(Commands 2026-27)]]
    - [[#1.0 指揮アビリティの概要(Commands Overview)]]
    - [[#2.0 ヒーローフェイズの指揮アビリティ(Hero Phase Commands)]]
    - [[#3.0 移動フェイズの指揮アビリティ(Movement Phase Commands)]]
    - [[#4.0 遠隔フェイズの指揮アビリティ(Shooting Phase Commands)]]
    - [[#5.0 突撃フェイズの指揮アビリティ(Charge Phase Commands)]]
    - [[#6.0 攻撃（遠隔と近接）の指揮アビリティ(Attacking (Shooting and Combat) Commands)]]
    - [[#7.0 防御の指揮アビリティ(Defensive Commands)]]
    - [[#8.0 ターン終了時の指揮アビリティ(End of Turn Commands)]]
  - [[#特殊地形 2026-27(Terrain 2026-27)]]
    - [[#1.0 特殊地形の概要(Terrain Overview)]]
  - [[#魔法 2026-27(Magic 2026-27)]]
    - [[#1.0 魔術師と神官(Wizards and Priests)]]
    - [[#2.0 呪文(Spells)]]
    - [[#3.0 奇蹟(Prayers)]]
    - [[#4.0 打ち消し呪文(Unbinding Spells)]]
    - [[#5.0 嫉妬に満ちた魔法使いと気まぐれな神々(Jealous Mages and Fickle Gods)]]
    - [[#6.0 習得している呪文と奇蹟(Known Spells and Prayers)]]
    - [[#7.0 顕現(Manifestations)]]
  - [[#アーミー編成 2026-27(Army Composition 2026-27)]]
    - [[#1.0 はじめに(Getting Started)]]
    - [[#2.0 陣営(Factions)]]
    - [[#3.0 ユニットの追加(Adding Units)]]
    - [[#4.0 最後の仕上げ(Finishing Touches)]]
  - [[#特殊兵 2026-27(Command Models 2026-27)]]
    - [[#1.0 豪傑(Champions)]]
    - [[#2.0 楽士(Musicians)]]
    - [[#3.0 旗手(Standard Bearers)]]
  - [[#補遺、エラッタ、多く寄せられた質問(Addenda, Errata and FAQs)]]
    - [[#エラッタ(Errata)]]
    - [[#多く寄せられた質問(Frequently Asked Questions)]]

## コアルール(Core Rules)

### コアルール 1.0 - 7.0(Core Rules 1.0 - 7.0)

#### 1.0 基本概念(Core Concepts)

##### 最も大切なルール(The Most Important Rule)

『ウォーハンマー：エイジ・オヴ・シグマー』を遊んでいるとき、どのように解決してよいのか分からないルールに遭遇するかもしれない。ゲームに初めて触れる方は、できるだけゲームをすぐに進められるように、対戦相手と話し合い、公平で合理的な解決を見い出すことをおすすめする。それが難しい場合には、このような状況の解決策を教えてくれるための詳細が**スペシャルルール**・セクションに記載されている。

> [!quote]- EN
> While you’re playing Warhammer Age of Sigmar, you might encounter a rules situation that you aren’t sure how to resolve. If you’re new to the game, we recommend discussing with your opponent and agreeing on a fair and reasonable solution so you can get on with the game as quickly as possible. Otherwise, the **Special Rules** section includes detailed instructions on how to resolve these situations.

##### ルール・アップデート(Rules Updates)

『ウォーハンマー：エイジ・オヴ・シグマー』のルールは、コミュニティからのフィードバックに基づいて、定期的な無料アップデートを通じてサポートされる。最新のアップデートやFAQは、**warhammer‑community.com**サイトでダウンロードできる。

> [!quote]- EN
> We are committed to supporting Warhammer Age of Sigmar rules via regular free updates based on community feedback. Please check **warhammer-community.com** to download the latest updates and FAQs.

『ウォーハンマー：エイジ・オヴ・シグマー』のバトルは、**戦場**と呼ばれる面の上で繰り広げられる。それぞれのバトルは**バトルプラン**と呼ばれるシナリオを用いており、戦場の設定方法や勝敗の決め方などが記載されている。

各プレイヤーは**アーミー**の**司令官**である。各々のアーミーは**陣営**に属しており、**ユニット**と呼ばれる**兵**のグループから構成されている。自軍側のアーミーに属する兵やユニットは、「**味方兵**」「**味方ユニット**」と呼ばれ、敵軍側のアーミーに属する兵やユニットは、「**敵兵**」「**敵ユニット**」と呼ばれる。

> [!quote]- EN
> Battles in Warhammer Age of Sigmar are fought on a surface that is referred to as the **battlefield**. Each battle uses a scenario called a **battleplan**, which will explain how to set up the battlefield and how to determine the winner.
>
> Each player is the **commander** of an **army**. Each army belongs to a **faction** and is made up of groups of **models** called **units**. Models and units in your army are referred to as **friendly** models and units, and models and units in your opponent’s army are referred to as **enemy** models and units.

#### 2.0 戦いの道具(Tools of War)

バトルするために必要なものは：

- テープメジャー
- ダイス
- 遊ぶための平らな面（戦場）
- シタデルミニチュアのアーミー2つ

> [!quote]- EN
> To fight a battle, you will need:
>
> - A tape measure
> - Some dice
> - A surface to play on (the battlefield)
> - 2 armies of Citadel Miniatures

##### 2.1 距離の測定(Measuring Distances)

『ウォーハンマー：エイジ・オヴ・シグマー』における距離の単位は**mv**（1mv=2.54cm「"」とも表記される）であり、測定の対象であるミニチュアのベース同士の最短距離を用いて距離を測る。距離の測定は、好きなタイミングで自由に測ることができる。ユニット間の距離を測定する際には、必ず互いのユニットの中で最も相手のユニットに近い兵同士の間の距離を測定する。ベースを持たない兵との距離は、ベースではなく兵の一部のうち、最も近い部分から測定する。

> [!quote]- EN
> Distances in Warhammer Age of Sigmar are measured in **inches** ("), between the closest points on the bases of the models you’re measuring to and from. You can measure distances whenever you wish. When measuring the distance between units, always measure the distance between the closest points on the bases of the closest models in each unit. If a model does not have a base, measure to and from the closest point on the model instead.

##### 2.1.1 「以内に一部でも入っている」と「以内に全体が入っている」(Within and Wholly Within)

「**兵**が何かの一定距離内に**一部でも入っている**」という場合（たとえば、別のユニット、陣地、作戦目標）、その兵のベースの一部が指定された距離内に入っていなければならない。

「**兵**が何かの一定距離内に**全体が入っている**」という場合、その兵のベースのすべてが指定された距離内に入っていなければならない。

「**ユニット**が何かの一定距離内に**一部でも入っている**」という場合、そのユニット内に属するいずれかの兵のベースの一部が指定された距離内に入っていなければならない。「**ユニット**が何かの一定距離内に**全体が入っている**」という場合、そのユニット内に属する全兵のベースのすべてが指定された距離内に入っていなければならない。

> [!quote]- EN
> A **model** is **within** a certain distance of something (e.g. another unit, a territory or an objective) if any part of its base is within that distance.
>
> A **model** is **wholly within** a certain distance of something if every part of its base is within that distance.
>
> A **unit** is **within** a certain distance of something if any part of the base of any model in the unit is within that distance. A **unit** is **wholly** **within** a certain distance of something if every part of the bases of all of the models in the unit is within that distance.

##### 2.2 ダイス(Dice)

『ウォーハンマー ~~~~==：==エイジ・オヴ・シグマー』では六面ダイスを使用する（これはときに**D6**という省略形で表記される）。

> [!quote]- EN
> Warhammer Age of Sigmar uses six-sided dice, often abbreviated to **D6**.

- ルールの中には「2D6」「3D6」といった表記を参照するものもある。そのような場合は、最初の数字に等しい個数のD6をロールし、出目を足し合わせる。
- ロール結果「2+」と表記されている場合は、出目2以上が必要である。また、ロール結果「3+」と表記されている場合は、出目3以上が必要である。
- ルールによって**D3**のロールが指示された場合は、ダイスを1個ロールし、その出目を半分にする（端数切り上げ）。D3ロールで「2+」と記されている場合は、ロール結果である出目を半分にし、端数を切り上げて得た数値が2以上でなければならない。
- ダイスの出目を変更する効果は**修正**と呼ばれる。
- 一部のルールでは、ダイスロールを**リロール**できるものがある。つまり、ダイスのロールを一部またはすべてをリロールすることができる。ダイスをリロールできるのは最大1回だけであり、ロールに対して修正（修正がある場合）が適用される前にリロールが実行される。
- **ロールオフ**が指示された場合、各プレイヤーはそれぞれダイスを1個ロールする。より高い出目を出したプレイヤーがロールオフに勝利する。出目の結果が等しい場合、特に明記されていない限り、各プレイヤーは明確な勝者が決定されるまで再びロールオフを実行する。

> [!quote]- EN
> - Some rules refer to ‘2D6’, ‘3D6’ and so on – in such cases, roll a number of dice equal to the number before ‘D6’ and add the results together.
> - A roll of ‘2+’ means a roll of 2 or more, a roll of ‘3+’ means a roll of 3 or more, and so on.
> - If a rule requires you to roll a **D3**, roll a dice and halve the total, rounding up. For D3 rolls, a roll of ‘2+’ means a result of 2 or more after halving the total and rounding up.
> - Effects that allow you to modify a dice roll are called **modifiers**.
> - Some rules allow you to **re-roll** a dice roll, which means you get to roll some or all of the dice again. You cannot re-roll a dice more than once, and re-rolls happen before modifiers to the roll (if any) are applied.
> - If you are instructed to **roll off**, each player should roll a dice. Whichever player has a higher roll wins the roll-off. If the result is a tie, each player should roll off again until there is a clear winner, unless otherwise specified.

#### 3.0 陣営(Factions)

各々のアーミーは1つの**陣営**に属している（たとえば、ストームキャスト・エターナルやスケイヴン）。

それぞれの陣営には一連の**陣営ルール**がある。陣営ルールには**戦闘特性**、**戦闘陣形**、**強化**、**伝承**が収録されている。陣営ルールはさまざまな書籍に記載されているが、最も一般的には陣営の**バトルトーム**に書き記されている。

> [!quote]- EN
> Each army belongs to a **faction**, e.g. Stormcast Eternals or Skaven.
>
> Each faction has a set of **faction rules**, which include **battle traits**, **battle formations**, **enhancements** and **lores**. These can be found in various publications but most commonly in the faction’s **battletome**.

#### 4.0 ウォースクロール(Warscrolls)

各ユニットのルールは、**ウォースクロール**に記載されている：

> [!quote]- EN
> The rules for each unit are contained on a **warscroll**:

![An example warscroll. At the top of the left-hand column of the warscroll are the unit's characteristics: Move, Save, Control and Health. Beneath that is a short description of the unit. On the right is shown the name of the unit, and beneath that is a table that lists the weapons that the unit is armed with, along with their respective characteristics. Beneath the weapon table are the unit's abilities; each of these is contained in its own little box. Some units only have one ability; others have more. Finally, running along the bottom of the warscroll is the keywords bar. This is a list of words that are used to group units that share common traits or to indicate that certain special rules apply to the unit.](https://dhss9aar8ocw.cloudfront.net/7a212d8c-82a0-414d-8796-3126e4f5f757)

- 1. 【**移動力**】は、ユニットが戦場をどれだけ速く移動できるかを決定する（15.0参照）。
- 2. 【**体力**】は、ユニット内に属する1体の兵が撃破されるまで、ユニットにどれくらいのダメージが割り振られなければならないのかを表している（18.2参照）。
- 3. 【**確保力**】は、ユニット内の各兵が作戦目標の争奪においてどれくらいの能力があるのかを表している（32.2参照）。
- 4. 【**防御力**】は、ユニットがどれぐらいの優れた防具を身に着けているのかを決定する。【防御力】は、兵をダメージから守るために必要とする出目を表しているため、示される数値に等しいまたはそれ以上の出目が必要となる。そのため、数値が小さいほど優れている（17.0==参照==）。
- 5. **ユニット種別**。
- 6. ユニットが有する**キーワード**（5.1参照）==。==
- 7. ユニットが装備している**武器名**。武器には**メレーアタック**をする**近接武器**か、**レンジアタック**をする**遠隔武器**がある。各武器には、それぞれの能力値がある（16.0参照）。
- 8. ユニットが使用できる特殊**アビリティ**（5.0参照）。

> [!quote]- EN
> - 1. The **MOVE** characteristic determines how quickly the unit can move across the battlefield (see 15.0).
> - 2. The **HEALTH** characteristic determines how many damage points can be allocated to a unit before a model in the unit is slain (see 18.2).
> - 3. The **CONTROL** characteristic determines how well each model in the unit can contest objectives (see 32.2).
> - 4. The **SAVE** Characteristic determines how well armoured the unit is. This characteristic is the roll you need to equal or exceed to save a model from harm, so a lower value is better (see 17.0).
> - 5. The **UNIT TYPE**.
> - 6. The **KEYWORDS** that the unit has (see 5.1).
> - 7. The **WEAPONS** the unit is armed with. Weapons are either **melee weapons**, used to make **combat attacks**, or **ranged weapons**, used to make **shooting attacks**. Each weapon has its own characteristics (see 16.0).
> - 8. Any special **ABILITIES** the unit can use (see 5.0).

#### 5.0 アビリティ(Abilities)

『ウォーハンマー：エイジ・オヴ・シグマー』のユニットが実行できることの大部分は、『**アビリティ**』と呼ばれる。アビリティの例は次の通り：

> [!quote]- EN
> The vast majority of things that units can do in Warhammer Age of Sigmar are called **abilities**. This is an example of an ability:

![An example ability. Abilities are contained in their own box. The bar at the top tells you when the ability can be used. Beneath that, in the main part of the box, is the name of the ability, a small passage of text that puts the ability into context to help you imagine what is happening on the battlefield when it is being used. Beneath that are the Declare instructions (if any), and beneath that is the Effect of the ability – in other words, what the ability actually does in the game. Beneath the effect is a keywords bar. Ability keywords are used to group abilities of a similar type.](https://dhss9aar8ocw.cloudfront.net/6e5902c8-11d4-45d3-8708-eb281114cfc1)

- 1. **タイミング**
- 2. **アビリティ名と説明**
- 3. **宣言手順**
- 4. **効果**
- 5. **キーワード**

> [!quote]- EN
> - 1. **Timing**
> - 2. **Name and Description**
> - 3. **Declare Instructions**
> - 4. **Effect**
> - 5. **Keywords**

![This key shows the different ability icons and their names. The Movement icon is a small arrow, the Offensive icon is a crossed axe and sword, the Defensive icon is a shield bearing the twin-tailed comet symbol, the Shooting icon is a bow and arrow, the Rallying icon is a flag, the Special icon is a twelve-pointed halo, and the Control icon is a solid circle.](https://dhss9aar8ocw.cloudfront.net/894e4f94-7170-4edf-92c0-c086214d4359)

##### 5.1 キーワード(Keywords)

アビリティの中には、アビリティの下部にある**キーワード欄**に1つ以上の**キーワード**が記されているものがある。たとえば、上記に示されている『遠隔攻撃』アビリティは**コア**、**アタック**、**遠隔攻撃**のキーワードを有する。ユニットもまた、ウォースクロールにキーワード欄を有する。

キーワードは、どのアビリティを使用できるのか、アビリティの対象としてどのユニットを選べるのかを示してくれる。たとえば『突撃』アビリティは、~~直前~~==こ==のターン中に自身のユニットが**全力移動**または**退却**のキーワードを持つアビリティを宣言していない場合にだけ使用できる。（以下、英語版に関して）キーワードは単数形であれ複数形であれ、ルール上に違いはない。

> [!quote]- EN
> Some abilities have one or more **keywords** listed at the bottom of the ability on their **keywords bar**, e.g. the ‘Shoot’ ability shown above has the **CORE**, **ATTACK** and **SHOOT** keywords. Units also have a keywords bar on their warscroll.
>
> Keywords let you know which abilities can be used or which units can be picked as targets for an ability. For example, the ‘Charge’ ability can only be used by a unit if it did not use an ability with the **RUN** or **RETREAT** keyword earlier in the turn. The singular and plural forms of a keyword are synonymous for rules purposes.

##### 5.2 アビリティの宣言(Using Abilities)

アビリティの**タイミング**は、いつアビリティを使用できるのかを示している。アビリティを宣言する際は、以下の手順に従う：

1. **アビリティの宣言**：対戦相手にどのアビリティが使用されるのかを宣言する。アビリティに**宣言**が記載されている場合は、このステップ中に宣言内容を解決する。
2. **リアクションの宣言**：そのアビリティを宣言したプレイヤーから順に、各プレイヤーは交互に、適切な**リアクション**のタイミングを持つアビリティを宣言する。プレイヤーはリアクションの使用をパスしてもよいが、双方のプレイヤーが連続してリアクションの使用をパスした場合、そのアビリティに対してこれ以上リアクションを宣言することはできない。
3. **効果の解決**：アビリティに記されている**効果**部分の手順に従う。

> [!quote]- EN
> The **timing** of an ability tells you when it can be used. When using an ability, follow these steps:
>
> 1. Declare the Ability: Tell your opponent which ability is being used. If the ability has **Declare** instructions, resolve them at this step.
> 2. Use Reactions: Starting with the player using the ability, the players alternate using any abilities with an appropriate **Reaction** timing. Players can choose to pass instead of using a reaction, but once both players consecutively pass, no further reactions to that ability can be used.
> 3. Resolve the Effect: Follow the instructions in the **Effect** part of the ability.

##### 5.3 一度限りのルール(The Rules of One)

- ユニットは、同じフェイズ中に『**コア**』アビリティを1個だけ使用できる（14.0参照）。
- 特に明記されていない限り、ユニットは同じフェイズ中に**同一のアビリティ**を1回だけ宣言できる。
- ユニットは、同じ**パッシブアビリティ**の効果を受けることができるのは同時に1個だけである。たとえばユニットが『遮蔽物』パッシブアビリティを持つ、異なる2つの特殊地形の効果範囲内に一部でも入っている場合、その効果はユニットに1回だけ適用される。

> [!quote]- EN
> - A unit cannot use more than 1 **CORE** ability per phase (see 14.0).
> - A unit cannot use the **same ability** more than once per phase, unless specified otherwise.
> - A unit cannot be affected by the same **passive ability** more than once at the same time. For example, if a unit is within range of two different terrain features that have the ‘Cover’ passive ability, the effect only applies to it once.

##### 5.4 パッシブアビリティ(Passive Abilities)

**パッシブ**のタイミングを持つアビリティは、**パッシブアビリティ**と呼ばれる。パッシブアビリティは宣言されない。アビリティの条件が満たされている限り、パッシブアビリティの効果は常に適用される。また、パッシブアビリティが適用可能であれば、それは必ず適用されなければならない。

> [!quote]- EN
> Abilities that have the **Passive** timing are called passive abilities. **Passive abilities** are not declared. The effects of passive abilities always apply if the conditions of the ability are met, and they must be applied if it is possible to do so.

##### アビリティの使用例(Abilities Example)

**バトル中のベンとジェス、ベンが操作するラットオゴウルがジェスのリベレイターに突撃を実行した。これはベンがユニットを選択し、『近接攻撃』を使用するターンを示している。次の例は、アビリティの使い方を示しているものであるが、アビリティの詳細は後のルールで説明されるために、気に留めずに読み進めてみよう。**

> [!quote]- EN
> Ben and Jes are fighting a battle, and Ben’s Rat Ogors have charged into Jes’s Liberators. It is Ben’s turn to pick a unit to fight. The following example shows how abilities are used, but don’t worry too much about the specific abilities, as they will be explained later in the rules.

1. ベンは『近接攻撃』アビリティを使用した。初めにアビリティの宣言手順を解決する。この例において、『近接攻撃』アビリティを使用するために、ベンは自軍側ラットオゴウル・ユニットを選択する。次に選択された味方ユニットで接敵移動を実行した。最後に、ベンはラットオゴウルが持つすべての攻撃の対象としてジェスのリベレイター・ユニットを選択する。

> [!quote]- EN
> 1. Ben uses the ‘Fight’ ability. The first step is to resolve any Declare instructions for the ability. In this case, Ben picks his unit of Rat Ogors to use the ability, then they make a pile-in move. Finally, Ben picks Jes’s Liberators unit as the target of all the Rat Ogors’ attacks.

> **近接攻撃(Fight)**（任意の近接フェイズ）
>
> *熾烈な接近戦が繰り広げられる中、戦士たちは敵に襲い掛かる。*
>
> - **宣言:** **近接戦闘中**またはこのターン中に**突撃を実行**している味方ユニットを1個選択し、このアビリティを使用する。選択された味方ユニットは**接敵移動**を1回実行できる（15.3参照）。次に、選択された味方ユニットが**近接戦闘中**である場合、その味方ユニットが持つ攻撃の対象として、敵ユニットを1個または複数選ばなければならない（16.0参照）。
> - **効果:** 攻撃対象であるユニットに対して**メレーアタック**を解決する。
> - **キーワード:** コア、アタック、近接攻撃

> [!quote]- EN
> **Fight**（Any Combat Phase）
>
> *Locked in a deadly melee, the fighters strike out at their foes.*
>
> - **Declare:** Pick a friendly unit that is **in combat** or that **charged** this turn to use this ability. That unit can make a **pile-in move** (see 15.3). Then, if that unit is **in combat**, you must pick one or more enemy units as the target(s) of that unit’s attacks (see 16.0).
> - **Effect:** Resolve **combat attacks** against the target unit(s).
> - **Keywords:** Core, Attack, Fight

![A unit of three Skaven Rat Ogors is piling in towards a unit of five Stormcast Eternals Liberators. Two arrows indicate that two of the Rat Ogor models made a pile-in move to get into combat with the Liberators, while the third Rat Ogor has not moved because it was already in combat. The starting positions of the Rat Ogors that moved are indicated by fainter images.](https://dhss9aar8ocw.cloudfront.net/ac6ce57b-1dd0-4c6b-bdf5-6da435fc8170)

2. アビリティを宣言した後、ベンは任意の**リアクション**を最初に使用する機会を得る。『近接攻撃』は**アタック**のキーワードを有するため、ベンは『全力攻撃』アビリティを使用して自軍側ラットオゴウルの攻撃能力を向上させることができる。

ベンが『全力攻撃』を使用した後、ジェスは『全力防御』アビリティを使用して自軍側リベレイターに降りかかる猛攻撃を防ごうとする。その後、ベンはパスを選びそれ以上のリアクションを使用しないことを選択し、ジェスも同じようにパスを選択した。

> [!quote]- EN
> 2. After declaring the ability, Ben has the first opportunity to use any **reactions**. As ‘Fight’ has the **ATTACK** keyword, Ben is able to use the ‘All-out Attack’ ability to improve his Rat Ogors’ attacks.
>
> After Ben uses ‘All-out Attack’, Jes uses the ‘All-out Defence’ ability to try to protect his Liberators against the upcoming onslaught. Ben then passes on using any further reactions, then Jes does the same.

> **全力攻撃(All-out Attack)**（リアクション：自軍側が『アタック』アビリティを宣言｜1 CP）
>
> *熱狂的な勢いで戦士たちは攻撃を仕掛ける。*
>
> - **使用者:** その『**アタック**』アビリティを使用しているユニット1個。
> - **効果:** その『**アタック**』アビリティによる攻撃の**ヒットロール**は+1の修正を受ける。この効果は、**随行者**・武器アビリティを有する武器にも適用される。

> [!quote]- EN
> **All-out Attack**（Reaction: You declared an ATTACK ability｜1 CP）
>
> *The warriors fight with a frenzied vigour.*
>
> - **Used By:** The unit using that **ATTACK** ability.
> - **Effect:** Add 1 to **hit rolls** for attacks made as part of that **ATTACK** ability. This also affects weapons that have the **Companion** weapon ability.

> **全力防御(All-out Defence)**（リアクション：敵軍側が『アタック』アビリティを宣言｜1 CP）
>
> *身に迫る攻撃を防ぐため、兵士たちは隊列を組む。*
>
> - **使用者:** その『**アタック**』アビリティの攻撃対象となったユニット1個。
> - **効果:** このフェイズ中、その使用者ユニットの**セーブロール**は+1の修正を受ける。

> [!quote]- EN
> **All-out Defence**（Reaction: Opponent declared an ATTACK ability｜1 CP）
>
> *The soldiers close ranks to hold off an incoming attack.*
>
> - **Used By:** A unit targeted by that **ATTACK** ability.
> - **Effect:** Add 1 to **save rolls** for that unit in this phase.

『全力攻撃』と『全力防御』などは**上級ルール**の例であり、特定のバトルパックで用いられる。

> [!quote]- EN
> ‘All-out Attack’ and ‘All-out Defence’ are examples of **Advanced Rules**, which are used in certain battlepacks.

3. 宣言手順が解決され、双方のプレイヤーはリアクションを使用する機会を得た。ベンはアビリティの**効果**を解決し、結果的にリベレイター2体が撃破される（18.3参照）。

> [!quote]- EN
> 3. Now that the Declare instructions have been resolved and both players have had a chance to use reactions, Ben can resolve the effect of the ability, resulting in 2 Liberators being slain (see 18.3).

> **近接攻撃(Fight)**（任意の近接フェイズ）
>
> *熾烈な接近戦が繰り広げられる中、戦士たちは敵に襲い掛かる。*
>
> - **宣言:** **近接戦闘中**またはこのターン中に**突撃を実行**している味方ユニットを1個選択し、このアビリティを使用する。選択された味方ユニットは**接敵移動**を1回実行できる（15.3参照）。次に、選択された味方ユニットが**近接戦闘中**である場合、その味方ユニットが持つ攻撃の対象として、敵ユニットを1個または複数選ばなければならない（16.0参照）。
> - **効果:** 攻撃対象であるユニットに対して**メレーアタック**を解決する。
> - **キーワード:** コア、アタック、近接攻撃

> [!quote]- EN
> **Fight**（Any Combat Phase）
>
> *Locked in a deadly melee, the fighters strike out at their foes.*
>
> - **Declare:** Pick a friendly unit that is **in combat** or that **charged** this turn to use this ability. That unit can make a **pile-in move** (see 15.3). Then, if that unit is **in combat**, you must pick one or more enemy units as the target(s) of that unit’s attacks (see 16.0).
> - **Effect:** Resolve **combat attacks** against the target unit(s).
> - **Keywords:** Core, Attack, Fight

![The two slain Liberators are indicated by icons in the form of haloed skulls set over the images of the slain models.](https://dhss9aar8ocw.cloudfront.net/9f8ce4a9-7eb0-4298-9e0d-2907249fd5ed)

#### 6.0 視認(Visibility)

視認元である兵の任意の点から、視認対象である兵の任意の点まで、架空の直線を引くことができる場合（水平線、対角線、垂直線を問わない）、視認対象の兵は他の兵（「視認元の兵」）からみて**視認状態**にあるとみなされる。その直線は、視認元の兵が属するユニット内の他の兵と交差してもよいが、それ以外の物とは交差してはならない。視認対象ユニット内の少なくとも1体の兵が、視認元ユニット内の少なくとも1体の兵から見える場合、視認元ユニットからみて視認対象ユニットは視認状態にあるとみなされる。兵は、常に自分自身を視認できるものとする。

> [!quote]- EN
> A target model is visible to another model (which we’ll call the ‘observing model’) if you can draw a straight line through the air (whether horizontal, diagonal or vertical) from any point on the observing model to any point on the target model that does not intersect any objects except for other models in the observing model’s unit. A target unit is visible to an observing unit if at least 1 model in the target unit is visible to at least 1 model in the observing unit. A model is always considered to be visible to itself.

![A Stormcast Eternal Liberator partially obscured by a wall.](https://dhss9aar8ocw.cloudfront.net/61556fdc-0fe3-4c50-bf60-584b765457e2)

*このリベレイターは半分しか見えていないが、視認できる状態にあるとみなされる。兵全体の大部分が視認から遮られていても、あるいは視認できる部分がいかに少なくても、ある一部が視認できるならば、兵は視認状態にあるとみなされる。*

> [!quote]- EN
> Even though only half of this Liberator can be seen, he counts as being visible. A model is visible no matter how much of the model is blocked from sight or how little of it is visible; if any part of the model can be seen, it is visible.

![図](https://dhss9aar8ocw.cloudfront.net/e2603d4e-f5a6-46e3-a732-89dec981fae0)

*視認元の兵の視認は、敵兵によって遮られることがある。この写真のプレーグベアラーは、リベレイターから視認状態ではない。なぜなら、グレイト・アンクリーン・ワンによって視認が遮られているためだ。*

> [!quote]- EN
> An observing model's visibility can be blocked by enemy models. The Plaguebearer in this shot is not visible to the Liberator because it is hidden by the Great Unclean One.

![Three Liberators viewed from behind. One of them is a little further back than the other two.](https://dhss9aar8ocw.cloudfront.net/be9ee61a-836d-4bf0-90cc-ab52b7ac9124)

*このユニットの後方にいるリベレイターは、仲間を通して視認できるものとする。兵は、そのユニット内にいる他の兵の視認を遮ることはない。なぜなら、お互いの攻撃の妨げにならないように戦っていることが前提にあるからだ。*

> [!quote]- EN
> The Liberator at the back of this unit can see through their fellows. Models don’t block the visibility of other models in their unit – it is assumed that they fight in such a way as to not obstruct one another’s attacks.

> - 視認対象である兵の一部が視認元の兵から見える場合、視認対象である兵とその兵が属するユニットは、視認元の兵からみて**視認状態**にあるとみなされる。

> [!quote]- EN
> - If any part of another model can be seen by an observing model, both the target model and its unit are **visible** to that observing model.

時として、兵が視認できるかどうかがすぐにわからない場合もある。そのような場合は、身をかがめて視認元の兵の後ろから視認を確認してみよう。視認対象の兵の一部が見えていれば、たとえそれが槍の穂先であったとしても、ルール上その兵は視認状態にあるとみなされる。

> [!quote]- EN
> In some cases, it might not be immediately clear whether a model is visible. If so, stoop down to get a look from behind the observing model. If any part of the other model is visible, even if it is just the tip of a spear, then that model is visible for rules purposes.

ルールやアビリティにおいて、選択対象がアビリティ使用側のユニット（またはユニット内の兵）から射程内に入っていることと、かつ視認状態であることを同時に要求している場合、そのような条件は、選択対象内の同一の兵に対して満たされていなければならない。例えば、兵1体は射程内であるが視認状態ではなく、他の兵1体は射程内ではないが視認状態であるようなユニットを、選択対象とすることはできない。

> [!quote]- EN
> If a rule or ability requires a target to be both within a given range of and visible to the unit using that ability, or to a model in that unit, both conditions must be met by the same model in the target. You could not, for instance, target a unit where one model is within range but not visible and another model is not in range but is visible.

#### 7.0 近接範囲(Combat Range)

各兵は**近接範囲**を持っており、それは兵のベースから水平方向に3mv、その水平方向に進んだ地点から作られる円から、垂直方向に任意の距離伸びた円柱によって形成されている。ユニットの近接範囲は、そのユニットに属するすべての兵から水平方向に3mv伸び、任意の距離垂直方向に伸びている。自軍側アーミーのユニットと敵軍側アーミーのユニットが互いの近接範囲内に一部が入っており、互いに**視認**できる状態にある場合、それらは**近接戦闘中**であるとみなされる。近接戦闘中ではないユニットが、視認状態にある敵ユニットの近接範囲内に一部が入った場合、それは**近接戦闘に突入**する。

敵ユニットが兵の近接範囲内に一部でも入っており、かつその兵から敵ユニットが視認できる場合、兵は敵ユニットと近接戦闘中であるものとしてみなされる。

> [!quote]- EN
> Each model has a **combat range** that extends 3" horizontally from its base and any distance vertically from that circle to form a cylinder. The combat range of a unit extends 3" horizontally and any distance vertically from every model in that unit. Units from opposing armies that are within each other’s combat range and that are **visible** to each other are **in combat** with each other. When a unit that is not in combat enters the combat range of a visible enemy unit, it **moves into combat**.
>
> A model is considered to be in combat with an enemy unit if that unit is within the model’s combat range and visible to it.

> - ユニットの近接範囲は、そのユニットに属するすべての兵から水平方向に3mv伸びる。
> - 1体以上の敵兵がユニットの近接範囲内に一部が入っており、かつその敵兵が視認状態にある場合、そのユニットは近接戦闘中である。

> [!quote]- EN
> - A unit’s combat range extends 3" out from every model in that unit.
> - If any enemy models are within a unit’s combat range and visible to it, that unit is in combat.

![A blue overlay is set over a Liberator, stretching out 3 inches from the left and right of the model's base and stretching all the way up to the top of the image. This indicates the combat range of the model.](https://dhss9aar8ocw.cloudfront.net/42995b24-a75a-46b7-8726-8b8ad9203187)

*兵の近接範囲は、その兵から全水平方向に3mv伸び、垂直方向に無限に伸びている。なお、この距離は兵のベースの中心からではなくベースの端から測定される。*

> [!quote]- EN
> A model’s combat range extends 3" horizontally outwards from it in all directions and an infinite distance vertically. Note that this is measured from the edge of its base, not the centre.

![Two Rat Ogors, a Liberator and a wall. One Rat Ogor and the Liberator are on one side of the wall; the other Rat Ogor is on the opposite side of the wall. A large blue circle centred over the Liberator partially overlaps both the Rat Ogors and the wall.](https://dhss9aar8ocw.cloudfront.net/f8869d9a-0bcb-4477-9ee1-f09050463594)

*両方のラットオゴウルは、リベレイターの近接範囲内に一部が入っているにもかかわらず、壁の後ろ側にいるラットオゴウルはリベレイターから視認状態ではないため、近接戦闘中であるとはみなされない。*

> [!quote]- EN
> Even though both Rat Ogors are within the combat range of the Liberator, the Rat Ogor behind the wall is not visible to the Liberator and is therefore not in combat.

![Five large blue circles centred over each model in a unit of five Liberators have merged to indicate the combat range of the unit as a whole.](https://dhss9aar8ocw.cloudfront.net/2d2ffbe1-8d3c-4451-8a7d-43db8512b75c)

*ユニットの近接範囲は、そのユニットに属するすべての兵から水平方向に3mv伸び、任意の距離垂直方向に伸びている。写真で確認できる通り、これは「雲」のような形をしている。*

> [!quote]- EN
> A unit’s combat range extends 3" horizontally and any distance vertically from all models in the unit. As you can see, this forms a sort of ‘cloud’.

![A unit of five Liberators, a unit of three Rat Ogors and a unit consisting of a single Clawlord. The blue area indicating the Liberators' combat range is overlapping the Clawlord and two of the three Rat Ogors.](https://dhss9aar8ocw.cloudfront.net/b5ad61b9-e387-4802-a8bc-74b691655575)

*ユニットに属する兵が1体でも、その敵ユニットの近接範囲内に一部でも入っている場合、そのユニットは視認状態にある敵ユニットと近接戦闘中であるとみなされる。1体のラットオゴウルがリベレイターの近接範囲内に入っていないものの、ラットオゴウルのユニットはリベレイターと近接戦闘中であるとみなされる。*

> [!quote]- EN
> A unit is in combat with a visible enemy unit if any of its models are within the combat range of that enemy unit. Even though 1 Rat Ogor is not within the Liberators’ combat range, its unit is still in combat.

### バトルの設定 8.0 - 10.1(Setting up for Battle 8.0 - 10.1)

#### 8.0 アーミー(The Armies)

バトルを開始する前に、双方のプレイヤーは**アーミー**が必要となる。バトルパックの中には、あらかじめ決められたアーミーを用いるものもあれば、自軍のアーミーロスターをどのように編成するのかを記載しているものもある。

> [!quote]- EN
> Before starting a battle, both players will need an **army**. Some battlepacks use pre-made armies, while others include rules on how to fill your army roster.

> 特に明記されていない限り、バトルパックまたはバトルプランでは以下の手順に従ってバトルを設定する：
>
> - 作戦目標を配置する。
> - 特殊地形を配置する。
> - 陣地を決定する。
> - アーミーを初期配置する。
> - 陣地を決定するロールオフに負けたプレイヤーは、どちらのプレイヤーから順に初期配置するのかを決定する。

> [!quote]- EN
> Unless specified otherwise in the battlepack or battleplan:
>
> - Set up objectives.
> - Set up terrain.
> - Determine territories.
> - Deploy armies.
> - The player who lost the roll-off to choose territories decides who begins deployment

#### 9.0 バトルプラン(Battleplans)

バトルを開始する前に、まずは**バトルプラン**を選択しなければならない。それぞれの**バトルパック**には、さまざまなバトルプランが用意されており、他の書籍にも追加のバトルプランが収録されている。各バトルプランにはシナリオがあり、**陣地**や**作戦目標**、**勝利条件**、またそのバトル中に適用される追加のスペシャル==ル==ールが記載されている。

> [!quote]- EN
> Before any battle, you’ll need to pick a **battleplan**. A variety of battleplans are available in each **battlepack**, and additional battleplans are available in other publications. Each battleplan is a scenario to play – it outlines **territories**, **objectives** and **victory conditions**, in addition to any special rules that apply to that battle.

##### 9.1 戦場マップ(Battlefield Map)

各バトルプランには**戦場マップ**が存在し、そのマップは**4分の1区画**ごとに分けられている。戦場マップには、配置される**作戦目標**やプレイヤーの**陣地**が示されている。それぞれのバトルパックやバトルプランには、遊んでいるゲーム規模によって推奨の戦場サイズが示されている。

> [!quote]- EN
> Each battleplan includes a **battlefield map** that is divided into **quarters**. The map will show the locations of any **objectives** and the players’ **territories**. Each battlepack or battleplan will indicate the recommended battlefield size based on the size of game you are playing.

![A rectangular diagram of a battlefield is shown. At the top of the rectangle, stretching all the way from left to right, there is a blue strip captioned 'Defender's Territory'. At the bottom, there is a red strip captioned 'Attacker's territory'. Between these two strips, there is a wider grey strip that has no caption. On the horizontal centre line of the battlefield, there are two golden circles. The battlefield is symmetrical.](https://dhss9aar8ocw.cloudfront.net/fbd5b179-78b5-46fe-89dd-6fb0fd1425c7)

##### 9.1.1 作戦目標と特殊地形の配置(Setting up Objectives and Terrain Features)

多くの戦場には**作戦目標**と呼ばれる要所があり、概してすべての戦場には建物、遺跡、森などの**特殊地形**が配置されている。特に明記されていない限り、まずプレイヤーは初期配置マップ上に黄金色の丸で示されている位置に作戦目標マーカーを配置する。次に、プレイヤーはお互いに合意できる方法で特殊地形を配置する。多くのバトルパックやバトルプランには、特殊地形を配置するための詳細な説明が記されている。

> [!quote]- EN
> Many battlefields have key locations called **objectives**, and almost all battlefields have **terrain features** such as buildings, ruins and woods. Unless otherwise specified, players should first set up objective markers at the locations indicated by a gold circles on the deployment map, then set up terrain features in a mutually agreeable manner. Many battlepacks and battleplans include further instructions for setting up terrain.

##### 9.1.2 陣地(Territories)

バトルパックまたはバトルプランにおいて特に明記されていない限り、特殊地形が配置された後、プレイヤーはロールオフを実行する。ロールオフの勝者は、どちらのプレイヤーがどの陣地に属するかを決定する。次に勝者の対戦相手は、どちらのプレイヤーから順に初期配置を開始するのかを決定する。

> [!quote]- EN
> Unless otherwise specified in the battlepack or battleplan, after terrain has been set up, the players should roll off. The winner decides which territory belongs to which player. Their opponent decides which player begins deployment.

- ユニット内に属するいずれかの兵のベースの一部が指定された陣地内に入っている場合、それは**一部でも入っている**ものとみなされる。
- ユニット内に属する全兵のベースのすべて==が==指定された陣地内に入っている場合、それは**全体が入っている**とみなされる。
- どちらのプレイヤーの陣地にも属さない戦場エリアは、**中立地帯**である。

> [!quote]- EN
> - A unit is **within** a territory if any part of the base of any model in the unit is within that territory.
> - A unit is **wholly within** a territory if every part of the base of every model in the unit is within that territory.
> - The area of the battlefield that is neither player’s territory is **neutral territory**.

#### 10.0 初期配置フェイズ(The Deployment Phase)

戦場の設定が完了したら、プレイヤーは自軍のアーミーの**初期配置**をしなければならない。これは、**初期配置フェイズ**と呼ばれる特殊なフェイズで実行される。初期配置フェイズは、バトルにつき1度限りのものであり、第1バトルラウンド開始前に実施される（12.0参照）。

> [!quote]- EN
> Once the battlefield is ready, the players must **deploy** their armies. This is done in a special phase called the **deployment phase**. The deployment phase happens once per battle, before the start of the first battle round (see 12.0).

**ステップ1 ‒ 陣営地形の初期配置**

> [!quote]- EN
> Step 1 - Deploy Faction Terrain Features

陣営の中には、固有ウォースクロールを持つ**陣営地形**を有する陣営もあり、それらは『**特殊地形の初期配置**』アビリティを使用して配置される。初期配置を開始するプレイヤーは、最初に『**特殊地形の初期配置**』アビリティを使用しなければならない。その後、対戦相手も同様にアビリティを使用できる。

> [!quote]- EN
> Some factions have **faction terrain features**, which have their own warscrolls and are set up using **DEPLOY TERRAIN** abilities. The player who begins deployment must use **DEPLOY TERRAIN** abilities first, followed by their opponent.

**ステップ2 ‒ アーミーの初期配置**

> [!quote]- EN
> Step 2 - Deploy Armies

バトルプランにおいて特に明記されていない限り、**初期配置**を開始するプレイヤーから交互に『初期配置』アビリティを使用してユニットの初期配置をする。プレイヤーが『**初期配置**』アビリティを使用する対象のユニットがなくなった場合、対戦相手も『**初期配置**』アビリティを使用する対象のユニットがなくなるまで、そのアビリティを続けて使用する必要がある。

> [!quote]- EN
> Unless otherwise specified in the battleplan, the players alternate using **DEPLOY** abilities to deploy their units, starting with the player who begins deployment. Once one player has no more **DEPLOY** abilities to use, their opponent must continue to use **DEPLOY** abilities until they also have no more to use.

**ステップ3 ‒ 初期配置フェイズのアビリティ**

> [!quote]- EN
> Step 3 - Use Deployment Phase Abilities

双方のプレイヤーがユニットの初期配置を完了した後、初期配置を開始したプレイヤーは、『**初期配置**』または『**特殊地形の初期配置**』アビリティ**ではない**、『**初期配置フェイズ**』アビリティを任意の順に使用できる。その後、対戦相手も同様にアビリティを使用できる。

> [!quote]- EN
> After both players have finished deploying their units, the player who begins deployment can use any Deployment Phase abilities that are **not DEPLOY** or **DEPLOY TERRAIN** abilities, in the order of their choosing, then their opponent can do the same.

> - 初期配置を開始するプレイヤーは、最初に『**特殊地形の初期配置**』アビリティを使用できる。その後、対戦相手も同様にアビリティを使用できる。
> - プレイヤーは、交互に『**初期配置**』アビリティを使用する。
> - 初期配置を開始するプレイヤーは、他の『初期配置フェイズ』アビリティを使用しなければならない。その後、対戦相手も同様にアビリティを使用する。

> [!quote]- EN
> - Player who begins deployment can use any **DEPLOY TERRAIN** abilities, followed by their opponent.
> - Players alternate using **DEPLOY** abilities.
> - Player who begins deployment must use any other Deployment Phase abilities, then their opponent can do so.

##### 10.1 共通の初期配置フェイズアビリティ(Universal Deployment Phase Abilities)

> **ユニットの初期配置(Deploy Unit)**（初期配置フェイズ）
>
> *追加の戦力が戦場へと投入される。*
>
> - **宣言:** 自軍のアーミーロスターから**初期配置**されていない**ユニット**を1個選択する。
> - **効果:** 自軍側陣地に全体が入るように、かつあらゆる敵軍側陣地から9mvより遠く離れた位置に、選択されたユニットを配置する。配置された後、そのユニットは**初期配置**されたものとみなされる==。==
> - **キーワード:** 初期配置

> [!quote]- EN
> **Deploy Unit**（Deployment Phase）
>
> *Additional forces take to the field.*
>
> - **Declare:** Pick a **unit** from your army roster that has not been **deployed** to be the target.
> - **Effect:** Set up the target unit wholly within friendly territory and more than 9" from enemy territory. After you have done so, it has been **deployed**.
> - **Keywords:** Deploy

> **陣営地形の初期配置(Deploy Faction Terrain)**（初期配置フェイズ）
>
> *軍勢は重要で強力な建造物を囲むように陣地を構えた。*
>
> - **宣言:** **初期配置されていない、味方陣営地形**を1個選択する。
> - **効果:** 自軍側陣地内に全体が入るように、かつあらゆる作戦目標と他の特殊地形から3mvより遠く離れた位置に、選択された陣営地形を配置する。配置された後、そのユニットは**初期配置**されたものとみなされる。
> - **キーワード:** 特殊地形の初期配置

> [!quote]- EN
> **Deploy Faction Terrain**（Deployment Phase）
>
> *The army has taken to the field surrounding an important and powerful landmark.*
>
> - **Declare:** Pick a friendly **faction terrain feature** that has not been **deployed** to be the target.
> - **Effect:** Set up the target faction terrain feature wholly within friendly territory, more than 3" from all objectives and other terrain features. After you have done so, it has been **deployed**.
> - **Keywords:** Deploy Terrain

> **連隊の初期配置(Deploy Regiment)**（初期配置フェイズ）
>
> *偉大な英雄が従者を戦いに導く。*
>
> - **宣言:** 自軍のアーミーロスターから**連隊**を1個選択する。選択された連隊に属するすべてのユニットは、**初期配置**されていてはならない。
> - **効果:** その連隊に属するすべてのユニットが**初期配置**されるまで、『**初期配置**』アビリティを交互ではなく連続して使用する。~~選択された連隊内に属していないユニット（戦場あるいは予備戦力に配置されている）を、その一連の『**初期配置**』アビリティの対象として選択することはできない~~==その一連の『初期配置』アビリティにおいて、選択された連隊内に属していないユニットを戦場あるいは予備戦力に配置することはできない==。
> - **キーワード:** 初期配置

> [!quote]- EN
> **Deploy Regiment**（Deployment Phase）
>
> *A mighty hero leads their retinue into battle.*
>
> - **Declare:** Pick a **regiment** from your army roster to be the target. No units in that regiment can have already been **deployed**.
> - **Effect:** Keep using **DEPLOY** abilities without alternating until all units in that regiment have been **deployed**. You cannot set up units that are not in that regiment on the battlefield or in reserve as part of any of those **DEPLOY** abilities.
> - **Keywords:** Deploy

> **連隊**は、複数のユニットで構成されている。連隊はアーミーの主要な構成要素のひとつである（上級ルール「アーミー編成」参照）。
>
> 陣営の中には、ストームキャスト・エターナルの『嵐の御子』アビリティなど、特別な初期配置アビリティを持つものもいる。

> [!quote]- EN
> A **regiment** is a collection of units. It is one of the main building blocks of an army (see ‘Army Composition’ in the Advanced Rules).
>
> Some factions have special **DEPLOY** abilities, such as the ‘Scions of the Storm’ ability of the Stormcast Eternals.

### バトル 11.0 - 14.4(The Battle 11.0 - 14.4)

#### 11.0 バトル手順(Battle Sequence)

それぞれのバトルは、バトルプランで指定された回数の**バトルラウンド**終了時に終了する。各バトルラウンドにおいて、各プレイヤーは自身の**ターン**を1回実行する。各ターンは、いくつもの**フェイズ**に分かれている（13.0参照）。

> [!quote]- EN
> Each battle lasts a number of **battle rounds**, specified in the battleplan. During each battle round, each player will take a **turn**. Each turn is broken down into multiple **phases** (see 13.0).

> - バトルは、決まった回数の**バトルラウンド**で終了する。
> - 各バトルラウンドは、2つの**ターン**で構成されている。
> - 現在ターンの手番であるプレイヤーを『**手番プレイヤー**』とする。
> - 各ターンには7つの**フェイズ**が存在する。
> - 各フェイズにおいて、手番プレイヤーが最初にアビリティを使用し、その後に対戦相手がアビリティを使用する。

> [!quote]- EN
> - The battle lasts a fixed number of **battle rounds**.
> - Each battle round contains 2 **turns**.
> - The player whose turn is taking place is the **active player**.
> - Each turn contains 7 **phases**.
> - In each phase, the active player uses abilities first, then their opponent does the same.

#### 12.0 バトルラウンドの開始時(Start of Battle Round)

各バトルラウンドの開始時に、次の手順に従う：

1. **手番プレイヤーの決定**：**第1バトルラウンド**である場合、アーミーの初期配置を先に終えたプレイヤーが誰が先攻するのかを決定する（バトルパックまたはバトルプランに特に明記されていない限り）。

第1バトルラウンド**ではない**場合は、プレイヤー間で『**先制ロール**』と呼ばれるロールオフをして、その勝者が誰が先攻するのかを決定する。ロールオフが**引き分け**の場合、**直前**のバトルラウンドで先攻したプレイヤーが**現在**のバトルラウンドの先攻プレイヤーを決定する。

先攻か後攻かにかかわらず、自分のターンの処理を行なっている側のプレイヤーは**手番プレイヤー**と呼ばれる。

2. **アンダードッグの決定**：勝利ポイントの最も少ないプレイヤーが、そのバトルラウンドにおける**アンダードッグ**となる。勝利ポイントが同点である場合（たとえば第1バトルラウンド中）、特に明記されていない限りアンダードッグはいないものとする。
3. **バトルラウンドの開始時アビリティ**：手番プレイヤーは、最初に『**バトルラウンドの開始時**』アビリティを使用できる。その後、対戦相手も同様にアビリティを使用できる。

> [!quote]- EN
> At the start of each battle round, follow these steps:
>
> 1. **Determine the Active Player**: If it is the **first** battle round, the player who finished setting up their army first decides who will take the first turn (unless otherwise specified in the battlepack or battleplan).&#x20;
>
> If it is **not** the first battle round, the players make a roll-off called the **priority roll** and the winner decides who will take the first turn. If the roll-off is a **tie**, the player who took the first turn in the **previous** battle round decides who will take the first turn in the **current** battle round.&#x20;
>
> When it is a player’s turn, regardless of whether they take the first or second turn, they are referred to as the **active player**.
>
> 2. **Determine the Underdog**: Whichever player has the fewest victory points is the **underdog** for the battle round. If the players are tied (e.g. in the first battle round), then there is no underdog, unless otherwise specified.
> 3. **Start of Battle Round Abilities**: The active player can use any Start of Battle Round abilities first, then their opponent can do the same.

#### 13.0 ターンのフェイズ(Turn Phases)

それぞれのプレイヤーの1つのターンは、左に示されるように**7つのフェイズ**に分かれている。各フェイズにおいて、手番プレイヤーは任意の順序で「**自軍側（…）フェイズ**」あるいは「**任意の（…）フェイズ**」とタイミング欄に記載されているアビリティを使用できる。たとえば、**移動フェイズ中**、手番プレイヤーは「**自軍側移動フェイズ**」あるいは「**任意の移動フェイズ**」とタイミング欄に記載されているアビリティを使用してもよい。

手番プレイヤーがアビリティの使用を完了した後、対戦相手は任意の順序で「**敵軍側（…）フェイズ**」あるいは「**任意の（…）フェイズ**」とタイミング欄に記載されているアビリティを使用できる。

> [!quote]- EN
> Each player’s turn is broken down into 7 **phases**, as shown on the left. In each phase, the active player can use any abilities with the ‘**Your (…) Phase**’ or ‘**Any (…) Phase**’ timing in the order of their choosing. For example, in the **Movement Phase**, the active player could use abilities with the Your Movement Phase or Any Movement Phase timing.
>
> Once the active player has finished using abilities, their opponent can then use any abilities with an ‘**Enemy (…) Phase**’ or ‘**Any (…) Phase**’ timing, in the order of their choosing.

![A small diagram showing the colours that are associated with the different phases: black for the start of turn, gold for the hero phase, grey for the movement phase, blue for the shooting phase, orange for the charge phase, red for the combat phase, and purple for the end of turn.](https://dhss9aar8ocw.cloudfront.net/b87fa2d2-22e3-4964-9d22-7417dda8b542)

##### 13.1 近接攻撃アビリティ(Fight Abilities)

**近接攻撃**のキーワードを持つアビリティは、他のアビリティとは異なる順序に従う。13.0に記述されているように、プレイヤーが『**近接フェイズ**』アビリティを使用している際、プレイヤーは『**近接攻撃**』アビリティを使用することはできない。

プレイヤーは『**近接攻撃**』アビリティ**ではない**『**近接フェイズ**』アビリティの使用を完了した後、『**近接攻撃**』アビリティを使用するために選択可能なユニットを1個、手番プレイヤーから順に交互に選んでいく必要がある。近接戦闘中である各ユニットは、使用できるのであれば**必ず**『**近接攻撃**』アビリティを使用しなければならない。

一方のプレイヤーが『**近接攻撃**』アビリティを使用する選択可能なユニットがなくなった場合、もう一方のプレイヤーは、『**近接攻撃**』アビリティを使用する選択可能なユニットがなくなるまで、『**近接攻撃**』アビリティを使用できる選択可能なユニットを継続して選ぶ。

> [!quote]- EN
> Abilities with the **FIGHT** keyword follow a different sequence to other abilities. When the players are using Combat Phase abilities as described in 13.0, they cannot use **FIGHT** abilities.
>
> After the players have finished using Combat Phase abilities that are **not FIGHT** abilities, they must alternate picking 1 eligible unit to use a **FIGHT** ability, starting with the active player. Each unit in combat **must** use a **FIGHT** ability if it is able to.
>
> Once a player has no more units that are eligible to use a **FIGHT** ability, the other player continues to pick units that are eligible to use a **FIGHT** ability, one after another, until there are no more units that are eligible to use a **FIGHT** ability.

![Step one: the active player uses all their combat phase abilities that are not Fight abilities. Step two: their opponent does the same. Step three: the players alternate using Fight abilities, one at a time, starting with the active player.](https://dhss9aar8ocw.cloudfront.net/b86f02b6-134b-42e6-aabd-6262cef7a346)

> - 手番プレイヤーは、『近接攻撃』アビリティ**ではない**『**近接フェイズ**』アビリティを使用する。その後、対戦相手も同様にアビリティを使用する。
> - 手番プレイヤーから交互に、プレイヤーは『**近接攻撃**』アビリティを使用できるユニットを選択する。
> - 各ユニットは使用できるのであれば、**必ず**『**近接攻撃**』アビリティを使用しなければならない。

> [!quote]- EN
> - The active player uses Combat Phase abilities that are **not FIGHT** abilities, then the opponent does the same.
> - Players alternate picking a unit to use a **FIGHT** ability, starting with the active player.
> - Each unit **must** use a **FIGHT** ability if it is able to.

#### 14.0 共通コアアビリティ(Universal Core Abilities)

以下の『**コア**』アビリティは、どのユニットでも使用できる。なお各ユニットは、フェイズごとに『**コア**』アビリティを最大1個使用できる（5.3参照）。

> [!quote]- EN
> The following **CORE** abilities can be used by any unit. Remember that each unit can use a maximum of 1 **CORE** ability per phase (see 5.3).

##### 14.1 移動フェイズ(Movement Phase)

> **通常移動(Normal Move)**（自軍側移動フェイズ）
>
> *戦士たちは、しっかりと地面を踏んで前進する。*
>
> - **宣言:** **近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** 選択された味方ユニットは、自身が有する【**移動力**】の距離まで移動できる。その移動中、その味方ユニットは近接戦闘に突入するような移動を**実行できない**。
> - **キーワード:** コア、移動

> [!quote]- EN
> **Normal Move**（Your Movement Phase）
>
> *The warriors advance across the battlefield.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** to use this ability.
> - **Effect:** That unit can move a distance up to its **Move** characteristic. That unit **cannot** move into combat during any part of that move.
> - **Keywords:** Core, Move

> **全力移動(Run)**（自軍側移動フェイズ）
>
> *戦士たちは、所定の位置に全速力で進む。*
>
> - **宣言:** **近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** D6の**全力移動ロール**をする。選択された味方ユニットは、自身が有する【**移動力**】に**全力移動ロール**の結果を加算した距離まで移動できる。その移動中、その味方ユニットは近接戦闘に突入するような移動を**実行できない**。
> - **キーワード:** コア、移動、全力移動

> [!quote]- EN
> **Run**（Your Movement Phase）
>
> *The unit rushes into position.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** to use this ability.
> - **Effect:** Make a **run roll** of D6. That unit can move a distance up to its **Move** characteristic added to the **run roll**. That unit **cannot** move into combat during any part of that move.
> - **Keywords:** Core, Run, Move

> **退却(Retreat)**（自軍側移動フェイズ）
>
> *身を守ることが困難になることを知りながらも、戦士たちは撤退する。*
>
> - **宣言:** **近接戦闘中である**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** 選択された味方ユニットは**D3ポイントの致命的ダメージ**を受ける。その味方ユニットは自身が有する【**移動力**】の距離まで移動できる。その味方ユニットはあらゆる敵ユニットの近接範囲内を**通り抜けることができる**。ただし、敵ユニットの近接範囲内に一部でも入るような状態で移動を**完了することはできない**。
> - **キーワード:** コア、移動、退却

> [!quote]- EN
> **Retreat**（Your Movement Phase）
>
> *The fighters disengage from combat, though at the cost of lowering their defences.*
>
> - **Declare:** Pick a friendly unit that is **in combat** to use this ability.
> - **Effect:** Inflict **D3 mortal damage** on that unit. That unit can move a distance up to its **Move** characteristic. That unit **can** move through the combat ranges of any enemy units but **cannot** end that move within an enemy unit’s combat range.
> - **Keywords:** Core, Retreat, Move

##### 14.2 遠隔フェイズ(Shooting Phase)

> **遠隔攻撃(Shoot)**（自軍側遠隔フェイズ）
>
> *戦士たちは狙いを定め、強烈な斉射を放つ。*
>
> - **宣言:** このターン中に『**全力移動**』や『**退却**』アビリティを使用していない味方ユニットを1個選択し、このアビリティを使用する。その後、選択された味方ユニットが持つ攻撃の対象として、敵ユニットを1個または複数選択する（16.0参照）。
> - **効果:** 攻撃対象であるユニットに対して**レンジアタック**を解決する。
> - **キーワード:** コア、アタック、遠隔攻撃

> [!quote]- EN
> **Shoot**（Your Shooting Phase）
>
> *The warriors take aim and unleash a deadly volley.*
>
> - **Declare:** Pick a friendly unit that has not used a **RUN** or **RETREAT** ability this turn to use this ability. Then, pick one or more enemy units as the target(s) of that unit’s attacks (see 16.0).
> - **Effect:** Resolve **shooting attacks** against the target unit(s).
> - **Keywords:** Core, Attack, Shoot

##### 14.3 突撃フェイズ(Charge Phase)

> **突撃(Charge)**（自軍側突撃フェイズ）
>
> *勇ましい雄叫びとともに、戦士たちは敵に突撃する。*
>
> - **宣言:** このターン中に『**全力移動**』や『**退却**』アビリティを使用しておらず、かつ**近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。その後、2D6の**突撃ロール**をする。
> - **効果:** 選択された味方ユニットは、**突撃ロール**の結果に等しい数の距離まで移動できる。その味方ユニットは、あらゆる敵ユニットの近接範囲内を**通り抜ける**ことができる。またその移動は、視認状態にある敵ユニットの½mv以内に一部が入るように**完了**されなければならない。そのような移動を実行した場合、このアビリティを使用した味方ユニットは**突撃**したものとみなされる。
> - **キーワード:** コア、移動、突撃

> [!quote]- EN
> **Charge**（Your Charge Phase）
>
> *With a mighty battle cry, the warriors charge into combat with the enemy.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** and has not used a **RUN** or **RETREAT** ability this turn to use this ability. Then, make a **charge roll** of 2D6.
> - **Effect:** That unit can move a distance up to the value of the **charge** **roll**. That unit **can** move through the combat ranges of any enemy units and **must** end that move within ½" of a visible enemy unit. If it does so, the unit using this ability has **charged**.
> - **Keywords:** Core, Charge, Move

##### 14.4 近接フェイズ(Combat Phase)

> **近接攻撃(Fight)**（任意の近接フェイズ）
>
> *熾烈な接近戦が繰り広げられる中、戦士たちは敵に襲い掛かる。*
>
> - **宣言:** **近接戦闘中**またはこのターン中に**突撃を実行**している味方ユニットを1個選択し、このアビリティを使用する。選択された味方ユニットは**接敵移動**を1回実行できる（15.3参照）。次に、選択された味方ユニットが**近接戦闘中**である場合、その味方ユニットが持つ攻撃の対象として、敵ユニットを1個または複数選ばなければならない（16.0参照）。
> - **効果:** 攻撃対象であるユニットに対して**メレーアタック**を解決する。
> - **キーワード:** コア、アタック、近接攻撃

> [!quote]- EN
> **Fight**（Any Combat Phase）
>
> *Locked in a deadly melee, the fighters strike out at their foes.*
>
> - **Declare:** Pick a friendly unit that is **in combat** or that **charged** this turn to use this ability. That unit can make a **pile-in move** (see 15.3). Then, if that unit is **in combat**, you must pick one or more enemy units as the target(s) of that unit’s attacks (see 16.0).
> - **Effect:** Resolve **combat attacks** against the target unit(s).
> - **Keywords:** Core, Attack, Fight

### 移動 15.0 - 15.5(Movement 15.0 - 15.5)

#### 15.0 移動(Movement)

アビリティの中には、ユニットの移動を可能にするものがある。ユニットが移動する場合、そのユニット内に属する各兵は、そのユニットの司令官が選択した順序で、1個ずつ移動できる。

兵が移動するとき、兵は自由に旋回して方向を何度も変えることができるが、その兵が乗っているベースのどの部分も、使用されているアビリティで許されている最大距離を超えるような移動を実行することはできない。兵は戦場端を越えたり、他の兵を通り抜けたりすることはできない。また兵は、他の兵の上で移動が完了するような移動を実行することはできない（ベースは兵の一部として扱われる）。

兵のベースは、移動するときに戦場と平行であるとみなされている。兵が凸凹とした地面で移動を完了した場合、兵のベースは可能な限り戦場と平行になるように、兵は自力で立ち上がっている状態を保つことができなければならない（つまり、兵は戦場の地面に横たわったり、転倒しないように特殊地形に寄りかかったりすることはできない）。

> [!quote]- EN
> Some abilities allow a unit to move. When a unit moves, each model in that unit can move, one at a time, in the order chosen by that unit’s commander.
>
> When a model moves, it can pivot and change direction as often as you like, but no part of that model’s base can move a greater total distance than the maximum allowed by the ability used. Models cannot move beyond the edge of the battlefield or through other models, and they can never end a move standing on top of another model (the base counts as part of the model).
>
> A model’s base is assumed to remain parallel with the battlefield as it moves. If a model ends its move on an uneven surface, it must be able to stand up by itself with its base as close to parallel with the battlefield as possible (in other words, models cannot lie flat on the battlefield or lean against terrain to stop them from falling over).

![A unit of five Liberators with their combat range marked in blue, a Skaven Grey Seer, and a wall. The diagram shows the Grey Seer using the 'Normal Move' ability to move around the wall. Importantly, at no point does the Grey Seer's move encroach on the blue area indicating the Liberators' combat range.](https://dhss9aar8ocw.cloudfront.net/a6fa4d4d-693e-4cca-9e31-1076031a5982)

*このグレイシーアは、戦場での位置を変更するために『通常移動』アビリティを使用した。その移動中どのような状況においてもリベレイターの近接範囲内に入ることはできないため、グレイシーアは青枠で示された領域外にいなければならない。*

> [!quote]- EN
> This Grey Seer is using the ‘Normal Move’ ability to change its position on the battlefield. No part of that move can be within the combat range of the Liberators, so the Grey Seer has to stay outside the area marked in blue.

> - ユニットが移動する場合は、そのユニット内に属する任意の数の兵を移動させる。
> - 各兵は~~ベースの中心を軸として旋回できるが~~==自由に方向を変えたり旋回したりできるが==、ベースのどの部分も最大距離を超えて移動することはできない。
> - ユニットは、アビリティで指定される最大移動距離まで、任意の距離を移動してもよい。
> - ユニットは隊形を保~~持して移動~~==った状態で移動を完了==する必要がある。

> [!quote]- EN
> - When moving a unit, move any number of models in that unit.
> - Each model can turn and pivot, but no part of its base can move farther than the maximum distance.
> - Units can move any distance up to the maximum specified in the ability.
> - Units must end their move in coherency.

##### 15.1 ユニットの隊形(Coherency)

ユニットが**配置**されたり、**移動を完了**したりするとき、ユニットは常に単一のグループを保持していなければならない。ユニット内の各兵が、そのユニット内の自身以外である**他の兵1体以上**と水平方向に測定される**隊形範囲内**に一部でも入っている場合（兵2体の間の高低差は無視される）、そのユニットはユニットの隊形を保っている状態であるとみなされる。

ユニットの大部分において**隊形範囲は½mv**であるが、一部のユニット（特に突出した部分をもつ大型兵のユニット）では、プレイを分かり易くするためにウォースクロールに記載されている隊形範囲が大きくなっている。ユニット内に**7体以上**の兵がいる場合、そのユニット内の各兵がそのユニット内に属する自身以外の**他の兵2体以上**の隊形範囲内に一部でも入っているならば、そのユニットはユニットの隊形を保っている状態であるとみなされる。

ユニットが単一のグループとして移動を完了できない場合、その移動を実行することはできない。

> [!quote]- EN
> Any time a unit is **set up** or **ends a move**, it must be in a single group. A unit is considered to be in a coherent group if each model in that unit is within **coherency range**, measured horizontally, of **at least 1 other model** in that unit (ignore differences in height between the two models).
>
> For the majority of units, **coherency range is ½"**, though some units (particularly those with large models with overhanging parts) have a longer coherency range noted on their warscroll for ease of play. While there are **7 or more** models in a unit, that unit is considered to be in a coherent group if each model in that unit is within coherency range of **at least 2 other models** in that unit.
>
> If it is not possible for a unit to end a move in a single coherent group, that move cannot be made.

> - 移動が完了した後、ユニットは単一のグループを保持していなければならない。
> - 隊形範囲は水平方向に½mvである。
> - 各兵は、同じユニットに属する自身以外の兵1体の隊形範囲内に一部が入っていなければならない。
> - ユニットが7体以上の兵で構成されている場合、各兵はユニットに属する自身以外の兵2体の隊形範囲内に一部が入っていなければならない。

> [!quote]- EN
> - After finishing a move, a unit must be in a single group.
> - Coherency range is ½" horizontally.
> - Each model must be within coherency range of a different model from the same unit.
> - While a unit has 7+ models, each model must be in coherency with 2 other models in the unit.

##### 15.2 特殊地形上の移動(Moving Across Terrain)

兵が移動するとき、兵は**特殊地形**を乗り越えて移動できるが、特殊地形を通り抜けることはできない。兵は**高さが1mv以下**である特殊地形を、あたかもないかのように乗り越えて移動できる。兵は垂直方向に移動することで、高さが1mvを超える特殊地形を**昇り降り**できる。そのような垂直方向の移動距離は、その移動の一部としてカウントされる。兵は昇っている最中に移動を完了することはできない。

> [!quote]- EN
> When a model moves, it can move over **terrain features** but not through them. A model can be moved over terrain features that are **1" or less in** **height** as if they were not there. A model can be moved vertically in order to **climb up or down** any terrain features that are taller than 1", counting the vertical distance as part of its move. Models cannot end a move mid-climb.

##### 15.2.1 飛び降りる(Jumping Down)

特殊地形上にいる兵は移動するとき、特殊地形の端から**飛び降りる**ことができ、同じ特殊地形または異なる特殊地形の下部に着地したり、戦場の地面に着地できる。飛び降りる場合、その兵の移動進路を特殊地形の端まで引く必要がある。その後、その兵は任意の距離を飛び降りることができるが、任意の距離を飛び降りた場合、その移動はただちに終了する。兵は飛び降りている途中にどのような移動も完了することはできない。結果として移動を完了できない場合、その移動を実行することはできない。

> [!quote]- EN
> When a model that is on a terrain feature moves, it can **jump down** from the edge of the terrain feature to land on a lower part of the same or a different terrain feature or to land on the battlefield. To do so, you must trace the path of the model’s move to the edge of the terrain feature. Then, that model can jump down any distance, but doing so immediately ends their move. Models cannot end any kind of move mid-jump – if it is not possible to end the move as a result, that move cannot be made.

![A Liberator moving over a small piece of terrain. There is a white line that leads from the Liberator's starting position, flows over the terrain feature, and then ends at the model's final position. This indicates that the model is presumed to stay in contact with the terrain feature as it climbs over it.](https://dhss9aar8ocw.cloudfront.net/bf28d0a3-a741-47ac-bc6a-f87869f254c3)

*兵が特殊地形の上を移動するとき、兵のベースは特殊地形と接触しており、かつ戦場と平行であるとみなされる。兵は特殊地形を昇り降りできる。兵は特殊地形から任意の距離を飛び降りることができるが、そうした場合、その移動はただちに終了する。*

> [!quote]- EN
> As a model moves across terrain, its base is assumed to stay in contact with the terrain feature and parallel to the battlefield. Models can climb up or down terrain. They can jump down too, but this ends their move.

> - 高さ1mv以下の特殊地形を、兵はペナルティを受けることなく乗り越えることができる。
> - 兵は特殊地形を昇り降りすることができ、高所から飛び降りることができる。
> - 兵は昇ったり、降りたりしている最中に移動を完了することはできない。

> [!quote]- EN
> - Models can move freely over terrain features 1" or less in height.
> - Models can climb up and down terrain features, and they can jump down from a higher ledge.
> - Models cannot end a move mid-climb or mid-jump.

##### 15.3 接敵移動(Pile-in Moves)

**『近接攻撃』**アビリティなどの一部のアビリティにおいて、ユニットは**接敵移動**と呼ばれる短い距離の移動が可能であり、近接攻撃に適した位置取りを実行できる。接敵移動をする場合：

**自軍のユニットが近接戦闘中である場合：**自軍のユニットと**近接戦闘中**である、接敵移動の**対象**となる敵ユニットを1個選択する。自軍側ユニットの各兵は、最大3mvまで移動できる。その移動は、あらゆる敵ユニットの近接範囲内を通り抜けることができる。ただし、各兵はその移動を**攻撃対象**であるユニットから**離れることなく**完了しなければならない。移動の完了時、自軍のユニットは移動開始時に近接戦闘中であったすべてのユニットと近接戦闘状態でなければならない。

**自軍のユニットが近接戦闘中ではない場合：**自軍側ユニットの各兵は、どの方向にも最大3mvまで移動できる。その移動は、あらゆる敵ユニットの近接範囲内を通り抜けることができる。またその移動は、1個以上の敵ユニットの近接範囲内で完了してもよい。

> [!quote]- EN
> Some abilities, such as **Fight** abilities, allow a unit to make a short move called a **pile-in move** to get into a better position for combat. To do so:
>
> **If your unit is in combat**: Pick an enemy unit your unit is **in combat** with to be the **target** of the pile-in move. Each model in your unit can move up to 3". That move can pass through the combat ranges of any enemy units, but each model must end that move **no further from** the **target** unit. At the end of the move, your unit must still be in combat with all units that it was in combat with at the start of the move.
>
> **If your unit is not in combat**: Each model in your unit can move 3" in any direction. Th at move can pass through and end within the combat ranges of any enemy units.

> - 接敵移動：最大3mvまでの移動を実行する。
> - ユニットが近接戦闘中である場合、ユニットは攻撃対象となる敵ユニットに接近する、あるいは少なくとも同程度に接近している状態で移動を完了しなければならない。

> [!quote]- EN
> - Pile in: move up to 3".
> - If in combat, the unit must end the move closer, or at least as close, to the target enemy unit.

##### 15.4 飛行(Flying)

**飛行**のキーワードを持つユニットは、次のパッシブアビリティを得る：

> [!quote]- EN
> Units with the **FLY** keyword have the following passive ability:

> **飛行(Fly)**（パッシブ）
>
> *戦場の上空に舞い上がり、この部隊は他の兵が到達することのできぬ地点へと降り立つ。*
>
> - **効果:** このユニットは移動するとき、他の兵や特殊地形、敵ユニットの近接範囲を無視する。移動を可能にしたアビリティに明記されていない限り、近接戦闘に突入するような状態で移動を完了することはできない。このユニットの垂直方向に移動する距離は測定されず、無視される。

> [!quote]- EN
> **Fly**（Passive）
>
> *Soaring above the battlefield, this unit can reach destinations that are inaccessible to other troops.*
>
> - **Effect:** As this unit moves, it ignores other models, terrain features and the combat ranges of enemy units. It cannot end its move in combat unless specified in the ability that allowed it to move. Ignore any vertical distance moved for this unit.

飛行ユニットが移動するときは、移動の間にある兵や特殊地形を無視して、任意の水平方向に移動する。移動先の地点で移動を完了できる場合、その任意の場所に飛行ユニットを配置してもよい。なお、ユニットの中には、実際には飛べなくても**飛行**のキーワードを持つものもある。これは多くの場合、戦場を巧みに飛び跳ねたり、這い回ったりするユニットを表しているので、実際には飛べなくても飛んでいるようなものなのだ！

> [!quote]- EN
> When moving flying units, move them horizontally in any direction, ignoring intervening models and terrain, and place them where you wish, so long as they are allowed to end their move on that spot. Note that some units have the **FLY** keyword even if that unit can’t really fly. This often represents units that bounce, bound or skitter across the battlefield so adeptly that they might as well be flying!

##### 15.5 張り出したミニチュア(Overhanging Models)

ミニチュアの中には、ベースから張り出しているものがある。このようなミニチュアを移動させるとき、その兵がある場所に配置可能かどうかを判定する際、張り出している部分は存在しないものとして扱う。その付近で他の兵が移動を完了する場合、可能なら張り出したミニチュアを回転させ、他の兵の移動完了を妨げないようにする。そのように張り出したミニチュアを回転させるならば、ベースは同じ位置に留まっていなければならない。円形のベースは任意に回転させてよく、楕円のベースは~~180°まで~~==ちょうど180°だけ==回転させてよい。上記のようにできない場合は、兵が移動を完了するはずの場所を記録（同一サイズの空ベースを置くなど）し、兵自体は傍に置いておく。そして、物理的に配置が可能になり次第その兵を記録した場所に戻す。

> [!quote]- EN
> Some models overhang their base. When moving models, overhanging parts should be treated as if they do not exist when determining where a model could be placed. Where possible, a model should be rotated to allow for another model to end a move in proximity to it. When rotating a model this way, the base must occupy the same position – a circular base may be rotated any amount, while an oval base may only be rotated 180°. Otherwise, mark down the location of where the model should end its move (such as with an empty base of the same size) and place the model to the side. Return the model to the table as soon as it is physically possible to do so.

##### 15.6 突撃移動(Charge Moves)

ルールの中には、ユニットが突撃移動を完了したことを言及しているものがある。そのユニットが使用した『突撃移動』アビリティが解決され、そのアビリティの一環としてユニットが突撃を実行した場合、ユニットは突撃移動を完了したものとみなされる。

> [!quote]- EN
> Some rules reference a unit finishing or ending a charge move. This is considered to occur when a **CHARGE MOVE** ability that unit used resolves and the unit has charged as part of that ability.

### 攻撃 16.0 - 18.4(Attacking 16.0 - 18.4)

#### 16.0 攻撃対象の選択(Picking Targets)

ユニットが**『アタック』**アビリティを宣言するとき、ユニットは自身が持つ**攻撃**の対象として、ユニットを1個または複数選ばなければならない。それぞれの兵が繰り出すことのできる攻撃の数は、その兵が使用する**武器**の**【攻撃回数】**と等しい。多くの場合、兵は自身のウォースクロール上に記載されているすべての武器で攻撃をする（メレーアタックには近接武器、レンジアタックには遠隔武器）。一部のウォースクロールでは、ユニット内に属する特定の兵は特殊武器を装備していたり、ユニットは攻撃の際に2個以上の武器の中からどれかを選ばなけれ==ば==ならないと指定していることがある。

ユニットが**近接戦闘中**である場合、そのユニットは自身と近接戦闘中であるユニットだけを攻撃できる。兵が2個以上の攻撃を有する場合は、必要に応じて選択可能な攻撃対象に攻撃を振り分けることができる。

> [!quote]- EN
> When declaring an **ATTACK** ability for a unit, you must pick the target unit(s) for its **attacks**. The number of attacks each model can make is equal to the **Attacks** characteristic of the **weapons** it is using. In most cases, models attack with every weapon on their warscroll (melee weapons for combat attacks, ranged weapons for shooting attacks), though some warscrolls specify that certain models in the unit are armed with special weapons or that the unit must pick between multiple weapons when it attacks.
>
> If the unit is **in combat**, it can only target units that are in combat with it. If a model has more than one attack, you can split the attacks between eligible targets as you wish.

- **メレーアタック**は、**近接武器**によって実行される。攻撃対象であるユニットは、攻撃側の兵の**近接範囲内**に一部が入っており、かつ攻撃側の兵から**視認状態**でなければならない。装備しているすべての近接武器で、兵は攻撃をしなければならない。
- **レンジアタック**は、**遠隔武器**によって実行される。攻撃対象であるユニットは、攻撃側の兵が使用する武器の**射程内**に一部が入っており、かつ攻撃側の兵から**視認状態**でなければならない。特に明記されていない限り、兵は**近接戦闘中**にレンジアタックをすることは**できない**（20.0武器アビリティ参照）。

> [!quote]- EN
> - **Combat attacks** are made with **melee weapons**. The target unit(s) must be within the **combat range** of the attacking model and **visible** to it. The model must attack with all of the melee weapons it is armed with.
> - **Shooting attacks** are made with **ranged weapons**. The target unit(s) must be within a distance equal to the **Range** characteristic of the weapon being used and **visible** to the attacking model. Models **cannot** make shooting attacks if their unit is **in combat**, unless otherwise specified (see 20.0 Weapon Abilities).

- **『アタック』**アビリティを宣言するとき、自身が持つ**すべて**の攻撃において、その攻撃対象を選択する。
- ユニットが**近接戦闘中**である場合、そのユニットは自身と**近接戦闘中**であり、かつ自身から**視認状態**にあるユニットだけを攻撃できる。
- **メレーアタック**をする場合、攻撃側の兵の**近接範囲内**に攻撃対象の一部が入っていなければならない。
- **レンジアタック**をする場合、攻撃対象は武器の**射程内**に一部が入っており、かつ**視認状態**でなければならない。
- 特に明記されていない限り、ユニットは**近接戦闘中**に**レンジアタック**を実行することはできない。

> [!quote]- EN
> - Pick targets for **all** attacks when declaring an **ATTACK** ability.
> - If a unit is **in combat**, it can only attack units it is **in combat** with and that are **visible** to it.
> - If making a **combat attack**, the target must be within the attacking model’s **combat range**.
> - If making a **shooting attack**, the target must be **visible** and within the weapon’s **Range**.
> - A unit cannot make **shooting attacks** if it is **in combat**, unless otherwise specified.

#### 17.0 攻撃手順(The Attack Sequence)

攻撃対象であるユニットに対して実行する攻撃ごとに、次の手順1-4を解決する。**『アタック』**アビリティにおいて2個以上の敵ユニットを選択した場合は、1個のユニットに対する攻撃をすべて解決した後、任意の順序で次のユニットを攻撃する。攻撃手順に慣れてきて、プレイスピードを上げたい場合は、「ダイスロールの高速化」（17.3参照）を読み進めてみよう。

**1. ヒットロール：**ダイスを1個ロールする。ヒットロールが攻撃側の武器が示している**【ヒット成功値】**以上であれば、その攻撃は**ヒット成功**である：次の手順に進む。それ以外の場合、その攻撃は**失敗**し、攻撃手順はここで終了する。ヒットロールで修正前の出目1が出た場合は、それは失敗として扱われる。武器のヒットロールで修正前の**出目6**が出た場合は、その攻撃は**クリティカルヒット**として扱われる。

**2. ウーンズロール：**ダイスを1個ロールする。ウーンズロールが攻撃側の武器が示している**【ウーンズ成功値】**以上であれば、その攻撃は**ウーンズ成功**である：次の手順に進む。それ以外の場合、その攻撃は**失敗**し、攻撃手順はここで終了する。ウーンズロールで修正前の出目1が出た場合は、それは失敗として扱われる。

**3. セーブロール：**攻撃によって選択された**攻撃対象**のユニットを操作する司令官はダイスを1個ロールする。攻撃側の武器が示している**【貫通値】**の数、セーブロールは減算される。セーブロールで修正前の出目1が出た場合は、それは失敗として扱われる。攻撃対象であるユニットがセーブロールで**【防御力】**以上の出目を出した場合、その攻撃は**失敗**したものとして扱われ、攻撃手順はここで終了する。それ以外の場合、その**攻撃は成功**し、次の手順に進む。

**4. ダメージ量の判定：**攻撃は、武器の**【ダメージ量】**に等しい数の**ダメージ**をユニットに**与える**。加えられたダメージは、攻撃対象であるユニットの一時的な**ダメージプール**に追加される。

**『アタック』**アビリティの手順の中で実行されたすべての攻撃に対して、これらの手順を完了した後、そのアビリティにおける攻撃は**解決**され、**ダメージ手順**（18.0参照）に進むことができる。

> [!quote]- EN
> Resolve steps 1-4 below for each attack made against a target unit, one attack at a time. If you picked more than one target unit for the **ATTACK** ability, resolve all the attacks made against one unit before moving on to the next, in an order of your choosing. Once you are familiar with the attack sequence, see ‘Fast Dice Rolling’ (see 17.3) if you want to speed up play.
>
> **1. Hit Roll**: Roll a dice. If the roll equals or exceeds the attacking weapon’s **Hit** characteristic, the attack scores a **successful hit**: move on to the next step. If not, the attack **fails** and the attack sequence ends. Unmodified hit rolls of 1 always fail. If an unmodified hit roll for an attack made with a weapon is a **6**, that attack is a **critical hit**.
>
> **2. Wound Roll**: Roll a dice. If the roll equals or exceeds the attacking weapon’s **Wound** characteristic, the attack **successfully wounds**: move on to the next step. If not, the attack **fails** and the attack sequence ends. Unmodified wound rolls of 1 always fail.
>
> **3. Save Roll**: The commander of the **target** unit rolls a dice, subtracting the attacking weapon’s **Rend** characteristic from the roll. Unmodified save rolls of 1 always fail. If the roll equals or exceeds the **Save** characteristic of the target unit, the attack **fails** and the attack sequence ends. If not, it is a **successful attack**: move on to the next step.
>
> **4. Determine Damage**: Th e attack **inflicts** a number of **damage points** on the unit equal to the **Damage** characteristic of the weapon. Inflicted damage points are added to a temporary **damage pool** for the target unit.
>
> After completing these steps for all of the attacks made as part of that **ATTACK** ability, the attacks for that ability are **resolved** and you can move on to the **damage sequence** (see 18.0).

> クリティカルヒットはそれ自体には効果がないが、追加の効果を引き起こすことがある（20.0武器アビリティ参照）。

> [!quote]- EN
> Critical hits have no effect on their own but often trigger additional effects (see 20.0 Weapon Abilities).

> 攻撃対象であるユニットのダメージプールに記録されているダメージの数を管理する。ダメージを受けているユニットの傍らにダイスを置いておくとダメージ管理が便利である。

> [!quote]- EN
> Keep track of the number of damage points in the damage pools of target units. Placing dice next to those units is a handy way of doing this.

##### 17.1 攻撃の修正と上限値(Attack Modifiers and Caps)

**ヒットロール**、**ウーンズロール**、**セーブロール**には、絶大的な威力を誇るアビリティの組み合わせを防ぐために**上限値**が設けられている。**ヒットロール**または**ウーンズロール**をする際、ロールに適用されるすべての+修正と-修正を合計する。ヒットロールとウーンズロールに対する修正の上限値は、**最大+1の修正**（プラス修正の場合）あるいは**最大-1の修正**（マイナス修正の場合）である。**セーブロール**をする際、ロールに適用されるすべてのプラス修正とマイナス修正を合計する。セーブロールに対する修正の上限値は、**最大+1**の修正である。なお、**ヒットロール**と**ウーンズロール**とは異なり、**セーブロール**から**減算**できる量に**上限**はない。

> [!quote]- EN
> Modifiers to **hit rolls**, **wound rolls** and **save rolls** are **capped** to prevent overwhelming combinations of abilities. When making a **hit roll** or a **wound roll**, add up all positive and negative modifiers that apply to the roll, then cap the result at a **maximum of +1** (if positive) or a **minimum of -1** (if negative). When making a **save roll**, add up all the positive and negative modifiers that apply to the roll, then cap the result at a **maximum of** **+1**. Note that, unlike **hit rolls** and **wound rolls**, there is **no cap** on the amount that can be **subtracted** from **save rolls**.

##### 17.2 致命的ダメージ(Mortal Damage)

アビリティの中には、**致命的ダメージ**を与えるものがある。アビリティがユニットに致命的ダメージを与える場合、そのアビリティが与えるユニットのダメージプールに致命的ダメージの量を加算する（18.2ダメージの割り振り参照）。

> [!quote]- EN
> Some abilities inflict **mortal damage**. If an ability inflicts mortal damage on a unit, add that number of damage points to the unit’s damage pool for that ability (see 18.2 Allocating Damage).

##### 17.3 ダイスロールの高速化(Fast Dice Rolling)

ゲーム展開のスピードを向上させるために、多くの場合は同時に2個以上の攻撃をすることができる。同時に2個以上の攻撃をする場合、すべての攻撃は同じ**【ヒット成功値】**、**【ウーンズ成功値】**、**【貫通値】**、**【ダメージ量】**、同じ**武器アビリティ**（武器アビリティがある場合、20.0参照）==を==持っており、かつ同一の敵ユニットを攻撃対象にしていなければならない。上記を満たす攻撃を実行する場合、すべてのヒットロールを同時にし、すべてのウーンズロール、すべてのセーブロールも同時に実施する。次に、攻撃目標のユニットに与えられるすべてのダメージを合計し、ダメージ手順に進む（18.0参照）。

ダイスロールの高速化をする最中に攻撃の攻撃手順が終了した場合、その特定の攻撃だけが終了するのであり、すべての攻撃における攻撃手順が停止するわけではない。

> [!quote]- EN
> In order to speed up play, it is often possible to make several attacks at once. If you choose to do so, all of the attacks must have the same **Hit, Wound, Rend and Damage** characteristics, the same **weapon abilities** (if any – see 20.0), and they must target the same enemy unit. If this is the case, make all of the hit rolls at the same time, then all of the wound rolls and finally all of the save rolls. Then, add up all the damage points inflicted on the target unit and move on to the damage sequence (see 18.0).
>
> If the attack sequence ends for an attack made while fast dice rolling, it doesn’t stop the attack sequence for all the attacks, just that specific attack.

#### 18.0 ダメージ手順(The Damage Sequence)

ユニットにダメージを与えるアビリティの効果を解決した後、以下の手順に従う。アビリティが2個以上のユニットにダメージを与える場合は、それらのユニットに1個ずつ、以下の手順を実行する。それぞれの司令官は、手番プレイヤーから順に、任意の順番で自軍のユニットにダメージを割り振る。

**1. 適用できるのであれば、**攻撃対象であるユニットのダメージプールにあるすべてのダメージに対して加護セーブを解決する（17.0参照）。

**2. ユニットのダメージプールにあるダメージを割り振り、**撃破された兵を取り除く（18.3参照）。

> [!quote]- EN
> After resolving the effect of any ability that inflicts damage points on a unit, follow the steps below. If the ability inflicted damage points on more than one unit, follow the steps below for each of those units, one at a time. Each commander allocates damage points to their own units, in the order of their choosing, starting with the active player.
>
> **1. Resolve ward saves** for all damage points in the target unit’s damage pool, if applicable (see 17.0).
>
> **2. Allocate the damage points** in the unit’s damage pool and remove slain models (see 18.3).

##### 18.1 加護セーブ(Ward Saves)

**加護**のキーワードを持つユニットは、『加護セーブ』パッシブアビリティを得る。**加護**のキーワードの後に記されている数値は、『加護セーブ』の**加護の値**を示している。ユニットが**加護（5+）**を有する場合、加護の値は5になる。ユニットが2個以上の加護セーブを持っている場合は、最も数値の低い加護セーブが適用され、他の加護セーブは適用されない。

> [!quote]- EN
> Units with the **WARD** keyword have the ‘Ward Save’ passive ability. The number after the **WARD** keyword indicates the **ward value** for the ward save. If a unit had **WARD** **(5+)**, for example, its ward value would be 5. If a unit has more than one ward save, only the ward save with the lowest value applies to it; the other has no effect.

> **加護セーブ(Ward Save)**（パッシブ）
>
> *稀にみる反射神経、耐久力、神秘なる保護の源を通じて、これらの戦士はさもなければ致命的な傷とならん攻撃を巧みに避ける。*
>
> - **効果:** ダメージ手順のステップ1において（18.0参照）、このユニットの**ダメージプール**にある**ダメージ1ポイント**につき、D6の**加護ロール**を1回実行する。加護ロールがこのユニットの**加護の値**以上であれば、その1ポイントのダメージはダメージプールから取り除かれる。

> [!quote]- EN
> **Ward Save**（Passive）
>
> *Whether through their uncanny reflexes, unnatural toughness or a source of mystical protection, these warriors can avoid otherwise lethal attacks.*
>
> - **Effect:** In step 1 of the damage sequence (see 18.0), make a **ward roll** of D6 for each **damage point** in this unit’s **damage pool**. If the roll equals or exceeds this unit’s **ward value**, remove that damage point from the damage pool.

##### 18.2 ダメージの割り振り(Allocating Damage)

ダメージを与えるアビリティの効果を解決した後（攻撃、致命的~~な~~ダメージ、またはその両方）、ダメージを**割り振る**必要がある。

ユニットにダメージを**割り振る**とき、そのダメージプールのダメージは1ポイントずつユニットに割り振られる。ユニットに割り振られるダメージの数がそのユニットの**【体力】**と等しくなるたびに、そのユニット内に属する1体の兵が**撃破**される（戦場から取り除かれる）。ユニット内に属する兵が1体取り除かれた後、そのユニットに割り振られているダメージの数は0にリセットされる。ダメージプールにあるダメージが無くなるまで、ダメージの割り振りを継続する。

ユニットに割り振られるダメージの数が、兵を撃破するのに十分でない場合は、現在ユニットに割り振られているダメージの数を記録する（多くのプレイヤーは、ユニットの傍らにダイスまたはマーカーをおいてダメージを記録している）。ユニットに1ポイント以上のダメージが割り振られているならば、そのユニットは**損傷状態**にある。

> [!quote]- EN
> After resolving the effect of any ability that inflicts damage points (whether via attacks, mortal damage or both), you must **allocate** the damage points.
>
> When **allocating** damage points to a unit, the damage points in its damage pool are allocated to it one at a time. Each time the number of damage points allocated to the unit equals the **Health** characteristic of that unit, 1 model in that unit is **slain** (and removed from play) and the number of damage points allocated to that unit is reset to 0. Keep allocating damage points until there are none left in the damage pool.
>
> If the number of damage points allocated to a unit is not enough to slay a model, keep track of the number of damage points currently allocated to the unit (most players place a dice or markers next to the unit). While a unit has any damage points allocated to it, it is **damaged**.

##### 18.3 撃破された兵(Slain Models)

ユニットを操作する司令官は、ユニット内のどの兵が撃破されたのかを選ばなければならない。しかしながら、撃破された各兵が戦場から取り除かれた後、そのユニットは単一のグループとして隊形を保っている必要がある（15.1参照）。隊形を保つことができない場合は、そのユニットが単一のグループとして隊形を保つようになるまで、兵は1体ずつ取り除かれる。

可能な限り少ない数の兵を取り除いて、単一のグループとして隊形を保つようにしなければならない。

> [!quote]- EN
> The commander of a unit must pick which model(s) in the unit are slain. However, after each slain model is removed, the unit must be in a single coherent group (see 15.1). If this is not possible, continue to remove models, one at a time, until the unit is in a single coherent group.
>
> You must remove the fewest models possible to make the unit a single coherent group.

##### 18.4 全滅したユニット(Destroyed Units)

ユニット内の最後の兵が撃破されたとき、そのユニットは**全滅**したことになる。また、そのユニットに与えられる残りのダメージはすべて無効になる。同様に何かがユニットを全滅させた場合、そのユニットのすべての兵は撃破され、ゲームから取り除かれる。

> [!quote]- EN
> When the last model in a unit is slain, the unit is **destroyed** and all remaining damage points inflicted on that unit have no effect. Similarly, if something causes a unit to be destroyed, all models in the unit are slain and removed from play.

#### 攻撃の図解(Attacking Diagram)

![A flow chart that shows the steps of the attack sequence and the damage sequence.](https://dhss9aar8ocw.cloudfront.net/a25431c4-38f6-41e2-8c6c-c817a0b0505e)

> - 攻撃側は、D6の**ヒットロール**を1回実行する。ヒットロールが攻撃側の武器が示している**【ヒット成功値】**以上であれば、その攻撃は**ヒット成功**である。
> - 攻撃側は、D6の**ウーンズロール**を1回実行する。ウーンズロールが攻撃側の武器が示している**【ウーンズ成功値】**以上であれば、その攻撃は**ウーンズ成功**である。
> - 防衛側は、D6の**セーブロール**を1回実行する。攻撃側の武器が示している**【貫通値】**の数、セーブロールは減算される。セーブロールが防衛側ユニットの**【防御力】**を下回る場合、その攻撃は**攻撃成功**である。
> - 攻撃側の武器が示している**【ダメージ量】**に等しい数の**ダメージ**を攻撃対象に**与える**。
> - 加護ロールを解決する。
> - ダメージの割り振りをする。
> - **ヒットロール**、**ウーンズロール**、**セーブロール**で修正前の出目1が出た場合、それは失敗として扱われる。

> [!quote]- EN
> - Attacker makes a **hit roll** of D6. If the roll equals or beats the weapon’s **Hit** characteristic, it is a **successful hit**.
> - Attacker makes a **wound roll** of D6. If the roll equals or beats the weapon’s **Wound** characteristic, it is a **successful wound**.
> - Defender makes a **save roll** of D6. Subtract the attacking weapon’s **Rend** characteristic from the roll. If the result is less than the defending unit’s **Save** characteristic, it is a **successful attack**.
> - **Inflict** an amount of **damage** on the target equal to the attacking weapon’s **Damage** characteristic.
> - Resolve ward saves.
> - Allocate damage points.
> - Unmodified **hit rolls**, **wound rolls** and **save rolls** of 1 always fail.

#### 攻撃の使用例(Attacking Example)

**司令官エリックのストームキャストが、エマが指揮するスケイヴンとスピアヘッドのゲームでぶつかり合う。エリックのリベレイターは突撃（14.3参照）を実行する。そして『近接攻撃』アビリティの宣言手順において、リベレイターはエマのクロウロード（15.3参照）に接敵移動をし、かつ自身が持つすべての攻撃（16.0参照）の攻撃対象としてクロウロードのユニットを選択している。この例では、ゲームの展開を速めるために「ダイスロールの高速化」を用いている。**

> [!quote]- EN
> Erik’s Stormcast Eternals are facing off against Emma’s Skaven in a close game of Spearhead. Erik’s Liberators have charged (see 14.3), and in the declare step of the ‘Fight’ ability, they have piled in towards Emma’s Clawlord (see 15.3) and targeted that unit with all of their attacks (see 16.0). In this example we’ll be using fast dice rolling to speed up play.

![A unit of five Liberators in combat with a Skaven Clawlord on Gnaw-beast. Four of the Liberators are picked out with green borders to indicate that those are the models that are armed with Warhammers.](https://dhss9aar8ocw.cloudfront.net/9983f29d-b710-423a-8956-7d873521fba3)

エリックが操作する4体のリベレイターは、装備している戦鎚で先に攻撃を実行する。各戦鎚はそれぞれ2回攻撃できる（戦鎚の**【攻撃回数】**は2であるため）。エリックは戦鎚に示されている**【ヒット成功値】**3+以上の**ヒットロール**結果を出す必要がある。リベレイターは、8個のヒットロールのうち5個のヒットを成功させる。

> [!quote]- EN
> Erik’s 4 Liberators armed with Warhammers attack first. They can each make 2 attacks (as a Warhammer has an **Attacks** characteristic of 2), and Erik needs to make **hit rolls** equal to or higher than their **Hit** characteristic of 3+. The Liberators score 5 successful hits out of 8 attacks.

![Erik's hit rolls on 8 dice. Erik rolled two fives, a four, two threes, two twos and a one. There are green check marks next to each of the rolls that are three or higher. The rest have red crosses next to them.](https://dhss9aar8ocw.cloudfront.net/803a6fba-20f8-4cad-bf02-d48661e40cab)

![A weapon table showing the weapon profile for the Liberators' Warhammers. The characteristics of a Warhammer are as follows: Attacks 2, Hit 3+, Wound 3+, Rend 1, Damage 1. It also has the Crit (Mortal) ability, shown at the end of the row. The Hit characteristic has a soft glow around it.](https://dhss9aar8ocw.cloudfront.net/f54b9f0e-4013-43e9-afb7-a58d4ae20caa)

次に、エリックは5個あるヒット1個につき、**ウーンズロール**を1回実行する。戦鎚は**【ウーンズ成功値】**3+を持つ。リベレイターは3個のウーンズロールを成功させる。

> [!quote]- EN
> Erik then makes a **wound roll** for each of the 5 hits. The Warhammers have a **Wound** characteristic of 3+. The Liberators successfully wound with 3 of their attacks.

![Erik's wound rolls on 5 dice. Erik rolled a six, two fours, a two and a one. There are green check marks next to each of the rolls that are three or higher. The rest have red crosses next to them.](https://dhss9aar8ocw.cloudfront.net/63bf497c-f83c-42ad-88af-7571128ad04a)

![Emma's save rolls on three dice. Emma rolled a five, a four and a one. The five has a green check mark; the other two have red crosses.](https://dhss9aar8ocw.cloudfront.net/75e89613-92b9-431b-9ba3-8726dbe9a61c)

3個あるウーンズロール1個につき、エマは**セーブロール**を1回実行する。エマのクロウロードは**【防御力】**4+を持つ。しかし戦鎚は**【貫通値】**1を持つため、エマの各ロールは1減算される。そのため彼女は、セーブロールで5以上の出目を出さなければならない。

クロウロードは3個のウーンズロールに対してセーブロールを1個成功させる。その結果、戦鎚は**【ダメージ量】**1を持つため、**ダメージプール**に2ポイントのダメージが加算される。

> [!quote]- EN
> Emma makes a **save roll** for each of the 3 successful wounds. Her Clawlord has a **Save** characteristic of 4+, but the Warhammers have a **Rend** characteristic of 1, so Emma must subtract 1 from each roll, meaning she now needs to roll a 5 or more.
>
> The Clawlord successfully saves 1 of the 3 attacks, resulting in 2 damage points being added to his **damage pool** (1 for each Warhammer, as they have a **Damage** characteristic of 1).

![This time, only the Clawlord has a green border around it to indicate that Emma is making save rolls for it. Beneath it, there is a red circle showing the number two. This indicates the number of damage points in the Clawlord's damage pool after the save rolls were made.](https://dhss9aar8ocw.cloudfront.net/5beee394-c102-42c6-b84b-90c7875dd3a2)

エリックは、強力な大鎚を装備しているユニット内の残りのリベレイターで、この手順を繰り返す。エリックは2個のヒットロールを成功させ、そのうちの1つは出目6による**クリティカルヒット**である。この結果は、大鎚の**『クリティカル（致命的）』**武器アビリティを発生させる。これによって、大鎚は2ポイントの致命的ダメージを与えることになり（17.2参照）、ダメージプールに直接2ポイントのダメージが加算される。

> [!quote]- EN
> Erik repeats this process with the remaining Liberator in the unit, who wields a mighty Grandhammer. He scores 2 hits, one of which is a **critical hit** of 6. Th is result triggers the Grandhammer’s **Crit (Mortal)** weapon ability, which inflicts 2 mortal damage (see 17.2), directly adding 2 damage points to the damage pool.

![The hit rolls and the wound roll that Erik made for the Grandhammer. The hit rolls show a six and a three; the wound roll shows a four. There is a little green star next to the six to indicate that this roll triggered the Grandhammer's Crit (Mortal) ability.](https://dhss9aar8ocw.cloudfront.net/02113bdf-45df-4a5e-b53b-00c42526da2a)

次に、エリックはもう1個の成功したヒットのウーンズロールをし、**ウーンズロール**を成功させた。

> [!quote]- EN
> Erik then makes a wound roll for the other hit, which **successfully wounds**.

![The image of the Liberators and the Clawlord is shown again. This time, the green border appears around the Liberator who is armed with the Grandhammer. The red circle showing the Clawlord's damage pool now shows the number four.](https://dhss9aar8ocw.cloudfront.net/34ab5251-2744-4c1a-a8dd-9083ddaff686)

![A weapon table showing the weapon profile for the Liberators' Grandhammer. The characteristics of the Grandhammer are as follows: Attacks 2, Hit 3+, Wound 2+, Rend 1, Damage 2. It also has the Crit (Mortal) ability, shown at the end of the row. The Damage characteristic has a soft glow around it.](https://dhss9aar8ocw.cloudfront.net/42dc0299-7330-4246-9522-fcf3a9b32cbe)

エマは成功した1個のウーンズロールに対して、**セーブロール**を1回実行する。大鎚の**【貫通値】**は1であるため、再びエマの**セーブロール**は1減算される。残念ながら、エマのセーブロールは失敗に終わる。その結果、大鎚は**【ダメージ量】**2を持つため、さらに**ダメージプール**に2ポイントのダメージが加算される。

リベレイターの攻撃は**解決**されたので、エマはダメージ手順に進む必要がある。

> [!quote]- EN
> Emma makes a **save roll** for the successful wound, and again must subtract 1 from the roll due to the Grandhammer’s **Rend** characteristic of 1. Unfortunately, her **save roll** is unsuccessful, resulting in another 2 **damage points** being added to the **damage** pool, as the Grandhammer has a Damage characteristic of 2.
>
> The Liberators’ attacks are **resolved**, so Emma must move on to the damage sequence.

![Emma's save roll for the Grandhammer attack that did not automatically wound the Clawlord. The dice shows a three with a red cross, indicating that Emma did not roll high enough to save against the attack.](https://dhss9aar8ocw.cloudfront.net/aac26d84-a822-4874-9f45-a4ab23243dd0)

![The Clawlord now has six damage points in its damage pool, shown by the number in the red circle beneath it.](https://dhss9aar8ocw.cloudfront.net/d5f44137-2446-4ec1-8bad-7dd388744fb8)

クロウロードは重傷の危機にさらされている。ダメージプールには6ポイントのダメージがあり、クロウロードの**【体力】**は7しかないためだ！ 幸いなことに、クロウロードは**加護（6+）**を持っているため、ダメージを避ける最後のチャンスがある。エマはダメージプールにある6ポイントのダメージ1ポイントにつき、それぞれ**加護ロール**を1回実行する。加護ロールのうち2つは出目6であり、その結果ダメージプールから2ポイントのダメージが取り除かれる。

残りの4ポイントのダメージは、クロウロードに**割り振られる**。エマはクロウロードの傍らにダイスを置き、そのユニットに現在割り振られているダメージの数を記録する。

クロウロードは現在**損傷状態**にある。エマにとっては運の良いことに、これでエマはクロウロードの『窮鼠猫を噛む』アビリティを用いて、卑劣な解放者どもに復讐することができる……

> [!quote]- EN
> The Clawlord is in grave peril, with 6 damage points in the damage pool (and only 7 **Health**!). Fortunately, he has **WARD (6+)**, which gives him one last chance to avoid the damage. Emma makes a **ward roll** for each of the 6 damage points in the damage pool, and 2 of those rolls are sixes, meaning 2 damage points are removed from the damage pool.
>
> The remaining 4 damage points are **allocated** to the Clawlord. Emma places a dice next to the Clawlord to keep track of the number of damage points that are currently allocated to that unit.
>
> The Clawlord is now **damaged** – luckily for Emma, this allows her Clawlord to use his ‘Cornered Rat’ ability to exact revenge on the dastardly Liberators…

![Emma's ward rolls for her Clawlord. From left to right, the dice show a one, a three, a six, a four, a five, and a six. The two sixes have green check marks; the others have red crosses.](https://dhss9aar8ocw.cloudfront.net/cf31f2ac-6c9c-47d9-8302-4fb069316d80)

![A red dice has been placed next to the Clawlord. This indicates the number of damage points allocated to the Clawlord after all the Liberators' attacks have been resolved.](https://dhss9aar8ocw.cloudfront.net/134ed873-5220-4875-bbfe-41a96de583c7)

### スペシャルルール 19.0 - 30.0(Special Rules 19.0 - 30.0)

#### 19.0 先手効果と後手効果(STRIKE-FIRST and STRIKE-LAST)

**『近接攻撃』**以外の任意の近接フェイズアビリティが使用された後、近接戦闘中である**『先手効果』**を持つユニットが1個以上いる場合、それらのユニットが**『近接攻撃』**アビリティを使用するために選択されるまで、他のユニットを選択して**『近接攻撃』**アビリティを使用することはできない。すべての**『先手効果』**を持つユニットが近接攻撃をした後、手番プレイヤーは近接攻撃を実行する次のユニットを選択する。

**近接戦闘中**である**『後手効果』**を持つユニットが1個以上いる場合、**『後手効果』**を持っておらず、かつ**『近接攻撃』**アビリティをまだ使用していない**近接戦闘中**のユニットが1個以上いるならば、『後手効果』を持つユニットを選択して**『近接攻撃』**アビリティを使用することはできない。

ユニットが**『先手効果』**と**『後手効果』**の両方を有する場合、どちらの効果も持っていないものとして扱う。

> [!quote]- EN
> If there are any **STRIKE-FIRST** units **in combat** after any non-**FIGHT** Combat Phase abilities have been used, other units cannot be picked to use a **FIGHT** ability until those units have been picked to use a **FIGHT** ability. After all those **STRIKE-FIRST** units have fought, the active player picks the next unit to fight.
>
> If there are any **STRIKE-LAST** units **in combat**, they cannot be picked to use a **FIGHT** ability if there are any units **in combat** that do not have **STRIKE-LAST** and have not yet used a **FIGHT** ability.
>
> If a unit has **STRIKE-FIRST** and **STRIKE-LAST**, treat it as if it had neither.

> フェイズ開始時に**『先手効果』**を持つユニットが近接戦闘中ではないことがあるかもしれない。しかし『接敵移動』などの移動によって、そのようなユニットがフェイズの後半で「近接戦闘に突入」する場合がある。そのような場合、フェイズ開始時に近接戦闘中ではなかったため、そのユニットは**『先手効果』**の効果を得ることはない。
>
> 別ユニットの近接攻撃の直後に**『近接攻撃』**アビリティを使用可能にするようなアビリティは、**『先手効果』**または**『後手効果』**のルール制限を無効にすることはないため、**『先手効果』**を持つユニットの直後に**『後手効果』**を持つユニットを選択して近接攻撃をすることはできない。

> [!quote]- EN
> There may be situations when a unit that has **STRIKE-FIRST** is not in combat at the start of the phase, but because of moves such as pile-in moves, it is ‘pulled into combat’ later in the phase. In such cases, **STRIKE-FIRST** has no effect on that unit because it was not in combat at the start of the phase.
>
> Abilities that allow a unit to use a **FIGHT** ability immediately after another unit do not override the **STRIKE-FIRST** or **STRIKE-LAST** constraints, so you could not pick a unit with **STRIKE-LAST** to fight immediately after a unit with **STRIKE-FIRST**.

#### 20.0 武器アビリティ(Weapon Abilities)

武器の中には、以下のパッシブ・**武器アビリティ**を1つ以上有するものがある。武器にクリティカルヒットが出た際に適用される武器アビリティが2つ以上ある場合、攻撃手順が開始される前に、攻撃側の兵を操作している司令官は、それらのアビリティのうち1つを選んで使用しなければならない。

> [!quote]- EN
> Some weapons have one or more of the passive **weapon abilities** below. If a weapon has multiple weapon abilities that apply on a critical hit, before the attack sequence starts, the commander of the attacking model must pick 1 of those abilities to use.

**共通武器アビリティ(Universal Weapon Abilities)**

- **対～（+1貫通値）：**対象が「**対～**」のキーワードを持つか、「**対～**」の後の条件を満たす場合、この武器の**【貫通値】**は+1の修正を受ける。このアビリティの効果と、同種のアビリティの効果は累積する。たとえば、武器が**対突撃（+1貫通値）**と**対英雄（+1貫通値）**の両方を有する場合、現在のターン中に**突撃**を実行している**英雄**を対象とする攻撃は、武器の**【貫通値】**に+2の修正を受ける。
- **突撃（+1ダメージ量）：**攻撃側ユニットがこのターン中に**突撃**を実行している場合、この武器の**【ダメージ量】**は+1の修正を受ける。
- **随行者：**特に明記されていない限り、この武器はヒットロール、ウーンズロール、武器能力値に修正を加える味方アビリティの効果を受けない。ただし、マイナス修正は適用される（たとえば『援護射撃』）。
- **クリティカル（2ヒット）：**この武器による攻撃が**クリティカルヒット**した場合、その攻撃は攻撃対象であるユニットに1回ではなく2回ヒットしたものとして扱われる。それぞれのヒットに対して**ウーンズロール**を1回実行する。
- **クリティカル（自動ウーンズ）：**この武器による攻撃が**クリティカルヒット**した場合、そのウーンズロールは自動的に成功する。この場合も、通常通りに**セーブロール**をする。
- **クリティカル（致命的）：**この武器による攻撃が**クリティカルヒット**した場合、その攻撃はその武器能力値に示される**【ダメージ量】**に等しい数の**致命的ダメージ**を攻撃対象であるユニットに与え、その攻撃の攻撃手順は終了する。
- **近接射撃：**この武器は、攻撃側ユニットが近接戦闘中であっても、レンジアタックをするために使用できる。

> [!quote]- EN
> - **Anti-X (+1 Rend):** Add 1 to this weapon’s **Rend** characteristic if the target has the keyword after ‘**Anti**-’ or fulfils the condition after ‘**Anti-’**. Multiples of this ability are cumulative. For example, if a weapon has both **Anti-charge (+1 Rend)** and **Anti-HERO (+1 Rend)**, then add 2 to the **Rend** characteristic of the weapon for attacks that target a **HERO** that **charged** in the same turn.
> - **Charge (+1 Damage):** Add 1 to this weapon’s **Damage** characteristic if the attacking unit **charged** this turn.
> - **Companion:** Unless otherwise specified, attacks made by this weapon are not affected by friendly abilities that modify hit rolls, wound rolls or weapon characteristics, except for those that apply negative modifiers (e.g. ‘Covering Fire’).
> - **Crit (2 Hits):** If an attack made with this weapon scores a **critical hit**, that attack scores 2 hits on the target unit instead of 1. Make a **wound roll** for each hit.
> - **Crit (Auto-wound)**: If an attack made with this weapon scores a **critical hit**, that attack automatically wounds the target. Make a **save roll** as normal.
> - **Crit (Mortal):** If an attack made with this weapon scores a **critical hit**, that attack inflicts **mortal damage** on the target unit equal to the **Damage** characteristic of that weapon and the attack sequence ends.
> - **Shoot in Combat:** This weapon can be used to make shooting attacks even if the attacking unit is in combat.

> 武器アビリティ**『随行者』**は、乗騎のような存在に対して、ユニットの能力を向上させる効果のほとんどを受けられないように制限している。

> [!quote]- EN
> The **Companion** weapon ability restricts things like mounts from benefiting from most effects that augment a unit’s capabilities.

#### 21.0 回復(Healing)

アビリティの中には、ユニットを**回復**するものがある。ユニットを回復するには、**「回復」**の後に記載されている括弧内の数値と等しい数のダメージをユニットから取り除く（たとえば**回復（2）**）。

> [!quote]- EN
> Some abilities allow you to **heal** a unit. To heal a unit, remove a number of damage points from the unit equal to the number in brackets after ‘**Heal**’, e.g. **Heal (2)**.

#### 22.0 兵の復帰と追加(Returning and Adding Models)

アビリティの中には、撃破された兵をユニットに**復帰**させたり、新たな兵をユニットに**追加**させたりすることを可能にするものがある。いずれの場合も、そのような兵は1体ずつ、このフェイズ中に復帰あるいは追加されていない、そのユニット内に属する兵と隊形（15.1参照）を保つようにして配置される。そのユニットが7体以上（配置される兵も含む）の兵で構成されているならば、このフェイズ中に復帰あるいは追加されていない、そのユニット内に属する兵の少なくとも2体以上と隊形を保つようにして配置される。新たに追加される兵は、追加される先のユニットがすでに敵ユニットと近接戦闘中である場合にだけ、敵ユニットと近接戦闘中の状態で配置できる。

> [!quote]- EN
> Some abilities allow you to **return** slain models to a unit or **add** new models to a unit. In either case, set up those models, one at a time within coherency range (see 15.1) of the model(s) in that unit that were not returned or added this phase. If that unit has 7 or more models (including the model being set up), it must be set up within coherency range of at least 2 other models in that unit that were not returned or added this phase. The new models can only be set up in combat with an enemy unit if their unit is already in combat with that enemy unit.

> - 復帰する兵は、そのアビリティにおける手順の中で復帰していない、復帰先のユニットに属している兵と**隊形**を保つように配置されなければならない。
> - 復帰する兵は、復帰先のユニットがすでに**近接戦闘中**である場合にだけ、敵ユニットと近接戦闘中の状態で配置できる。

> [!quote]- EN
> - Returned models must be set up in **coherency** with the models in their unit that were not returned as part of that ability.
> - Returned models can only be set up **in combat** with an enemy unit if their unit is already in combat with it.

#### 23.0 トークン(Tokens)

ルール上、トークンは兵とはみなされていない。また視認状態、隊形、アビリティの目的のために無視したり、邪魔にならないようにトークンを移動してもよい。アビリティの対象としてトークンを選択することはできない。トークンの目的は、トークンが置かれたユニットの~~永続的な効果~~==継続効果==を示すことである。トークンを有するユニットが移動を完了したり、配置されるたびに、そのトークンをユニットの傍らに置く。

> [!quote]- EN
> Tokens are not considered to be models for rules purposes and can be ignored or moved out of the way for purposes of visibility, coherency or abilities. They cannot be picked as the target of abilities. Their purpose is to indicate persisting effects on units they are placed next to. Each time a unit with a token finishes a move or is set up, place the token next to the unit.

![This Gryph-crow is a token.](https://dhss9aar8ocw.cloudfront.net/b0ef4f24-7219-4753-b931-590bd1668fab)

*このグリフクロウはトークンである。*

> [!quote]- EN
> This Gryph-crow is a token.

#### 24.0 ユニットの配置(Setting up Units)

アビリティの中には、戦場にユニットを配置できるようにするものがある。戦場にユニットを配置するとき、そのユニットに属するすべての兵を配置しなければならない。それが不可能な場合は、そのアビリティを使用することはできない。初期配置フェイズ以外のフェイズ中に戦場に配置されたユニットは、その配置された同一のターン中の移動フェイズ中に**『移動』**アビリティを使用することはできない。

> [!quote]- EN
> Some abilities allow you to set up a unit on the battlefield. When doing so, you must set up all models in that unit. If this is impossible, you cannot use that ability. A unit set up on the battlefield in a phase other than the deployment phase cannot use **MOVE** abilities in the movement phase of the same turn.

##### 24.1 予備戦力ユニット(Reserve Units)

アビリティの中には、**予備戦力**にユニットを配置できるようにするものがある。予備戦力のユニットは戦場の上に配置されるのではなく、戦場の傍らに配置される。第4バトルラウンド開始時、**『初期配置』**アビリティによって予備戦力に配置され~~たユニットや~~==、まだ==予備戦力に残っているユニットはすべて全滅する。

> [!quote]- EN
> Some abilities allow you to set up units **in reserve**. These units are placed to one side instead of being set up on the battlefield. At the start of the fourth battle round, units that were set up in reserve using a **DEPLOY** ability and that are still in reserve are destroyed.

##### 24.2 代替ユニット(Replacement Units)

アビリティの中には、**代替ユニット**の配置を可能にするものがある。代替ユニットを配置するとき、アビリティに特に明記されていない限り、代替ユニットは元のユニットと同じウォースクロール種別、武器オプション、兵数を持っていなければならない。これらの多くのアビリティは、代替ユニットの兵数の割合を指定している（たとえば、元のユニットの半数となる兵数）。このような場合は、元のユニットのどの兵が配置されるのかを選択してもよい。

それ以外の場合、代替ユニットは新しいユニットとして扱われる。元のユニットがバトル中に獲得したキーワードやアビリティ、そのユニットに適用されていた~~永続的な効果~~==継続効果==は、代替ユニットには適用されない。各ユニットは、それぞれ1度だけ代替ユニットに置き換えることができる。なお代替ユニットに置き換えられたユニットを、再び代替ユニットに置き換えることはできない。

元のユニットが増強されており、代替ユニットが元のユニットの半分より多い兵数で構成されている場合、その代替ユニットは増強ユニットとみなされる。

> [!quote]- EN
> Some abilities allow you to set up a **replacement unit**. When setting up that unit, it should have the same warscroll type, weapon options and number of models as the original unit, unless otherwise specified in the ability. Many of these abilities specify the proportion of models in the replacement unit (e.g. half the number of models from the original unit). In these cases, you can pick which models from the original unit are set up.
>
> The replacement unit is otherwise treated as a new unit; any keywords or abilities the original unit gained during the battle, and any persisting effects that applied to it, do not apply to the replacement unit. Each unit can only be replaced once, and you cannot replace replacement units.
>
> If the original unit was reinforced and the replacement unit has more than half the number of models from the original unit, the replacement unit is considered to be reinforced.

> 代替ユニットは完全に新しいユニットとして扱われるため、たとえば代替される前のユニットが、そのウォースクロールに記されている**「バトル中1回限り」**のアビリティをバトル中の初期に使用していたとしても、新しい代替ユニットはそのアビリティを再び使用できる。

> [!quote]- EN
> Because a replacement unit is treated as a completely new unit, it could, for instance, use a **Once Per Battle** ability on its warscroll even if the unit it replaced used that ability earlier in the battle.

#### 25.0 護られし英雄(Guarded Heroes)

**大型獣**または**戦闘兵器**ではないすべての**英雄**は、『護られし英雄』パッシブアビリティを有する：

> [!quote]- EN
> All **HEROES** that are not **MONSTERS** or **WAR MACHINES** have the ‘Guarded Hero’ passive ability:

> **護られし英雄(Guarded Hero)**（パッシブ）
>
> *率いる戦士たちの密集陣形によって、指揮官は危機から守られている。*
>
> - **効果:** この**英雄**が、**英雄ではない**味方ユニットの近接範囲内に一部でも入っている場合：
>
>   - その**英雄**を攻撃対象とする**レンジアタック**は、**ヒットロール**に-1の修正を受ける。
>   - その**英雄**が**歩兵**である場合、その英雄から12mvより遠く離れている兵は、その英雄を**レンジアタック**の攻撃対象として選択することはできない。

> [!quote]- EN
> **Guarded Hero**（Passive）
>
> *The leader is shielded by their warriors, who close ranks around them to protect them from harm.*
>
> - **Effect:** If this **HERO** is within the combat range of a friendly unit that is **not** a **HERO**:
>
>   - Subtract 1 from **hit rolls** for **shooting attacks** that target this **HERO**.
>   - If this **HERO** is **INFANTRY**, they cannot be picked as the target of **shooting attacks** made by models more than 12" from them.

> **大型獣**と**戦闘兵器**は『護られし英雄』アビリティのボーナスを受けない。なぜならこれらのユニットは、たとえ同胞に囲まれていたとしても、非常に目立つターゲットだからだ！

> [!quote]- EN
> Understandably, **MONSTERS** and **WAR MACHINES** don’t benefit from the ‘Guarded Hero’ ability. These units are very conspicuous targets even if they are surrounded by their fellows!

#### 26.0 ランダム能力値(Random Characteristics)

いくつかのウォースクロールは、固定値の代わりに**ランダム能力値ロール**を示している。そのような場合、アビリティに~~必要とされる能力値~~==その能力値が必要とされるたびに、そ==の値は、当該ユニットの司令官によって生成される。

ランダム武器能力値の場合、**『アタック』**アビリティを宣言するたびに、その攻撃側ユニット内に属する各兵のためにランダム**【攻撃回数】**を生成する。また、その武器でダメージを与えるたびに**ランダム【ダメージ量】**を生成する（各攻撃に対して個別にロールする）。

> [!quote]- EN
> Some warscrolls show a **random characteristic roll** instead of a fixed value. When this is the case, the value of the characteristic is generated by the commander of the unit in question each time an ability requires that characteristic.
>
> In the case of random weapon characteristics, generate a **random Attacks** characteristic for each model in the attacking unit each time you declare an **ATTACK** ability, and generate a **random Damage** characteristic each time you inflict damage with that weapon (roll once for each attack).

> - **ランダム能力値**を使用する場合は、アビリティに必要になるたびに生成する。
> - **ランダム【ダメージ量】**を使用する場合は、攻撃ごとに生成する。

> [!quote]- EN
> - When using a **random characteristic**, generate it each time it is needed for an ability.
> - When using **random Damage**, generate it for each attack made.

#### 27.0 修正の順序(Modifier Order)

いくつかのアビリティの効果は、能力値またはロールを修正する。特に明記されていない限り、能力値またはロールは1より小さくなるような値に変更することはできない。例外は【貫通値】であり、【貫通値】の最小修正値は0である（「-」）。

能力値が**ランダム能力値ロール**（上記参照）を使用する場合は、能力値が生成された**後**に、能力値への修正を適用する。

能力値またはロールが半分にされたり、整数以外の値に変更される場合は、最も近い整数にまで**端数切り捨て**を実施する。

次の順序で能力値の修正を適用する：

**1.** 能力値を固定値に**設定**する修正。

**2.** 能力値に対して**掛け算**または**割り算**をする修正。

**3.** 能力値に対して**加算**または**減算**をする修正。

同じ種別の修正が2つ以上ある場合（たとえば、能力値を設定する場合）は、効果の順序で適用される（30.0参照）。

特定のアビリティ（『過剰なる堕落』など）の効果により、自軍のロール結果を特定の数値に置き換えできる場合がある。そのような効果を使用する場合、自軍は実際にダイスをロールする前に置き換えなければならない。

> [!quote]- EN
> The effects of some abilities modify a characteristic or roll. Unless stated otherwise, a characteristic or roll cannot be modified to less than 1. The exception to this is Rend, which can be modified to a minimum of 0 (‘-’).
>
> If a characteristic uses a **random characteristic roll** (see 26.0 Random Characteristics), apply characteristic modifiers **after** that characteristic has been generated.
>
> If a characteristic or roll is halved or would be modified to a value that is not a whole number, **round it down** to the nearest whole number.
>
> Apply characteristic modifiers in the following order:
>
> **1.** Modifiers that **set** a characteristic to a fixed value.
>
> **2.** Modifiers that **multiply** or **divide** a characteristic.
>
> **3.** Modifiers that **add to** or **subtract from** a characteristic. If there are multiple modifiers of the same type (e.g. that set a characteristic), apply them in the Order of Effects (see 30.0).
>
> The effects of some abilities (e.g. ‘An Excess of Depravity’) allow you to replace a roll with a fixed value. When doing so, you must replace the roll before rolling the dice for it.

#### 28.0 上級アビリティのルール(Advanced Ability Rules)

- 特に明記されていない限り、アビリティを使用するユニットまたはアビリティの一部として選択されるユニットは、戦場に配置されていなければならない。
- 効果によってユニットが何かを**できる、してもよい**と記している場合、そのユニットを操作している司令官は、効果に記されている内容を解決するかどうかを選ぶことができる。
- 効果が何かを**しなければならない、する必要がある**と記している場合、司令官には選択の余地がなく、効果に記されている内容を解決する必要がある。これが不可能な場合、効果は適用されないが、そのアビリティは使用されたものとして扱われる。
- アビリティの文中（大部分の場合、ウォースクロール）に「このユニット」が記されている場合、それはアビリティを使用しているユニットを指している。
- アビリティが2個以上のユニットに効果を付与する場合、そのアビリティを使用したプレイヤーは、どの順序でユニットがそのアビリティの効果を受けるのかを選択できる。
- 効果を解決するとき、効果を受ける複数のユニットに対してダイスを振らなければならない場合、ダイスを振って1個のユニットに対する効果を解決した後、次のユニットの効果を解決する。
- ==ア==ビリティが複数のユニットを選ぶように指示している場合、特に明記されていない限り、選択する各ユニットはすべて異なるユニットでなければならない。

> [!quote]- EN
> - Unless stated otherwise, units using or picked as part of an ability must be on the battlefield.
> - If an effect states that a unit **can** do something, its commander can choose whether to resolve that part of the effect or not.
> - If an effect states that a unit **must** do something, its commander has no choice and must resolve that part of the effect. If this is impossible, no part of the effect is applied but the ability is still considered to have been used.
> - When ‘this unit’ appears in ability text (most often on warscrolls), it means the unit that is using the ability.
> - If an ability affects more than one unit, the player who used the ability can choose the order in which units are affected by it.
> - When resolving an effect, if you need to roll a dice for multiple affected units, roll and resolve the effect for one unit before moving on to the next.
> - If an ability instructs you to pick more than 1 unit, each unit you pick must be a different unit unless stated otherwise.

##### 28.1 継続効果(Persisting Effects)

アビリティの中には、すぐに解決されない効果を有するものもある（たとえば、「そのターン中、このユニットのセーブロールは+1の修正を受ける」または「そのターン中、このユニットは**加護（5+）**を持つ」）。これらの効果は、指定されている時間の間、パッシブアビリティ（5.4参照）を有するかのように扱われる。

> [!quote]- EN
> Some abilities have effects that aren’t immediately resolved (e.g. ‘add 1 to save rolls for this unit for the rest of the turn’ or ‘this unit has **WARD (5+)** for the rest of the turn’). These effects count as the effects of passive abilities (see 5.4) for their duration.

##### 28.2「1回限り」「につき1回」のタイミング('Once per' Timings)

アビリティの中には、タイミング欄に**各フェイズにつき1回**、**各ターンにつき1回**、**バトル中1回限り**と記しているものがある。アビリティがユニットによって使用される場合、そのアビリティを使用できる各ユニットは、そのフェイズ中、ターン中、バトル中にそのアビリティを最大1回使用できる。アビリティがプレイヤーによって使用される場合、そのプレイヤーは指定されたタイミングの間に、そのアビリティを最大1回使用できる。

ユニットによって使用されるアビリティの中には、**各フェイズにつき1回（アーミ~~－~~==ー==）**、**各ターンにつき1回（アーミー）**、**バトル中1回限り（アーミー）**と記しているものがある。これらのアビリティは、そのアビリティを使用できるアーミー内のユニット数に関係なく、そのフェイズ中やターン中、バトル中に最大1回使用できるものとする。

> [!quote]- EN
> The timing part of some abilities says **Once Per Phase, Once Per Turn** or **Once Per Battle**. If the ability is used by a unit, it can be used a maximum of one time in that phase, turn or battle by each unit that can use the ability. If the ability is used by a player, it can be used a maximum of one time in that timing window by that player.
>
> Some abilities that are used by units say **Once Per Phase (Army),** **Once Per Turn (Army)** or **Once Per Battle (Army)**. These abilities can be used a maximum of one time in that phase, turn or battle regardless of the number of units in the army that can use the ability.

##### アビリティを使用しているのは誰か？(Who is Using the Ability?)

アビリティの大部分はウォースクロールに記載されているが、他の多くの箇所にも記されている。その最~~もの~~==たる==例は、共通コアアビリティである（14.0参照）。

ウォースクロール上に記載されているアビリティは、そのウォースクロールが示しているユニットによって常に使用されるが、ウォースクロールに記載されていないアビリティの中には、アビリティを使用するユニットを選択するように明示しているものがある。どちらの場合も、どのユニットがアビリティを使用するのかが明確にわかる。

ウォースクロールには記載されていないアビリティもあり、最も一般的なのは『強化』（4.1アーミー編成参照）であるが、それらは自軍側アーミー内の特定のユニットに付与される。このような場合、『強化』を付与されたユニットがそのアビリティを使用することになる。

ウォースクロールに記載されておらず、アビリティを使用するユニットを選択するように指示していないアビリティは、プレイヤーによって使用される。最後に本セクションのルールとして、ルールがアビリティを使用するプレイヤーに言及している場合、これはそのプレイヤーが操作しているアーミー内のユニットによって使用されるアビリティも含まれる。

> [!quote]- EN
> Most abilities are found on warscrolls, but many appear elsewhere – the best examples being the Universal Core Abilities (see 14.0).
>
> While abilities on warscrolls are always used by the unit whose warscroll it is, some abilities that do not appear on warscrolls will tell you explicitly to pick a unit to use the ability. In both cases, it should be clear which unit is using the ability.
>
> Some abilities that do not appear on warscrolls, most commonly enhancements (see Army Composition, 4.1), are given to certain units in your army. In such cases, the unit to which the enhancement was given is the one using the ability.
>
> Abilities that neither appear on a warscroll nor tell you to pick a unit to use the ability are used by you, the player. Finally, for the purposes of the rules in this section, when a rule refers to a player using an ability, this includes abilities used by units in that player’s army.

#### 29.0 両立しないルール(Contradictory Rules)

2つ以上のルールが両立せず、一方のルールが何かが何かをすることは**できない**と記している場合、それはもう一方のルールが最初のルールを明確に無効にできると示していない限り、それは何かが何かをすることが**できる**、または**しなければならない**と記しているルールよりも優先される。たとえば『通常移動』アビリティでは、その移動中に近接戦闘に突入するような移動を実行できないと指定しているが、『飛行』アビリティでは、その移動中に敵兵の近接範囲を無視するようにと指定している。

上記を除いて、最も直前に使用したアビリティの効果が優先される。

> [!quote]- EN
> If two or more rules contradict, if one of those rules states that something **cannot** do something, this takes precedence over rules that state it **can** or **must** do that thing, unless the second rule specifically overrides the restriction of the first. For example, while the ‘Normal Move’ ability states you cannot move into combat during that move, the ‘Fly’ ability specifies to ignore the combat ranges of enemy models during a move.
>
> Excepting the above, the effect of the most recently used ability takes precedence.

#### 30.0 効果の順序(Order of Effects)

パッシブアビリティの効果は、他のアビリティやルールの効果よりも直前に適用されているものとして扱われる。手番プレイヤーが持つパッシブアビリティの効果は、対戦相手が持つパッシブアビリティの効果よりも直前に適用されているものとして扱われる。また、その対戦相手のパッシブアビリティは、中立的なパッシブアビリティ（たとえば、どちらのプレイヤーにも属していない特殊地形のパッシブアビリティ）の効果よりも直前に適用されているものとして扱われる。手番プレイヤーは、中立的なパッシブアビリティが適用される順序を選択する。

一部のアビリティでは、効果が遅れて発揮するものがある（たとえば、「味方ユニットが**『近接攻撃』**アビリティを使用する際、そのアビリティが解決された直後に、~~こ~~==そ==のユニットを**回復（D3）**する。」）。これらのような効果が同じタイミングで2個以上解決される場合は、まず手番プレイヤーが使用したアビリティの遅れて発揮する効果を任意の順番で解決し、その後に対戦相手も同じように効果を解決する。

> [!quote]- EN
> The effects of passive abilities are considered to be applied more recently than the effects of other abilities and rules. The effects of the active player’s passive abilities are considered to be applied more recently than the effects of their opponent’s passive abilities, whose passive abilities are considered to be applied more recently than the effects of neutral passive abilities (e.g. passive abilities on a terrain feature that is in neither player’s army). The active player chooses the order in which neutral passive effects are applied.
>
> Some abilities have a delayed effect (e.g. ‘each time a friendly unit uses a **FIGHT** ability, after that ability has been resolved, **Heal (D3)** that unit’). If more than one of these effects would be resolved at the same time, the active player resolves the delayed effects of their abilities first, in an order of their choosing, then their opponent does the same.

### ターン終了 31.0 - 33.0(End of Turn 31.0 - 33.0)

#### 31.0 ターン終了時の概要(End of Turn Overview)

各ターンの終了時に、以下の手順に従う：

**1.** 手番プレイヤーは、任意の順序で**「自軍側~~フェイズ~~==ターン==終了時」**または**「任意の~~フェイズ~~==ターン==終了時」**とタイミング欄に記載されているアビリティを使用できる。次に、対戦相手は任意の順序で**「敵軍側~~フェイズ~~==ターン==終了時」**または**「任意の~~フェイズ~~==ターン==終了時」**とタイミング欄に記載されているアビリティを使用できる。

**2.** 各作戦目標を**確保**しているプレイヤーを決定する（もしある場合）。

**3.** 手番プレイヤーは、バトル~~中~~==プラン==に記載されている通りに**勝利ポイント**を獲得する。

> [!quote]- EN
> At the end of each turn, follow these steps:
>
> **1.** The active player can use any abilities with the End of Your Turn or End of Any Turn timing, in the order of their choosing, then their opponent can use any abilities with the End of Enemy Turn or End of Any Turn timing, in the order of their choosing.
>
> **2.** Determine which player **controls** each objective (if any).
>
> **3.** The active player scores **victory points** as described in the battleplan.

#### 32.0 作戦目標(Objectives)

多くのバトルプランでは、**作戦目標マーカー**で表されている**作戦目標**を確保することで勝利ポイントを獲得できる。特に明記されていない限り、作戦目標マーカーは直径40mmの丸型マーカーである。兵は作戦目標マーカーを乗り越えたり、作戦目標マーカー上で移動を完了できる。作戦目標マーカーが陣地の間の境界に配置されている場合、それらはすべての陣地内に一部が入っているが、どの陣地内にも全体が入っているとはみなされない。作戦目標マーカーは視認状態を遮ることはない。

> [!quote]- EN
> Many battleplans award victory points for controlling **objectives**, which are represented by **objective markers**. Unless otherwise specified, objective markers are round and 40mm wide. Models can move over and end their moves on objective markers. If an objective marker is on the border between territories, it is within all those territories but wholly within none of them. Objective markers don’t block visibility.

- 作戦目標マーカーは、40mmの丸型マーカーである。
- 兵の近接範囲内に作戦目標マーカーが一部でも入っている場合、兵はその作戦目標を**争奪**している。
- 作戦目標を争奪している味方兵の**【確保力】**の合計が、その作戦目標を争奪している敵兵の【確保力】の合計を上回る場合、プレイヤーはその作戦目標を**確保**していることになる。
- 第1バトルラウンド開始時と各ターンの終了時に、自軍が作戦目標を確保しているかどうかを確認する。
- 自軍が確保している作戦目標は、対戦相手がその作戦目標を確保するまで、自軍側が確保しているものとしてみなされる。
- 特殊地形は作戦目標マーカーと同じ方法で確保されるが、その特殊地形を争奪する味方兵が1体もいなくなった時点で、その特殊地形は自軍によって確保されていないものとして扱われる。

> [!quote]- EN
> - An objective marker is a 40mm round marker.
> - A model **contests** an objective if the objective marker is within its combat range.
> - A player **gains control** of an objective if the sum of the **Control** characteristics of friendly models contesting that objective is higher than that of enemy models.
> - Check if you gain control of objectives at the start of the first battle round and at the end of each turn.
> - An objective remains in your control until your opponent gains control of it.
> - Terrain features are controlled in the same way as objective markers but do not remain in your control if no friendly models are contesting them.

> 兵を移動させているときに、作戦目標マーカーが誤って動いてしまうことがある。これは特に問題ではなく、作戦目標の確保を決定する際に、それらを適切な位置に戻すことを忘れないでおこう。

> [!quote]- EN
> Sometimes objective markers get accidentally nudged while you are moving models around. This is perfectly fine – just remember to put them back in their proper positions when determining objective control.

##### 32.1 作戦目標の争奪(Contesting Objectives)

特に明記されていない限り、兵の近接範囲内に作戦目標が一部でも入っている場合、その兵はその作戦目標を**争奪中**である。ユニット内に属するいずれかの兵が作戦目標を争奪している場合、そのユニットはその作戦目標を争奪中である。

作戦目標を確保するルール上（32.2参照）、各ユニットは1つの作戦目標を争奪しているものとしてのみカウントされる。作戦目標の確保を決定する前に、2個以上の作戦目標を争奪中である各ユニットにおいて、手番プレイヤーは自軍のユニットがどの作戦目標を争奪しているのかを最初に選ばなければならない。その後、対戦相手も同じように作戦目標を選択する。

> [!quote]- EN
> Unless otherwise specified, if an objective is within a model’s combat range, that model is **contesting** that objective. If any models in a unit are contesting an objective, that unit is contesting that objective.
>
> Each unit can only count as contesting a single objective for the purposes of determining objective control (see 32.2). Before determining objective control, for each of their units contesting two or more objectives, the active player must pick one of those objectives for it to contest. Then, their opponent does the same.

**デザイナーズ・ノート：作戦目標を確保するルール以外において、ユニットは2個以上の作戦目標を争奪することができる。**

> [!quote]- EN
> **Designer’s Note:** *For purposes other than determining objective control, a unit can contest more than one objective.*

##### 32.2 作戦目標の確保(Objective Control)

**初期配置フェイズ**において、すべての『初期配置フェイズ』アビリティが使用された後、==および==**各ターン終了時**に手番プレイヤーが選んだ順番で作戦目標ごとに次の手順を実行する：

1. 手番プレイヤーから、各プレイヤーは争奪している作戦目標に対して自軍の各ユニットの**確保スコア**を決定する。ユニットの確保スコアは、ユニット内の作戦目標を争奪している各兵の**【確保力】**を合計したものである。アビリティの中には、ユニットの確保スコアを修正するものもあるが、確保スコアを1より小さくなるような値に変更することはできない。
2. 各プレイヤーは、その作戦目標を争奪しているすべてのユニットの確保スコアを合計する。この合計は、該当する作戦目標に対する自軍の**アーミー確保スコア**である。
3. プレイヤーたちは、対象となっている作戦目標のアーミー確保スコアを比較する。アーミー確保スコアの高い方のプレイヤーが、該当する作戦目標を**確保**したことになる。あるプレイヤーが作戦目標を確保したら、対戦相手がその作戦目標を確保するまで、そのプレイヤーが該当の**作戦目標を確保し続けているもの**とみなされる。

> [!quote]- EN
> In the **deployment phase** after all Deployment Phase abilities have been used and at the **end of each turn**, follow this sequence for **each objective** in an order chosen by the active player:
>
> 1. Starting with the active player, each player determines the control score of each of their units that is contesting that objective. A unit’s **control score** is the combined **Control** characteristics of all the models in that unit that are contesting the objective. Some abilities modify a unit’s control score, but it cannot be reduced to less than 1.
> 2. Each player adds up the control scores of all of their units contesting that objective. This is their **army control score** for that objective.
> 3. The players compare their army control scores for that objective. If one player’s score is higher, that player **gains control** of that objective. Once a player gains control of an objective, it **remains under their control** until their opponent gains control of it.

##### 32.3 特殊地形の確保(Terrain Control)

バトルプランのいくつかでは、特殊地形の確保を必要とする。特殊地形は作戦目標と同じように争奪することができたり、確保したりすることができる。ただし、特殊地形は自軍側のユニットが争奪中でなければ、その確保していた状態は維持されない。作戦目標や特殊地形の確保の判定をするためのルール上、各ユニットは同じタイミングに作戦目標１個と特殊地形１個を争奪することができる。

**デザイナーズ・ノート：特殊地形の確保の判定をする以外のルール上では、ユニットは２個以上の特殊地形を争奪することができる。**

> [!quote]- EN
> Some battleplans require you to gain control of terrain features. Terrain features are contested and controlled in the same way as objectives, but terrain features **do not remain in your control** if your units are no longer contesting them. For the purposes of determining objective control and terrain feature control, each unit can contest 1 objective and 1 terrain feature at the same time.
>
> **Designer’s Note:** *For purposes other than determining terrain feature control, a unit can contest more than one terrain feature.*

#### 33.0 バトルラウンドの終了時(End of Battle Round)

各バトルラウンドの終了時に、手番プレイヤーは**『バトルラウンドの終了時』**アビリティを使用できる。その後、対戦相手も同様にアビリティを使用できる。各バトルプランは、指定された回数のバトルラウンドに基づいて展開される。バトルプランに指定された回数のバトルラウンド終了時に、バトルは終了する。その後、バトルプランに記載されているルールに従って勝者を決定する。

> [!quote]- EN
> At the end of each battle round, the active player can use any End of Battle Round abilities, then their opponent can do the same. Each battleplan will specify the number of battle rounds that should be fought. If you have completed the number of battle rounds specified in your battleplan, the battle has ended, and you should follow the rules included in that battleplan to determine the winner.

### 補遺、エラッタ、多く寄せられた質問(Addenda, Errata and FAQs)

#### 補遺(Addenda)

下記に記載されているルールのアップデートは、曖昧さや意図しない影響を回避したりするために文が追加されている。

> [!quote]- EN
> The following rules updates add text in order to clarify ambiguities and/or avoid unintended interactions.

##### 2.2 ダイス(Dice)

以下を加える：

“• 一部のルールでは、ダイスロールを**リロール**できるものがある。つまり、ダイスのロールを一部またはすべてをリロールすることができる。ダイスをリロールできるのは最大1回だけであり、ロールに対して修正（修正がある場合）が適用される前にリロールが実行される。”

> [!quote]- EN
> Add the following:
>
> ‘• Some rules allow you to **re-roll** a dice roll, which means you get to roll some or all of the dice again. You cannot re-roll a dice more than once, and re-rolls happen before modifiers to the roll (if any) are applied.’

##### 7.0 近接範囲(Combat Range)

以下を加える：

“敵ユニットが兵の近接範囲内に一部でも入っており、かつその兵から敵ユニットが視認できる場合、兵は敵ユニットと近接戦闘中であるものとしてみなされる。”

> [!quote]- EN
> Add the following:
>
> ‘A model is considered to be in combat with an enemy unit if that unit is within the model’s combat range and visible to it.’

##### 15.6 突撃移動(Charge Moves)

以下を追加する：

“ルールの中には、ユニットが突撃移動を完了したことを言及しているものがある。そのユニットが使用した『突撃移動』アビリティが解決され、そのアビリティの一環としてユニットが突撃を実行した場合、ユニットは突撃移動を完了したものとみなされる。~~’~~==”==

> [!quote]- EN
> Add the following:
>
> ‘Some rules reference a unit finishing or ending a charge move. This is considered to occur when a **CHARGE MOVE** ability that unit used resolves and the unit has charged as part of that ability.’

##### 18.3 撃破された兵(Slain models)

以下を加える：

“可能な限り少ない数の兵を取り除いて、単一のグループとして隊形を保つようにしなければならない。”

> [!quote]- EN
> Add the following:
>
> ‘You must remove the fewest models possible to make the unit a single coherent group.’

##### 24.2 代替ユニット(Replacement Units)

以下を加える：

“元のユニットが増強されており、代替ユニットが元のユニットの半分より多い兵数で構成されている場合、その代替ユニットは増強ユニットとみなされる。”

> [!quote]- EN
> Add the following:
>
> ‘If the original unit was reinforced and the replacement unit has more than half the number of models from the original unit, the replacement unit is considered to be reinforced.'

##### 27.0 修正の順序(Modifier Order)

以下を加える：

“特定のアビリティ（『過剰なる堕落』など）の効果により、自軍のロール結果を特定の数値に置き換えできる場合がある。そのような効果を使用する場合、自軍は実際にダイスをロールする前に置き換えなければならない。”

> [!quote]- EN
> Add the following:
>
> ‘The effects of some abilities (e.g. ‘An Excess of Depravity’) allow you to replace a roll with a fixed value. When doing so, you must replace the roll before rolling the dice for it.’

##### 30.0 効果の順序(Order of Effects)

以下を加える：

“一部のアビリティでは、効果が遅れて発揮するものがある（たとえば、「味方ユニットが『**近接攻撃**』アビリティを使用する際、そのアビリティが解決された直後に、このユニットを**回復（D3）**する。」）。これらのような効果が同じタイミングで2個以上解決される場合は、まず手番プレイヤーが使用したアビリティの遅れて発揮する効果を任意の順番で解決し、その後に対戦相手も同じように効果を解決する。”

> [!quote]- EN
> Add the following:
>
> ‘Some abilities have a delayed effect (e.g. ‘each time a friendly unit uses a **FIGHT** ability, after that ability has been resolved, **Heal (D3)** that unit’). If more than one of these effects would be resolved at the same time, the active player resolves the delayed effects of their abilities first, in an order of their choosing, then their opponent does the same.’

#### エラッタ(Errata)

下記に記載されているルールのアップデートは、曖昧さや意図しない影響を回避したりするために間違いが更新されている。

> [!quote]- EN
> The following rules updates correct errors in order to clarify ambiguities and/or avoid unintended interactions.

##### 5.2 アビリティの宣言(Using Abilities)

第2項目（リアクションの使用）を以下のように変更する：

“そのアビリティを宣言したプレイヤーから順に、各プレイヤーは交互に、適切な**リアクション**のタイミングを持つアビリティを宣言する。プレイヤーはリアクションの使用をパスしてもよいが、双方のプレイヤーが連続してリアクションの使用をパスした場合、そのアビリティに対してこれ以上リアクションを宣言することはできない。”

> [!quote]- EN
> Change point 2 (Use Reactions) to:
>
> ‘Starting with the player using the ability, the players alternate using any abilities with an appropriate **Reaction** timing. Players can choose to pass instead of using a reaction, but once both players consecutively pass, no further reactions to that ability can be used.’

##### 6.0 視認(Visibility)

以下を追加する：

“ルールやアビリティにおいて、選択対象がアビリティ使用側のユニット（またはユニット内の兵）から射程内に入っていることと、かつ視認状態であることを同時に要求している場合、そのような条件は、選択対象内の同一の兵に対して満たされていなければならない。例えば、兵1体は射程内であるが視認状態ではなく、他の兵1体は射程内ではないが視認状態であるようなユニットを、選択対象とすることはできない。”

> [!quote]- EN
> Add the following:
>
> ‘If a rule or ability requires a target to be both within a given range of and visible to the unit using that ability, or to a model in that unit, both conditions must be met by the same model in the target. You could not, for instance, target a unit where one model is within range but not visible and another model is not in range but is visible.’

##### 10.1 共通の初期配置フェイズアビリティ(Universal Deployment Phase Abilities)

『連隊の初期配置』の最終文を以下のように変更する：

選択された連隊内に属していない~~ユニット（戦場あるいは予備戦力に配置されている）を、その一連の『**初期配置**』アビリティの対象として選択することはできない~~==ユニットを、その一連の『初期配置』アビリティの一環として戦場あるいは予備戦力に配置することはできない==。

> [!quote]- EN
> Change the last sentence of ‘Deploy Regiment’ to:&#x20;
>
> ‘You cannot set up units that are not in that regiment on the battlefield or in reserve as part of any of those **DEPLOY** abilities.’

##### 14.4 近接フェイズ(Combat Phase)

『近接攻撃』アビリティの宣言手順において：“**接敵移動**（15.4参照）”を“**接敵移動**（15.3参照）”に変更する。

> [!quote]- EN
> In the declare step of the ‘Fight’ ability, change ‘**pile-in move** (see 15.4)’ to ‘**pile-in move** (see 15.3)’.

##### 15.5 張り出したミニチュア(Overhanging Models)

ミニチュアの中には、ベースから張り出しているものがある。このようなミニチュアを移動させるとき、その兵がある場所に配置可能かどうかを判定する際、張り出している部分は存在しないものとして扱う。その付近で他の兵が移動を完了する場合、可能なら張り出したミニチュアを回転させ、他の兵の移動完了を妨げないようにする。そのように張り出したミニチュアを回転させるならば、ベースは同じ位置に留まっていなければならない。円形のベースは任意に回転させてよく、楕円のベースは180°~~まで~~==だけ==回転させてよい。上記のようにできない場合は、兵が移動を完了するはずの場所を記録（同一サイズの空ベースを置くなど）し、兵自体は傍に置いておく。そして、物理的に配置が可能になり次第その兵を記録した場所に戻す。”

> [!quote]- EN
> Some models overhang their base. When moving models, overhanging parts should be treated as if they do not exist when determining where a model could be placed. Where possible, a model should be rotated to allow for another model to end a move in proximity to it. When rotating a model this way, the base must occupy the same position – a circular base may be rotated any amount, while an oval base may only be rotated 180°. Otherwise, mark down the location of where the model should end its move (such as with an empty base of the same size) and place the model to the side. Return the model to the table as soon as it is physically possible to do so.'

##### 19.0 先手効果と後手効果(STRIKE-FIRST and STRIKE-LAST)

第一文中の「そのフェイズ開始時」を「『**近接攻撃**』以外の任意の近接フェイズアビリティが使用された後」に変更する。

> [!quote]- EN
> In the first sentence, replace ‘at the start of the phase’ with ‘after any non-**FIGHT** Combat Phase abilities have been used’.

##### 20.0 武器アビリティ(Weapon Abilities)

**随行者**の武器アビリティを下記のように変更する：

“特に明記されていない限り、この武器はヒットロール、ウーンズロール、武器能力値に修正を加える味方アビリティの効果を受けない。ただし、マイナス修正は適用される（たとえば『援護射撃』）。”

> [!quote]- EN
> Change the **Companion** weapon ability to:
>
> ‘Unless otherwise specified, attacks made by this weapon are not affected by friendly abilities that modify hit rolls, wound rolls or weapon characteristics, except for those that apply negative modifiers (e.g. ‘Covering Fire’).'

##### 22.0 兵の復帰と追加(Returning and Adding Models)

変更元：

「いずれの場合も、そのような兵は1体ずつ、このターン中に復帰あるいは追加されていない、そのユニット内に属する兵と隊形（15.1参照）を保つようにして配置される。」

以下に変更する：

「いずれの場合も、そのような兵は1体ずつ、このフェイズ中に復帰あるいは追加されていない、そのユニット内に属する兵と隊形（15.1参照）を保つようにして配置される。そのユニットが7体以上（配置される兵も含む）の兵で構成されているならば、このフェイズ中に復帰あるいは追加されていない、そのユニット内に属する兵の少なくとも2体以上と隊形を保つようにして配置される。」

> [!quote]- EN
> Replace:
>
> ‘In either case, set up those models, one at a time, in coherency (see 15.1) with the model(s) in that unit that were not returned or added this phase.’
>
> with:
>
> ‘In either case, set up those models, one at a time within coherency range (see 15.1) of the model(s) in that unit that were not returned or added this phase. If that unit has 7 or more models (including the model being set up), it must be set up within coherency range of at least 2 other models in that unit that were not returned or added this phase.’

##### 25.0 護られし英雄(Guarded Hero)

“護られし英雄”の効果~~を~~==の==以下の部分を：

“この**英雄**が**歩兵**である場合、その英雄から12mvより遠く離れているユニットは、その英雄をレンジアタックの攻撃対象として選択することはできない。==”==

以下のように変更する：

“この**英雄**が**歩兵**である場合、その英雄から12mvより遠く離れている兵は、その英雄をレンジアタックの攻撃対象として選択することはできない。==”==

> [!quote]- EN
> In the effect of ‘Guarded Hero’, replace:
>
> ‘If this **HERO** is **INFANTRY**, they cannot be picked as the target of shooting attacks made by units more than 12" from them.’
>
> with:
>
> ‘If this **HERO** is **INFANTRY**, they cannot be picked as the target of shooting attacks made by models more than 12" from them.’

##### 32.1 作戦目標の争奪(Contesting Objectives)

第二段落を以下のように変更する：

“作戦目標を確保するルール上（32.2参照）、各ユニットは1つの作戦目標を争奪しているものとしてのみカウントされる。作戦目標の確保を決定する前に、2個以上の作戦目標を争奪中である各ユニットにおいて、手番プレイヤーは自軍のユニットがどの作戦目標を争奪しているのかを最初に選ばなければならない。その後、対戦相手も同じように作戦目標を選択する。

**デザイナーズ・ノート：作戦目標を確保するルール以外において、ユニットは2個以上の作戦目標を争奪することができる。**”

> [!quote]- EN
> Change the second paragraph to:
>
> ‘Each unit can only count as contesting a single objective for the purposes of determining objective control (see 32.2). Before determining objective control, for each of their units contesting two or more objectives, the active player must pick one of those objectives for it to contest. Then, their opponent does the same.
>
> **Designer’s Note:** *For purposes other than determining objective control, a unit can contest more than one objective*.’

##### 32.2 作戦目標の確保(Objective Control)

第一文を次のように変更する：

“**初期配置フェイズ**において、すべての『初期配置フェイズ』アビリティが使用された後、==および==**各ターン終了時**に手番プレイヤーが選んだ順番で作戦目標ごとに次の手順を実行する：”

> [!quote]- EN
> Change the first sentence to:
>
> ‘In the **deployment phase** after all Deployment Phase abilities have been used and at the **end of each turn**, follow this sequence for **each objective** in an order chosen by the active player:’

##### 32.3 特殊地形の確保(Terrain Control)

文章を以下のように変更する：

“バトルプランのいくつかでは、特殊地形の確保を必要とする。特殊地形は作戦目標と同じように争奪することができたり、確保したりすることができる。ただし、特殊地形は自軍側のユニットが争奪中でなければ、その確保していた状態は維持されない。作戦目標や特殊地形の確保の判定をするためのルール上、各ユニットは同じタイミングに作戦目標１個と特殊地形１個を争奪することができる。

**デザイナーズ・ノート：特殊地形の確保の判定をする以外のルール上では、ユニットは２個以上の特殊地形を争奪することができる。**”

> [!quote]- EN
> Change the text to:
>
> ‘Some battleplans require you to gain control of terrain features. Terrain features are contested and controlled in the same way as objectives, but terrain features **do not remain in your control** if your units are no longer contesting them. For the purposes of determining objective control and terrain feature control, each unit can contest 1 objective and 1 terrain feature at the same time.
>
> **Designer’s Note:** *For purposes other than determining terrain feature control, a unit can contest more than one terrain feature.*’

#### 多く寄せられた質問(Frequently Asked Questions)

この質問と回答のシリーズでは、ルール執筆チームがプレイヤーから寄せられた質問に答え、ルールがどのように使用されることを意図しているかを説明する。

> [!quote]- EN
> In this series of questions and answers, the rules-writing team respond to players’ queries and explain how the rules are intended to be used.

##### 2.2 ダイス(Dice)

*Q: アビリティによってXD6ロールからダイスを１個リロールできる場合（たとえば、虚ろの王刃団の『アウレリアス』アビリティ）、別のアビリティを使用してXD6のロールを全てリロールできるようにすることはできる？*

> [!quote]- EN
> *Q: If an ability allows me to re-roll one dice from an XD6 roll (e.g. the Blades of the Hollow King ‘Aurelias’ ability), could I then use a different ability to re-roll the entire XD6 roll?*

A: できない。

> [!quote]- EN
> A: No.

##### 4.0 ウォースクロール(Warscrolls)

*Q: 自軍が敵の【確保力】を参照するアビリティ（ウショーランの『檻の破片』など）を解決する際、対象が【確保力】を有していない（顕現など）場合、どうすればよい？*

> [!quote]- EN
> *Q: How should I resolve an ability that refers to an enemy’s Control characteristic (e.g. Ushoran’s ‘Shroudcage Fragment’) if the target does not have a Control characteristic (e.g. a manifestation)?*

A: そのような対象は、【確保力】0であるものとして扱う。

> [!quote]- EN
> A: The target is treated as having a Control characteristic of 0.

##### 5.0 アビリティ(Abilities)

*Q: 一部のアビリティ（たとえば『全力攻撃』）のタイミング欄は赤色で示されていますが、これらのアビリティは近接フェイズにのみ使用できるの？*

> [!quote]- EN
> *Q:* *Some abilities (e.g. ‘All-out Attack’) have a red timing bar. Can these abilities only be used in the combat phase?*

A: いいえ。タイミング欄に記されている文、またはリアクションやパッシブ・アビリティの場合は、そのアビリティの特定の表現によって、いつそのアビリティを使用できるかが正確にわかる。色は、単にプレイを助けるためのものである。フェイズが指定されていない場合、色はアビリティが使用される最も一般的なフェイズを示している。また、複数のフェイズで均等に使用される場合、タイミング欄は黒色になっている。

> [!quote]- EN
> A: No. The words in the timing bar or, in the case of reactions and passive abilities, the specific wording of the ability will let you know exactly when you can use it; the colour is just there as a play aid. If a phase is not specified, the colour indicates the most common phase it is used in or, if it is used in multiple phases equally, the timing bar is black.

*Q: 一部のアビリティのタイミング欄は緑色ですが、これにはどのような意味があるの？*

> [!quote]- EN
> *Q: Some abilities have a green timing bar. What does this mean?*

A: 緑色のタイミング欄は、防御系のアビリティを示しており、その多くは種々のフェイズで使用することができる。

> [!quote]- EN
> A: The green timing bar is used to indicate defensive abilities, many of which can be used in multiple phases.

*Q: 『燃え盛る魔炎波』のようなパッシブアビリティではないものは、任意で使用できるの？*

> [!quote]- EN
> *Q:* *Are non-passive abilities such as ‘Burning Wyrdflame’ optional to use?*

A: その通りだ。パッシブアビリティと、可能であれば使用しなければならないと記述しているアビリティの効果は適用する必要があるが、他のすべてのアビリティは任意で使用できる。

> [!quote]- EN
> A: Yes. You must apply the effects of passive abilities and abilities that state that they must be used if it is possible to do so, but all other abilities are optional to use.

##### 5.1 キーワード(Keywords)

*Q: 「既に全滅している**英雄**ではない味方**第一君主の兵団**・**ディーモン・歩兵**あるいは**騎兵**・ユニットを1個選択」することに関して（また、これと同様に複数のキーワードを含むルール上の文言に関して）、「**騎兵**・ユニット」の部分はただそれだけあれば良いということか（つまり、直前の他のキーワードを含まない）？それとも、「**英雄ではない味方第一君主の兵団・ディーモン・騎兵**・ユニット」ということか？*

> [!quote]- EN
> Q: *In ‘Pick a friendly non-**HERO LEGION OF THE FIRST PRINCE DAEMON INFANTRY** or **CAVALRY** unit that has been destroyed to be the target’ (and similar wordings with multiple keywords), does ‘**CAVALRY** unit’ mean just that (i.e. with no other keywords) or does it mean ‘ friendly non-**HERO LEGION OF THE FIRST PRINCE DAEMON CAVALRY UNIT**’?*

A: 「**英雄ではない味方第一君主の兵団・ディーモン・騎兵**・ユニット」ということだ。

> [!quote]- EN
> A: It means ‘friendly non-**HERO LEGION OF THE FIRST PRINCE DAEMON CAVALRY** unit’.

*Q: アビリティにおいて「non-」の後に複数のキーワードが続いている場合（non-Sk~~y~~ryre Moulder・ユニットを対象とする、スケイヴン・ブルードテラーの『爪の手も借りたい』アビリティなど）、それは続けて記載されているキーワードを全て持っていてはならない（この場合**Skryre**も**Moulder**もどちらも持っていてはならない）ということなのか、それともnon-なのは最初のキーワードだけで、2個目のキーワードは持っている必要がある（この場合**Skryreは持っていてはならないが、Moulderは持っている必要がある**）ということなのか？*

> [!quote]- EN
> Q: *Where an ability references multiple keywords but has ‘non-’ at the start of the sequence of keywords(for example, the Skaven Brood Terror’s Lend a Claw ability which targets ‘non-**SKRYRE MOULDER**’ units’), does this mean the target must not have any of the keywords listed (in this example, the target couldn’t have **SKRYRE** or **MOULDER** keywords), or does it mean the target cannot have the first keyword but must have the second (in this example, it cannot have **SKRYRE** but must have **MOULDER**)?*

A: 「non-」というのは、直後に続くキーワードにのみ掛かるものである。すなわち、挙げられた例で言えば**Skryre**のキーワードを持っていてはならないが、**Moulder**のキーワードは持っている必要がある。どちらも禁止する意図のある場合、ルール文は「non-**Skryre** non-**Moulder**」という表記になる。

\* こちらは英語語順によって生じる不明瞭の解決であり、日本語版においては「**スクリール**でない**モウルダー・ユニット**」「**スクリール**でなく**モウルダー**でもないユニット」という表記になっています。

> [!quote]- EN
> A: The ‘non-’ only relates to the keyword it is directly attached to. Therefore, in the example given, the target cannot have the **SKRYRE** keyword but must have the **MOULDER** keyword. If the intent were to exclude both keywords, then it would be expressed as ‘non-**SKRYRE** non-**MOULDER**'.

##### 5.2 アビリティの宣言(Using Abilities)

*Q: アビリティの効果を解決する際に、【防御力】3+あるいはそれよりも優れている場合と記載されていますが（たとえば、『足枷のぬかるみ』呪文）、「あるいはそれよりも優れている」とはどういう意味なのですか？*

> [!quote]- EN
> *Q:* *When resolving the effect of an ability that refers to a Save characteristic of 3+ or better (e.g. the ‘Cloying Quagmire’ spell), what does ‘or better’ mean?*

A: 【防御力】が3+よりも低い値、たとえば2+のことを指している。つまり、ダメージに対してより効果的に防御できる値のことである。

> [!quote]- EN
> A: It means any Save characteristic with a lower value than 3+, such as 2+, that better protects against incoming damage.

*Q: アビリティによって味方ユニットが『近接攻撃』アビリティを使用した直後に、ただちに別の味方ユニットを選択して『近接攻撃』アビリティを使用できるとき（たとえば、クリプトホーンター・コーティアーの『騎士の模範』）、その２番目のユニットは『近接攻撃』アビリティの宣言ステップの条件を満たしていなければならないの？*

A: はい、条件を満たしている必要がある。たとえば２番目のユニットが、『**近接攻撃』アビリティを**使用する場合、そのユニットは近接戦闘中あるいは現在のターン中に突撃をしていなければならない。

> [!quote]- EN
> *Q: If an ability allows another friendly unit to be picked to use a **FIGHT** ability immediately after a friendly unit has used a **FIGHT** ability (for example, the Crypt Haunter Courtier’s ‘Knightly Exemplar’ ability), does the second unit being activated have to meet the requirements of the Declare step of the **FIGHT** ability it is using?*
>
> A: Yes. So, for example, if the second unit being activated was using the ‘Fight’ ability, it would need to be in combat or have charged in the same turn.

*Q: アビリティが限定している複数の目標物が同条件に等しい場合（例えば、覚醒せし森林が『果てしない生長』を使用した際に２つの特殊地形が同等に近い場合）、どのようになるの？*

A: そのアビリティを使用したプレイヤーがどの対象が影響をうけるのかを選択する。

> [!quote]- EN
> *Q: If an ability references a qualifier that multiple objects are tied for (e.g. two terrain features are equally close to an Awakened Wyldwood that is using the ‘Ever Growing’ ability), what happens?*
>
> A: The player who used the ability chooses which object to affect.

##### 5.3 一度限りのルール(The Rules of One)

*Q: リアクションのアビリティは、一度限りのルールが適用されるの？たとえば、ユニットのウォースクロールにリアクションのアビリティが記されている場合、それは各フェイズにつき1回だけ使用できることなの？*

> [!quote]- EN
> *Q: Are Reaction abilities subject to the Rules of One? For example, if a unit has a Reaction ability on their warscroll, could they only use it once per phase?*

A: その通りだ。

> [!quote]- EN
> A: Yes.

##### 6.0 視認(Visibility)

*Q: 飛行を持たない歩兵・英雄（たとえば、サイナーリ・キャサラー）が光輝の神殿の「神殿の守護者」であり、かつその「神殿の守護者」が射線妨害を持つ特殊地形の１mv以内に一部でも入っている場合、その「神殿の守護者」を対象とする敵アビリティはその「神殿の守護者」を視認できるの？*

A: 視認できる。

> [!quote]- EN
> *Q: If a non-**FLY INFANTRY HERO** (e.g. a Scinari Cathallar) is a Shrine Guardian of a Shrine Luminor, and that Shrine Guardian is within 1" of an obscuring terrain feature, is the Shrine Guardian visible to enemy abilities that target the Shrine Guardian?*
>
> A: Yes.

##### 7.0 近接範囲(Combat Range)

*Q: 敵兵のベースと自身のベースが直接触れている兵が~~３~~==その敵兵からまっすぐ離れるように3==mv退却した場合、その兵は敵兵と近接戦闘中であるとみなされるの？*

A: いいえ、近接戦闘中であるとはみなされない。

> [!quote]- EN
> *Q. If a model in base-to-base contact with an enemy model retreats 3" directly away from the enemy model, is it still in combat with that enemy model?*
>
> A. No.

##### 9.1.1 作戦目標と特殊地形の配置(Setting up Objectives and Terrain Features)

*Q: バトルプランの説明で、戦場の四隅のいずれかに作戦目標を配置するように記されている場合、戦場に作戦目標の全体（40mm）が入るように配置すればいいの？それとも作戦目標の中央が戦場の角に来るように配置すればいいの？*

> [!quote]- EN
> *Q:* *If a battleplan instructs you to set up an objective on a corner of the battlefield, should you place the entire 40mm objective marker on the battlefield, or should the centre of the objective marker be on the corner?*

A: 作戦目標の中央部分が戦場の角の上に来るように配置する。

> [!quote]- EN
> A: The centre of the objective marker should be on the corner.

##### 9.1.2 陣地(Territories)

*Q: ルールにおいてユニットが「自軍側陣地外」や「自軍側陣地から全体が出ている」ことを要求されている場合、戦場にいないユニット（全滅したユニットや予備戦力内のユニットなど）は、そのような状態であるとみなされる？*

A: みなされない。

> [!quote]- EN
> *Q: If a rule requires that a unit be ‘outside of friendly territory’ or ‘wholly outside of friendly territory’, would a unit that is not on the battlefield (for example a destroyed unit or a unit in reserve) count?*
>
> A: No.

##### 10.1 共通の初期配置フェイズアビリティ(Universal Deployment Phase Abilities)

*Q: 『連隊の初期配置』ではなく『ユニットの初期配置』アビリティを使用して、連隊に属するユニットを初期配置することはできるの？*

> [!quote]- EN
> *Q: Can you choose to deploy units that are in a regiment using the ‘Deploy Unit’ ability instead of ‘Deploy Regiment’?*

A: できる。ただし、一度この方法で連隊に属するユニットが初期配置された場合、プレイヤーは『連隊の初期配置』を使用してその連隊に属する残りのユニットを初期配置することができなくなる。なぜなら、そのアビリティの宣言手順において、「選択された連隊内に属するユニットは、1度も初期配置されていてはならない。」と記述されているからだ。

> [!quote]- EN
> A: Yes, however, once a unit in a regiment has been deployed in this manner, you can no longer use ‘Deploy Regiment’ to deploy the remaining units in that regiment, since the declare step of that ability specifies that ‘No units in that regiment can have already been deployed.’

*Q: 初期配置フェイズ中、プレイヤーは陣営地形を必ず配置しなければいけないの？（そのプレイヤーのロスターに陣営地形がある場合）*

> [!quote]- EN
> *Q: Is it mandatory for players to set up a faction terrain feature (if one is included on their roster) during the deployment phase?*

A: いいえ。プレイヤーは『陣営地形の初期配置』アビリティを使用するかどうかを選択できる。ただし、双方のプレイヤーが陣営地形を配置すると決めた場合は、初期配置を開始するプレイヤーがまず、陣営地形を配置しなければならない（10.0のステップ1）。

> [!quote]- EN
> A: No. A player can choose not to use the ‘Deploy Faction Terrain’ ability. However, if both players choose to set up a faction terrain feature, the player who begins deployment must set up their faction terrain features first (as specified in Step 1 of 10.0).

##### 12.0 バトルラウンドの開始時(Start of Battle Round)

*Q: 手番プレイヤーを決定する際、プレイヤーが「アーミーの初期配置を終えた」かどうかは、どうやって判断する？*

> [!quote]- EN
> *Q:* *When determining the active player, how do you determine when a player has ‘finished setting up their army’?*

A: プレイヤーがアーミーの初期配置を終えたというのは、そのプレイヤーのアーミー内のすべてのユニットを初期配置し終えたということである。つまり、『**初期配置**』以外の初期配置フェイズアビリティ（マスクの『終わりなき舞踏』など）は、「自軍アーミーを初期配置」し終えた後に発生するものとなる。

> [!quote]- EN
> A: A player has finished setting up their army when all units in their army have been deployed. This means that non-**DEPLOY** Deployment Phase abilities (e.g. The Masque’s ‘The Endless Dance’ ability) happen after your army has ‘finished setting up’.

##### 14.3 突撃フェイズ(Charge Phase)

*Q: 『突撃』アビリティを使用するとき、自軍のユニットは突撃移動の開始時に突撃するユニットから視認状態であった敵ユニットの½mv以内に一部が入るように突撃移動を完了しなければならないの？*

> [!quote]- EN
> *Q:* *When using the ‘Charge’ ability, does my unit need to end the charge move within 1⁄2" of an enemy unit that was visible to the charging unit at the start of that charge move?*

A: いいえ。突撃するユニットがその突撃移動を完了するときに、視認状態である敵ユニットの½mv以内に一部が入っていなければならない。

> [!quote]- EN
> A: No. It must end the charge move within 1⁄2" of an enemy unit that is visible to the charging unit when it finishes that charge move.

*Q: アビリティが『突撃ロール』のダイス個数を減らしたり、増やしたりする場合、それは突撃ロールに対する修正値なの？*

A: いいえ。それは突撃ロールへの修正値ではありません。

> [!quote]- EN
> *Q. If an ability adds to or subtracts from the number of dice that make up a charge roll, is that a modifier to the charge roll?*
>
> A. No.

##### 15.2 特殊地形上の移動(Moving Across Terrain)

*Q: 特殊地形の上を移動するルールにおいて、兵は昇ったり、降りたりしている最中に移動を完了することはできない==と==記されているけど、兵が昇ったり、降りたりしている最中であることをどう判断するの？*

> [!quote]- EN
> *Q:* *The rules for moving across terrain state that a model cannot end a move mid-climb. How can you tell if a model is mid-climb?*

A: 兵が昇り降りしている最中と判断されるのは、何かしらの支えがない限り、その兵のベースがその場所で留まることができない場合のことを指している。多種多様な地形や兵が存在し、凸凹した地形もあるため、兵のベースがその下にある地形に対して少し斜めになっている状態で移動を完了しても構わない。しかし、そのベースの少なくとも半分が、その兵が配置されている特殊地形から1mv以内に入っていなければならない。そうではない場合、その兵は昇り降りしている最中とみなされる。

> [!quote]- EN
> A: A model is mid-climb if it is not possible to rest it on its base in that location without additional support. As there is a wide variety of terrain and models, it is acceptable for a model to end a move with its base at a slight angle because of uneven terrain beneath it, but at least half of its base must be within 1" of the terrain feature that the model is on or it will be considered mid-climb.

##### 15.4 飛行(Flying)

*Q: ユニットの移動を可能にするアビリティが、ユニットが近接戦闘に突入することができないと記している場合（たとえば、通常移動）、飛行を有するユニットは敵ユニットの近接範囲を通り越えることはできるの？*

> [!quote]- EN
> *Q:* *If an ability that allows a unit to move states that the unit cannot move into combat (e.g. Normal Move), does Fly allow that unit to move across an enemy unit’s combat range?*

A: できる。

> [!quote]- EN
> A: Yes.

##### 16.0 攻撃対象の選択(Picking Targets)

*Q: レンジアタックをする際、攻撃対象であるユニットが一部の攻撃側ユニット内にいる兵から視認状態ではなかったとしても、攻撃側ユニット内にいるすべての兵で攻撃することができるの？*

> [!quote]- EN
> *Q: When making shooting attacks, can all models in the attacking unit shoot even if the target unit is not visible to some of those models?*

A: いいえ。攻撃側ユニット内の兵でレンジアタックをすることができるのは、攻撃対象のユニットが視認状態である兵だけである。

> [!quote]- EN
> A: No, the only models in the attacking unit that can make shooting attacks are those that the target unit is visible to.

*Q: ユニットが『**遠隔攻撃**』アビリティを使用するとき、そのユニットが装備している全部の遠隔武器で遠隔攻撃をしないといけないの？*

> [!quote]- EN
> *Q. When a unit uses a **SHOOT** ability, does it have to shoot with all of the ranged weapons that it is armed with?*

A: その通りだ。

> [!quote]- EN
> A: Yes.

##### 17.0 攻撃手順(The Attack Sequence)

*Q: アビリティによって、ヒットロールの修正前の出目5+でクリティカルヒットがでる場合、しかしそのユニットがヒットを成功させるためには出目6が必要であるならば（たとえば、ヒットロールに-1の修正を受ける）、ヒットロールの修正前の出目5~~+~~は攻撃対象にヒットするの？またその場合、クリティカルヒットの効果は発生するの？*

> [!quote]- EN
> *Q:* *If an ability allows a unit to score critical hits on unmodified rolls of 5+, but that unit needs a 6 to hit (e.g. as a result of subtracting 1 from hit rolls), would unmodified hit rolls of 5 hit the target? If so, would they still trigger any critical hit effects?*

A: ヒットはクリティカルヒットとして扱われるが、その攻撃のヒットは成功していないことになる。その攻撃が失敗した場合、攻撃手順は終了するため、**クリティカル（2ヒット）**や**クリティカル（自動ウーンズ）**は効果を発揮しない。ただし、即座に効果を発揮するもの、たとえば**クリティカル（致命的）は**、それらのクリティカルヒットで効果を発揮する。

> [!quote]- EN
> A: Although the hits would count as critical hits, the attacks would not score a successful hit. As the attack sequence ends if an attack fails, effects such as **Crit (2 Hits)** or **Crit (Auto-wound)** would have no effect. However, effects that are resolved immediately, such as **Crit (Mortal)**, would still be triggered by those critical hits.

*Q: ユニットがフェイズ中に受けた最初のダメージを無視できるようにする2つの異なるアビリティから影響を受けた場合（例えばアシェンエルダーの『煽り立てられた熱狂』とタールの大炉軍の『魔鋼強化』など）、そのフェイズ中最初のダメージと2つ目のダメージを無効化できる？また、フェイズ中最初のダメージを無効化できるようなアビリティの影響を受ける前に、そのフェイズ中最初のダメージを受けていた場合、その後同じフェイズ中に受ける最初のダメージを無効化できる（前者のダメージで兵が戦死して、アビリティの効果を受けられる条件が整った、などの展開により）？*

A: どちらもそうはならない。そのようなアビリティは、フェイズ中でユニットが最初に受けるダメージポイントを無効化するだけである。

> [!quote]- EN
> *Q: If a unit is affected by two different abilities (such as the Ashen Elder’s ‘Stoked Fanaticism’ and the Taar’s Grand Forgehost spell ‘Reinforce Daemonsteel’) that would let it ignore the first damage in a phase, will it ignore the first and second damage points in that phase? If a unit takes damage in a phase before being affected by an ability that would let it ignore the first damage in a phase (e.g. by killing models that brought it wholly within such an effect), will it ignore the next damage point it would take that phase?*
>
> A: No and no. It will only ever ignore the first damage point that was dealt to that unit in that phase.

##### 18.3 撃破された兵(Slain Models)

*Q: 隊形を保つことができず取り除かれた兵は、撃破されたものとして扱われるの？*

> [!quote]- EN
> *Q:* *Do models removed as a result of a unit being out of coherency count as having been slain?*

A: その通りだ。

> [!quote]- EN
> A: Yes.

##### 19.0 先手効果と後手効果(STRIKE-FIRST and STRIKE-LAST)

*Q: まだ近接攻撃をしていない『**先手効果**』を有する敵ユニットが1個以上いる場合、『**先手効果**』を有する味方ユニットが近接攻撃した直後に、『**先手効果**』を持っていない味方ユニットでただちに近接攻撃をすることはできるの？*

> [!quote]- EN
> *Q: Can I use an ability that allows a friendly unit that does not have **STRIKE-FIRST** to fight immediately after a friendly unit that has **STRIKE-FIRST** if there are one or more enemy units with **STRIKE-FIRST** that have not yet been picked to fight?*

A: できない。19.0の横枠に記されているように、別のユニットのアビリティ直後に『**近接攻撃**』アビリティの使用を可能にするアビリティは、『**先手効果**』の制限を無効にするものではない。したがって、すべての『**先手効果**』を有するユニットが近接攻撃をするまで、『**先手効果**』を持たないユニットを選んで近接攻撃をすることはできない。

> [!quote]- EN
> A: No. As mentioned in the sidebar next to 19.0, abilities that allow a unit to use a **FIGHT** ability immediately after another unit do not override the **STRIKE-FIRST** constraints, so you cannot pick a unit that does not have **STRIKE-FIRST** to fight until all other units that have **STRIKE-FIRST** have fought.

*Q: 戦場に配置されている『**先手効果**』を有するユニットが味方ユニットだけであり、かつそのユニットが自身のアビリティ直後に味方ユニットの近接攻撃を可能にするアビリティを持っている場合、どの順番でユニットを選択して近接攻撃を実行するの？*

> [!quote]- EN
> *Q:* *If a friendly unit is the only unit that has **STRIKE-FIRST** on the battlefield and it has an ability that allows a friendly unit to fight immediately after it, in what order would units be picked to fight?*

A: 自身が手番プレイヤーである場合、まず『**先手効果**』を有するユニットが近接攻撃を実行する。次に、その直後に別の味方ユニットの近接攻撃を可能にするアビリティを使用できる。そして、再び自身が次に近接攻撃を実行するユニットを選択する（3個の味方ユニットが立て続けに近接攻撃をすることになる）。敵軍側が手番プレイヤーである場合、まず『**先手効果**』を持つユニットが近接攻撃を実行する。次に、変わることなくその直後に別の味方ユニットの近接攻撃を可能にするアビリティを使用できる。そして、敵軍側が近接攻撃をするユニットを選択する。

> [!quote]- EN
> A: If you are the active player, the unit that has **STRIKE-FIRST** would fight first, then you could use the ability to allow another friendly unit to fight immediately after it, and then you would pick the next unit to fight (i.e. three friendly units would fight back to back). If your opponent is the active player, the unit that has **STRIKE-FIRST** would fight first, you could still use the ability to allow another friendly unit to fight, and then your opponent would pick the next unit to fight.

*Q: 近接フェイズ中に『後手効果』を持たないユニットのあらゆる『近接攻撃』アビリティが解決された後、『後手効果』を持つ最初のユニットを選択するのは、どちらのプレイヤーなの？*

> [!quote]- EN
> Q: *In the combat phase, if all eligible non-**STRIKE‑LAST** units have used a **FIGHT** ability, which player gets to pick the first **STRIKE-LAST** unit to fight?*

A: 『近接攻撃』アビリティを使用するユニットを交互に選択する手順は継続される。つまり『後手効果』を持~~つ~~==たない==ユニットの最後のユニットを選択した後、その対戦相手のプレイヤーは『後手効果』を持つ、攻撃できる最初の自軍側ユニットを1個選択して『近接攻撃』アビリティを使用する。

> [!quote]- EN
> A: The alternating sequence of picking units to use a **FIGHT** ability would continue and so the player who did not pick the last non-**STRIKE-LAST** unit would get to pick the first eligible **STRIKE-LAST** unit in their army to use a **FIGHT** ability.

##### 20.0 武器アビリティ(Weapon Abilities)

*Q: 同じ武器アビリティを複数組み合わせることはできる？たとえば、武器が**対歩兵（+1貫通値）**を有する場合、別の形で同じ武器アビリティを得たならば、その武器は**歩兵**・ユニットに対して+2の【貫通値】を得ることになる？*

> [!quote]- EN
> *Q: Can I combine multiple instances of the same weapon ability? For example, if a weapon already has* **Anti-INFANTRY (+1 Rend)** *and it can also gain that ability from another source, would it now have +2 Rend against* **INFANTRY** *units?*

A: ならない。

> [!quote]- EN
> A: No.

*Q: 武器が『**随行者**』の武器アビリティを有する場合、その武器は新しい武器アビリティを付与する味方アビリティからの効果を受==け==たり、その武器が持つ武器アビリティに修正を加える効果を受けたりするの？*

> [!quote]- EN
> *Q: If a weapon has the* **Companion** *weapon ability, would it be affected by friendly abilities that grant new weapon abilities or that modify weapon abilities that the weapon already has?*

A: その武器の名前を指定していたり、『**随行者**』の武器に効果を付与することを明記していない限り、効果を受けない。

> [!quote]- EN
> A: No, unless the ability specifically names the weapon or states that it affects **Companion** weapons.

##### 21.0 回復(Healing)

*Q: アビリティ（たとえば『復活の種』）によって全滅するはずのユニットの残りのダメージが無効化され、そのユニットが回復される場合、別のアビリティ（たとえば『必死の消火』）によってそのユニットが回復できない状態であるならば、そのユニットは全滅するの？*

> [!quote]- EN
> *Q: If an ability (e.g. ‘Seed of Rebirth’) would allow a unit that would be destroyed to negate all remaining damage points then heal to prevent that unit from being destroyed, and another ability (e.g. ‘Quenching the Flames’) prevents that unit from healing, would that unit still be destroyed?*

A: その通りだ。

> [!quote]- EN
> A: Yes.

##### 24.0 ユニットの配置(Setting Up Units)

*Q: すでに『**移動**』アビリティを使用したユニットが、それと同じ移動フェイズ中に、ユニットを戦場から取り除いて再び配置するようなアビリティの効果を受けることはできる？例えば、**大型獣**ではない味方**ストームキャスト・エターナル**・ユニットが、『到嵐の転移門』の6mv以内に全体が入るように移動し、その後同じ移動フェイズ中に『嵐に足を踏み入れよ』アビリティを使用することはできる？*

> [!quote]- EN
> *Q: Can a unit use a **MOVE** ability and then be affected by an ability which removes them from the battlefield and sets them up again in the same movement phase? For example, could a friendly non-**MONSTER** **STORMCAST ETERNALS** unit move to be wholly within 6" of a Stormreach Portal, and then in the same movement phase use the ‘Step Into the Storm’ ability?*

A: できる。ユニットは、移動フェイズ中、そのターンにおいて戦場に配置された後には『**移動**』アビリティを使用できないが、配置される以前に『**移動**』アビリティを使用することはできる。

> [!quote]- EN
> A: Yes. Units cannot use **MOVE** abilities in the movement phase after being set up on the battlefield that turn, but are able to use **MOVE** abilities before doing so

##### 24.2 代替ユニット(Replacement Units)

*Q: 全滅したユニットが強化を有しており、アビリティによってその代替ユニットを配置できる場合、代替ユニットもその強化を持つことになる？*

> [!quote]- EN
> *Q:* *If a destroyed unit had an enhancement, and an ability allows me to set up a replacement of that unit, would the replacement unit also have that enhancement?*

A: ならない。

> [!quote]- EN
> A: No.

*Q: アビリティが元のユニットの代替ユニット（半減した兵数）を配置できる場合、元のユニットのある割合の兵が特定の武器を装備していなければならなかったならば、その新しい代替ユニットもその制限に従わなければならないの？*

> [!quote]- EN
> *Q: If an ability allows a replacement unit to be set up with half the models from the original unit, and the original unit has to have a certain proportion of models equipped with specific weapons, does the new unit also need to adhere to the same restrictions?*

A: 制限に従う必要はない。24.2に記されている通り、代替ユニットに配置される兵は、元のユニットから任意で選択できる。

> [!quote]- EN
> A: No. As stated in 24.2, you can pick any models from the original unit to be set up in the replacement unit.

*Q: アビリティによって元のユニットの半分の兵数からなる代替ユニットを配置できる場合、『再結集』のようなアビリティを使用してその代替ユニットに兵を復帰させ、元のユニットの構成兵数まで戻すことはできる？*

A: できない。代替ユニットは、新しい構成兵数を持つ、新しいユニットとして扱われるためだ。

> [!quote]- EN
> *Q: If an ability allows a replacement unit to be set up with half the models from the original unit, could I then use an ability such as ‘Rally’ to return models to that unit until it reached the unit size of the original unit?*
>
> A: No. A replacement unit is treated as a new unit with a new unit size.

##### 25.0 護られし英雄(Guarded Heroes)

*Q: アビリティによって==、攻撃対象を選択する際に==『護られし英雄』アビリティの効果を無視することができる場合（たとえば、ウォーロック・エンジニアの『一流スナイパー』アビリティ）、攻撃側ユニットは『護られし英雄』アビリティによって発生するヒットロールの-1の修正を受けるの？*

> [!quote]- EN
> *Q:* *If an ability allows me to ignore the effects of the ‘Guarded Hero’ ability when picking targets (e.g. the Warlock Engineer’s ‘Sniper-master’ ability), would the attacking unit still be affected by the -1 to hit penalty from ‘Guarded Hero’?*

A: 受ける。

> [!quote]- EN
> A: Yes.

##### 26.0 ランダム能力値(Random Characteristics)

*Q: ランダム能力値のロールは『全力移動』アビリティの宣言前なの？それとも後なの？*

> [!quote]- EN
> Q: *Do you roll a random characteristic roll before or after declaring a **RUN** ability?*

A: アビリティ宣言後、リアクション使用後のタイミングにロールする。

> [!quote]- EN
> A: After declaring it and after all reactions are used.

##### 28.0 上級アビリティのルール(Advanced Ability Rules)

*Q: ルールに、あるキーワードか別のキーワードを持つユニットを何個か選ぶように記されている場合（たとえば、「**スキンク・歩兵**または**騎兵**・ユニットを最大3個まで選択する」)、どちらかのキーワードを持つユニットを組み合わせて選ぶことができるのか、それとも選ぶユニットはすべて同じキーワードを持っていなければならないの？*

> [!quote]- EN
> *Q: If a rule says to pick a number of units with one keyword or another (e.g. ‘Pick up to 3 friendly **SKINK INFANTRY** or **CAVALRY** units’), could you pick a combination of units with either keyword, or do all the units you pick need to have the same keyword?*

A: 自由に組み合わせることができる。上記の例では、たとえば1個の**スキンク・歩兵**・ユニットと2個の**スキンク・騎兵**・ユニットを選択することができる。

> [!quote]- EN
> A: You can mix and match. In the example given, you could pick 1 **SKINK INFANTRY** unit and 2 **SKINK CAVALRY** units.

*Q: 全滅したユニットに継続効果が適用されており、別のアビリティによってそのユニットが戦場に復帰した場合（たとえば、『栄光への道：アセンション』・バトルパックの『蘇生』奇蹟）、その継続効果は復帰したユニットにも適用される？*

> [!quote]- EN
> *Q:* *If a persisting effect applies to a unit that is destroyed, and another ability allows that unit to return to the battlefield (e.g. the ‘Resurrection’ prayer from the Path to Glory: Ascension battlepack), does the persisting effect apply to the returned unit?*

A: 適用される。

> [!quote]- EN
> A: Yes.

*Q: アビリティの効果の一部において「できる」あるいは「しなければならない」と記されていなくても、その効果の一部を必ず解決しなければならないの？*

> [!quote]- EN
> *Q: If a part of an ability’s effect does not state that you ‘can’ or ‘must’ do it, is it mandatory to resolve that part of the effect?*

A: 解決する必要がある。任意でない効果は、必ず解決されなければならない。効果の一部を解決することができない場合、その効果全体が適用されなくなる。たとえば、プレイヤーが『ゴルクの手』の選択対象として、その呪文を唱えた**魔術師**自身を選んだ場合、効果を完全に解決することができず（選択された魔術師は戦場から取り除かれることもなければ、詠唱者の24mv以内に全体が入るように配置されることもない）、その呪文の効果は発揮されない。

> [!quote]- EN
> A: Yes. Any part of an effect that is not optional is mandatory. If you cannot resolve one part of an effect, none of it applies. For instance, if a player picked the **WIZARD** casting ‘The Hand of Gork’ to also be the target of the spell, the effect could not be fully resolved – it would be impossible for the target to be removed from the battlefield and set up again wholly within 24" of the caster – and so the spell would have no effect.

*Q: 継続効果は全滅したユニットに適用された状態が続くことになるの？*

A: その通りだ。

> [!quote]- EN
> *Q: Do persisting effects continue to apply to a unit that has been destroyed?*
>
> A: Yes.

##### 28.2「1回限り」「につき1回」のタイミング('Once Per' Timings)

*Q: ユニットのウォースクロールに記載されていないアビリティが「各ターンにつき1回限り」「バトル中1回限り」「各バトルラウンドにつき1回」（その後に「アーミー」と記されていない）とタイミング欄に記している場合、複数の味方ユニットがそのアビリティをそのタイミング中に使用できるの？*

> [!quote]- EN
> *Q:* *If an ability that is not on a unit’s warscroll has the ‘Once Per Turn’, ‘Once Per Battle’ or ‘Once Per Battle Round’ timing (without ‘(Army)’ afterwards), can multiple friendly units use that ability in that time period?*

A: それは、誰がアビリティを使用するかによって異なる（28.2の横枠を参照）。ユニットがアビリティを使用する場合は（たとえば、宣言ステップにユニットを選ぶように記載されている）、各ユニットがそのアビリティをそのタイミング中に使用できる。プレイヤーがアビリティを使用する場合は（アビリティの説明にユニットが使用すると明記されていない）、そのタイミング中に1回だけ使用できることになる。アビリティの効果が発揮される対象と、アビリティを使用するためにユニットを選択することは、まったく別のことであることに注意する。

> [!quote]- EN
> A: It depends on who is using the ability (see the sidebar next to 28.2). If a unit is using the ability (i.e. the declare step specifically says to pick a unit to use it), then each unit could use that ability in that time period. If the player is using the ability (i.e. nothing in the ability specifically says that it is used by a unit), it can only be used once in that time period. Note that picking the target of an ability is not the same as picking a unit to use that ability.

##### 32.3 特殊地形の確保(Terrain Control)

*Q: プレイヤーが~~特殊地形の一部分を確保している場合、そのユニットが一部分を確保している状態を保ちながら、そのユニットは別の特殊地形の一部を確保するためにカウントすることはできるの~~==特殊地形を確保している場合、最初の特殊地形を確保している状態を保ちながら、ユニットは別の特殊地形を争奪しているものとしてカウントすることはできるの==？*

A: できる。

> [!quote]- EN
> *Q: If a player controls a piece of terrain, can a unit be counted towards contesting a different piece of terrain while still maintaining control of the first piece?*
>
> A: Yes.

## 上級ルール 2026-27(Advanced Rules)

### 上級ルール 2026-27(Advanced Rules 2026-27)

#### Introduction

The *General’s Handbook 2026-27* battlepack uses the following Advanced Rules modules:

#### 指揮アビリティ 2026-27(Commands 2026-27)

これらのルールは、プレイヤーがどのようにして**指揮ポイント**を獲得し、アビリティや対戦相手のターンに反応したりすることができる強力な**『指揮アビリティ』**を使用する方法を説明している。**『指揮アビリティ』**ルールを使用していない場合は、指揮ポイントの記号があるアビリティを無視する。

> [!quote]- EN
> These rules explain how you can earn **command points** to use powerful **commands** that allow you to react to abilities and interact in your opponent’s turn. If you are not using the **Commands** rules, ignore any abilities that have the command point symbol in the corner.

#### 特殊地形 2026-27(Terrain 2026-27)

これらのルールは、兵がどのように特殊地形とかかわるのか、たとえば兵がどのようにして遮蔽のボーナスを受けられるのか、どのようにして神秘なる力を呼び起こすのかなどの詳細が記載されている。

> [!quote]- EN
> These rules go into more detail about how your models interact with terrain features, such as how they can take cover or even draw power from arcane nexuses.

#### 魔法 2026-27(Magic 2026-27)

**魔術師**、**神官**、**顕現**を用いて、絶大な神秘の力を唱えたい場合は**魔法**を参照する。

> [!quote]- EN
> If you’d like to wield unlimited mystical power by including **WIZARDS**, **PRIESTS** and **manifestations** in your battles, see **Magic**.

#### アーミー編成 2026-27(Army Composition 2026-27)

独自の**アーミーロスター**を作成し、**連隊**や**戦闘陣形**、**強化**をカスタマイズする準備ができている場合は、**アーミー編成**を参照する。

> [!quote]- EN
> If you’re ready to build your own **army roster** and customise your army with **regiments**, **battle formations** and **enhancements**, see **Army Composition**.

#### 特殊兵 2026-27(Command Models 2026-27)

ここでは『ウォーハンマー：エイジ・オヴ・シグマー』の多くのユニットに見られる**豪傑**、**旗手**、**楽士**と呼ばれる特殊兵のルールが記載されている。

> [!quote]- EN
> Here you will find rules for special models called **champions**, **standard bearers** and **musicians**, which are found in many Warhammer Age of Sigmar units.

#### 戦術目標 2026-27(Battle Tactics 2026-27)

**戦術目標**と呼ばれる副次目標をゲームに含めることで、ゲームにさらなる戦術的なチャレンジを追加する。

> [!quote]- EN
> Add an additional tactical challenge to your games by including secondary objectives called **Battle Tactics**.

#### 独自のバトルパックを構築(Build your Own Battlepack)

『ウォーハンマー：エイジ・オヴ・シグマー』には、進行中のキャンペーンに連動した物語主導のバトルに焦点を当てた**栄光への道**・バトルパックから、バランスと対戦プレイに重点を置く**スピアヘッド**・バトルパックや**マッチプレイ**・バトルパックまで、多くの遊び方が存在する。

公式のバトルパックを使用するだけでなく、このセクションに収録されているルールを一揃いの機能として使用し、その中の要素を組み合わせて、独自のバトルプランやバトルパックを作って友人とプレイすることをお勧めする。

集めてきたミニチュアで友人と大規模なバトルを繰り広げたり、どの怪物が頂点に君臨するのか試してみたりと、きっと色々な遊び方を想像するだけでワクワクするはずだ。固有のバトルプランやスペシャルルールをデザインしたい場合もあれば、弟や妹に遊び方を教えるためにルールを単純にしておきたい場合もあるだろう。これらのルールは、個々の要望に合わせて自由に用いることのできる枠組みを与えてくれる。

ここでいくつかのアイデアを紹介したい：

- 上級ルールを用いてアーミー編成をする代わりに、お気に入りのブラックライブラリーの物語に基づいて、または自らが作り上げたシナリオに基づいて、アーミー編成をしてみるのも楽しいかもしれない。たとえば、5体のストームキャスト・エターナルの英雄たちが、巨大な渾沌の怪物を相手にどこまで戦うことができるのかを試してみるのはどうだろうか？
- 戦場を各プレイヤーの陣地に分割し、作戦目標を配置し、バトルで起こる展開を一考し、自分だけのバトルプランをデザインしてみるのもいいだろう。楽しみながら、色々なアイデアを試してみよう。固定した場所に作戦目標を配置するのではなく、プレイヤーで交互に作戦目標を配置してみたり、二つの小さな戦場を境界門でつなげてみるのはどうだろうか？
- 上級ルールは、バトルにルールを一つずつ取り入れながら学んでいこう。たとえば『指揮アビリティ』のルールをまず試してみて、その次に『魔法』を加えてみる。最後にそれらを組み合わせて相手を出し抜き、『戦術目標』でポイントを獲得してみたりするのも良いかもしれない。

> [!quote]- EN
> There are many, many ways to play Warhammer Age of Sigmar, from **Path to Glory** battlepacks, which focus on narrative-driven battles linked in an ongoing campaign, to **Spearhead** and **Matched Play** battlepacks, in which the emphasis is on balance and competitive play.
>
> In addition to using official battlepacks, we’d encourage you to use the rules in this section as a toolbox, mixing and matching the elements within to build your own battleplan or battlepack to play with your friends.
>
> Are you excited to field your entire collection against your friends or to see which monster reigns supreme? Maybe you want to design your own battleplans and special rules, or perhaps you want to keep things simple in order to teach a younger sibling how to play. These rules provide an open framework that makes each of these things possible.
>
> Here are some ideas to get you started:
>
> - Instead of using the Advanced Rules for Army Composition, make an army based on your favourite Black Library story or based on a made‑up scenario that sounds exciting to you. For instance, how would 5 different Stormcast Eternals heroes fare against a pair of massive Chaos monsters?
> - Design your own battleplan by dividing portions of the battlefield into a territory for each player, placing objectives and thinking up a fun twist for the battle. Have fun and experiment with different ideas – why not try alternating placing objectives instead of having fixed locations, or try having two smaller battlefields connected by realmgates?
> - Learn the Advanced Rules by introducing each module into your battles one at a time – for instance, start by experimenting with Commands, then try adding Magic into your battles, and finally put them all together to outwit your opponent and score Battle Tactics.

### 指揮アビリティ 2026-27(Commands 2026-27)

#### 1.0 指揮アビリティの概要(Commands Overview)

**『指揮アビリティ』**と呼ばれる一部のアビリティは、そのアビリティを使用するために1ポイント以上の**指揮ポイント**を必要とするものがある。**指揮ポイントコスト**（アビリティの右上隅に示される）を持つアビリティは、すべて指揮アビリティである。

> [!quote]- EN
> Some abilities, called commands, require that you spend one or more command points to use that ability. Any ability that has a command point cost (indicated in the top right corner of the ability) is a command.

##### 1.1 指揮ポイントの獲得(Earning Command Points)

各バトルラウンドの開始時に、**アンダードッグ**を決定した後、各プレイヤーは**4指揮ポイント**を獲得する。**アンダードッグ**のプレイヤーがいる場合、そのプレイヤーは追加の1指揮ポイントを獲得する。バトルラウンドの終了時に、プレイヤーの指揮ポイントは0ポイントにリセットされる（使用されていない指揮ポイントは破棄される）。

> [!quote]- EN
> At the start of each battle round, after determining the underdog, each player gains 4 command points. If there is an underdog, they gain 1 extra command point. At the end of the battle round, the players’ command points are reset to 0 (any that have not been used are lost).

##### 1.2 指揮アビリティの使用方法(Using Commands)

指揮アビリティは、他のアビリティと同じように使用される。ただし、各ユニットはフェイズごとに指揮アビリティを1回だけしか使用できない。また、各アーミーはフェイズごとに、それぞれの指揮アビリティを1回しか使用できない。指揮アビリティを使用するには、**指揮ポイントコスト**に等しい数の指揮ポイントを消費しなければならない。

> [!quote]- EN
> Commands are used in a similar manner to any other ability. However, each unit can only use 1 command in each phase, each command can only be used 1 time by each army in each phase, and you must spend a number of command points equal to the command point cost to use a command.

#### 2.0 ヒーローフェイズの指揮アビリティ(Hero Phase Commands)

> **再集結(Rally)**（任意のヒーローフェイズ｜1 CP）
>
> *奮起を呼び起こす声によって、負傷した戦士たちは再び立ち上がり、新たな隊が倒れた同胞の意志を受け継ぎ戦場に立つ。*
>
> - **宣言:** **近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** D6の**再集結ロール**を6回実行する。ロール結果で4+が出るたびに、1**再集結ポイント**を獲得する。再集結ポイントは、以下の方法で使用できる：
>
>   - 1再集結ポイントごとに、そのユニットを**回復（1）**する。
>   - ユニットの**【体力】**に等しい数の再集結ポイントを消費して、そのユニットに撃破された兵を1体**復帰**させることができる。
>
>   上記に示す任意の組み合わせで、再集結ポイントを消費してもよい。その後、消費されていない再集結ポイントは破棄される。

> [!quote]- EN
> **Rally**（Any Hero Phase｜1 CP）
>
> *With an inspiring call to action, wounded soldiers get a second wind and fresh troops take the field to replace their fallen comrades.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** to use this ability.
> - **Effect:** Make 6 **rally rolls** of D6. For each 4+, you receive 1 **rally point**. Rally points can be spent in the following ways:
>
>   - For each rally point spent, **Heal (1)** that unit.
>   - You can spend a number of rally points equal to the **Health** characteristic of that unit to **return** a slain model to that unit.
>
>   You can spend the rally points in any combination of the above. Unspent rally points are then lost.

> **魔法の介入(Magical Intervention)**（敵軍側ヒーローフェイズ｜1 CP）
>
> *神秘なる力を習得せし戦士は、敵の策を妨害するために口早に呪文を唱える。*
>
> - **宣言:** 味方**魔術師**または**神官**を1体選択し、このアビリティを使用する。
> - **効果:** That friendly unit can use a **SPELL**, **PRAYER** or **BANISH** ability (as appropriate) as if it were your hero phase. If you do so, subtract 1 from **casting rolls** or **chanting rolls** made as part of that ability.

> [!quote]- EN
> **Magical Intervention**（Enemy Hero Phase｜1 CP）
>
> *A warrior learned in the mystic arts utters a rapid incantation to disrupt the enemy’s plans.*
>
> - **Declare:** Pick a friendly **WIZARD** or **PRIEST** to use this ability.
> - **Effect:** That friendly unit can use a **SPELL**, **PRAYER** or **BANISH** ability (as appropriate) as if it were your hero phase. If you do so, subtract 1 from **casting rolls** or **chanting rolls** made as part of that ability.

#### 3.0 移動フェイズの指揮アビリティ(Movement Phase Commands)

> **再配置(Redeploy)**（敵軍側移動フェイズ｜1 CP）
>
> *敵の動きに対して先手を打つため、戦士たちは急いで新しい位置に展開する。*
>
> - **宣言:** **近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** 選択された味方ユニット内の各兵は、最大D6mvまで移動できる。その移動は、敵ユニットの近接範囲内を通り抜けたり、近接範囲内で完了することは**できない**。
> - **キーワード:** 移動、全力移動

> [!quote]- EN
> **Redeploy**（Enemy Movement Phase｜1 CP）
>
> *Taking initiative, the warriors hastily reposition to respond to enemy movements.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** to use this ability.
> - **Effect:** Each model in that unit can move up to D6". That move **cannot** pass through or end within the combat range of an enemy unit.
> - **Keywords:** Move, Run

> **駆け足、急げ！(At the Double)**（リアクション：自軍側が『全力移動』アビリティを宣言｜1 CP）
>
> *指揮官の号令とともに、戦士たちは戦場の要所へと全力疾走で向かう。*
>
> - **使用者:** その**『全力移動』**アビリティを使用しているユニット1個。
> - **効果:** その**『全力移動』**アビリティの手順の中で、**全力移動ロール**を実行しない。代わりに、選択されたユニットの**【移動力】**に6mvが加算され、そのユニット内の各兵がその**『全力移動』**アビリティの手順の中で移動できる距離を決定する。

> [!quote]- EN
> **At the Double**（Reaction: You declared a **RUN** ability｜1 CP）
>
> *At a command from their general, the warriors sprint to a key position on the battlefield.*
>
> - **Used By:** &#x20;The unit using that **RUN** ability.
> - **Effect:** Do not make a **run roll** as part of that **RUN** ability. Instead, add 6" to that unit’s **MOVE** characteristic to determine the distance each model in that unit can move as part of that **RUN** ability.

#### 4.0 遠隔フェイズの指揮アビリティ(Shooting Phase Commands)

> **援護射撃(Covering Fire)**（敵軍側遠隔フェイズ｜1 CP）
>
> *戦士たちは近くの敵部隊に素早く一斉射撃を放ち、矢継ぎ早に戦闘へと突入する。*
>
> - **宣言:** このターン中、**『全力移動』**アビリティを使用しておらず、かつ**近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。選択された味方ユニットに最も近く、かつレンジアタックの対象として選択可能な敵ユニットを選択する。**顕現**や陣営地形はこのアビリティの対象として選択できない。
> - **効果:** 選択された敵ユニットに対して、このアビリティを使用したユニットのレンジアタックを解決する。これらのヒットロールは-1の修正を受ける。
> - **キーワード:** 遠隔攻撃、アタック

> [!quote]- EN
> **Covering Fire**（Enemy Shooting Phase｜1 CP）
>
> *The warriors unleash a quick volley at a nearby enemy unit before it charges into combat.*
>
> - **Declare:** Pick a friendly unit that did not use a **RUN** ability this turn and that is **not in combat** to use this ability, then pick the closest enemy unit (to that unit) that can be picked as the target of shooting attacks to be the target. You cannot pick **MANIFESTATIONS** or faction terrain features as the target of this ability.
> - **Effect:** Resolve shooting attacks for the unit using this ability against the target. You must subtract 1 from the hit rolls for those attacks.
> - **Keywords:** Attack, Shoot

#### 5.0 突撃フェイズの指揮アビリティ(Charge Phase Commands)

> **報復攻撃(Counter-Charge)**（敵軍側突撃フェイズ｜2 CP）
>
> *決定的一打を必要とする戦士たちは、敵の前進を阻止したり、大胆な迎撃に打って出る。*
>
> - **宣言:** **近接戦闘中ではない**味方ユニットを1個選択し、このアビリティを使用する。
> - **効果:** 選択された味方ユニットは、あたかも自軍側突撃フェイズ中かのように**『突撃』**アビリティを1回使用できる。

> [!quote]- EN
> **Counter-Charge**（Enemy Charge Phase｜2 CP）
>
> *Seeing the need for decisive action, the warriors charge forth to stall the enemy’s advance or enact a bold interception.*
>
> - **Declare:** Pick a friendly unit that is **not in combat** to use this ability.
> - **Effect:** That unit can use a **CHARGE** ability as if it were your charge phase.

> **勝利に向かって進め(Forward to Victory)**（リアクション：自軍側が『突撃』アビリティを宣言｜1 CP）
>
> *軍勢の勢いが衰えようとした瞬間、魂が赤々と燃えるような指令が隊に新たな活力を与える。*
>
> - **使用者:** その**『突撃』**アビリティを使用しているユニット1個。
> - **効果:** その**突撃ロール**をリロールできる。

> [!quote]- EN
> **Forward to Victory**（Reaction: You declared a Charge ability｜1 CP）
>
> *With their charge faltering, a rousing command gives the unit renewed energy to reach their foes.*
>
> - **Used By:** The unit using that **CHARGE** ability.
> - **Effect:** You can re-roll the **charge roll**.

#### 6.0 攻撃（遠隔と近接）の指揮アビリティ(Attacking (Shooting and Combat) Commands)

> **全力攻撃(All-Out Attack)**（リアクション：自軍側が『アタック』アビリティを宣言｜1 CP）
>
> *熱狂的な勢いで戦士たちは攻撃を仕掛ける。*
>
> - **使用者:** その**『アタック』**アビリティを使用しているユニット1個。
> - **効果:** Add 1 to **hit rolls** for attacks made as part of that **ATTACK** ability. This also affects weapons that have the **Companion** weapon ability. For the rest of the turn, subtract 1 from **save rolls** for the unit using this ability.

> [!quote]- EN
> **All-Out Attack**（Reaction: You declared an **ATTACK** ability｜1 CP）
>
> *The warriors fight with frenzied vigour.*
>
> - **Used By:** The unit using that **ATTACK** ability.
> - **Effect:** Add 1 to **hit rolls** for attacks made as part of that **ATTACK** ability. This also affects weapons that have the **Companion** weapon ability. For the rest of the turn, subtract 1 from **save rolls** for the unit using this ability.

#### 7.0 防御の指揮アビリティ(Defensive Commands)

> **全力防御(All-Out Defence)**（リアクション：敵軍側が『アタック』アビリティを宣言｜1 CP）
>
> *身に迫る攻撃を防ぐため、兵士たちは隊列を組む。*
>
> - **使用者:** その**『アタック』**アビリティの攻撃対象となったユニット1個。
> - **効果:** Add 1 to **save rolls** for that unit until that **ATTACK** ability has been resolved.

> [!quote]- EN
> **All-Out Defence**（Reaction: Opponent declared an **ATTACK** ability｜1 CP）
>
> *The soldiers close ranks to hold off an incoming attack.*
>
> - **Used By:** A unit targeted by that **ATTACK** ability.
> - **Effect:** Add 1 to **save rolls** for that unit until that **ATTACK** ability has been resolved.

#### 8.0 ターン終了時の指揮アビリティ(End of Turn Commands)

> **強行突破(Power Through)**（任意のターン終了時｜1 CP）
>
> *戦士たちは巨躯なる塊となって、またその耐久力を駆使して、弱者どもを吹き飛ばしては敵陣を粉砕する。*
>
> - **宣言:** このターン中に突撃を実行している味方ユニットを1個選択し、このアビリティを使用する。次に、選択された味方ユニットと近接戦闘中である敵ユニットを1個選択しなければならない。選択された敵ユニットの【体力】は、このアビリティを使用する味方ユニットの【体力】より低くなければならない。
> - **効果:** その敵ユニットは**D3ポイントの致命的ダメージ**を受ける。次に、このアビリティを使用するユニットは、自身の【移動力】に示された距離まで移動してもよい。その移動は、移動開始時に近接戦闘中であった敵ユニットの近接範囲を通り抜けたり、その近接範囲内で完了できる。ただし、その他の敵ユニットであれば、選択された味方ユニットはそのような敵ユニットを通り抜けたり、その近接範囲内で移動を完了することはできない。またその味方ユニットは、近接戦闘に突入するように移動を完了する必要はない。
> - **キーワード:** 移動

> [!quote]- EN
> **Power Through**（End of Any Turn｜1 CP）
>
> *The warriors use their sheer mass or resilience to drive through a group of weaker foes, leaving broken bodies in their wake.*
>
> - **Declare:** Pick a friendly unit that charged this turn to use this ability, then you must pick an enemy unit **in combat** with it to be the target. The target must have a lower **Health** characteristic than the unit using this ability.
> - **Effect:** Inflict **D3 mortal damage** on the target. Then, the unit using this ability can move a distance up to its **Move** characteristic. It can pass through and end that move within the combat ranges of enemy units that were in combat with it at the start of the move, but not those of other enemy units. It does not have to end the move in combat.
> - **Keywords:** Move

### 特殊地形 2026-27(Terrain 2026-27)

#### 1.0 特殊地形の概要(Terrain Overview)

特殊地形は、戦場に戦術的な挑戦要素をもたらしてくれる。特殊地形の配置方法については、使用しているバトルプランまたはバトルパックを参照。

> [!quote]- EN
> Terrain features add interest and tactical challenges to the battlefield. The battleplan or battlepack you are using will explain how to set up terrain.

> The Citadel Terrain List, available at **warhammer-community.com**, includes a list of Warhammer Age of Sigmar terrain features and tells you which terrain abilities each of them has.

##### 1.1 特殊地形の上に全体が入っている、特殊地形の背後にいる(Wholly On Terrain and Behind Terrain)

兵のベースがその特殊地形上に配置されており、ベースのどの部分もその特殊地形の端を越えていない場合、その兵は**特殊地形の上に全体が入っている**とみなされる。「ユニットが特殊地形の上に全体が入っている」という場合、そのユニット内に属する全兵のベースのすべてが特殊地形の端を越えないように入っていなければならない。

ユニットが攻撃の対象となるとき、攻撃側兵のベースの最も近い部分から射程内にいる対象ユニットの兵==のベースの最も近い部分==まで直線を引くことができず、その直線が特殊地形の上を通過しなければならない場合、その攻撃側兵の攻撃から、その攻撃対象のユニットは特殊地形の背後にいる状態とみなされる。攻撃対象が特殊地形の背後にいるかどうかを判定する際、攻撃側ユニットの近接範囲内に一部でも入っている特殊地形~~やそ~~の~~特殊地形の一部である~~パーツは無視される。

> [!quote]- EN
> A model is **wholly on a terrain feature** if its base is on that terrain feature and no part of its base extends past the edge of that terrain feature. A unit is wholly on a terrain feature if every model in that unit is wholly on that terrain feature.
>
> When a unit is targeted by an attack, if it is impossible to draw a straight line from the closest point on the attacking model’s base to the closest point on the base of a model in the target unit that is in range without that line passing over that terrain feature, the target unit is considered to be **behind a terrain feature** for the attack made by that attacking model. Ignore parts of the terrain feature within the attacking unit’s combat range for the purposes of determining if the target is behind that terrain feature.

##### 1.2 共通の特殊地形アビリティ(Universal Terrain Abilities)

それぞれの特殊地形は、以下のパッシブアビリティを1個以上有する：

> [!quote]- EN
> Each terrain feature has one or more of the following passive abilities:

- **遮蔽物：**特殊地形の背後にいる、または特殊地形の上に全体が入っているユニットを対象とする攻撃は**ヒットロール**に-1の修正を受ける。攻撃~~側~~==対象の==ユニットが現在のターン中に**突撃**を実行している、または**飛行**・キーワードを有する場合、そのマイナス修正を受けない。
- **通り抜け不可能：**兵は、この特殊地形の一部を通り抜けて移動することも、特殊地形の上で移動を完了することもできない。また、兵をこの特殊地形の一部の上に配置することもできない。
- 射線妨害：~~ユニット内の全兵が~~**大型獣**でなく**戦闘兵器**でない、**飛行**を持たないユニット==の全兵==が、この特殊地形の1mv以内に一部でも入っている場合、以下が適用される：
  - そのユニットは、近接範囲内に入っている敵からのみ視認状態となる。
  - そのユニットの遠隔武器の【射程】は半減する（最も近いmv数まで切下げ）
- **力を秘めし地形：この特殊地形の3mv以内に一部でも入っている英雄は、**『力を秘めし地形の解放』アビリティを使用できる（下記参照）。
- **不安定：**兵はこの特殊地形を**通り抜ける**ことができる。しかし、高さが1mvを超えるこの特殊地形の任意の部分に兵を配置できない。また兵は、高さが1mvを超えるこの特殊地形の任意の部分でどのような移動も完了することは**できない**。

> [!quote]- EN
> - **Cover:** Subtract 1 from hit rolls for attacks that target a unit that is behind or wholly on this terrain feature, unless that unit charged this turn or has the **FLY** keyword.
> - **Impassable:** Models cannot move across, be set up on or end moves on any part of this terrain feature.
> - **Obscuring:** While every model in a non-**MONSTER** non-**WAR MACHINE** unit that does not have the **FLY** keyword is within 1" of this terrain feature, the following apply:
>   - That unit is only visible to enemy units that are within its combat range.
>   - The Range characteristic of that unit’s ranged weapons is halved (rounding down to the nearest inch).
> - **Place of Power: HEROES** within 3" of this terrain feature can use the ‘Activate Place of Power’ ability.
> - **Unstable:** Models can move across but cannot be set up on or end any type of move on any part of this terrain feature that is more than 1" tall.

> **力を秘めし地形の解放(Activate Place of Power)**（各ターンにつき1回（アーミー）、任意のターン開始時）
>
> - **宣言:** **力を秘めし地形**の3mv以内に一部でも入っている味方**英雄**を1体選択し、このアビリティを使用する。
> - **効果:** Roll a dice. On a 1, inflict D3 mortal damage on that **HERO**. On a 2+, pick 1 of the following effects:
>
>   - *I**gnite Fury:*** Gain 2 **rage dice**, then increase your **fury level** by 2, to a maximum of 7.
>   - ***Channel Wrath:*** If that **HERO** is a **WIZARD** or **PRIEST**, add 1 to casting rolls or chanting rolls for that **HERO** for the rest of the turn.
>   - ***Dizzying Rage:*** For the rest of the turn, if that **HERO** is not a **WIZARD** or **PRIEST**, they can use the ‘Unbind’ or ‘Banish Manifestation’ ability as if they had **WIZARD (1)**.
> - **キーワード:** コア

> [!quote]- EN
> **Activate Place of Power**（Once Per Turn (Army), Start of Any Turn）
>
> *There are many locus points of volcanic magic in Aqshy. From these simmering fonts of passion and fury, one can draw great strength or unleash a dizzying wave of anger that causes spellcasters to lose control of their magic.*
>
> - **Declare:** Pick a friendly **HERO** within 3" of any **Places of Power** to use this ability.
> - **Effect:** Roll a dice. On a 1, inflict D3 mortal damage on that **HERO**. On a 2+, pick 1 of the following effects:
>
>   - *I**gnite Fury:*** Gain 2 **rage dice**, then increase your **fury level** by 2, to a maximum of 7.
>   - ***Channel Wrath:*** If that **HERO** is a **WIZARD** or **PRIEST**, add 1 to casting rolls or chanting rolls for that **HERO** for the rest of the turn.
>   - ***Dizzying Rage:*** For the rest of the turn, if that **HERO** is not a **WIZARD** or **PRIEST**, they can use the ‘Unbind’ or ‘Banish Manifestation’ ability as if they had **WIZARD (1)**.
> - **Keywords:** Core

##### 1.3 特殊地形のサイズ(Terrain Sizes)

- 7mv×7mv以下の面積に入りきる特殊地形は、**小型地形**である。
- 小型地形ではないものの、7mv×12mv以下の面積に入りきる特殊地形は、**中型地形**である。
- 7mv×12mv以内の面積に入りきることができない特殊地形は、**大型地形**である。

> [!quote]- EN
> - Terrain that fits into an area no larger than 7" × 7" is **small**.
> - Terrain that is not small and fits into an area no larger than 7" × 12" is **medium**.
> - Terrain that is too big to fit into an area 7" × 12" is **large**.

##### 1.4 特殊地形の種別(Terrain Types)

『ウォーハンマー：エイジ・オヴ・シグマー』のそれぞれの**特殊地形**は、次のいずれかの種別である：

- **障害物**
- **射線妨害特殊地形**
- **エリア地形**
- **力を秘めし地形**
- **陣営地形**

バトルが開始される前に、プレイヤーはそれぞれの特殊地形に適用される特徴について合意しなければならない。

> [!quote]- EN
> Each **terrain feature** in Warhammer Age of Sigmar is one of the following types:
>
> - **Obstacle**
> - **Obscuring Terrain**
> - **Area Terrain**
> - **Place of Power**
> - **Faction Terrain**
>
> Before the battle begins, players must agree on which type applies to each terrain feature.

##### 1.4.1 障害物(Obstacles)

**例：**残骸、廃墟、像、バリケード

**特殊地形アビリティ：**遮蔽物、不安定

> [!quote]- EN
> **Examples:** Ruins, debris, statues, barricades
>
> **Terrain Abilities:** Cover, Unstable

##### 1.4.2 射線妨害特殊地形(Obscuring Terrain)

**例：**森林、城壁

**特殊地形アビリティ：**遮蔽物、射線妨害、不安定

> [!quote]- EN
> **Examples:** Wyldwood, fortress wall
>
> **Terrain Abilities:** Cover, Obscuring, Unstable

##### 1.4.3 エリア地形(Area Terrain)

**例：**丘、嵐の宝物庫

**特殊地形アビリティ：**遮蔽物

> [!quote]- EN
> **Examples:** Hills, Stormvault Terrain
>
> **Abilities:** Cover

##### 1.4.4 力を秘めし地形(Places of Power)

**例：**~~魔力抽出器~~==境界門==、浄化の聖水源、魔力抽出器

**特殊地形アビリティ：**遮蔽物、力を秘めし==地形==、不安定

> [!quote]- EN
> **Examples:** Realmgate, Cleansing Aqualith, Nexus Syphon
>
> **Abilities:** Cover, Place of Power, Unstable

##### 1.5 陣営地形(Faction Terrain)

Some factions have special terrain features called **faction terrain features**. Faction terrain features have their own warscrolls. They are not considered to be units, with the following exceptions:

- In the combat phase, they are treated as if they were units for the purposes of movement, combat range and being in combat.
- They are affected by all enemy abilities as if they were units.
- They can be damaged in the same manner as units. However, when they are removed from play, they count as being **demolished** instead of slain or destroyed (this means that they do not count as destroyed units for the purposes of abilities, scoring battle tactics etc.).
- Enemy units can finish a charge move within ½" of a terrain feature that is **garrisoned** (see 1.5.1). Faction terrain features cannot contest objectives even while they are garrisoned.
- If a terrain feature has any melee or ranged weapons, it can use the ‘Fight’ and ‘Shoot’ **CORE** abilities as if it were a unit.
- Terrain features that have a Move characteristic of 0" (‘-’) cannot move (note that pile-in moves are a type of move).
- Faction terrain features with a Move characteristic greater than ‘-’ are treated as if they were units in all phases for the purposes of movement, combat range, being in combat and setting up terrain features, other manifestations and other units.

Some faction terrain features allow you to place a unit on them (this will be clearly specified in that terrain feature’s rules). When doing so, instead of measuring range or visibility to and from the unit that is on that terrain feature, measure to and from the terrain feature instead. Unless otherwise specified, units on a faction terrain feature cannot use **FIGHT** abilities.

If a unit placed on a terrain feature is removed from it (e.g. if an ability removes them from the battlefield), that unit counts as having left that terrain feature and loses any special role or benefits it had as a result of being placed on it.

##### 1.5.1 陣営地形の駐留(Garrisoning Faction Terrain Features)

Some faction terrain features allow you to place another unit on them using an ability on the terrain feature’s warscroll. While a faction terrain feature has another unit on it that was placed there in this way, that terrain feature is **garrisoned**.

Garrisoned terrain features can use abilities and be affected by enemy abilities, but they cannot be affected by friendly abilities other than **CORE** abilities, abilities on their warscroll and abilities that specifically affect terrain features. Any time you would measure range or visibility to or from a unit that is on a garrisoned terrain feature (including if that unit is contesting an objective), measure to and from the terrain feature instead. Unless otherwise specified, units on a faction terrain feature are not eligible to use **FIGHT** abilities.

Units cannot move while they are garrisoned on a terrain feature.

##### 1.6 特殊地形上の突撃ユニット(Charging Units on Terrain)

時として、敵ユニットが特殊地形の上に全体が入っているときに（たとえば、塔の頂上付近にいるユニット）、**『突撃』**アビリティを使用して敵ユニットに到達することができないことがある。これは、突撃ユニットが特殊地形を昇っている途中で移動を完了できず、特殊地形の上に兵を配置するために十分なスペースがないためである。このような場合、突撃ユニットは代わりに、**その特殊地形の½mv以内**で突撃を完了できる。ただし、これによって突撃ユニットが、特殊地形の上に全体が入っている敵ユニットと**近接戦闘中**になるように移動を完了できる場合に限られる。

> [!quote]- EN
> In some cases, it is not possible to reach an enemy unit using a **CHARGE** ability when they are wholly on a terrain feature (e.g. a unit on top of a tower) because the charging unit is unable to end their move mid-way up the terrain feature and there is not enough room for the models to be placed at the top. In these cases, the charging unit can end their charge within **½" of that terrain feature** instead if this would result in the charging unit ending their move **in combat** with any enemy units wholly on a terrain feature.

##### 1.7 情景(Scenery Pieces)

特殊地形の中には、森林や小さな遺跡がいくつもある、複数の**情景モデル**で構成されているものがある。同じ特殊地形の一部であるそれぞれの情景モデルは、すべてがその特殊地形のサイズに対応する範囲内に配置されなければならない（1.3参照）。いくつもの情景モデルで構成されている特殊地形は、1個の特殊地形として扱われる。

> [!quote]- EN
> Some terrain features, such as wyldwoods or collections of smaller timeworn ruins, are made up of multiple **scenery pieces**. Each scenery piece that makes up a part of the same terrain feature must be set up so that all of the scenery pieces fit into the area that corresponds to the terrain feature’s size (see 1.3). The full collection of scenery pieces is considered to be a single terrain feature.

![図](https://dhss9aar8ocw.cloudfront.net/5cbc3fd7-71d2-42ec-84b9-2137ea04390e)

この戦場ではシタデルの特殊地形が使用されているため、プレイヤーはシタデルの特殊地形リストで、各特殊地形の特徴を簡単に調べることができた。

**1** 破壊された住居（障害物）

**2** 住居外壁（障害物）

**3** 守護聖像（障害物）

**4** 浄化の聖水源（力を秘めし地形）

**5** 魔力抽出器（力を秘めし地形）

**6** 森林（射線妨害特殊地形）

> [!quote]- EN
> This battlefield uses Citadel terrain, so the players were able to simply look up the terrain type of each terrain feature in the Citadel Terrain List.
>
> **1** Ruined Domicile (Obstacle)
>
> **2** Domicile Shell (Obstacle)
>
> **3** Guardian Idol (Obstacle)
>
> **4** Cleansing Aqualith (Place of Power)
>
> **5** Nexus Syphon (Place of Power)
>
> **6** Wyldwood (Obscuring Terrain)

![図](https://dhss9aar8ocw.cloudfront.net/fe1e25c6-42a4-4cdf-8b2f-3a15e9c4646b)

2つ目の戦場は、スクラッチビルドされた特殊地形を使用している。特殊地形を配置する前に、双方のプレイヤーは次に示されるように、使用しているそれぞれの特殊地形の特徴について話し合い、合意している。

**1** 力を秘めし地形

**2** エリア地形

**3** 障害物

**4** 射線妨害特殊地形

> [!quote]- EN
> The second battlefield uses scratch-built terrain. Before setting up the terrain, both players discussed and agreed on the terrain type of each terrain feature they were using, as shown below.
>
> **1** Place of Power
>
> **2** Area Terrain
>
> **3** Obstacle
>
> **4** Obscuring Terrain

### 魔法 2026-27(Magic 2026-27)

#### 1.0 魔術師と神官(Wizards and Priests)

**魔術師**は**呪文**を詠唱できる特殊なユニットであり、**神官**は**奇蹟**を祈願できる特殊なユニットである。呪文や奇蹟は強力な**アビリティ**であり、バトルに劇的な影響を与えることができる。

> [!quote]- EN
> **WIZARDS** are special units that can cast **spells**, and **PRIESTS** are special units that can chant **prayers**. Spells and prayers are powerful **abilities** that can have a dramatic impact on the battle.

##### 1.1 パワーレベル(Power Level)

各魔術師と神官にはパワーレベルがあり、パワーレベルは魔術師（2）のようにキーワードの後に括弧内に示されている。魔術師の詠唱のパワーレベルは、フェイズごとに使用できる『呪文』アビリティの数を決めている。神官の祈願のパワーレベルは、フェイズごとに使用できる『奇蹟』アビリティの数を決めている。

> [!quote]- EN
> Each **WIZARD** and **PRIEST** has a power level shown after the keyword, e.g. **WIZARD (2)**. A **WIZARD**’s casting power level determines how many Spell abilities they can use per phase. A **PRIEST**’s chanting power level determines how many **PRAYER** abilities they can use per phase.

**複数のパワーレベル(1.1.1 Multiple Power Levels)**

- アビリティがユニットのパワーレベルを参照する際、そのユニットが複数のパワーレベルを有する場合、高い方のパワーレベルを使用する。
- アビリティがユニットのパワーレベルを修正する際、そのユニットが複数のパワーレベルを有する場合、それらすべてのパワーレベルが修正される。

> [!quote]- EN
> - If an ability references a unit’s power level and that unit has more than one power level, use whichever power level is higher.
> - If an ability modifies a unit’s power level and that unit has more than one power level, it modifies both.

#### 2.0 呪文(Spells)

各呪文の宣言手順では、**2D6**の**詠唱ロール**をするようにと記されている。詠唱ロールが呪文の**【詠唱値】**（呪文の右上隅）以上で**なければ**、その呪文は詠唱に失敗し、その効果は解決されない。詠唱ロールで**修正前の出目1が2個以上出た場合**、呪文は**暴発**する。呪文は失敗となり、その効果は解決されず、その呪文の詠唱を試みた**魔術師**は**D3ポイントの致命的ダメージ**を受ける。また、その**魔術師**はそのフェイズ中にそれ以上の呪文を使用できなくなる。

敵軍側がリアクションを使用できるのは、**詠唱ロール**が呪文の**【詠唱値】**以上であった場合のみである。詠唱された呪文が**打ち消されていない限り**（4.0参照）、その呪文は**詠唱成功**となり、その**効果**が解決される。

> [!quote]- EN
> The declare step of each spell will tell you to make a **casting roll** of **2D6**. If the roll does **not** equal or exceed the spell’s **casting value** (at the top-right corner of the spell), the spell fails and its effect is not resolved. If the unmodified casting roll includes **2 or more rolls of 1**, the spell is **miscast**: the spell fails, its effect is not resolved, **D3 mortal damage** is inflicted on the **WIZARD** that used it, and that **WIZARD** cannot use any more spells in that phase.
>
> Enemy reactions can only be used if the **casting roll** equals or exceeds the spell’s **casting value**. So long as the spell is not **unbound** (see 4.0), then it is **successfully cast**: resolve its **effect**.

#### 3.0 奇蹟(Prayers)

The declare step of each prayer will tell you to make a **chanting roll** of **D6**. On an unmodified chanting roll of **1**, the prayer fails, its effect is not resolved and you must **remove D3 ritual points** from the **PRIEST** using the prayer. Otherwise, pick one of the following:

- Give a number of **ritual points** to the **PRIEST** equal to the chanting roll (ritual points can be accumulated over multiple turns).
- You can add the **PRIEST**’s ritual points to the chanting roll. If the chanting roll equals or exceeds the prayer’s **chanting value** (at the top-right corner of the prayer), it is **answered**: resolve the **effect** of the prayer, then reset the **PRIEST**’s ritual points total to 0.

All **PRIESTS** know the following prayer:

> **神聖儀式(Sacred Rites)**（自軍側ヒーローフェイズ｜2 CP）
>
> - **宣言:** Pick a friendly **PRIEST** to use this ability, then make a **chanting roll** of D6. On an unmodified chanting roll of 1, remove 1 ritual point from that **PRIEST** instead of D3.
> - **効果:** 修正前の祈願ロール結果に等しい数の儀式ポイントを**神官**に付与する。また、**神官**が有する儀式ポイントを0にリセットしない。
> - **キーワード:** 奇蹟、無制限

> [!quote]- EN
> **Sacred Rites**（Your Hero Phase｜2 CP）
>
> *The priest focuses on safely setting their ritual into motion.*
>
> - **Declare:** Pick a friendly **PRIEST** to use this ability, then make a **chanting roll** of D6. On an unmodified chanting roll of 1, remove 1 ritual point from that **PRIEST** instead of D3.
> - **Effect:** Give a number of ritual points to the **PRIEST** equal to the unmodified chanting roll and do not reset the **PRIEST**'s ritual points total to 0.
> - **Keywords:** Prayer, Unlimited

#### 4.0 打ち消し呪文(Unbinding Spells)

各**魔術師**は、フェイズごとにその**パワーレベル**に等しい数の『打ち消し』リアクションを使用できる。これは、「一度限りのルール」（コアルール、5.3）の例外である。

> [!quote]- EN
> Each **WIZARD** can use the ‘Unbind’ reaction a number of times per phase equal to their **power level**. This is an exception to The Rules of One (Core Rules, 5.3).

> **打ち消し(Unbind)**（リアクション：敵軍側が『呪文』アビリティを宣言）
>
> *魔法使いは敵が唱えんとする呪文の力を奪い、その効果を無と化す。*
>
> - **使用者:** **呪文**の詠唱を試みようとしている、敵**魔術師**の30mv以内に一部でも入っている味方**魔術師**1体。
> - **効果:** 2D6の**打ち消しロール**をする。打ち消しロールが呪文の**詠唱ロール**を上回る場合、その呪文は**打ち消され**、その呪文の効果は解決されない。このリアクションは、**詠唱ロール**ごとに1回だけ使用できる。
> - **キーワード:** 打ち消し

> [!quote]- EN
> **Unbind**（Reaction: Opponent declared a **SPELL** ability）
>
> *The wizard saps the energy from an enemy’s spell, nullifying its effects.*
>
> - **Used By:** A friendly **WIZARD** within 30" of the enemy **WIZARD** casting the spell.
> - **Effect:** Make an **unbinding roll** of 2D6. If the roll exceeds the **casting roll** for the spell, then the spell is unbound and its effect is not resolved. This reaction cannot be used more than once per **casting roll**.
> - **Keywords:** Unbind

#### 5.0 嫉妬に満ちた魔法使いと気まぐれな神々(Jealous Mages and Fickle Gods)

最大1体の味方**魔術師**が、ターンごとに同じ呪文を1回だけ詠唱できる。例外は、その呪文が**無制限**のキーワードを持っている場合に限られる。同じように、最大1体の味方**神官**が、ターンごとに同じ奇蹟を1回だけ祈願できる。例外は、その奇蹟が**無制限**のキーワードを持っている場合に限られる。なお各ユニットは、フェイズごとに呪文または奇蹟アビリティを使用できるのは1回だけであることに注意する（「一度限りのルール」コアルール、5.3）。

> [!quote]- EN
> No more than 1 friendly **WIZARD** can cast the same spell per turn, unless that spell has the **UNLIMITED** keyword. Likewise, no more than 1 friendly **PRIEST** can chant the same prayer per turn, unless that prayer has the **UNLIMITED** keyword. Keep in mind that each unit can still only use any given spell or prayer ability once per phase (see The Rules of One, Core Rules, 5.3).

#### 6.0 習得している呪文と奇蹟(Known Spells and Prayers)

**魔術師**と**神官**は、**習得**している呪文や奇蹟しか使用できない。それぞれの**魔術師**と**神官**は、自身のウォースクロールに記されているすべての呪文や奇蹟を習得している。さらに、自軍のアーミーは必要に応じて取得している**呪文伝承**、**顕現伝承**、**奇蹟伝承**の**すべて**の呪文と奇蹟を習得している（アーミー編成参照）。

> [!quote]- EN
> **WIZARDS** and **PRIESTS** can only use spells or prayers that they know. Each **WIZARD** and **PRIEST** knows any spells or prayers on its warscroll, plus all of the spells and prayers in the spell lores, manifestation lores and prayer lores you take for your army.

#### 7.0 顕現(Manifestations)

There are two types of **manifestation: endless spells**, which can be summoned by **WIZARDS**, and **invocations**, which can be summoned by **PRIESTS**. Each manifestation has its own **warscroll**, and the **spell** or **prayer** that allows that manifestation to be summoned will be found in the appropriate **manifestation lore**. No more than 1 friendly **WIZARD** or **PRIEST** can attempt to summon the same manifestation per turn, and a friendly **WIZARD** or **PRIEST** cannot attempt to summon a friendly manifestation that was removed from play in the same turn.

Manifestations are not units but can be interacted with in similar ways, as explained next:

**All Manifestations**

Models can move through them but cannot end a move on them.

Units can finish a charge move within ½" of an enemy manifestation instead of within ½" of an enemy unit.

They can be damaged and destroyed as if they were units but do not count as destroyed units for the purposes of battle tactics and abilities.

They are affected by all enemy abilities as if they were units.

They can use **CORE** abilities as if they were units, and they can use abilities on their warscroll. Unless specified otherwise, they cannot use and are not affected by any other friendly abilities, and they do not count as units for the purposes of battle tactics or friendly abilities.

They can only use the ‘Shoot’ or ‘Fight’ abilities if they have weapons of the appropriate type.

**Manifestations With a Move Characteristic of '-'**

They cannot move.

They only count as being in combat in the combat phase, and enemy units only count as being in combat with them in the combat phase.

They cannot make shooting attacks with ranged weapons that do not have **Shoot in Combat** while there is a visible enemy unit within 3" of them.

**Manifestations With a Move Characteristic Greater Than '-'**

They are treated as if they were units for the purposes of movement, combat range, being in combat and setting up terrain features, other manifestations and other units.

##### 7.1 連結の解除(Severed Connection)

If the unit that summoned a manifestation is destroyed, that manifestation is removed from the battlefield.

##### 7.2 顕現の追放(Banishing Manifestations)

Instead of using a **SPELL** or **PRAYER** ability (including when using the ‘Magical Intervention’ ability), each **WIZARD** and **PRIEST** can use the ‘Banish Manifestation’ ability:

> **顕現の追放(Banish Manifestation)**（自軍側ヒーローフェイズ）
>
> *魔術師または神官は、顕現を保たせる神秘なる力を打ち砕き、眼前の顕現を消し去る。*
>
> - **宣言:** Pick a friendly **WIZARD** or **PRIEST** to use this ability, pick a **MANIFESTATION** within 30" of them that was not summoned this turn to be the target, then make a banishment roll of 2D6. Add 1 to the **banishment roll** for each additional enemy **MANIFESTATION** on the battlefield after the first. You cannot pick the same **MANIFESTATION** to be the target of this ability more than once per turn.
> - **効果:** **追放ロール**が顕現のウォースクロールに示されている**【追放値】**以上であれば、顕現は**追放され**、戦場から取り除かれる。
> - **キーワード:** 追放

> [!quote]- EN
> **Banish Manifestation**（Your Hero Phase）
>
> *The wizard or priest disrupts the arcane forces sustaining a manifestation, wiping it from existence.*
>
> - **Declare:** Pick a friendly **WIZARD** or **PRIEST** to use this ability, pick a **MANIFESTATION** within 30" of them that was not summoned this turn to be the target, then make a banishment roll of 2D6. Add 1 to the **banishment roll** for each additional enemy **MANIFESTATION** on the battlefield after the first. You cannot pick the same **MANIFESTATION** to be the target of this ability more than once per turn.
> - **Effect:** If the **banishment roll** equals or exceeds the banishment value listed on the **MANIFESTATION**’s warscroll, it is banished and removed from play.
> - **Keywords:** Banish

### アーミー編成 2026-27(Army Composition 2026-27)

#### アーミー編成の概要(Army Composition Overview)

![図](https://dhss9aar8ocw.cloudfront.net/8af17b77-0daf-458f-900b-b20fca05a6d0)

#### 1.0 はじめに(Getting Started)

##### 1.1 アーミーロスター(Army Roster)

These rules will explain how to create an **army roster** to prepare for a battle. You can find a blank army roster in the Generals Handbook 2025-26, or go to **warhammer‑community.com** to download a printable copy.

##### 1.2 ポイント上限(Points Limit)

Before you start filling your roster, you and your opponent must agree on a **points limit** for the battle. You can agree on any points limit, but most players use a limit of 1000 points, 2000 points or somewhere in between. If a unit, Regiment of Renown, faction terrain feature, enhancement or lore has a points value, you must spend that number of points to include it on your army roster. The total points value of the options you have picked in your army must not exceed the agreed points limit of the battle. No more than half of your points can be spent on a single unit.

##### 1.2.1 多勢に無勢(Underspending)

In many cases, the total points cost of your army will not add up to the exact points limit, but you might not have enough points left to add something else. If the points cost of your army is **50 or more points lower** than the points limit of the battle, you gain **1 extra command point at the start of the first battle round**.

##### 1.3 バトルプロフィール(Battle Profiles)

自軍のアーミ==ー==ロスターを作成するときに必要な情報は、各ユニットの**バトルプロフィール**に記載されている。各ユニットのバトルプロフィールは、warhammer-community.comに掲載されている。

> [!quote]- EN
> The information you’ll need when building your army roster is found in each unit’s **battle profile**. The battle profiles for all units are also available online at warhammer-community.com.

#### 2.0 陣営(Factions)

自軍のアーミーロスターを作成するときに最初にしなければならないことは、自軍の**陣営**（たとえば、ストームキャスト・エターナルまたはスケイヴン）を選ぶことである。

各陣営には固有ウォースクロール、バトルプロフィール、陣営ルールがある。陣営ルールはさまざまな書籍に記載されているが、最も一般的には陣営の**バトルトーム**に書き記されている。

> [!quote]- EN
> The first thing you need to do when building your army roster is to pick your **faction** (e.g. Stormcast Eternals or Skaven).
>
> Each faction has its own warscrolls, battle profiles and faction rules. These can be found in various publications but most commonly in the faction’s **battletome**.

##### 2.1 戦闘陣形(Battle Formations)

多くの陣営には1つ以上の**戦闘陣形**が含まれている。それぞれの戦闘陣形は、自軍のアーミーに独自の効果をもたらしてくれる。選んだ陣営の**陣営ルール**において、戦闘陣形の選択肢が説明されている。

> [!quote]- EN
> Many factions contain one or more **battle formations**. Each battle formation grants unique benefits to your army. The **faction rules** for your faction will explain any battle formation options.

##### 2.2 名高き軍勢(Armies of Renown)

一部の陣営は、**名高き軍勢**と呼ばれる特定のテーマに基づくアーミーを用いることができる。名高き軍勢を自軍のアーミーとして使用する場合、その名高き軍勢のルールは、そのアーミーが持つ通常の陣営ルールに置き換わる。

> [!quote]- EN
> Some factions have access to rules for themed armies called **Armies of Renown**. If you choose to use an Army of Renown, the rules for that Army of Renown replace the normal faction rules for that army.

#### 3.0 ユニットの追加(Adding Units)

##### 3.1 連隊(Regiments)

Armies are made up of one or more **regiments**, each of which is led by a Hero. You must have **at least 1** regiment in your army, and you can include a **maximum of 5** regiments. To add a regiment, pick **1** **HERO** from your faction, then pick up to **3** non‑**HERO** units to accompany them.

Each **HERO’**&#x73; battle profile lists which units can be added to their regiment, and each non-**HERO** unit’s battle profile lists any relevant keywords it has. The battle profiles of some **HEROES** may say that they can be added to the regiment of another **HERO** in place of a non-**HERO** unit in that regiment.

**正規連隊(3.1.1 Regimented Forces)**

バトル開始時、一方のプレイヤーが対戦相手より多くの連隊を有しているならば、バトル中1回限り、先制ロールで両プレイヤーのロール結果を確認した後、そのバトルラウンドでどちらが先制となるかを決定する前のタイミングで、より多くの連隊を有している方のプレイヤーは先制ロールをリロールしてもよい。

> [!quote]- EN
> If a player has more regiments than their opponent at the start of the battle, then once per battle, that player can re-roll their priority roll after seeing the result of both players’ rolls but before determining priority for that battle round.

##### 3.2 ジェネラル(The General)

You must pick 1 **HERO** in your army that is leading a regiment to be your general. If any units in your army have the **WARMASTER** keyword, you must pick one of those units to be your general and they must lead a regiment. Your general’s **regiment** can include up to **4** non‑**HERO** units in addition to your general.

##### 3.3 増強ユニット(Reinforced Units)

When you add a unit to your army roster, you can add it as a **reinforced unit**. A reinforced unit has **twice as many models** as its minimum unit size and costs **twice as many points**. If a unit has a minimum unit size of 1, it cannot be reinforced. In addition, some units with a unit size of more than 1 can not be reinforced. This will be noted on their battle profile.

##### 3.4 固有ユニット(Unique Units)

自軍のアーミーに同一の**固有**ユニットを編入できるのは1個までである。**固有**ユニットを増強ユニットにすることはできない。

> [!quote]- EN
> You cannot include the same **UNIQUE** unit more than once in your army. **UNIQUE** units cannot be reinforced.

##### 3.5 名高き連隊(Regiments of Renown)

独自の連隊を編成するだけでなく、ポイントを消費して**名高き連隊**を1個編入することもできる。名高き連隊はあらかじめ~~に~~編成されている連隊であり、それぞれが固有の特殊アビリティを持っている。それぞれの名高き連隊のルールは、どの陣営がその名高き連隊を編入できるのかを示している。名高き連隊に含まれているユニットは、それが総大将であったとしても自軍のジェネラルになることはできない。

- 連隊のバトルプロフィールに特に明記されていない限り、自軍のアーミーに編入することができる名高き連隊は1個だけである。
- 名高き連隊に属するユニットは、その陣営の名前と一致するキーワードを持っていない限り、強化や伝承を含め、同盟している陣営の陣営ルールを使用することはできない（ただし、もし他の条件を満たす場合、それらの対象として選択することはできる）。
- アビリティによって、名高き連隊に属するユニットの代替ユニット（コアルール、24.2）を配置できる場合、その代替ユニットは名高き連隊の一部としてカウントされる。

> [!quote]- EN
> In addition to creating your own regiments, you can also spend points to include 1 **Regiment of Renown**. Regiments of Renown are pre‑built regiments, each with their own special abilities. The rules for each Regiment of Renown will specify which factions can include it. A unit in a Regiment of Renown cannot be your general even if it is a **WARMASTER**.
>
> - You cannot include more than one Regiment of Renown in your army unless otherwise specified in the notes column of that regiment’s battle profile.
> - Units in a Regiment of Renown cannot use (but can be picked as the target of, if otherwise eligible) any faction rules from the faction they are allied into, including enhancements and lores, unless they have a keyword that matches that faction’s name.
> - If an ability allows you to set up a replacement unit (see Core Rules 24.2) for a unit from a Regiment of Renown, that unit also counts as being part of the Regiment of Renown.

##### 3.6 支援ユニット(Auxiliary Units)

**支援ユニット**を用いることで連隊の制限なしに陣営から任意のユニットを編入できるが、それは敵にとって有利になる可能性がある。自軍のアーミーロスターの支援ユニットには、任意の数のユニットを追加できる。しかしながら、アーミーロスターに編入されている支援ユニットの数が最も少ないプレイヤーは、**各バトルラウンドの開始時に追加の1指揮ポイント**を獲得する（プレイヤーが同じ数の支援ユニットを有する場合、どちらのプレイヤーも追加の指揮ポイントを獲得しない）。連隊オプションの制限がある英雄を支援ユニットとして編入することはできない。

自軍ロスターに追加される２つ目の支援ユニットから、支援ユニット1個につき累積する20ポイントコストが発生する。たとえば、２つ目の支援ユニットは+20ポイントコスト、３つ目は+40ポイントコスト、4つ目は+60ポイントコストと増える。

> [!quote]- EN
> **Auxiliary units** allow you to take any units from your faction without the constraints of regiments, at the cost of potentially giving your opponent an advantage. You can add any number of units to the auxiliary units section of your army roster. However, the player with the fewest auxiliary units on their roster gains **1 extra command point at the start of each battle round** (if the players have the same number of auxiliary units, neither player receives an extra command point). **HEROES** that have compulsory regiment options cannot be taken as auxiliary units.
>
> Each auxiliary unit after the first that is added to your roster will incur a cumulative surcharge of 20 points. For example, the second auxiliary unit will cost +20 points, the third will cost +40 points, the fourth will cost +60 points and so on.

##### 3.7 陣営地形(Faction Terrain Features)

自軍の陣営に**陣営地形**あるいは一組となる陣営地形がある場合は、それらの中から自軍のアーミーロスターに1つ陣営地形を編入できる。

> [!quote]- EN
> If your faction has a **faction terrain feature**, or a set of faction terrain features, you can pick 1 to include on your army roster.

#### 4.0 最後の仕上げ(Finishing Touches)

##### 4.1 強化(Enhancements)

陣営ルールの各セットには、ユニットに付与できる多くの**強化**が存在する。たとえば、**英雄特性**、**神器**などである。自軍の**陣営ルール**に記されている**それぞれ**の強化表から、**強化を1個**取得できる。それぞれの強化表には、その強化を取得できるユニットが一覧で示されている。**固有**ユニットは強化を取得することはできない。

アビリティの中には、追加の強化を取得可能にするものもあるが、同一のユニットは同じタイプの強化を最大1個までしか取得することができない。また、アーミーは同じ強化を最大1個までしか取得することができない。名高き連隊ユニットが陣営の名前と同じキーワードを持っていない限り、その名高き連隊ユニットに対して強化を与えることはできない。

> [!quote]- EN
> Each set of faction rules include a number of **enhancements** that can be given to units, e.g. **heroic traits** and **artefacts of power**. You can take **1 enhancement** from **each** enhancement table in your **faction rules**. Each enhancement table lists which units are eligible to be given that enhancement. **UNIQUE** units cannot be given enhancements.
>
> While some abilities allow you to take extra enhancements, the same unit can never have more than 1 enhancement of the same type, and you can never include the same enhancement in your army more than once. Enhancements cannot be given to Regiment of Renown units unless they have a keyword that matches that faction’s name.

##### 4.2 伝承(Lores)

You can pick 1 **spell lore** available to your faction. If you do, **all** **WIZARDS** in your army with the same faction keyword as your general know **all** spells from that lore.

You can pick 1 prayer lore available to your faction. If you do, **all** **PRIESTS** in your army with the same faction keyword as your general know **all** prayers from that lore.

You can pick 1 **manifestation lore** available to your faction. If you do, **all WIZARDS** in your army know **all** spells from that lore, and **all** **PRIESTS** in your army know **all** prayers from that lore.

##### 4.3 戦術目標カード(Battle Tactics Cards)

You can pick up to 2 battle tactics cards from the Battle Tactics 2026‑27 module for your army. Make a note of these battle tactics in the appropriate section on your army roster.

### 特殊兵 2026-27(Command Models 2026-27)

#### 1.0 豪傑(Champions)

**豪傑**のキーワードを持つユニットには、**豪傑**・兵が1体以上いる。**豪傑**のキーワードの後に数字がある場合、その数字は、そのユニット内で豪傑になってもよい兵の割合を示している。それ以外の場合は、ユニット内にいる1体の兵が豪傑になることができる。**豪傑**のキーワードを持つユニットは、次のパッシブアビリティを得る：

> [!quote]- EN
> Units with the **CHAMPION** keyword have one or more **champion** models. If there is a number after the **CHAMPION** keyword, that number indicates the proportion of models in that unit that can be champions. In any other case, 1 model in the unit can be a champion. Units with the **CHAMPION** keyword have the following passive ability:

> **豪傑(Champion)**（パッシブ）
>
> *古参戦士が先頭に立って戦う。*
>
> - **効果:** Add 1 to the **Attacks** characteristic of weapons used by champions in this unit. If this unit is a **BEAST**, this ability affects this unit’s **Companion** weapons.

> [!quote]- EN
> **Champion**（Passive）
>
> *A veteran fighter leads the charge.*
>
> - **Effect:** Add 1 to the **Attacks** characteristic of weapons used by champions in this unit. If this unit is a **BEAST**, this ability affects this unit’s **Companion** weapons.

> ユニットのキーワード欄に**豪傑（1/10）**が記されている場合、ユニット内の兵10体につき、そのうちの1体を豪傑にすることができる。

> [!quote]- EN
> If a unit had **CHAMPION (1/10)** on its keywords bar, then 1 model in that unit could be a champion for every 10 models in the unit.

#### 2.0 楽士(Musicians)

**楽士**のキーワードを持つユニットには、**楽士**・兵が1体以上いる。**楽士**のキーワードの後の数字は、そのユニット内で楽士になってもよい兵の割合を示している。**楽士**のキーワードを持つユニットは、次のパッシブアビリティを得る：

> [!quote]- EN
> Units with the **MUSICIAN** keyword have one or more **musician** models. The number after the **MUSICIAN** keyword indicates the proportion of models in that unit that can be musicians. Units with the **MUSICIAN** keyword have the following passive ability:

> **楽士(Musician)**（パッシブ）
>
> *太鼓や角笛の音によって鼓舞された兵士たちは、前へ前へとひたすら突き進む。*
>
> - **効果:** このユニット内に楽士が1体以上いる間、そのユニットが『再集結』アビリティを使用した場合、D6の**再集結ロール**を追加で1個ロールできる。

> [!quote]- EN
> **Musician**（Passive）
>
> *The beat of a drum or the blast of a horn drives the soldiers ever onward.*
>
> - **Effect:** While this unit contains any musicians, if it uses the ‘Rally’ command, you can make one additional **rally roll** of D6.

> ミニチュアを見て豪傑、楽士、旗手がはっきりしない場合は、ユニット内のどの兵がそうであるのかを対戦相手に知らせる。

> [!quote]- EN
> Let your opponent know which models in a unit are champions, musicians and standard bearers if it’s not already clear from the miniatures.

#### 3.0 旗手(Standard Bearers)

**旗手**のキーワードを持つユニットには、**旗手**・兵が1体以上いる。**旗手**のキーワードの後の数字は、そのユニット内で旗手になってもよい兵の割合を示している。**旗手**のキーワードを持つユニットは、次のパッシブアビリティを得る：

> [!quote]- EN
> Units with the **STANDARD BEARER** keyword have one or more **standard bearer** models. The number after the **STANDARD BEARER** keyword indicates the proportion of models in that unit that can be standard bearers. Units with the **STANDARD BEARER** keyword have the following passive ability:

> **旗手(Standard Bearer)**（パッシブ）
>
> *戦闘の混乱の中で、掲げられし旗は部隊盛り返しの場となる。*
>
> - **効果:** このユニット内に旗手が1体以上いる間、このユニットの**確保スコア**は+1の修正を受ける。

> [!quote]- EN
> **Standard Bearer**（Passive）
>
> *The unit’s standard provides a rallying point in the chaos of battle.*
>
> - **Effect:** While this unit contains any standard bearers, add 1 to this unit’s **control score**.

### 補遺、エラッタ、多く寄せられた質問(Addenda, Errata and FAQs)

#### エラッタ(Errata)

下記に記載されているルールのアップデートは、曖昧さや意図しない影響を回避したりするために間違いが更新されている。

> [!quote]- EN
> The following rules updates correct errors in order to clarify ambiguities and/or avoid unintended interactions.

##### アーミー編成 2026-27, 3.6 支援ユニット(Army Composition 2026-27, 3.6 Auxiliary Units)

このセクションの最後に以下を追加する：

“自軍ロスターに追加される２つ目の支援ユニットから、支援ユニット1個につき累積する20ポイントコストが発生する。たとえば、２つ目の支援ユニットは+20ポイントコスト、３つ目は+40ポイントコスト、4つ目は+60ポイントコストと増える。”

> [!quote]- EN
> Add the following to the end of this section:
>
> ‘Each auxiliary unit after the first that is added to your roster will incur a cumulative surcharge of 20 points. For example, the second auxiliary unit will cost +20 points, the third will cost +40 points, the fourth will cost +60 points and so on.’

#### 多く寄せられた質問(Frequently Asked Questions)

この質問と回答のシリーズでは、ルール執筆チームがプレイヤーから寄せられた質問に答え、ルールがどのように使用されることを意図しているかを説明する。

> [!quote]- EN
> In this series of questions and answers, the rules-writing team respond to players’ queries and explain how the rules are intended to be used.

##### 魔法、2.0 呪文(Magic,2.0 Spells)

*Q: 暴発によって与えられた致命的ダメージは『呪文』アビリティによって与えられたことになるの？　たとえば、モルガスト・アルカイのユニットによる『黒檀色の甲冑』アビリティなどの効果に関連して？*

A: ならない。

> [!quote]- EN
> Q: *Is mortal damage inflicted by a miscast considered to be ‘mortal damage inflicted by a **SPELL** ability’ for the purposes of abilities like a Morghast Archai unit’s ‘Ebon-wrought Armour’ ability?*
>
> A: No.

##### アーミー編成、3.1 連隊(ARMY COMPOSITION, 3.1 REGIMENTS)

*Q: 英雄が別の英雄が率いる連隊に加わることができる場合（たとえば、シャドウクイーンがモラスィ＝カインの連隊に加わる）、その英雄は連隊の中では英雄ではないユニット~~として扱われる~~==の枠を使う==の？*

A: その通りだ。

> [!quote]- EN
> Q: *If a **HERO** is able to join another **HERO**'s regiment (e.g. The Shadow Queen joining Morathi-Khaine, do they take the place of a non-**HERO** unit in that regiment?*
>
> A: Yes.

##### アーミー編成、4.1 強化(ARMY COMPOSITION, 4.1 ENHANCEMENTS)

*Q: アビリティによってバトル中に強化を獲得できる際（たとえば、カラドロン・オーヴァーロードの『特殊な軍事調達』アビリティ）、ポイントコストを必要とする強化を選んだ場合、自軍のアーミーロスターにその強化に必要なポイントを持っていなければならないの？*

A: いいえ、持っていなくてもよい。バトル中に追加される強化はポイントコストを必要としない。

> [!quote]- EN
> Q: *If an ability allows a unit to gain an enhancement during a battle (for example, the Kharadron Overlords ‘Special Procurement’ ability) and I pick an enhancement that costs points, do I need to have sufficient spare points in my army roster in order to pay for that enhancement?*
>
> A: No. Enhancements added to your army during a battle do not cost any points.
