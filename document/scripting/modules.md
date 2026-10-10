---
name: Modules
label: 모듈과 조립
group: Scripting
order: 30
---

루프를 블록 단위 모듈로 한 벌만 두고, 루프마다 레시피로 조립하는 방식이다. 폴더, 레시피와 모듈의 형식, 조립 규칙, base와 블록끼리 주고받는 이름, 작업 순서, 옮긴 기록을 다룬다.
스크립트 모양과 이름 규칙은 [conventions.md](conventions.md), Razor 문법의 함정은 [razor.md](razor.md)에 있다.

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | 왜 모듈로 나누나. 왜 게임 안에서 이어 달리지 않나 |
| [02](#02) | 어느 폴더에 무엇이 있나 |
| [03](#03) | 레시피는 어떻게 생겼고, 블록 상자에는 무엇이 들어가나. 블록 여러 개를 한 조건으로 묶으려면 |
| [04](#04) | 모듈 파일 하나는 어떻게 생겼나 |
| [05](#05) | 조립기는 무엇을 만들고 무엇을 막나 |
| [06](#06) | base에는 무엇이 있고, 블록끼리 무엇을 주고받나 |
| [07](#07) | 값을 바꿀 때, 블록을 넣거나 모듈에 없는 동작을 더할 때의 순서 |
| [08](#08) | 2026-10-10 옮기고 다시 짜면서 바뀐 것 |
| [09](#09) | 아직 옮기지 않은 것 |

인게임 확인 항목은 [open-items.md](../questions/open-items.md) 09절 (lumberjack-enhanced), 10절 (pvp), 11절 (skinning-enhanced), 12절 (tamer-mage-enhanced), 14절 (bard-necro-enhanced)에 있다.

::part[설계]

## <a id="01"></a>01 왜 모듈인가

**같은 블록이 루프마다 복사돼 있었다.** 2026-10-09 스탯 포션 판정을 바꾸는 데 스크립트 8개를 고쳤고,
그중 skinning-enhanced에는 다른 루프에서 이미 고친 `elseif` 사슬 버그가 그대로 남아 있었다.
회복·포션·버프·시약 같은 블록은 모듈로 한 벌만 두고, 루프마다의 레시피에는 어떤 블록을 어떤 순서로 쓰는지와 그 루프가 기본과 다르게 쓰는 설정만 적는다.

**조립은 저장소에서 한다.** Razor는 한 번에 스크립트 하나만 돌리고, 다른 스크립트를 켜면 지금 것이 멈춘다. 함수 호출이나 include도 없다.
게임 안에서 모듈 스크립트를 차례로 켜는 방식은 쓰지 않는다.

- 패스마다 스크립트를 몇 번씩 새로 켜야 하는데, 그 비용은 재 본 적이 없다. 회복이 늦어질 수 있다.
- `script`가 돌아오는지 넘어가는지 확인되지 않았다.
- Esc는 지금 모듈만 멈추고, 한 모듈의 오류가 사슬 전체를 조용히 끊는다.

조립기가 만든 결과물은 지금까지와 같은 단일 `.razor` 파일이다. 게임과 핫키는 달라지지 않는다.

**네 가지를 지킨다.**

1. 모듈 파일 하나는 블록 하나다. 모든 모듈이 같은 칸을 같은 순서로 가진다 (04절).
2. 블록이 아닌 공용 바탕은 `module/base.razor` 한 파일이다. 모든 레시피가 첫 블록으로 적는다 (06절).
3. 레시피는 블록마다 상자 하나다. 상자 안에 블록이 하는 일과, 바꾸는 설정이 무엇을 하는지, 기본값, 함께 읽는 블록을 조립기가 쓰고, 값은 상자 밑에 붙인다.
   사람은 바꿀 값과 이유만 쓴다 (03절).
4. 모듈과 레시피는 같은 모양이다. 설명은 `-` 상자 안에 모으고, 설명을 받는 줄은 상자 밑에 이어 붙인다 (03절, 04절).

## <a id="02"></a>02 폴더

`module/` 아래 폴더는 블록이 무엇을 맡는지로 나눈다. 어느 루프가 쓰는지로 나누지 않는다. 모듈은 `recovery/heal`처럼 폴더와 파일 이름으로 부르고,
그 이름이 곧 `module/recovery/heal.razor`다.

| 자리 | 맡는 것 | 모듈 |
| --- | --- | --- |
| `module/base.razor` | 모든 루프의 뼈대 | 공용 설정, 표준 대기, 경고 간격, 블록끼리의 신호, 구조적 PvP 정지, 시작 4줄, 패스 끝 대기 (06절) |
| `module/recovery/` | 살아남기 | `cure` (마비면 파우치, 독이면 포션이나 에이전트), `heal`, `bandage`, `light-heal`, `refresh` |
| `module/magery/` | 공격 주문과 시약 | `reagents` (모든 마법 블록이 읽는 시약 표시와 서클별 마나), `rotation` (Mana Drain·Curse, Grimoire 프록 넷, 그 사이 Energy Bolt), `flamestrike` (aspect 발동용) |
| `module/buff/` | 버프 아이콘 유지 | `spells` (Reactive Armor, Magic Reflection, 설정으로 Bless·Arch Protection·Spell Siphon용 자기 Magic Arrow), `potions` (Strength, Agility, Magic Resist), `food` (Food Satisfaction), `mushroom` (Magic Mushroom 먹기와 Create Food) |
| `module/bard/` | 바드 스킬 | `instrument` (악기 찾기와 점검), `disco`, `peace`, `song` (이동 중 노래 셋을 차례로) |
| `module/necro/` | 네크로 핫바와 소환수 | `symbols` (핫바를 열어 두고 Unholy Symbol 수 읽기), `summon-names` (소환수 이름 바꾸기), `burst` (Blood Oath, Corpse Skin, Evil Omen), `poison-strike`, `vampiric-embrace` |
| `module/tamer/` | 펫 스킬 | `herding` (목동 지팡이), `vet-kit` (나와 펫에게 수의사 키트) |
| `module/fight/` | 근접 전투 보조 | `target` (기억한 적), `weapon-swap` (pvp 무기 슬롯), `axe`, `sword-codex`, `parry-codex`, `weapon-ability` |
| `module/gather/` | 채집 | `lumberjacking` (Smart Harvest), `skinning` (칼질) |
| `module/pack/` | 무게와 루트 파우치 | `gold-drop`, `leather`, `lumber` (Logs → Boards → 파우치), `scavenger` (스캐빈저 캐시 비우기) |
| `module/escape/` | PK 피하기 | `tracking` (헌트 필터 설정과 Hunting 점검), `recall` (자동 리콜 한 번) |
| `recipe/<루프>-recipe.razor` | 루프 하나 | 헤더, 도는 순서대로 적은 블록과 그 밑에 붙인 설정 변경, 이 루프만의 준비 (03절) |
| `util/build-scripts.mjs` | 조립기 | 결과물을 만들고 레시피의 블록 칸을 정리한다. `--settings`, `--new-module`, `--check` (05절) |
| `script/combat/*.razor`, `script/gather/*.razor` | 결과물 | 직접 고치지 않는다 |

레시피 이름에 `-recipe`를 붙이는 것은 편집기 탭에서 결과물과 헷갈리지 않게 하려는 것이고, `.razor`는 하이라이팅을 받으려는 것이다.
`module/`과 `recipe/`는 저장소 루트에 둔다. `script/`는 Razor Scripts 폴더에 링크되므로, 그 안에 두면 조각 파일이 스크립트 목록에 떠서 혼자 실행될 수 있다.

::part[형식]

## <a id="03"></a>03 레시피

레시피와 모듈은 모두 **상자**로 짠다. 상자는 `-`로 그은 줄 두 개 사이에 `# @` 줄, 빈 `#` 줄, 그 뒤를 설명하는 `#` 줄을 넣고,
상자 밑에 그 설명을 받는 줄을 빈 줄 없이 이어 붙인 것이다. 레시피의 큰 칸 네 개와 그룹 줄 (아래)만 `=`로 긋는다. 상자와 상자 사이는 빈 줄로 띄운다.
`# @` 줄은 조립기가 읽는 지시이고, Razor에서는 주석이다.

| 부분 | 무엇 |
| --- | --- |
| 맨 위의 `#` 주석 | 레시피를 고치는 사람을 위한 메모. 결과물에 나가지 않는다 |
| `# @ output script/<폴더>/<루프>.razor` | 결과물 경로. 첫 상자 앞에 쓴다 |
| `# @ header` 상자 | 밑에 결과물 맨 위 주석 ([conventions.md](conventions.md#02.C) 02.C절). 핫키 줄은 조립기가 붙인다 |
| `# @ blocks` 상자 | 안에 쓰는 법 네 줄 (조립기가 쓴다), 밑에 블록마다 상자 하나. 도는 순서대로 적고, 이 순서가 setup 순서도 된다. 첫 블록은 늘 `# @ use base`다 |
| `# @ state`, `# @ setup` 상자 | 밑에 그 루프만의 상태 (모듈 상태의 다른 시작값도 된다)와 루프 전 준비. 없어도 된다 |

**블록 하나는 상자 하나다.** 상자 안에 `# @ use` 줄과 설명, 상자 밑에 그 블록에서 바꾸는 설정의 `@setvar!` 줄이다.
바꾸는 설정이 없는 블록도 상자로 두어, 모든 블록이 같은 자리에 같은 것을 보여 준다.

- **상자 안은 조립기가 쓴다.** 모듈의 한 줄 요약, 루프 앞에서 한 번만 도는 블록이면 `Runs once, before the loop.`,
  그리고 이 루프가 바꾸는 설정마다 이름과 기본값, 모듈이 그 설정에 단 설명, 그 설정을 함께 읽는 다른 블록이다. 모듈 파일을 열지 않아도 블록이 무엇을 하는지 보인다.
- **사람이 쓰는 것은 세 가지다.** `# @ use` 줄, `>` 줄, `@setvar!` 줄이다.
  `>` 줄은 상자 안 요약 밑에 쓰면 그 루프만의 블록 메모, 설정 밑에 쓰면 이 루프가 그 값을 쓰는 이유가 된다.
- 새 설정은 아무 상자 밑에나 `@setvar!` 한 줄로 쓰고, 이유는 그 바로 위 `#` 줄에 쓴다.
  조립기가 설정을 주인 블록의 상자 밑으로 옮기고, 이유는 상자 안 `>` 줄로 옮긴다.
- 상자 안의 다른 줄은 조립할 때마다 다시 쓰인다. 조립기가 쓰는 모양이 아닌 줄 (`# 메모`처럼)이 있으면 지우면서 경고하니, 메모는 `>` 줄로 쓴다.
- 기본값과 같은 값이면 `(default 120, the same value)`로 드러나서, 일부러 못 박아 둔 값인지 지워도 되는 값인지 보인다.
  모듈 설명이 바뀌면 다음 조립 때 레시피도 바뀌고, 조립하지 않은 채 커밋하면 `--check`가 잡는다.

```
# ========================================================================================
# @ blocks
#
#   One box per block, in the order the blocks run, base first. The builder writes the box.
#   Yours are the "> " lines in it (a note on the block, or under a setting the reason for
#   its value) and the @setvar! lines under it. Write a new @setvar! line under any box, its
#   reason as a "#" line right above it: the builder moves both to the box it belongs to.
# ========================================================================================

# ----------------------------------------------------------------------------------------
# @ use base
#
#   The frame of every loop. Every recipe lists it first.
#
#   warmode_is_manual (default 0)
#      Whose warmode it is.
#        0  ours: our casts ignore it
#        1  the player's manual control window: our casts and the food stand down while it
#           is on. Potions and bandages still go out
#      Read by recovery/cure, recovery/heal, recovery/light-heal, buff/spells, buff/food.
#      > Warmode is the player's: recovery casts and buffs stand down, potions still go out.
# ----------------------------------------------------------------------------------------
@setvar! config__warmode_is_manual 1

# ----------------------------------------------------------------------------------------
# @ use escape/tracking
#
#   Before the loop: reuses a confirmed Tracking hunt colour, or sets the filter once.
#   Runs once, before the loop.
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# @ use recovery/cure
#
#   The trapped pouch while paralyzed, else a cure potion or the Smart Heal/Cure agent.
# ----------------------------------------------------------------------------------------

...

# ----------------------------------------------------------------------------------------
# @ use recovery/heal
#
#   Heal potion at heal_hits, else Greater Heal at emergency_hits.
#
#   emergency_hits (default 35)
#      Missing hit points that cast Greater Heal when no heal potion went out on this
#      pass. Not below heal_hits.
#      > Bandages handle ordinary damage, so Greater Heal waits for 45.
# ----------------------------------------------------------------------------------------
@setvar! config__emergency_hits 45
```

결과물에는 설명이 나가지 않는다. CONFIG에는 모듈마다 경로 상자와 이 루프의 값만 있고, 설정이 하는 일과 바꾼 이유는 레시피와 모듈에서 읽는다 (05절).

블록 순서는 루프 안 순서다. `insysmsg`는 맞은 줄과 그보다 오래된 줄을 함께 소비하므로 Journal을 읽는 블록끼리는 순서가 중요하다.
lumberjack-enhanced는 Tracking 줄을 먼저 읽도록 `magery/reagents`를 `escape/recall` 뒤에, skinning-enhanced는 칼질 응답 뒤에 둔다.

**그룹은 블록 여러 개를 한 조건 밑에 묶는다.** 블록마다 같은 조건을 따로 물으면 그 조건이 거짓인 패스도 블록 수만큼 문장 값을 낸다
([razor.md](razor.md#06) 06절). 묶으면 한 번만 묻는다. 그룹 줄은 블록 상자 사이에 쓰고, 조립기가 `=` 상자로 정리한다.

| 줄 | 결과물 |
| --- | --- |
| `# @ when 조건` | `if 조건`. 조건은 Razor 그대로 쓴다. 괄호가 없으니 and와 or를 섞지 않는다 ([razor.md](razor.md#03) 03절) |
| `# @ otherwise` | `else`. `when` 안에서 한 번 쓴다 |
| `# @ every interval__이름` | `if timer "timer__이름" >= interval__이름`과 `settimer "timer__이름" 0`. 시계 `timer__이름`은 조립기가 TIMER에 만들고, 첫 패스에 준비돼 있다 |
| `# @ end` | `endif`. 가장 안쪽의 열린 그룹을 닫는다 |

- 그룹 안의 블록은 한 단계마다 네 칸 들어가고, 배너 줄은 줄어든 폭에 맞춘다. 그룹 안에 그룹을 둘 수 있다.
- 그룹이 막는 것은 블록의 loop 부분뿐이다. 선언과 setup은 그룹과 상관없이 늘 나간다. base의 `end`는 그룹 밖 맨 끝이다.
- 조건과 `every`에 쓴 이름도 블록 코드처럼 주인 모듈을 찾는다. `interval__housekeeping`은 base의 것이다.
- **회복 블록은 모든 레시피에서 한 그룹이다.** `recovery/cure`, `heal`, `bandage`, `light-heal`은
  `# @ when paralyzed or poisoned or diffhits > 0` 안에 둔다. 이 조건은 네 블록이 움직이는 조건을 모두 합친 것이라 (붕대는 HP가 1만 줄어도 시작한다)
  레시피가 기준값을 어떻게 바꾸든 맞고, 다치지 않은 패스는 블록 수만큼이 아니라 한 줄만 밟는다. `recovery/refresh`는 기력을 보므로 밖에 둔다.
- 블록 안의 시계와 그룹의 시계는 겹친다. `every interval__housekeeping` 안의 `buff/food`는 5초마다 자기 60초 타이머를 본다.

```
# ========================================================================================
# @ when var__fighting = 1
# ========================================================================================

# ----------------------------------------------------------------------------------------
# @ use bard/disco
#
#   Discordance once per target, read off its label, then left alone for 30 seconds.
# ----------------------------------------------------------------------------------------

...

# ========================================================================================
# @ otherwise
# ========================================================================================

...

# ========================================================================================
# @ end
# ========================================================================================
```

## <a id="04"></a>04 모듈

모든 모듈이 같은 모양이다. 맨 위 상자에 블록이 하는 일과 `# @ hotkeys`, 그 밑으로 칸마다 상자 하나다. 쓸 것이 없는 칸은 뺀다.
**칸마다 담는 이름의 접두가 하나로 정해져 있다.** 그래서 어떤 이름이 어느 칸에 있는지, 결과물의 어느 자리로 가는지가 접두만 보고 정해진다.

| 칸 | 상자 안 | 상자 밑 | 결과물 자리 |
| --- | --- | --- | --- |
| 맨 위 | 블록이 하는 일. 첫 줄은 86자 안의 한 줄 요약이고 레시피와 `--settings`에 보인다. `# @ hotkeys A, B` |   | 헤더의 `Hotkeys:` 줄 |
| `# @ config` | 설정마다 `#   이름`과 그 밑 `#      하는 일` | `config__` 기본값을 이어 붙인다 | CONFIG |
| `# @ wait` | 같은 모양 | `wait__`, `interval__`, `cooldown__`. 모든 루프가 같은 값을 쓰는 내부 값 | WAIT AND COOLDOWN |
| `# @ timer` | 같은 모양. 없어도 된다 | 한 줄에 `timer__이름 시작값`. 시작값이 `interval__` 이름이면 첫 패스에 준비돼 있고, `0`이면 한 주기를 기다린다 | TIMER. `createtimer`와 첫 `settimer`는 조립기가 쓴다 ([conventions.md](conventions.md#04) 04절) |
| `# @ state` | 같은 모양 | `var__` 선언. Play를 넘어 남길 것은 `if not varexist`로 감싼다 | STATE |
| `# @ setup`, `# @ loop`, `# @ end` | `# @` 줄만 | 코드. `loop`와 `end`는 블록 배너로 시작한다 ([conventions.md](conventions.md#02.B) 02.B절). 단계가 있는 블록은 단계마다 같은 모양의 배너를 더 둔다. `end`는 base만 쓴다 | setup, MAIN LOOP, MAIN LOOP 끝 |

- 상자 안의 항목 사이는 `#` 한 줄로 띄운다. 같은 설명을 나누는 이름 (무기 슬롯 네 개처럼)은 `#   이름, 이름`으로 한 항목에 둔다. 글은 90자 안에서 줄을 바꾼다.
- 값이 몇 가지 중 하나인 설정은 첫 줄에 무엇을 고르는지 쓰고, 선택지를 `값  뜻`으로 한 줄에 하나씩 쓴다. 켜고 끄는 설정은 "1 keeps …"처럼 1이 하는 일을 한 줄로 쓴다.
- 칸이 선언하는 이름은 모두 설명해야 하고, 설명에는 그 칸이 선언하는 이름만 쓴다. 어긋나면 조립이 멈춘다. 상자 밑에 이어 붙인 줄 사이에는 주석을 두지 않는다.

```
# ----------------------------------------------------------------------------------------
# Reactive Armor, then Magic Reflection, whenever one is missing.
#
# @ hotkeys > Interrupt
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# @ config
#
#   config__use_reactive_armor
#      1 keeps Reactive Armor up.
#
#   config__use_magic_reflect
#      1 keeps Magic Reflection up.
#
#   config__mana_reactive_armor
#      Minimum current mana to start Reactive Armor.
#
#   config__mana_magic_reflect
#      Minimum current mana to start Magic Reflection.
#
#   config__buff_max_loss
#      Missing hit points at which buffs are not started, and cut mid cast.
#
#   config__buff_when_poisoned
#      Buffs while poisoned.
#        0  no: hold them back and cut one that is casting, so the cure goes first
#        1  yes
# ----------------------------------------------------------------------------------------
@setvar! config__use_reactive_armor 1
@setvar! config__use_magic_reflect 1
@setvar! config__mana_reactive_armor 4
@setvar! config__mana_magic_reflect 14
@setvar! config__buff_max_loss 35
@setvar! config__buff_when_poisoned 1


# ----------------------------------------------------------------------------------------
# @ loop
# ----------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------
    # SELF BUFFS
    #
    # Reactive Armor, then Magic Reflection, whenever one is missing and the window is
    # free. Not started at config__buff_max_loss, and cut there mid cast so the next pass
    # can heal. With config__buff_when_poisoned 0 poison holds them back and cuts them
    # too, so the cure goes first. var__hold_casts lets another block keep the cast window
    # (a latched Recall). config__walk_guard and config__warmode_is_manual apply as for
    # the heal agents. The reflect bar is the server's recast lock after Reflect is used
    # up.
    # ------------------------------------------------------------------------------------
    ...
```

**이름 하나는 모듈 하나의 것이다.** 저장소 전체에서 한 이름을 두 모듈이 선언하면 조립이 멈춘다. 그래서 "이 이름은 어디 것인가"의 답은 늘 한 파일이다.
블록은 루프에 든 다른 모듈의 이름을 써도 되고, 그 관계를 따로 적지 않는다. 조립기가 코드에서 이름을 읽어 주인을 찾고,
주인 모듈이 레시피에 없으면 어느 모듈을 넣으라고 알려 준다 (05절).

블록 코드는 `config__`에 값을 넣지 않는다. 설정은 모듈의 `# @ config`가 기본값을 정하고 레시피가 바꾼다.
`wait__`, `interval__`, `cooldown__`은 모든 루프가 같은 값을 쓴다. 루프마다 달라야 하는 값이 생기면 `config__` 설정으로 옮긴다.

블록 하나를 켜고 끄는 설정은 두지 않는다. 그 블록을 레시피에 넣거나 빼면 된다. 설정은 블록 안의 선택에만 둔다
(`use_resist_potion`, `skin_unowned`처럼). 예외는 `use_bandages`다. `recovery/light-heal`이 이 값을 보고 붕대 대신 나간다.

## <a id="05"></a>05 조립 규칙

1. 헤더: 레시피 헤더 → 블록들이 선언한 핫키를 모은 `Hotkeys:` 줄 → "Generated from recipe/… by util/build-scripts.mjs" 줄.
2. CONFIG → WAIT AND COOLDOWN → TIMER → STATE → setup → MAIN LOOP (`while not dead`, 블록마다의 `loop`, base의 `end`, `endwhile`).
   자리마다 base가 먼저, 블록이 레시피 순서대로, 레시피가 마지막이다. 그룹은 loop 안에서 `if`·`else`·`endif`가 되고, `# @ every`의 시계는 TIMER 끝에 레시피 몫으로 나온다. 레시피의 STATE가 뒤에 오므로 모듈 상태에 다른 시작값을 줄 수 있다 (pvp의 `var__fighting 1`).
3. 큰 칸 (CONFIG 등)은 conventions의 배너 모양이다 ([conventions.md](conventions.md#02.B) 02.B절). **결과물에는 설명을 넣지 않는다.**
   그 안의 조각은 어느 파일에서 왔는지만 적은 상자 (`# module/recovery/heal.razor`) 밑에 값과 코드가 온다. loop 안의 블록은 배너의 줄과 제목만 나가고 제목 오른쪽에 모듈 경로가 붙는다.
   설정과 블록이 하는 일, 레시피가 값을 바꾼 이유는 그 경로의 파일에서 읽는다. 코드 사이 주석은 그대로 나간다.
   TIMER는 timer마다 `createtimer`와 첫 `settimer`를 붙여 쓴다.
4. 레시피는 조립할 때마다 정리된 모양으로 다시 쓴다. 큰 칸마다 `=` 상자, 블록마다 `-` 상자, 설정은 주인 블록의 상자 밑이다.
5. 조립기는 아래에서 멈추고 고칠 곳을 알려 준다.
   - 블록이 쓰는 이름의 주인 모듈이 레시피에 없다: "module/gather/skinning.razor uses timer__combat_target_grace from module/fight/target.razor. Add "# @ use fight/target""
   - 첫 블록이 `# @ use base`가 아니다.
   - 레시피에 적은 설정이 어느 모듈에도 없거나, 레시피가 쓰지 않는 모듈의 것이다.
   - 상자 밖의 주석이 `@setvar!` 줄 바로 위에 있지 않다. 어느 설정의 이유인지 모르는 채로 지우지 않으려고 멈춘다.
   - 모듈 칸의 상자가 칸이 선언하는 이름을 빠뜨렸거나, 선언하지 않는 이름을 설명한다. 설명 줄이 `#   이름`, `#      설명` 모양이 아니다.
   - 두 모듈이 같은 이름을 선언한다. 칸에 다른 접두의 이름이 있다. 블록이 `config__`에 값을 넣는다.
   - 결과물 주석에 `;`이 있다 ([razor.md](razor.md#03) 03절).
   - 모듈 첫 줄 요약이 86자를 넘는다. 레시피 상자에 한 줄로 보여야 한다.
   - 그룹 줄이 짝이 맞지 않는다: `when` 밖의 `otherwise`, 열린 그룹이 없는 `end`, 닫지 않은 그룹, `# @ use base` 앞의 그룹, 조건이나 이름이 빠진 `when`·`every`.
6. 줄 끝은 CRLF로 쓴다 (`.gitattributes`). 바뀐 결과물과 레시피만 다시 쓴다.
7. `util/check.sh`를 인자 없이 돌리면 끝에 `node util/build-scripts.mjs --check`도 돈다. 누가 결과물을 직접 고쳤거나, 모듈 설명을 고치고 조립하지 않았으면 여기서 잡힌다.

::part[base]

## <a id="06"></a>06 base와 블록끼리 주고받는 것

`module/base.razor`는 모든 레시피의 첫 블록이다. 정본은 그 파일이고, 아래는 무엇을 왜 거기 두었는지다.

| 칸 | 가진 것 | 바꾸는 루프 |
| --- | --- | --- |
| `# @ config` | `chatty`, `sysmsg`: 출력 스위치 |   |
|   | `clear_at_start`: Play 때 시작 4줄 ([conventions.md](conventions.md#02.D) 02.D절) | pvp 0. 플레이어가 들고 있던 커서와 시전을 지키려고 |
|   | `use_magery`, `use_potions`: 회복과 버프 블록 여럿이 같이 보는 스위치 | dexxer-basic은 마법 0 |
|   | `walk_guard`: 1이면 우리 시전이 `walk` 바가 도는 동안 기다린다 | pvp 0. 싸움 중에는 기다릴 더 나은 때가 없다 |
|   | `warmode_is_manual`: 1이면 워모드가 플레이어의 조작 창이라 우리 시전과 음식이 선다. 포션과 붕대는 나간다. `recover_in_warmode`: 그때 회복 시전도 설지 | lumberjack-enhanced 1, bard-necro-enhanced 1과 회복은 계속 (1) |
|   | `use_bandages`, `heal_skill_min`: 붕대를 쓸지. 못 쓰면 `recovery/light-heal`이 대신한다 | dexxer-basic·skinning-enhanced는 Healing 10 초과에서만, bard-necro-enhanced는 붕대 없음 |
|   | `settle_first`: 1이면 패스 첫머리에서 아이템 큐와 시전이 끝나기를 기다린다 | bard-necro-enhanced 1 |
| `# @ wait`, `# @ timer` | `wait__poll`, `wait__short`, 경고 간격 `interval__message`와 `timer__message`, 레시피 그룹 `# @ every`가 쓰는 `interval__housekeeping` |   |
| `# @ state` | 블록끼리의 신호 세 개 (아래 표) | pvp는 `var__fighting`을 1로 |
| `# @ setup`, `# @ loop`, `# @ end` | 구조적 PvP 정지 (루프 앞과 패스 첫머리), 시작 4줄, `settle_first`, 패스 끝 `wait wait__poll` |   |

**신호는 쓰는 블록이 없어도 읽는 블록이 돌아야 하는 값이다.** 그래서 base가 중립값으로 선언하고, 쓰는 블록이 있는 루프에서만 값이 바뀐다.
새 신호가 필요하면 base의 `# @ state`와 이 표에 더한다.

| 신호 | 쓰는 곳 | 읽는 곳 |
| --- | --- | --- |
| `var__fighting` | `fight/target` (기억한 적이 `target_range` 안에 있으면 1), pvp 레시피 (늘 1) | `buff/potions`, `buff/spells`의 Bless·Arch Protection, `buff/mushroom`의 Create Food, `magery/flamestrike`, bard-necro-enhanced의 교전 그룹 |
| `var__hold_casts` | `escape/recall` (리콜을 정하면 1) | `buff/spells` |
| `var__hold_gathering` | `escape/recall` (리콜을 정했거나, 필요한 책이 없거나, 감지 리콜인데 Tracking이 사냥 중이 아니면 1) | `gather/lumberjacking`, `pack/lumber` |

신호가 아닌 이름은 주인 모듈이 있어야 쓸 수 있다. 그래서 아래 블록은 주인 모듈과 함께 들어간다. 조립기가 코드에서 읽어 확인하는 관계다.

- `magery/reagents`의 `var__regs_*`, 서클별 마나, `interrupt_to_heal`, `wait__cast`: 회복 시전, `buff/spells`, `buff/mushroom`, 공격 주문 (`magery/*`).
- `recovery/heal`의 `config__heal_hits`: 다쳤을 때 쉬는 블록 (`gather/*`, `pack/leather`, `escape/tracking`).
  `emergency_hits`: 시전 중에 끊는 공격 주문 (`magery/*`). `recovery/light-heal`의 `light_hits`: `pack/lumber`.
- `fight/target`의 `var__combat_target`과 사거리: `fight/parry-codex`, `fight/weapon-ability`, `pack/leather`, 바드·네크로·공격 주문 블록.
  `var__keep_lasttarget`: 자기나 백팩을 찍기 전에 lasttarget을 한 번 더 읽는 블록 (`bard/song`, `magery/flamestrike`, `necro/vampiric-embrace`).
  `gather/skinning`은 칼 커서 중에 고른 적을 여기에 적는다.
- `escape/tracking`의 `var__tracking_*`, `tracking_color`: `escape/recall`.
- `bard/instrument`의 `var__my_instrument`, `var__instrument_ok`, `wait__bard_target`: `bard/disco`, `bard/peace`, `bard/song`.
- `necro/symbols`의 `list__necro_symbols`, `var__symbols_spent`, `interval__necro_action`, `wait__message`, `wait__ability_target`: 네크로 능력 블록.
- `magery/rotation`의 순서 플래그 `var__opener_done`, `var__procs_done`, `var__proc_target`: `necro/poison-strike`.

::part[쓰는 법]

## <a id="07"></a>07 작업 순서

### <a id="07.A"></a>07.A 값을 바꿀 때

1. `node util/build-scripts.mjs --settings recipe/<루프>-recipe.razor`로 그 루프의 설정 전체를 본다.
   설정마다 지금 값, 하는 일, 읽는 블록, `module/…razor:줄`이 나온다. 터미널에서 그 경로를 누르면 파일로 간다.
2. 레시피에서 그 설정을 가진 블록의 상자 밑에 `@setvar! config__이름 값` 한 줄을 쓰고, 바로 위 `#` 줄에 이유를 쓴다.
   다른 상자 밑에 적어도 조립기가 주인 블록으로 옮긴다.
3. `node util/build-scripts.mjs`를 돌린다. 설정이 주인 블록 밑으로 가고, 설명이 다시 쓰이고, 결과물이 다시 만들어진다.
   `util/check.sh`를 돌리고, 게임에서는 Reload all scripts 뒤 Play한다 ([workflow.md](../working/workflow.md#04) 04절).

기본으로 돌리려면 레시피에서 그 줄과 이유를 지운다. 모든 루프의 기본을 바꾸려면 모듈의 `# @ config` 값을 고친다.

### <a id="07.B"></a>07.B 블록을 넣거나 빼고, 새 동작을 더할 때

- 있는 블록을 쓰려면 레시피 `# @ blocks`의 도는 순서 자리에 `# @ use <폴더>/<이름>` 한 줄을 넣는다. 설정은 기본값으로 돈다. 회복 블록은 회복 그룹 안에 넣는다 (03절).
  그 블록에 필요한 모듈이 빠졌으면 조립기가 이름을 대 준다.
- 블록을 끄려면 그 줄을 지운다. 다른 블록이 그 모듈의 이름을 쓰고 있으면 조립기가 알려 준다.
- **모듈에 없는 동작이 필요하면 결과물에 손으로 넣지 않는다.** 다음 조립이 덮어쓴다.
  `node util/build-scripts.mjs --new-module <폴더>/<이름>`으로 빈 틀을 만들어 채우고 레시피에 `# @ use`로 넣는다.
  폴더는 그 블록이 무엇을 맡는지로 고른다 (02절). 맞는 폴더가 없으면 새 관심사이므로 폴더를 먼저 만든다.
- 시작 메시지, 루트 파우치, 복귀 등록처럼 그 루프만 루프 앞에서 한 번 하는 짧은 준비는 레시피의 `# @ setup`에 쓴다.
- 있는 블록을 한 루프에서만 다르게 돌게 하려면 복사하지 말고 그 모듈에 설정을 하나 더한다. 기본값을 지금 동작으로 두면 다른 루프는 그대로다.
- 블록의 동작을 고치면 그 모듈을 쓰는 루프가 모두 바뀐다. 모듈, 레시피, 결과물을 한 커밋에 넣는다.
- Razor 편집기에서 결과물을 저장해 버렸으면 `--check`가 잡는다. 바뀐 줄을 모듈이나 레시피로 옮기고 다시 만든다.

::part[기록]

## <a id="08"></a>08 2026-10-10 기록

### <a id="08.A"></a>08.A 처음 옮길 때

**pvp (v9)는 동작이 같다.** 처음에는 블록을 그대로 잘라 옮겨 루프가 글자까지 같았다. 공용 스위치를 넣은 뒤에도
pvp 설정값 (`walk_guard` 0, `warmode_is_manual` 0, `buff_when_poisoned` 1, `heal_skill_min` 0,
`buff_max_loss` 35 = `emergency_hits`)을 넣어 항상 참인 감싸기 조건을 걷어 내면 원래 루프와 문장이 같았다.

**skinning-enhanced (v11)와 lumberjack-enhanced (v17)는 회복·포션·버프·시약이 pvp와 같은 블록으로 바뀌었다.**
두 루프만의 블록 (전투 대상, 도끼, 골드, codex, 무기 능력, 칼질, 가죽, Tracking 설정, 자동 리콜, 벌목)은 경고 타이머 이름을 `timer__message`로 바꾼 것 말고는 글자까지 같았다.
손실선·마나·Refresh 기준 같은 값은 레시피의 설정으로 그대로 두었다. 바뀐 동작은 아래와 같다.

| 무엇 | 전 | 지금 |
| --- | --- | --- |
| 회복 주문 선택 | 위에서 `var__heal_spell`을 고르고 아래 SELF AGENT가 시전 | 큐어, 힐, 가벼운 Heal 블록이 각자 지금 상태를 읽고 바로 시전 |
| 재시도 타이머 | 큐어·힐 포션·Refresh 1초, 붕대 1.2초, 회복 주문 2.5초, 버프 3초 (lumberjack 10초) | 없음. 행동 큐, `bandaging`, `findbuff`, 포션 라벨과 바가 반복을 막는다 |
| Greater Heal | 손실 45부터 포션과 같은 패스에도 나갈 수 있었다 | 그 패스에 힐 포션이 나가지 않았을 때만 |
| 붕대 | 우리 시전 중에는 기다렸다 | 시전 중에도 나간다 (pvp와 같은 입력 규칙) |
| 포션을 쓰는 방법 | skinning은 `findtype` 뒤 `dclick` | `Drink Cure` 같은 Razor 핫키 |
| 경고 | 두 루프 모두 `[ refresh, out ]`을, skinning은 힐 포션 쿨 라벨과 `[ str, out ]`·`[ agi, out ]`·`[ resist, out ]`도 띄웠다 | pvp처럼 띄우지 않는다. 큐어·힐 포션·붕대가 없을 때의 경고는 그대로다 |
| 블록 순서 | 큐어 → 붕대 → 힐 포션 → 회복 주문 → Refresh | 큐어 → 힐 (포션, Greater Heal) → 붕대 → 가벼운 Heal → Refresh |
| Refresh (skinning) | 스태미나 60 미만 | 60 이하 |
| 버프를 끊는 선 (lumberjack) | 15 미만에서 시작하고 35에서 끊었다 | 15에서 시작하지 않고 15에서 끊는다 |
| Journal 문구 (skinning) | `Heal agent: …`, `Buff cast: …` | `Agent: …`, `Buff: …`. lumberjack은 이 줄이 새로 생긴다 |

레시피를 `-recipe.razor`로 바꾸고 기본과 다른 설정만 적게 하면서, 루프마다 다르던 내부 값 두 개를 모듈 값으로 맞췄다.
skinning-enhanced의 경고 간격은 2.7초에서 3초로, 두 채집 루프의 시약 확인은 30초에서 10초로 바뀌었다.

### <a id="08.B"></a>08.B 다시 짠 것

**왜 다시 짰나.** 레시피의 설정 줄만 보고는 무엇을 하는 설정인지, 어느 모듈이 읽는지 알 수 없었고 그 파일로 찾아갈 길도 없었다.
모듈은 설정 한두 개만 든 것 (`core/output`, `core/switches`), 대기 값만 든 것 (`core/wait`, `core/message`), 블록이 섞여 있었고,
`needs`·`after`·`ready`를 손으로 적어야 했다. 폴더도 core·gather·combat처럼 쓰는 루프로 나뉘어 있었다.

| 무엇 | 전 | 지금 |
| --- | --- | --- |
| 폴더 | `core/`, `combat/`, `gather/` (쓰는 루프로) | `recovery/`, `buff/`, `fight/`, `gather/`, `pack/`, `escape/` (맡는 일로), 그리고 `base.razor` |
| 공용 모듈 | `core/output`, `switches`, `wait`, `message`, `start`, `pvp-stop`, `pass-wait` | `base.razor` 하나. 시작 4줄은 `config__clear_at_start`가 정한다 |
| 모듈 사이 관계 | `# @ needs`, `# @ after`를 손으로 | 조립기가 코드의 이름으로 찾는다 |
| 타이머 | `# @ timer`에 `createtimer` 묶음, `# @ ready`에 `settimer` | `# @ timer`에 `timer__이름 시작값` 한 줄 |
| 모듈의 설정 칸 | `# @ settings` | `# @ config`. 설정마다 설명이 있어야 한다 |
| 레시피 설정 | `# @ config` 칸에 값과 이유만 | 블록마다 상자 하나. 조립기가 상자 안에 설명, 기본값, 함께 읽는 블록을 쓰고, 값은 상자 밑에 붙인다. `# @ use base`가 첫 블록이다 |
| 모양 | 칸과 항목이 붙어 있고, 이름마다 바로 위에 주석이 달려 있었다 | 블록과 칸마다 `-` 상자 (레시피의 큰 칸은 `=`). 설명은 상자 안에 모으고 이름은 상자 밑에 이어 붙인다. 선택지는 한 줄에 하나, 글은 90자 안. 레시피 블록에 모듈 요약이 보인다. 결과물도 같은 모양이다 |
| 블록 켜고 끄기 설정 | `use_weapon`, `use_sword_codex`, `use_parry_codex`, `use_weapon_ability`, `use_skinning`, `use_gold_drop`, `pack_leather`, `pack_lumber`, `use_tracking`, `auto_recall`, `use_stat_potions` | 없앴다. 레시피에 넣으면 켜지고 빼면 꺼진다 |
| codex·무기 능력의 슬롯 번호 | `sword_stance_warrior 4`처럼 바꿀 일이 없는 설정 18개 | 위키 순서의 숫자를 코드에 쓰고, 고르는 설정 (`sword_stance_main` 등)의 설명에 번호표를 둔다 |
| 이름 | `config__weapon_graphic` (도끼), `wait__long`, `wait__target`, 두 codex가 같이 쓰던 `cooldown__stance_*` | `config__axe_graphic`, `wait__gold_drop`, `wait__tracking_gump`, `interval__sword_*`와 `interval__parry_*` |

**pvp (v9)와 skinning-enhanced (v11)는 동작이 같다.** 루프 문장의 차이는 늘 1이던 켜고 끄기 조건이 빠진 것, 슬롯 상수가 숫자가 된 것, 이름이 바뀐 것뿐이다.
pvp 결과물에는 시작 4줄이 `if config__clear_at_start = 1` 안에 들어가고 pvp는 그 값이 0이다.

**lumberjack-enhanced는 v18이 됐다.** 5초 housekeeping 시계 (`var__housekeeping_pass`)를 없애면서 동작이 바뀌었다.

| 무엇 | v17 | v18 |
| --- | --- | --- |
| 책·Tracking·무게 점검 | housekeeping 시계 (5초) | `escape/recall`의 자기 시계 `interval__recall_check` (5초) |
| 음식 | housekeeping 패스에서, 손실 `light_hits` 미만이고 독·워모드·리콜 결정이 없을 때 | skinning과 같은 `buff/food`. 패스마다 60초 타이머와 Food Satisfaction을 보고, 워모드에서는 쉰다 (`warmode_is_manual` 1). 손실·독·리콜 결정은 보지 않는다 |
| 목재 정리 | housekeeping 패스에서, 리콜 결정이 없을 때 | 패스마다 120초 타이머를 본다. `var__hold_gathering`이 1이면 쉰다 |
| 채집이 기다리는 것 | 리콜 결정은 장착과 채집을 모두, 책 없음·Hunting 아님은 채집만 막았다 | 셋 다 `var__hold_gathering` 하나로 장착과 채집을 함께 막는다 |
| 시작 메시지 | `v17 loaded: auto recall=…, tracking color=…` | `v18 loaded: tracking color=…` |

인게임 확인 항목은 [open-items.md](../questions/open-items.md#09) 09절에 더했다.

### <a id="08.C"></a>08.C dexxer-basic

같은 날 `combat/dexxer-basic`을 `recipe/dexxer-basic-recipe.razor`로 옮겼다. 블록은 모두 있던 모듈이고,
30초마다 `Clear Scavenger Cache`를 누르는 부분만 `pack/scavenger`로 새로 만들었다. 옛 값은 레시피 설정으로 옮겼다
(Healing 10 초과에서 붕대, 스태미나 5 미만에서 Refresh, 골드 500씩, 마법 끔).

| 무엇 | 전 | 지금 |
| --- | --- | --- |
| 힐 포션 | HP 65 이하 | 잃은 HP 35 이상 (`heal_hits`). 최대 HP 100이면 같다 |
| 음식 | 패스마다 Food Satisfaction을 보고 먹었다 | 60초마다 본다 (`buff/food`) |
| 포션 쓰기 | `findtype` 뒤 `dclick` | `Drink Cure` 같은 Razor 핫키 |
| 경고 | Refresh·스탯 포션이 없을 때도 띄웠다 | 큐어·힐 포션·붕대·주머니가 없을 때만 |
| 스탯 포션 | 코드는 있었지만 꺼져 있었다 (`var_use_potion 0`) | 넣지 않았다. 쓰려면 `buff/potions`와 `fight/target`을 더한다 |
| 패스 첫머리 | `queued`와 시전이 끝날 때까지 기다렸다 | 블록마다 `queued`와 시전을 보고 비켜 간다 |

### <a id="08.D"></a>08.D bard-necro-enhanced

같은 날 `combat/bard-necro-enhanced`도 `recipe/bard-necro-enhanced-recipe.razor`로 옮겼다. 이 루프는 하우스키핑 틱과 교전·이동 분기로
패스를 나누어서 블록을 그대로 늘어놓을 수 없었다. 그 구조는 레시피 그룹 (03절)으로 옮겼다.
생존 네 블록은 다른 레시피와 같은 `# @ when paralyzed or poisoned or diffhits > 0`, 하우스키핑은 `# @ every interval__housekeeping`,
교전과 이동은 `# @ when var__fighting = 1`과 `# @ otherwise`다.

- 바드·네크로·공격 주문 블록은 새 모듈로 옮겼다 (02절의 `bard/`, `necro/`, `magery/`, `buff/mushroom`). 코드는 원본과 같고 이름만 지금 규칙을 따른다.
  `cooldown__` 간격은 `interval__`, `wait__target`은 바드의 `wait__bard_target`과 네크로의 `wait__ability_target`,
  `wait__long`은 `wait__instrument_pick`, 핫바 대기는 `wait__hotbar_gump`가 됐다.
- 생존·전투 대상·시약·음식·스탯 포션·골드·Refresh·셀프 버프는 다른 루프와 같은 공용 모듈이다. 원본에만 있던 동작은 공용 모듈의 설정으로 더했다
  (`settle_first`, `recover_in_warmode`, heal pot 바 시작).
- Herding은 꺼져 있었으므로 `tamer/herding`은 만들기만 하고 레시피에 넣지 않았다. Herding은 테이머 스킬이라 `tamer/`에 둔다. 켜고 끄는 설정 `use_herding`과 `name_summons`는 없앴다.
- 소환수 이름은 내 이름의 닮은꼴 셋에서 종류를 알아볼 수 있는 이름 (`leech`, `mumi` 등)으로 바꿨다. 종류 단어와 한 글자 차이까지는 서버가 거절한다. 무엇이 나와 있는지 체력바로 보려는 것이다.

| 무엇 | 전 | 지금 |
| --- | --- | --- |
| 힐 간격 | 두 힐 사이 1.2초, Greater Heal 재시도 2.5초 타이머 | 없앴다. 힐 포션은 heal pot 바와 라벨로, Greater Heal은 그 패스에 포션이 나가지 않았을 때 (`recovery/heal`) |
| 독에 걸린 채 다쳤을 때 | Smart Heal/Cure가 독이든 HP든 맡았다 | 큐어가 먼저다. 힐 포션과 Greater Heal은 독이 풀릴 때까지 기다린다 |
| 가벼운 Heal | 잃은 HP 15 초과 35 미만 | 15 이상, 위 한계 없음 (`recovery/light-heal`) |
| 셀프 버프 | 잃은 HP와 상관없이 시전 | 잃은 HP 35 이상이면 시작하지 않고 시전 중이면 끊는다 (`buff_max_loss`) |
| Spell Siphon | RA·Reflect와 한 `elseif` 사슬의 셋째 갈래. 자기를 찍기 전에 lasttarget을 한 번 더 읽었다 | `buff/spells` 사슬의 마지막 갈래 (`use_spell_siphon`). 순서는 같다. 한 시간에 한 번 나가므로 lasttarget은 다시 읽지 않는다 |
| 스탯 포션 | 10초마다 셋을 보고, 없으면 경고. 민첩 기준선 120 | 하우스키핑 5초 안에서 포션마다 5초 재시도. 없어도 경고하지 않는다. 민첩 기준선은 이 템플릿의 DEX 25 + 20인 45 (사용자 확인) |
| Refresh | 없으면 경고 | 경고하지 않는다 |
| 골드 | 하우스키핑마다 무게 밑으로 내려갈 때까지 반복 | 하우스키핑마다 한 번 (`pack/gold-drop`) |
| 음식 | 워모드와 상관없이 | 워모드에서 쉰다 (`warmode_is_manual` 1) |
| 버섯 먹기 | 이동 중에만, 걷기 바와 시전을 기다렸다 | 교전 중에도 마나 55 이하면 먹는다. 포션처럼 커서만 기다린다. Create Food는 그대로 이동 중에만 |
| 시약 읽기 | 30초마다 | 10초마다 (`interval__reagents`) |
| 경고 간격 | 2초 | 3초 (base의 `interval__message`) |
| 전투 대상 | lasttarget이 무엇이든 받았다 | 모바일 serial만 받는다 (`fight/target`) |
| Disco가 기억한 대상 | 하우스키핑에서 30초 뒤 잊었다 | 교전 패스마다 `bard/disco` 첫머리에서 본다. 교전 패스에 문장이 하나 는다 |
| 패스 | 시작에 queued·시전 대기 | 같다 (`settle_first` 1). 끝에 `wait wait__poll` 0.1초가 붙고, 구조적 PvP에서 멈춘다 (base) |
| Journal | 쓰지 않았다 | 다른 루프처럼 `config__sysmsg` 1로 진단 줄을 쓴다 |

인게임 확인 항목은 [open-items.md](../questions/open-items.md#14) 14절에 더했다.

### <a id="08.E"></a>08.E tamer-mage-enhanced

같은 날 archive에 있던 `tamer-mage-enhanced` (v5)를 `recipe/tamer-mage-enhanced-recipe.razor`로 옮기고 결과물을 `script/combat/`에 되돌렸다 (v6).
새 모듈은 `tamer/vet-kit`과 `magery/flamestrike` 둘이고, 나머지는 공용 모듈을 넓혀서 썼다.

- `magery/reagents`가 Bless, Arch Protection, Flamestrike 시약도 읽는다.
- `buff/spells`에 Bless와 Arch Protection 갈래를 더했다. 기본은 꺼져 있고 (`use_bless`, `use_arch_protection`) tamer 레시피만 켠다.
- Hunting 점검을 `escape/recall`에서 `escape/tracking`으로 옮겼다. 리콜이 없는 tamer도 같은 경고를 받는다.
- 켜고 끄는 설정 (`use_vet_kit`, `use_flamestrike`, `use_stat_potions`, `use_gold_drop`, `use_tracking`)은 없앴다. 레시피에 넣으면 켜진다.
  가벼운 Heal은 기본이 꺼져 있었으므로 `recovery/light-heal`을 넣지 않았다.

| 무엇 | 전 | 지금 |
| --- | --- | --- |
| Bless·Arch Protection | 기억한 적이 없을 때 | 교전 중이 아닐 때 (`var__fighting` 0). 적이 10칸 밖에 있으면 건다 |
| 버프 끊기 | 잃은 HP 35 (`emergency_hits`) | 같은 35지만 `buff_max_loss`를 본다 |
| Flamestrike 끊기 | 늘 끊었다 | `interrupt_to_heal`을 따른다 (기본 1). 끊으면 `[ flamestrike, cut ]`. 대상에 쏜 뒤 대기는 0.3초 (`wait__cast`) |
| 시약 읽기 | 30초마다, 패스 맨 앞 | 10초마다, 수의사 키트 뒤. 키트의 Journal 줄을 먼저 읽게 한다 |
| 힐 포션 | 마신 뒤 바를 켜지 않았다 | heal pot 바를 켠다 (`recovery/heal`) |
| 음식 | 시전 중에도 | 시전이 끝나면 |
| 골드 | 떨군 뒤 0.2초 | 1초 (`wait__gold_drop`), `[ gold, dropped ]` |
| 전투 대상 | lasttarget이 무엇이든 받았다 | 모바일 serial만 받는다 (`fight/target`) |

인게임 확인 항목은 [open-items.md](../questions/open-items.md#12) 12절에 있다.

### <a id="08.F"></a>08.F 마무리 점검에서 합친 모듈

같은 날 모든 루프를 옮긴 뒤 다시 보니, 따로 쓸 수 없거나 너무 작아 모듈을 나눈 값이 없는 것이 넷 있었다. 합쳐서 모듈이 43개에서 38개가 됐다.
결과물의 코드는 Spell Siphon 말고는 같다.

| 합친 것 | 된 것 | 왜 |
| --- | --- | --- |
| `necro/hotbar` | `necro/symbols` | 같은 gump를 열고 읽는 한 가지 일이다. 핫바 확인을 심볼 사슬의 마지막 갈래 (수를 못 읽었을 때) 안에 두어, 수를 읽는 패스는 문장을 하나도 더 쓰지 않는다. 전에는 하우스키핑 5초마다 한 줄이었다 |
| `magery/spell-siphon` | `buff/spells`의 마지막 갈래 (`use_spell_siphon`) | RA·Reflect 뒤에 서려고 `var__buff_cast` 플래그를 주고받았는데, `elseif` 사슬 하나면 순서가 저절로 지켜진다. 플래그와 패스마다의 한 줄이 없어졌다. 한 시간에 한 번 나가는 화살이라 자기를 찍기 전에 lasttarget을 다시 읽지 않는다 |
| `recovery/pouch` | `recovery/cure` | 코드 9줄이고 모든 레시피에서 cure 바로 앞에 붙어 있었다. 마비면 파우치, 아니면 독을 본다 (`if` / `elseif`) |
| `magery/opener`, `proc-core`, `filler` | `magery/rotation` | 프록은 Curse를 (`var__opener_done`), Energy Bolt는 프록을 (`var__procs_done`) 기다려서 하나만 쓸 수 없다. 단계마다 배너는 그대로 두었다 |

합치지 않은 것도 적어 둔다. `fight/axe`와 `fight/weapon-swap`은 비슷해 보이지만, 앞의 것은 2초 시계로 빈 손만 보고 뒤의 것은 패스마다 두 손을 읽는 PvP용이라 비용이 다르다.
`bard/disco`와 `bard/peace`, 두 codex는 서로 주고받는 것이 없는 독립 블록이다. `recovery/refresh`와 `buff/food`는 작지만 맡는 일이 다르다.

## <a id="09"></a>09 아직 옮기지 않은 것

- `script/archive/`: 쓰지 않는 스크립트라 옮기지 않는다.
