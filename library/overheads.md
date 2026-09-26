# 오버헤드 · 쿨다운 알림

두 설정 파일과 스크립트의 `overhead` 를 **한 컨벤션**으로 다룬다. 같은 사건은 쿨다운 바 하나 + 오버헤드 한 줄이 짝이고,
둘은 **같은 단어**를 쓴다. 바가 뜨면 어느 오버헤드 짝인지 바로 안다.

| 어디 | 무엇 |
|---|---|
| `config/<이름>/classicuo/<캐릭>/cooldowns.xml` | 시스템 메시지로 시작하는 타이머 바. 스크립트가 `cooldown "이름"` 으로 읽는다 |
| `config/<이름>/razor/profiles/<프로필>.xml` 의 `<overheadmessages>` | 시스템 메시지를 머리 위 한 줄로 바꿔 띄운다 |
| `script/**/*.razor` 의 `overhead "..."` | 스크립트가 직접 띄우는 줄 |

설정 파일 둘은 **게임을 끈 상태에서만 고친다.** 종료할 때 클라이언트가 통째로 덮어쓴다.

## 형식 — `[ 대상, 상태 ]`

| 규칙 | 내용 |
|---|---|
| 형태 | `[ 대상, 상태 ]`. 전부 소문자, 대괄호 안쪽 공백 한 칸, 쉼표 뒤 공백 한 칸. 느낌표 · 마침표 · 대문자 강조 없음. 심각도는 hue 가 말한다 |
| 대상 | 아래 글로서리 단어. 없으면 온전한 단어. 줄임말은 **말로 할 때도 줄이는 것만** (`hams` `teleki` `inst` `explo` `eb` …). `magic arrow` `fireball` `lightning` 은 안 줄인다 |
| 상태 | 아래 어휘. 드문 상태는 한 단어 |
| 시전 알림 | `[ blood oath ]` 처럼 **대상만**. hue 44 / 83 이 "지금 나간다" 를 말하므로 상태가 필요 없다 |
| 값 | 서버 문장의 n 번째 단어는 `{n}` 으로 그대로 넣는다: `[ unholy, {4} ]`. 스크립트 변수는 `{{var}}` |
| 폭 | 대괄호 포함 **18자 목표, 22자 상한.** 넘으면 대상을 줄인다 (`No Longer Paralyzed` → `[ para, off ]`) |
| 구분 | 서버 문장은 절대 `[` 로 시작하지 않는다. 대괄호가 곧 "커스텀" 표시다 |
| 쿨다운 바 이름 | 같은 단어, **대괄호 없이**. 방향이 있을 때만 쉼표: `hams, me` / `teleki, target`. 그 외는 한 단어: `music` `heal pot` |

## 상태 어휘

| 뜻 | 단어 | 예 |
|---|---|---|
| 상대가 나에게 | `me` | `[ hams, me ]` `[ teleki, me ]` `[ disarm, me ]` |
| 내가 상대에게 걸림 | `target` | `[ hams, target ]` `[ teleki, target ]` `[ bleed, target ]` |
| 내 시도 실패 | `miss` | `[ hams, miss ]` `[ disco, miss ]` `[ lock, miss ]` |
| 잘못된 것 | `wrong` | `[ inst, wrong ]` `[ steal, wrong ]` |
| 쿨 끝 · 할 수 있음 | `ready` | `[ str, ready ]` `[ hide, ready ]` `[ fireball, ready ]` |
| 켜짐 · 진행 중 | `on` | `[ para, on ]` `[ guard, on ]` `[ bank safe, on ]` |
| 풀림 · 아직 안 됨 | `off` | `[ para, off ]` `[ stealth, off ]` `[ guard, off ]` |
| 다 떨어짐 · 없음 | `out` | `[ pouch, out ]` `[ inst, out ]` `[ range, out ]` |
| 들어오는 중 | `coming` | `[ heal, coming ]` `[ world, coming ]` |
| 골라라 (프롬프트) | `pick` | `[ inst, pick ]` `[ shelf, pick ]` |
| 저장됨 | `set` | `[ target, set ]` `[ var, set ]` `[ chest, set ]` |
| 끝남 | `done` | `[ lock, done ]` `[ loadout, done ]` |
| 시전이 끊김 | `disturbed` / `cut` | `[ heal, disturbed ]` (서버가 끊음) / `[ curse, cut ]` (힐하려고 내가 끊음) |
| 수량 · 초 | 숫자 | `[ stealth, 3 ]` `[ mush, {5} ]` `[ planted, 2s ]` `[ murder, +1 ]` |
| 드문 상태 | 한 단어 | `full` `over` `free` `blocked` `near` `slow` `clear` `deadly` `lethal` `refund` `charged` `extended` `moved` `worn` `back` `take` `skip` `dropped` |

`target` 은 방향에만 쓴다. "찍어라" 는 `pick`.

## 글로서리 (대상)

| 뜻 | 단어 | 뜻 | 단어 | 뜻 | 단어 |
|---|---|---|---|---|---|
| hamstring | `hams` | telekinesis | `teleki` | paralyze | `para` |
| instrument | `inst` | explosion | `explo` | energy bolt | `eb` |
| discordance / provocation | `disco` / `provo` | peacemaking | `peace` | barding song | `song` |
| greater heal | `gheal` | mana drain / vampire | `drain` | meditation | `medi` |
| magic mushroom | `mush` | criminal | `crim` | veterinary | `vet` |
| herbal poultice | `herb` | herding | `herd` | invisibility | `invis` |
| chain lightning | `chain` | meteor swarm | `meteor` | teleport | `tp` |
| str / agi / resist 포션 | `str` `agi` `resist` | heal / cure 포션 | `heal pot` `cure pot` | refresh 포션 | `refresh` |
| explosion 포션 | `explo pot` | 나에게 붙은 폭탄 | `bomb` | trapped pouch | `pouch` |
| smoke bomb | `smoke` | reagent satchel | `reg satchel` | alchemists satchel | `alch satchel` |
| identification wand | `id wand` | necromancy book | `necro book` | reactive armor | `reactive` |
| 그 외 | 온전한 단어 | | | | |

`heal` `cure` 는 주문이라 포션은 `heal pot` `cure pot`. 힘·민·레지는 주문을 안 쓰니 `str` `agi` `resist` 그대로.

## hue 팔레트

| hue | 뜻 | XML | 스크립트 |
|---|---|---|---|
| 33 | 위험 — 나에게 걸린 것, 없으면 못 싸우는 것 | `[ para, on ]` `[ hams, me ]` `[ pouch, out ]` | 에러, 못 찾음 (`[ inst, out ]`) |
| 43 | 경고 — 실패 · 막힘 · 재고 없음 | `[ hams, miss ]` `[ field, out ]` | 경고 (`[ heal pot, out ]` `[ heal, disturbed ]`) |
| 53 | 정보 · 카운터 · 진행 | `[ unholy, {4} ]` `[ medi, on ]` | 상태, 정보. `config__chatty` 로 끔 |
| 55 | 프롬프트 | `[ rope, pick ]` `[ herd, pick ]` | `[ inst, pick ]` `[ shelf, pick ]` |
| 68 | 준비됨 · 내 것 성공 | `[ str, ready ]` `[ lock, done ]` | `[ hide, ready ]` |
| 65 | 해제 — 나쁜 게 풀림 | `[ para, off ]` `[ poison, off ]` | — |
| 63 | 내 공격이 먹힘 | `[ hams, target ]` `[ bleed, target ]` | — |
| 93 | 아군 · 파티 | `[ heal, coming ]` `[ party, on ]` | — |
| 44 | 능력 · 네크로 시전 | — | `[ blood oath ]` `[ pummel ]` |
| 83 | 매저리 시전 | — | `[ drain ]` `[ curse ]` |
| 9 | 월드 이벤트 | `[ world, saving ]` `[ boss, {7} ]` | — |

hue 번호는 이 뜻으로 이미 쓰이고 있던 값을 골랐다. 실제 색은 게임에서 본다.

## 쿨다운 바

- 이름은 소문자 글로서리 단어. 방향이 있을 때만 `, me` / `, target` / `, immune` / `, on`.
- `cooldownbartype="Criminal"` 과 `"PvP"` 는 **클라이언트가 서버 타이머로 직접 채우는 특수 바**다. 트리거를 달지 않는다.
  Heat of Battle 은 `pvp` 바가 그 자리다.
- 자기한테 TK 를 걸면 `teleki, target` 과 `teleki, me` 가 둘 다 뜬다. 서버가 시전자 문장과 대상 문장을 둘 다 보내므로 맞는 동작이다.
- `reflect` 바는 "Magic reflect removed." 로 시작하는 30초, 서버의 재시전 잠금 그대로다. 자기 주문으로 없애면
  "You remove your magic reflect spell." 이 한 줄 더 오는데 그건 트리거가 아니다.
- 스크립트가 읽는 이름은 `cooldown "이름"` 과 **정확히 일치**해야 한다. 바를 다시 이름 바꿀 때는 `grep -rn 'cooldown "' script/` 부터.

### 바 이름표 (2026-09-26 이전 → 지금)

| 이전 | 지금 |
|---|---|
| `Skill` | `skill` |
| `Music` | `music` |
| `Discord` | `disco` |
| `Peace/Provo` | `peace/provo` |
| `Song` | `song` |
| `Magic Arrow` | `magic arrow` |
| `Harm` | `harm` |
| `Fireball` | `fireball` |
| `Lightning` | `lightning` |
| `Mushroom` | `mush` |
| `Heal Potion` | `heal pot` |
| `Steal` | `steal` |
| `Hiding` | `hide` |
| `Stealth` | `stealth` |
| `Void Mana` | `void mana` |
| `Void Health` | `void health` |
| `Swing Stage 1` | `swing 1` |
| `Swing Stage 2` | `swing 2` |
| `Swing Stage 3` | `swing 3` |
| `Swing Stage 4` | `swing 4` |
| `Meditate` | `medi` |
| `Pain Spike` | `pain spike` |
| `Necrosis` | `necrosis` |
| `Hamstring Out` | `hams, target` |
| `Hamstring On Me` | `hams, me` |
| `Hamstring Immune` | `hams, immune` |
| `Disarm Out` | `disarm, target` |
| `N.Sacrifice` | `noble sacrifice` |
| `H.Light` | `holy light` |
| `Aspect` | `aspect` |
| `P.Strike` | `poison strike` |
| `Curse` | `curse` |
| `Chain Lightning` | `chain` |
| `Meteor Swarm` | `meteor` |
| `Mass Curse` | `mass curse` |
| `Boarding` | `boarding` |
| `Combatish` | `sea combat` |
| `Repair` | `repair` |
| `Spyglass` | `spyglass` |
| `Cannons` | `cannons` |
| `Mana Vampire` | `drain` |
| `Herding` | `herd` |
| `Rope` | `rope` |
| `Tick` | `control points` |
| `TK Out` | `teleki, target` |
| `TK On Me` | `teleki, me` |
| `Paralyzed` | `para` |
| `Detonate` | `detonate` |
| `Reflect` | `reflect` |
| `Fish` | `fish` |
| `S.P.KEG` | `sp keg` |
| `Defensive` | `defensive` |
| `Sunder` | `sunder` |
| `Cleave` | `cleave` |
| `Wild Swing` | `wild swing` |
| `Shield Bash` | `shield bash` |
| `Warding` | `warding` |
| `Testudo` | `testudo` |
| `Mirror` | `mirror` |
| `Bulwark` | `bulwark` |
| `Arcane` | `arcane` |
| `Fowling` | `fowling` |
| `Incendiary` | `incendiary` |
| `Longshot` | `longshot` |
| `Maiming` | `maiming` |
| `Walk` | `walk` |
| `Explosion Potion` | `explo pot` |
| `Bandage` | `bandage` |
| `PvP Timer` | `pvp` |
| `Crim Timer` | `crim` |
| `Divine Fury` | `divine fury` |
| `Noble Sacrifice` | `(삭제, 이름만 다른 중복)` |
| `Holy Light` | `(삭제, 이름만 다른 중복)` |
| `Shrine Event` | `shrine` |
| `Sticky Pot` | `bomb, target` |
| `Contested` | `contested` |
| `Eject` | `eject` |
| `CCC` | `corpse creek` |
| `VIP Arrived` | `vip` |
| `DFP` | `flashpoint` |
| `F.CARAVAN` | `caravan` |
| `IDOC` | `idoc` |
| `Dock` | `dock` |
| `Smoke Bomb` | `smoke` |
| `Backstab` | `backstab` |
| `Reveal Timer` | `reveal` |
| `Taunt` | `taunt` |
| `Fortify Rati` | `fortify rations` |
| `Negate Time` | `negate time` |
| `Rune Timer` | `rune` |
| `Summon Timer` | `summon` |
| `Frost CD` | `frost` |
| `Frost Up` | `frost, on` |
| `Weapon Swing` | `weapon swing` |
| `ConsWeapon` | `consecrate weapon` |
| `Pedestal` | `pedestal` |
| `Bank Access` | `bank note` |
| `Panacea` | `panacea` |
| `Shoot` | `shoot` |
| `Spam Timer` | `spam` |
| `Crew Heal` | `crew heal` |
| `Quest Timer` | `quest` |
| `Omni Potion` | `omni pot` |
| `Ability` | `ability` |
| (신설) | `corpse skin` — backstab-mugging 이 `cooldown "corpse skin"` 으로 직접 세운다 |

## 오버헤드 표 (Razor 프로필 두 개, 같은 내용)

서버 문장(검색어) → 메시지. `default.xml` 에는 던지기 8줄이 없고 붕대 1줄이 더 있다.

| 서버 문장 | 이전 | 지금 (hue) |
|---|---|---|
|  : Attempting to heal you. | `[ - HEAL COMING - ]` | `[ heal, coming ] (93)` |
| You do not have a full suit of armor | `[ - Armor Missing.. - ]` | `[ armor, out ] (43)` |
| Now tracking | `Tracking ALERT ! {3} {4} {5}` | `[ track, {3} {4} {5} ] (53)` |
| spaces to target | `Tracking! {3} {4} {5}` | `[ track, {3} {4} {5} ] (53)` |
| You search the home and find no one hiding within. | `[ - CLEAR - ]` | `[ house, clear ] (68)` |
| script variable updated | `[ - Var SET - ]` | `[ var, set ] (53)` |
| Your attack hamstrings your target | `2-1 DROP` | `[ hams, target ] (63)` |
| There's not enough wood here to harvest. | `NO WOOD` | `[ wood, out ] (43)` |
| you notice | `[ - THIEF - ]` | `[ thief, me ] (33)` |
| you have already used the maximum | `[ - MAX FIELD - ]` | `[ field, out ] (43)` |
| You have been poisoned! | `[ - Poisoned! - ]` | `[ poison, on ] (33)` |
| You have been cured of all poisons. | `[ - Cured - ]` | `[ poison, off ] (65)` |
| You have been cured of all poisons! | `[ - Cured! - ]` | `[ poison, off ] (65)` |
| You are already at full health. | `[ - Full Health! - ]` | `[ hits, full ] (53)` |
| You increase your damage resistance to creature-casted spells | `[ - Drinking MR Potion -]` | `[ resist, on ] (53)` |
| You cannot move! | `[ - You are Paralyzed! - ]` | `[ para, on ] (33)` |
| You can move! | `[ - No Longer Paralyzed! - ]` | `[ para, off ] (65)` |
| seconds before you may use another strength potion. | `[ - Can't use Str Pot - ]` | `[ str, off ] (43)` |
| seconds before you may use another agility potion. | `[ - Can't use Agi Pot - ]` | `[ agi, off ] (43)` |
| you are already at full stamina. | `[ - TR Not Needed - ]` | `[ stam, full ] (53)` |
| You are not poisoned. | `[ - Not Poisoned! - ]` | `[ poison, off ] (53)` |
| You may now use a strength potion. | `[ - Str Pot is Ready - ]` | `[ str, ready ] (68)` |
| You may now use an agility potion. | `[ - Agi Pot is Ready - ]` | `[ agi, ready ] (68)` |
| Looting this corpse will be a criminal act! | `[ - Looting Is A Crime! - ]` | `[ loot, crim ] (43)` |
| Looting this monster corpse will be a criminal act! | `[ - Looting is a Crime! - ]` | `[ loot, crim ] (43)` |
| You are now a criminal. | `[ - Criminal! - ]` | `[ crim, on ] (33)` |
| You have been reported for a murder! | `+1 Murder Count` | `[ murder, +1 ] (33)` |
| You summon an ancient | `[ - Ancient Summoned - ]` | `[ ancient, on ] (68)` |
| Your spellbook generates mana for your spell. | `[ - You Regen Mana - ]` | `[ mana, refund ] (53)` |
| You fail to ignite the campfire. | `[ - Remake Campfire - ]` | `[ camp, miss ] (43)` |
| Your campfire is now secure. | `[ - Camp Secure - ]` | `[ camp, on ] (68)` |
| You feel it would take a few moments to secure your camp. | `[ - Securing Camp! - ]` | `[ camp, coming ] (53)` |
| You enter a meditative trance. | `[ - Meditating.. - ]` | `[ medi, on ] (53)` |
| Your concentration is disturbed, thus ruining thy spell. | `[ - Interrupted - ]` | `[ cast, disturbed ] (43)` |
| Being perfectly rested, you shove something invisible out of the way. | `[ - Reveal Here! - ]` | `[ hidden, near ] (43)` |
| You may now attempt to | `[ - Hamstring: Ready - ]` | `[ hams, ready ] (68)` |
| You refrain from making hamstring attempts. | `[ - Hamstring: OFF - ]` | `[ hams mode, off ] (53)` |
| You will now attempt to hamstring your opponents. | `[ - Hamstring: ON - ]` | `[ hams mode, on ] (53)` |
| You fail to hamstring your opponent. | `[ - Failed Hamstring - ]` | `[ hams, miss ] (43)` |
| Their attack hamstrings you! | `[ - HAMSTRUNG! - ]` | `[ hams, me ] (33)` |
| You are no longer hamstrung | `[ - No Longer Hamstrung! - ]` | `[ hams, off ] (65)` |
| You will now attempt to disarm your opponents. | `[ - Disarm: ON - ]` | `[ disarm mode, on ] (53)` |
| You refrain from making disarm attempts. | `[ - Disarm: OFF - ]` | `[ disarm mode, off ] (53)` |
| Your strike disarms your target! | `[ - TARGET DISARMED - ]` | `[ disarm, target ] (63)` |
| You fail to disarm your opponent. | `[ - FAILED Disarm - ]` | `[ disarm, miss ] (43)` |
| Their attack disarms you! | `[ - DISARMED! - ]` | `[ disarm, me ] (33)` |
| Where do you wish to traverse to? | `[ - Using Rope! - ]` | `[ rope, pick ] (55)` |
| That location is blocked. | `[ - Location Blocked! - ]` | `[ spot, blocked ] (43)` |
| Target cannot be seen. | `[ - Out of Range! - ]` | `[ range, out ] (43)` |
| You are now under the protection of the town guards. | `[ - In Guardzone! - ]` | `[ guard, on ] (53)` |
| You have left the protection of the town guards. | `[ - Left Guardzone! - ]` | `[ guard, off ] (43)` |
| Someone tried to steal from you. | `[ - There is a Thief! - ]` | `[ thief, me ] (33)` |
| You have been revealed! | `[ - You were REVEALED! - ]` | `[ reveal, me ] (33)` |
| You have been banned from this house. | `[ - Banned from House! - ]` | `[ ban, me ] (43)` |
| You have been ejected from this house! | `[ - Ejecting! - ]` | `[ eject, me ] (43)` |
| You have been added to the party. | `[ - Joined Party! - ]` | `[ party, on ] (93)` |
| You have been removed from the party. | `[ - Left Party! - ]` | `[ party, off ] (93)` |
| You feel ready to continue stealthing | `[ - STEALTH READY - ]` | `[ stealth, ready ] (68)` |
| You feel comfortable enough to begin stealthing | `[ - Start Stealthing - ]` | `[ stealth, ready ] (68)` |
| You have 5 stealth steps remaining | `[ - 5 STEPS LEFT! - ]` | `[ stealth, 5 ] (53)` |
| You have 3 stealth steps remaining | `[ - 3 STEPS LEFT!! - ]` | — |
| You have 1 stealth steps remaining | `[ - 1 STEPS LEFT!!! - ]` | — |
| You have successfully cleared it of traps | `[ - Removed Traps - ]` | `[ trap, done ] (68)` |
| You successfully pick the lock | `[ - Chest DONE - ]` | `[ lock, done ] (68)` |
| You fail to make any progress on the lock | `[ - Failed L/P - ]` | `[ lock, miss ] (43)` |
| You fail to make any progress towards removing traps | `[ - Failed R/T - ]` | `[ trap, miss ] (43)` |
| You finish using veterinary supplies | `[ - Vet Finished - ]` | `[ vet, done ] (68)` |
| You begin using veterinary supplies | `[ - Vet Started - ]` | `[ vet, on ] (53)` |
| What do you wish to focus your follower's aggression towards? | `[ - Herd Target - ]` | `[ herd, pick ] (55)` |
| you extend the life of your creature | `[ - Extend Life - ]` | `[ summon, extended ] (53)` |
| you are now under the effect of herbal poultice | `[ - Herbal Effect: ON - ]` | `[ herb, on ] (53)` |
| Your herbal poultice has lost its effectiveness. | `[ - Herbal Effect: OFF - ]` | `[ herb, off ] (43)` |
| That spell is already currently in effect. | `[ - Already Active - ]` | `[ buff, on ] (53)` |
| already at full repair | `[ - Repair DONE - ]` | `[ repair, done ] (53)` |
| You may now use another magic mushroom | `[ - Mushroom Ready ! - ]` | `[ mush, ready ] (68)` |
| before you may consume another magic mushroom | `Mushroom: {5}` | `[ mush, {5} ] (53)` |
| One of more of your ship crewmembers | `[ - CREW READY UPG ! - ]` | `[ crew, ready ] (68)` |
| Criminal healing will now be allowed | `[ - Crim Heal ON - ]` | `[ crim heal, on ] (53)` |
| Criminal healing will now be prevented | `[ - Crim Heal OFF - ]` | `[ crim heal, off ] (53)` |
| Criminal looting will now be allowed | `[ - Loot ON - ]` | `[ crim loot, on ] (53)` |
| Criminal looting will now be prevented | `[ - Loot OFF - ]` | `[ crim loot, off ] (53)` |
| Your lightning spell hinders your target | `[ - HINDER - ]` | `[ hinder, target ] (63)` |
| MagicResist skillgain | `!!! INCOMING !!!` | `[ spell, me ] (33)` |
| Your attack cripples your target, lowering their defense | `[ - Target CRIPPLED! - ]` | `[ cripple, target ] (63)` |
| You smash through | `[ - Target SMASHED! - ]` | `[ smash, target ] (63)` |
| susceptible to special | `[ - Target BLEEDING! - ]` | `[ bleed, target ] (63)` |
| armslore skillgain | `SWING!` | `[ swing ] (53)` |
| attack causes your target to bleed | `[ - TARGET BLEEDING - ]` | `[ bleed, target ] (63)` |
| must wait another | `[ - WAIT {5}s - ]` | `[ wait, {5}s ] (43)` |
| 0 Trapped pouches remain | `[ - Out of TPs! - ]` | `[ pouch, out ] (33)` |
| No trapped pouches found | `[ - Out of TPs! - ]` | `[ pouch, out ] (33)` |
| restricted from performing aggressive | `[ - RESTRICTION {14} - ]` | `[ restrict, {14} ] (33)` |
| world will save | `[ - World Save Comin.. - ]` | `[ world, coming ] (9)` |
| world is saving | `[ - WORLD SAVE - ]` | `[ world, saving ] (9)` |
| save complete | `[ - WS DONE! - ]` | `[ world, done ] (9)` |
| aspect and other bonuses return | `[ - ASPECT RETURNS - ]` | `[ aspect, on ] (68)` |
| free cure potion | `[ - FREE-CURE-POT - ]` | `[ cure pot, free ] (53)` |
| too fatiqued | `[ - OVERWEIGHT - ]` | `[ weight, over ] (43)` |
| too fatigued | `[ - OVERWEIGHT - ]` | `[ weight, over ] (43)` |
| are overloaded | `[ - OVERLOADED - ]` | `[ weight, over ] (43)` |
| contested boss has spawned | `[ - CONTESTED BOSS IN {7} - ]` | `[ boss, {7} ] (9)` |
| control points earned for current beacon | `+{2} points {12}` | `[ beacon, +{2} {12} ] (53)` |
| kill points earned | `[ - +{2} points {9} - ]` | `[ kill, +{2} {9} ] (53)` |
| DF A Dungeon Flashpoint will begin in 15 minutes. | `[ - FP Comin - ]` | `[ flashpoint, coming ] (9)` |
| cured the target of all poisons | `[ - Target CURED! - ]` | `[ cure, target ] (68)` |
| wizardry magic arrow | `[ - Magic Arrow Ready! - ]` | `[ magic arrow, ready ] (68)` |
| wizardry harm | `[ - Harm Ready! - ]` | `[ harm, ready ] (68)` |
| wizardry fireball | `[ - Fireball Ready! - ]` | `[ fireball, ready ] (68)` |
| wizardry lightning | `[ - Lightning Ready! - ]` | `[ lightning, ready ] (68)` |
| wizardry chain | `[ - Chain Light Ready! - ]` | `[ chain, ready ] (68)` |
| wizardry meteor | `[ - Meteo Swo Ready! - ]` | `[ meteor, ready ] (68)` |
| upgraded to Deadly | `[ - DEADLY Poi - ]` | `[ poison, deadly ] (63)` |
| upgraded to Lethal | `[ - LETHAL Poi - ]` | `[ poison, lethal ] (63)` |
| Triggered (Epic) | `[ - ASPECT ACTIVATED! - ]` | `[ aspect, on ] (68)` |
| enough experience to upgrade | `[ - Aspect UPGRADE! - ]` | `[ aspect, upgrade ] (53)` |
| Society Job Progress | `Soci: {4}` | `[ society, {4} ] (53)` |
| You have completed a society job | `[ - Society DONE! - ]` | `[ society, done ] (68)` |
| aspect experience | `{4}: {7}` | `[ {4}, {7} ] (53)` |
| resist a bleed | `[ - BLEED RESISTED! - ]` | `[ bleed, off ] (65)` |
| resist a disease effect | `[ - Disease RESISTED! - ]` | `[ disease, off ] (65)` |
| been struck by an ancient blight | `[ - HEAVY DISEASE! - ]` | `[ disease, on ] (33)` |
| may now review results | `[ - Boss Results Available! - ]` | `[ boss, done ] (53)` |
| struck by an evil omen | `[ - Omen Damage - ]` | `[ omen, target ] (63)` |
| enough unholy | `[ - Insufficient Unholy - ]` | `[ unholy, out ] (43)` |
| unholy symbols remaining | `[ - Unholy : {4} - ]` | `[ unholy, {4} ] (53)` |
| max unholy | `[ - Unholy Maxed: {5} - ]` | `[ unholy, {5} ] (68)` |
| You consume | `+{3} Arcane Essence` | `[ essence, +{3} ] (53)` |
| generates mana | `[ - Mana REFUNDED! - ]` | `[ mana, refund ] (53)` |
| progress on the lock | `[ - Lock: {8} - ]` | `[ lock, {8} ] (53)` |
| clearing it of traps | `[ - Trap: {10} - ]` | `[ trap, {10} ] (53)` |
| thrown at that player within 30 | `[ - Telekinesis Ready! - ]` | `[ teleki, target ] (63)` |
| free hand to drink | `[ - Hands full! - ]` | `[ hands, full ] (43)` |
| You will now automatically | `[ - SCROLL USE  ON - ]` | `[ scroll mode, on ] (53)` |
| You may only cast that spell on a player once every 30 seconds. | `[ - DONT - ]` | `[ limit, 30s ] (43)` |
| You may only cast that spell on a player once every 30 seconds. | `[ - DONT - ]` | — |
| Your boarding party fails to board the ship | `[ - FAIL BOARD - ]` | `[ boarding, miss ] (43)` |
| That ship is too far away to board. | `[ - FAR AWAY - ]` | `[ range, out ] (43)` |
| Your shot hinders your target! | `[ - Hinder - ]` | `[ hinder, target ] (63)` |
| You deactivate your stance. | `[ - CODEX OFF - ]` | `[ stance, off ] (43)` |
| You smash the unprotected | `[ - Smash - ]` | `[ smash, target ] (63)` |
| fallen to corruption | `[ - SHRINE EVENT - ]` | `[ shrine, on ] (9)` |
| You begin to move quietly | `GO` | `[ stealth, on ] (53)` |
| You have 4 stealth | `LAST STEPS` | `[ stealth, 4 ] (43)` |
| You have 3 stealth | `3` | `[ stealth, 3 ] (43)` |
| You have 2 stealth | `2` | `[ stealth, 2 ] (43)` |
| You have 1 stealth | `1` | `[ stealth, 1 ] (33)` |
| You have 0 stealth | `STOP` | `[ stealth, 0 ] (33)` |
| You must hide first | `NOT HIDDEN` | `[ hide, off ] (43)` |
| You charge your spell with additional energy! | `C^` | — |
| Those cannons are out of ammunition | `[ - RELOAD CANNONS - ]` | `[ cannon, out ] (43)` |
| You fail to steal | `[ - FAIL - ]` | `[ steal, miss ] (43)` |
| You fail in your stealing attempt | `[ - FAIL - ]` | `[ steal, miss ] (43)` |
| You steal | `[ - WOOP - ]` | `[ steal, done ] (68)` |
| You successfully steal | `[ - WOOP - ]` | `[ steal, done ] (68)` |
| You have already stolen from this creature | `[ - Already Stolen - ]` | `[ steal, wrong ] (43)` |
| You may now taunt again. | `[ - Taunt Ready! - ]` | `[ taunt, ready ] (68)` |
| Potion codex Panaccea upgrade is now ready. | `[ - Panaccea Ready - ]` | `[ panacea, ready ] (68)` |
| Your ability to hide is no longer impeded | `[ - Invis Ready - ]` | `[ hide, ready ] (68)` |
| Weapon ability ready | `[ - Weapon Abi Ready - ]` | `[ ability, ready ] (68)` |
| your rapid | `[ - SLOW DOWN - ]` | `[ move, slow ] (43)` |
| your movements attract | `[ - SLOW DOWN - ]` | `[ move, slow ] (43)` |
| your quick movements draw the attention | `[ - SLOW DOWN - ]` | `[ move, slow ] (43)` |
| iron flesh charges remaining | `[ - Iron Flesh : {1} - ]` | `[ iron flesh, {1} ] (53)` |
| You detonate a ground trap | `[ - BOOOM - ]` | `[ detonate, done ] (63)` |
| You may now detonate another trap | `[ - DETONATE NOW - ]` | `[ detonate, ready ] (68)` |
| You increase your [EventScore | `+ {6}` | `[ event, +{6} ] (53)` |
| You are now under the effect of a Song | `++` | `[ song, on ] (53)` |
| You fail to discord | `--` | `[ disco, miss ] (43)` |
| You fail to pacify | `--` | `[ peace, miss ] (43)` |
| You play successfully | `++` | `[ bard, target ] (63)` |
| additional energy | `+++` | `[ spell, charged ] (63)` |
| What instrument shall you play | `[ - INSTRUMENT BROKE - ]` | `[ inst, out ] (33)` |
| now planted | `You are now planted.` | `[ planted, on ] (53)` |
| 5 moving throws | `5 moving throws left.` | `[ throws, 5 ] (53)` |
| 4 moving throws | `4 moving throws left.` | `[ throws, 4 ] (53)` |
| 3 moving throws | `3 moving throws left.` | `[ throws, 3 ] (53)` |
| 2 moving throws | `2 moving throws left.` | `[ throws, 2 ] (53)` |
| 1 moving throws | `1 moving throw left.` | `[ throws, 1 ] (33)` |
| 0 moving throws | `No throws, plant now.` | `[ throws, 0 ] (33)` |
| wing your target | `You wing your target.` | `[ wing, target ] (63)` |
| Magic reflect removed. | (신규) | `[ reflect, off ] (43)` |

## 스크립트 오버헤드

- 우리 스크립트만 바꿨다. 외부 출처(`loot/recycle` `loot/bank-pouch` `train/barding` `train/carto` `train/magery` `train/steal` `gather/*`, `shelf/*`)는 그대로.
- 프롬프트는 55 + `pick`. 재고 없음은 43 (`[ heal pot, out ]`), 그것 없이는 루프가 못 도는 것만 33 (`[ inst, out ]` `[ necro book, out ]`).
- 시전 알림은 대상만: `[ blood oath ]` 44, `[ drain ]` 83.
- 변수 값은 `[ 대상, {{var}} ]`: `[ inst, {{label__picked_instrument}} ]` `[ worn, {{label__right_hand}} ]`.

| 이전 | 지금 |
|---|---|
| `"Select instrument:" 55` | `"[ inst, pick ]" 55` |
| `"{{label__picked_instrument}}" 55` | `"[ inst, {{label__picked_instrument}} ]" 55` |
| `"Instrument, that is not one" 34` | `"[ inst, wrong ]" 33` |
| `"Instrument, not in backpack" 34` | `"[ inst, out ]" 33` |
| `"Crook, none in backpack, followers lose the herding bonus" 33` | `"[ crook, out ]" 43` |
| `"Bard Necro Enhanced running" 32` | `"[ bard necro, on ]" 53` |
| `"Pouches, none left" 34` | `"[ pouch, out ]" 33` |
| `"Instrument, switched to a spare" 32` | `"[ inst, set ]" 53` |
| `"Instrument, none in backpack" 34` | `"[ inst, out ]" 33` |
| `"Target set" 32` | `"[ target, set ]" 53` |
| `"Cure potion" 32` | `"[ cure pot, on ]" 53` |
| `"Cure potions, none left" 33` | `"[ cure pot, out ]" 43` |
| `"Cure, disturbed" 32` | `"[ cure, disturbed ]" 43` |
| `"Heal, disturbed" 32` | `"[ heal, disturbed ]" 43` |
| `"Heal potion" 32` | `"[ heal pot, on ]" 53` |
| `"Heal potions, none left" 33` | `"[ heal pot, out ]" 43` |
| `"Greater Heal, disturbed" 32` | `"[ gheal, disturbed ]" 43` |
| `"Gold, dropped some on the ground" 32` | `"[ gold, dropped ]" 53` |
| `"Weight, over the cap with no gold to drop" 33` | `"[ weight, over ]" 43` |
| `"Refresh potions, none left" 33` | `"[ refresh, out ]" 43` |
| `"Strength potions, none left" 33` | `"[ str, out ]" 43` |
| `"Agility potions, none left" 33` | `"[ agi, out ]" 43` |
| `"Magic resist potions, none left" 33` | `"[ resist, out ]" 43` |
| `"Necro book, none in backpack" 34` | `"[ necro book, out ]" 33` |
| `"Create Food, disturbed" 32` | `"[ food, disturbed ]" 43` |
| `"Blood Oath" 44` | `"[ blood oath ]" 44` |
| `"Corpse Skin" 44` | `"[ corpse skin ]" 44` |
| `"Evil Omen" 44` | `"[ evil omen ]" 44` |
| `"Vampiric Embrace" 44` | `"[ vampiric embrace ]" 44` |
| `"Mana Drain, disturbed" 32` | `"[ drain, disturbed ]" 43` |
| `"Mana Drain, cut for a heal" 32` | `"[ drain, cut ]" 43` |
| `"Mana Drain" 83` | `"[ drain ]" 83` |
| `"Curse, disturbed" 32` | `"[ curse, disturbed ]" 43` |
| `"Curse, cut for a heal" 32` | `"[ curse, cut ]" 43` |
| `"Curse" 83` | `"[ curse ]" 83` |
| `"Magic Arrow, disturbed" 32` | `"[ magic arrow, disturbed ]" 43` |
| `"Magic Arrow, cut for a heal" 32` | `"[ magic arrow, cut ]" 43` |
| `"Harm, disturbed" 32` | `"[ harm, disturbed ]" 43` |
| `"Harm, cut for a heal" 32` | `"[ harm, cut ]" 43` |
| `"Fireball, disturbed" 32` | `"[ fireball, disturbed ]" 43` |
| `"Fireball, cut for a heal" 32` | `"[ fireball, cut ]" 43` |
| `"Lightning, disturbed" 32` | `"[ lightning, disturbed ]" 43` |
| `"Lightning, cut for a heal" 32` | `"[ lightning, cut ]" 43` |
| `"Poison Strike" 44` | `"[ poison strike ]" 44` |
| `"Energy Bolt, disturbed" 32` | `"[ eb, disturbed ]" 43` |
| `"Energy Bolt, cut for a heal" 32` | `"[ eb, cut ]" 43` |
| `"Not an instrument!" 33` | `"[ inst, wrong ]" 43` |
| `"Not in backpack" 33` | `"[ inst, out ]" 43` |
| `"No aspect weapon in backpack." 32` | `"[ aspect weapon, out ]" 43` |
| `"Instrument invalid, reselecting." 33` | `"[ inst, wrong ]" 43` |
| `'You drop some gold on the ground.' 55` | `"[ gold, dropped ]" 53` |
| `"Overweight and no gold to drop." 32` | `"[ weight, over ]" 43` |
| `"You are out of bandages." 32` | `"[ bandage, out ]" 43` |
| `"You are out of pouches." 32` | `"[ pouch, out ]" 43` |
| `label__heal_potion 83` | `"[ heal pot, {{label__heal_potion}} ]" 53` |
| `"You drink a healing potion." 53` | `"[ heal pot, on ]" 53` |
| `"You are out of healing potion." 32` | `"[ heal pot, out ]" 43` |
| `"You drink a cure potion." 44` | `"[ cure pot, on ]" 53` |
| `"You are out of cure potion." 32` | `"[ cure pot, out ]" 43` |
| `"You are out of refresh potions." 32` | `"[ refresh, out ]" 43` |
| `"You are out of strength potions." 32` | `"[ str, out ]" 43` |
| `"You are out of agility potions." 32` | `"[ agi, out ]" 43` |
| `"You are out of magic resist potions." 32` | `"[ resist, out ]" 43` |
| `"No stance on codex label." 33` | `"[ stance, out ]" 43` |
| `"Defensive stance." 32` | `"[ stance, defensive ]" 53` |
| `"Sunder stance." 32` | `"[ stance, sunder ]" 53` |
| `"Pummel ability." 32` | `"[ pummel ]" 44` |
| `"Select instrument:" 73` | `"[ inst, pick ]" 55` |
| `"{{label__picked_instrument}}" 73` | `"[ inst, {{label__picked_instrument}} ]" 55` |
| `"Not an instrument" 33` | `"[ inst, wrong ]" 43` |
| `"No throwing weapon in backpack." 43` | `"[ weapon, out ]" 43` |
| `"No parrying gauche in backpack." 43` | `"[ gauche, out ]" 43` |
| `"Planted 2s." 73` | `"[ planted, 2s ]" 53` |
| `"Planted 4s." 73` | `"[ planted, 4s ]" 53` |
| `"Planted 6s." 73` | `"[ planted, 6s ]" 53` |
| `"Planted 8s." 73` | `"[ planted, 8s ]" 53` |
| `"Moving throws gone." 33` | `"[ throws, out ]" 43` |
| `"You drop some gold on the ground." 73` | `"[ gold, dropped ]" 53` |
| `"Overweight, no gold to drop." 43` | `"[ weight, over ]" 43` |
| `"No bandages left." 43` | `"[ bandage, out ]" 43` |
| `"No pouches left." 43` | `"[ pouch, out ]" 43` |
| `label__heal_potion 73` | `"[ heal pot, {{label__heal_potion}} ]" 53` |
| `"You drink a healing potion." 63` | `"[ heal pot, on ]" 53` |
| `"No healing potions left." 43` | `"[ heal pot, out ]" 43` |
| `"You drink a cure potion." 63` | `"[ cure pot, on ]" 53` |
| `"No cure potions left." 43` | `"[ cure pot, out ]" 43` |
| `"No refresh potions left." 43` | `"[ refresh, out ]" 43` |
| `"No strength potions left." 43` | `"[ str, out ]" 43` |
| `"No agility potions left." 43` | `"[ agi, out ]" 43` |
| `"No magic resist potions left." 43` | `"[ resist, out ]" 43` |
| `"No stance on codex label." 43` | `"[ stance, out ]" 43` |
| `"Suppress stance." 73` | `"[ stance, suppress ]" 53` |
| `"Rake stance." 73` | `"[ stance, rake ]" 53` |
| `"Clash ability." 73` | `"[ clash ]" 44` |
| `"Blitz ability." 73` | `"[ blitz ]" 44` |
| `"You are in pvp" 33` | `"[ pvp, on ]" 33` |
| `"You are out of pouche." 32` | `"[ pouch, out ]" 43` |
| `found_potion_description 83` | `"[ heal pot, {{found_potion_description}} ]" 53` |
| `"You are out of bandage." 32` | `"[ bandage, out ]" 43` |
| `"Vanish activated." 89` | `"[ vanish, on ]" 53` |
| `"You are no longer hidden." 32` | `"[ hide, off ]" 43` |
| `'You carve materials from the corpse.' 49` | `"[ carve, done ]" 53` |
| `'You dont see anything nearby worth carving or investigating.' 42` | `"[ corpse, out ]" 43` |
| `'You must have a bladed weapon to carve this corpse.' 32` | `"[ blade, out ]" 43` |
| `"You are able to hide again." 1303` | `"[ hide, ready ]" 68` |
| `"You are under a stationary penalty." 33` | `"[ penalty, on ]" 43` |
| `"You must wait for stealth." 32` | `"[ stealth, off ]" 43` |
| `"You may now move into position." 25` | `"[ position, ready ]" 68` |
| `"You feel ready to conitunue stealthing." 28` | `"[ stealth, ready ]" 68` |
| `"You must wait a few moments to use another skill." 83` | `"[ skill, off ]" 43` |
| `"That target is out of range." 32 lasttarget` | `"[ range, out ]" 43 lasttarget` |
| `"Target the furniture the containers sit in" 55` | `"[ furniture, pick ]" 55` |
| `"Target the supply box that holds tools and instruments" 55` | `"[ supply box, pick ]" 55` |
| `"Target the recall scroll container" 55` | `"[ scroll box, pick ]" 55` |
| `"Target the bank deposit safe" 55` | `"[ bank safe, pick ]" 55` |
| `"Target the resource stockpile" 55` | `"[ stockpile, pick ]" 55` |
| `"Target the repair bench" 55` | `"[ repair bench, pick ]" 55` |
| `"Target the storage shelf" 55` | `"[ shelf, pick ]" 55` |
| `"Target the magic item recycler" 55` | `"[ recycler, pick ]" 55` |
| `"Bank Deposit safe" 82` | `"[ bank safe, on ]" 53` |
| `"Resource stockpile" 82` | `"[ stockpile, on ]" 53` |
| `"Pass repair bench" 82` | `"[ repair bench, skip ]" 53` |
| `"Repair bench" 82` | `"[ repair bench, on ]" 53` |
| `"Magic item recycler" 82` | `"[ recycler, on ]" 53` |
| `"Storage shelf restock" 82` | `"[ shelf, restock ]" 53` |
| `"Storage shelf resupply" 82` | `"[ shelf, resupply ]" 53` |
| `"back: sewing kit" 88` | `"[ sewing kit, back ]" 53` |
| `"take: sewing kit" 88` | `"[ sewing kit, take ]" 53` |
| `"No sewing kit in the supply box." 33` | `"[ sewing kit, out ]" 43` |
| `"back: identification wand" 88` | `"[ id wand, back ]" 53` |
| `"take: identification wand" 88` | `"[ id wand, take ]" 53` |
| `"No identification wand in the supply box." 33` | `"[ id wand, out ]" 43` |
| `"back: {{label__found_instrument}}" 88` | `"[ inst, back ]" 53` |
| `"take: {{label__found_instrument}}" 88` | `"[ inst, take ]" 53` |
| `"No magic instrument in the supply box." 33` | `"[ inst, out ]" 43` |
| `"Set looting pouch" 88` | `"[ loot pouch, set ]" 53` |
| `"Looting pouch not found."` | `"[ loot pouch, out ]" 43` |
| `"moved: pouch" 88` | `"[ pouch, moved ]" 53` |
| `"moved: trapped pouch" 88` | `"[ trapped pouch, moved ]" 53` |
| `"moved: reagent satchel" 88` | `"[ reg satchel, moved ]" 53` |
| `"moved: alchemists satchel" 88` | `"[ alch satchel, moved ]" 53` |
| `label__sorting_item 11` | `"[ sort, {{label__sorting_item}} ]" 53` |
| `"righthand: {{label__right_hand}}" 88` | `"[ right hand, {{label__right_hand}} ]" 53` |
| `"lefthand: {{label__left_hand}}" 88` | `"[ left hand, {{label__left_hand}} ]" 53` |
| `"onehandedsecondary: {{label__one_handed_secondary}}" 88` | `"[ secondary, {{label__one_handed_secondary}} ]" 53` |
| `"head: {{label__head}}" 88` | `"[ head, {{label__head}} ]" 53` |
| `"neck: {{label__neck}}" 88` | `"[ neck, {{label__neck}} ]" 53` |
| `"earrings: {{label__earrings}}" 88` | `"[ earrings, {{label__earrings}} ]" 53` |
| `"face: {{label__face}}" 88` | `"[ face, {{label__face}} ]" 53` |
| `"shirt: {{label__shirt}}" 88` | `"[ shirt, {{label__shirt}} ]" 53` |
| `"innertorso: {{label__inner_torso}}" 88` | `"[ inner torso, {{label__inner_torso}} ]" 53` |
| `"middletorso: {{label__middle_torso}}" 88` | `"[ middle torso, {{label__middle_torso}} ]" 53` |
| `"outertorso: {{label__outer_torso}}" 88` | `"[ outer torso, {{label__outer_torso}} ]" 53` |
| `"arms: {{label__arms}}" 88` | `"[ arms, {{label__arms}} ]" 53` |
| `"gloves: {{label__gloves}}" 88` | `"[ gloves, {{label__gloves}} ]" 53` |
| `"ring: {{label__ring}}" 88` | `"[ ring, {{label__ring}} ]" 53` |
| `"bracelet: {{label__bracelet}}" 88` | `"[ bracelet, {{label__bracelet}} ]" 53` |
| `"waist: {{label__waist}}" 88` | `"[ waist, {{label__waist}} ]" 53` |
| `"pants: {{label__pants}}" 88` | `"[ pants, {{label__pants}} ]" 53` |
| `"innerlegs: {{label__inner_legs}}" 88` | `"[ inner legs, {{label__inner_legs}} ]" 53` |
| `"outerlegs: {{label__outer_legs}}" 88` | `"[ outer legs, {{label__outer_legs}} ]" 53` |
| `"shoes: {{label__shoes}}" 88` | `"[ shoes, {{label__shoes}} ]" 53` |
| `"cloak: {{label__cloak}}" 88` | `"[ cloak, {{label__cloak}} ]" 53` |
| `"talisman: {{label__talisman}}" 88` | `"[ talisman, {{label__talisman}} ]" 53` |
| `"quiver: {{label__quiver}}" 88` | `"[ quiver, {{label__quiver}} ]" 53` |
| `"outerbody: {{label__outer_body}}" 88` | `"[ outer body, {{label__outer_body}} ]" 53` |
| `"backpack: {{label__backpack}}" 88` | `"[ backpack, {{label__backpack}} ]" 53` |
| `"Dress setting completed." 88` | `"[ dress, set ]" 53` |
| `"out of recall scroll" 34` | `"[ recall scroll, out ]" 33` |
| `label__found_runetome 88` | `"[ scroll, {{label__found_runetome}} ]" 53` |
| `"You finish loadout" 53` | `"[ loadout, done ]" 53` |
| `"wearing {{label__right_hand}}" 88` | `"[ worn, {{label__right_hand}} ]" 53` |
| `"wearing {{label__left_hand}}" 88` | `"[ worn, {{label__left_hand}} ]" 53` |
| `"wearing {{label__one_handed_secondary}}" 88` | `"[ worn, {{label__one_handed_secondary}} ]" 53` |
| `"wearing {{label__head}}" 88` | `"[ worn, {{label__head}} ]" 53` |
| `"wearing {{label__neck}}" 88` | `"[ worn, {{label__neck}} ]" 53` |
| `"wearing {{label__earrings}}" 88` | `"[ worn, {{label__earrings}} ]" 53` |
| `"wearing {{label__face}}" 88` | `"[ worn, {{label__face}} ]" 53` |
| `"wearing {{label__shirt}}" 88` | `"[ worn, {{label__shirt}} ]" 53` |
| `"wearing {{label__inner_torso}}" 88` | `"[ worn, {{label__inner_torso}} ]" 53` |
| `"wearing {{label__middle_torso}}" 88` | `"[ worn, {{label__middle_torso}} ]" 53` |
| `"wearing {{label__outer_torso}}" 88` | `"[ worn, {{label__outer_torso}} ]" 53` |
| `"wearing {{label__arms}}" 88` | `"[ worn, {{label__arms}} ]" 53` |
| `"wearing {{label__gloves}}" 88` | `"[ worn, {{label__gloves}} ]" 53` |
| `"wearing {{label__ring}}" 88` | `"[ worn, {{label__ring}} ]" 53` |
| `"wearing {{label__bracelet}}" 88` | `"[ worn, {{label__bracelet}} ]" 53` |
| `"wearing {{label__waist}}" 88` | `"[ worn, {{label__waist}} ]" 53` |
| `"wearing {{label__pants}}" 88` | `"[ worn, {{label__pants}} ]" 53` |
| `"wearing {{label__inner_legs}}" 88` | `"[ worn, {{label__inner_legs}} ]" 53` |
| `"wearing {{label__outer_legs}}" 88` | `"[ worn, {{label__outer_legs}} ]" 53` |
| `"wearing {{label__shoes}}" 88` | `"[ worn, {{label__shoes}} ]" 53` |
| `"wearing {{label__cloak}}" 88` | `"[ worn, {{label__cloak}} ]" 53` |
| `"wearing {{label__talisman}}" 88` | `"[ worn, {{label__talisman}} ]" 53` |
| `"wearing {{label__quiver}}" 88` | `"[ worn, {{label__quiver}} ]" 53` |
| `"wearing {{label__outer_body}}" 88` | `"[ worn, {{label__outer_body}} ]" 53` |
| `"wearing {{label__backpack}}" 88` | `"[ worn, {{label__backpack}} ]" 53` |
| `"Dress Suite - Equip completed" 88` | `"[ dress, done ]" 53` |
| `"Set chest" 88` | `"[ chest, set ]" 53` |
| `"Out of scrolls!" 34` | `"[ scroll, out ]" 33` |
| `desc 88` | `"[ scroll, {{desc}} ]" 53` |
| `"Target the vendor you are stocking" 55` | `"[ vendor, pick ]" 55` |
| `"Target the box holding what you want to sell" 55` | `"[ sell box, pick ]" 55` |
| `"Pricing gump did not open." 33` | `"[ pricing, out ]" 43` |
| `"Turn ON Use Item Pricing Menu in Vendor Settings." 33` | `"[ pricing menu, off ]" 43` |
| `"{{label__item}} : {{var__price_hint}}" 88` | `"[ {{label__item}}, {{var__price_hint}} ]" 53` |
| `"Aborted." 33` | `"[ vendor, cut ]" 43` |
| `"All items placed." 53` | `"[ vendor, done ]" 53` |
| `"Target the furniture the distribution chest sits in" 55` | `"[ furniture, pick ]" 55` |
| `"Target the distribution chest" 55` | `"[ share chest, pick ]" 55` |
| `"cannot find global__my_distribution_container" 34` | `"[ share chest, out ]" 33` |
| `distribute_item_description 11` | `"[ share, {{distribute_item_description}} ]" 53` |
| `"DONE DONE DONE"` | `"[ share loot, done ]" 53` |
| `"Target your own loot container" 55` | `"[ loot chest, pick ]" 55` |
| `"cannot find global__my_loot_container" 34` | `"[ loot chest, out ]" 33` |
| `distribute_item_description 11` | `"[ claim, {{distribute_item_description}} ]" 53` |
| `"LOOT LOOT LOOT"` | `"[ claim loot, done ]" 53` |
| `"Target an item to read its label:" 55` | `"[ label, pick ]" 55` |
| `"Nothing selected." 33` | `"[ label, out ]" 43` |
| `"{{label__dump}}" 88` | `"[ label, {{label__dump}} ]" 53` |
| `"{{found_instrument_description}}"` | `"[ inst, {{found_instrument_description}} ]" 55` |
| `"finding moongate" 460` | `"[ moongate, out ]" 43` |
| `"found moongate" 88 found_moongate` | `"[ moongate, set ]" 53 found_moongate` |
| `"escape done" 40` | `"[ moongate, done ]" 53` |
| `"Maxed Skill" 88` | `"[ herding, done ]" 53` |
| `"Need a crook" 34` | `"[ crook, out ]" 33` |

## 구멍 — 문장을 저널에서 잡아야 붙일 수 있는 것

| 상황 | 필요한 것 | 붙일 곳 |
|---|---|---|
| 폭탄이 나에게 붙음 | 대상이 보는 문장, 퓨즈 초 | 바 `bomb, me` + `[ bomb, me ]` |
| TK 건 사람 이름 | 문장 형식 (이름이 몇 번째 단어인지 → `{n}`) | `[ teleki, me ]` 에 이름 |
| Disarm On Me | 문장은 있음 "Their attack disarms you!" — **재장착까지 몇 초**인지 | 바 `disarm, me` |
| Mana Drain / Vampire 맞음 | 문장 | `[ drain, me ]` (레지 -10 / -20, 2분) |
| Curse / Weaken / Clumsy 맞음 | 문장 | `[ curse, me ]` 등 |
| Cure · Refresh 포션 마심 | 문장 (힐은 "You drink a healing potion" 으로 잡음) | 바 `cure pot` `refresh` |
| 트랩 파우치 남은 수 | "N Trapped pouches remain" 의 N 자리 → `{n}` | `[ pouch, {n} ]` |
| `sp keg` | 무엇의 줄임인지 모름 (오버헤드 "spkeg" 트리거) | 이름 |

## 아직 확인 안 된 것

- `para` 10s 바가 파우치로 깼을 때 "You can move!" 로 같이 꺼지는지
- `hams, me` 두 문장 중 실제로 오는 쪽 ("You have been hamstrung" / "Their attack hamstrings you!")
- `heal pot` 트리거 "You drink a healing potion" 이 실제 문장인지. 스크립트의 `cooldown "heal pot"` 과 겹쳐도 같은 시각에 다시 시작할 뿐이다
- 범죄자가 될 때 `crim` 바가 트리거 없이 저절로 뜨는지 (특수 바 타입)
- `{n}` 이 0부터인지 1부터인지 — `[ track, {3} {4} {5} ]` 가 원래 쓰던 자리라 그대로 뒀다

## 출처

- [Hamstring](https://wiki.uooutlands.com/Hamstring) — 3초 스태미나 0, 재적용 불가 30초, 시전자 쿨 30~53초
- [Magery](https://wiki.uooutlands.com/Magery) — Telekinesis 끈끈이 PvP 30초, Paralyze PvP 10초, Teleport PvP 쿨 15초
- [Alchemy](https://wiki.uooutlands.com/Alchemy) — Sticky Potions
- [Bapeths Total Cooldown XML](https://outlands.uorazorscripts.com/script/2138a7dc-785e-4d49-a465-e7c922d533ac) — 커뮤니티 트리거 문장, Criminal / PvP 바에 트리거가 없는 근거
- [overheadmessages 스니펫](https://outlands.uorazorscripts.com/script/8b4e1a67-5eb7-4933-8a07-a1ad1c797cc2)
