# Bard Necro Enhanced 전투 루프 설계

대상 파일: **`script/combat/bard-necro-enhanced.razor` (신규)**

구식 `bard-necro.razor` / `bard-necro-eval.razor` 를 대체했다. 둘은 지웠고 git 이력에만 남아 있다.
기존 파일을 고친 것이 아니라 **새로 구현했다.** 컨벤션은 `bard-throwing.razor` 와 `loadout.razor` 를 따른다
(`config__` / `wait__` / `cooldown__` / `var__` / `alias__` / `label__` / `timer__` / `global__`).

바드 숫자와 공식은 전부 **`bard-mechanics.md`** 에 있다. 이 문서에서 다시 추론하지 않는다.

**핫키 `bard-buff` 는 이 템플릿에서 필요 없어진다.** 루프가 이동 중에 세 곡을 알아서 돌린다.
다른 템플릿은 계속 쓰므로 파일 자체는 남긴다.

## 루프 한 장

한 패스에 **한 동작만** 한다. 위에서부터 조건이 맞는 첫 블록이 실행되고 나머지는 다음 패스로 넘어간다.
모든 블록이 같은 가드를 단다 -- **가드를 빠뜨린 블록은 항상 이긴다.**

```
if not targetexists and not casting and not warmode
```

```mermaid
flowchart TD
    S([패스 시작]) --> M0

    M0{"시스템 메시지<br/>방해 · 악기 분실"}
    M0 -->|yes| A0["replay / 악기 재선택"] --> E
    M0 -->|no| M1

    M1{"생존 위험<br/>마비 · 무게 · 독 · HP · 마나"}
    M1 -->|yes| A1["파우치 · 큐어 · 힐 · 포션 · 버섯"] --> E
    M1 -->|no| M2

    M2["타겟 캐시<br/>lasttarget → noto 검사"] --> M3

    M3{"몹이 근처에<br/>있나"}
    M3 -->|"없음 · 이동 중"| BUFF
    M3 -->|"있음 · 교전 중"| SKILL

    BUFF{"Reactive Armor 나<br/>Magic Reflection 이<br/>빠졌나"}
    BUFF -->|yes| ABUFF["다시 건다<br/>Reflect 는 반사 후 30초 쿨"] --> E
    BUFF -->|no| SONG

    SONG{"Music = 0 and<br/>Song = 0 and<br/>그 곡의 슬롯 = 0"}
    SONG -->|yes| ASONG["라운드로빈 한 곡<br/>Disco → Peace → Provo"] --> E
    SONG -->|no| E

    SKILL{"디스코 미적용<br/>또는 피스 만료"}
    SKILL -->|yes| ASKILL["Discordance / Peacemaking<br/>Ensemble 조건 유지"] --> E
    SKILL -->|no| NECRO

    NECRO{"Unholy Symbol<br/>충분한가"}
    NECRO -->|yes| ANECRO["Blood Oath → Corpse Skin → Evil Omen<br/>Vampiric Embrace (이동 중)"] --> E
    NECRO -->|no| OPEN

    OPEN{"이 대상에<br/>오프닝 완료"}
    OPEN -->|no| AOPEN["Mana Drain → Curse"] --> E
    OPEN -->|yes| PROC

    PROC{"프록 중<br/>쿨 끝난 것"}
    PROC -->|yes| APROC["Magic Arrow · Harm<br/>Fireball · Lightning"] --> E
    PROC -->|no| FILL

    FILL{"mana ><br/>filler_floor"}
    FILL -->|yes| AFILL["Energy Bolt"] --> E
    FILL -->|no| E

    E([패스 끝])
```

### 단계별 게이트

| # | 블록 | 게이트 | 비고 |
|---|---|---|---|
| 0 | 시스템 메시지 | `insysmsg` | 방해 -> `replay`, 악기 분실 -> 재선택 |
| 1 | 생존 | 마비 → 독 → HP → 무게 → 음식 → 포션 → 마나 | **아래 전부를 막는다.** 마비가 맨 앞: 그 상태에선 아래가 아무것도 못 한다. 큐어가 힐보다 앞: 큐어는 즉시고 힐은 독 틱에 일부가 샌다. 무게는 그 뒤: 과체중은 다음 1초에 죽지 않는다 |
| 2 | 타겟 캐시 | `lasttarget` + `noto` | `var__combat_target` 갱신 |
| 3 | 자기 버프 | `not findbuff` + `cooldown "reflect"` | **몹이 없을 때만.** 둘 다 시간이 아니라 소모로 끝난다. RA 는 25 흡수, Reflect 는 한 번 반사 뒤 30초 쿨 (반사 시점부터) |
| 4 | Barding Song | `Music=0 and Song=0 and <슬롯>=0` | **몹이 없을 때만.** 라운드로빈 |
| 5 | 바드 스킬 | `Music=0 and <슬롯>=0` | 디스코 1회 + **피스 12초마다** |
| 6 | 네크로 | `list 'necro_symbols' >= config__symbols_*` | Blood Oath → Corpse Skin → Evil Omen 순. **유휴 예약** 아래 참조 |
| 7 | 오프닝 | 마나 + 대상별 리스트 | Mana Drain -> Curse |
| 8 | 프록 코어 | `cooldown "magic arrow"` 등 | 네 개가 각자 쿨 |
| 9 | 필러 | `mana > config__filler_floor` | Energy Bolt. **여기부터 잘린다** |

**`PASS FLAGS` 는 교전 중에만 공격 시약 7종을 읽는다.** 이동 중엔 아무도 안 묻는 질문에 findtype 14회를
쓰고 있었다. 생존용 4종(큐어·힐·그레이터힐·음식)은 항상 읽는다.

### 데미지 사이클이 도는 모양

프록 네 개는 각자 쿨을 돌고, **비는 시간은 전부 Energy Bolt 가 채운다.**

```
0.0   Magic Arrow   1서클  0.50 + 0.2
0.7   Harm          2서클  0.75 + 0.2
1.7   Fireball      3서클  1.00 + 0.2
2.9   Lightning     4서클  1.25 + 0.2
4.3   ────── 프록 네 개 소진, 쿨 대기 ──────
4.3   Energy Bolt   6서클  1.75 + 0.2   실질 5마나
6.3   Energy Bolt
8.2   Energy Bolt
10.2  Energy Bolt
12.1  Energy Bolt
14.1  ────── 프록이 돌아오면 다시 위로 ──────
```

**15초당 시전 4회 -> 9회.** 프록이 쿨에서 돌아오는 순간 사다리 7번이 8번을 앞지르므로,
별도 상태값 없이 자연스럽게 사이클이 돈다.

**마나가 모자라면 8번부터 잘린다.** `config__filler_floor` 를 52 이상(오프닝 22 + 코어 30)으로
두어 필러가 다음 몹의 오프닝 마나를 먹지 않게 한다.


## 셋업에서 한 번만 하는 것

| | |
|---|---|
| 악기 | 캐시 → 자동 탐색 → 수동 선택. 없으면 `stop` |
| 크룩 활성화 | `config__use_herding 0`. Herding 이 템플릿에서 빠져서 (Resisting Spells 80) 크룩은 아무것도 안 한다. 다시 찍으면 1 로 |
| 네크로 핫바 | 루프 안 `NECRO HOTBAR` 가 첫 패스에 연다 (타이머가 만료 상태로 시작) |

## 캐릭터 전제

| 스킬 | 값 |
|---|---|
| Discordance / Peacemaking / Provocation | 80 / 80 / 80 |
| Musicianship | 0 (Bard Codex `Self Taught` T2 로 대체) |
| Spirit Speak | 120 |
| Resisting Spells | 80 (Herding 에서 바꿈, 2026-09-27) |
| Necromancy | 100 |
| Magery | 100 |
| Eval Int | 80 |

- **Effective Barding = 170** (송 메시지 `8.5%` 로 실측).
- **Meditation 없음.** 마나 회복은 환급 스택 + 이동 중 자연회복 + 버섯이다.
- **Inscription 없음.** `Bless` / `Protection` 지속 연장이 0 이고 `Reactive Armor` 는 무효.
- 장비: Avarhide 스펠북 (double mana regen 60%), Eldritch Aspect 8단계
  (mana refund 26%, special chance 7.2%).
- 소환수 딜 비중 **63.4%** (실측). 본체는 37%.

## 전투 사이클

```
한 마리 교전  ->  10~20초 이동  ->  다음 한 마리
```

**이동 구간이 전체의 약 4분의 1이다.** 마나가 회복되고 버섯 60초 쿨이 도는 시간이다.
반대로 2분짜리 버프는 이 구간에서 낭비된다. 그래서 **2분 버프는 몹이 근처에 있을 때만 건다.**

## 자원

| 자원 | 쓰는 곳 | 성격 |
|---|---|---|
| `cooldown "music"` | 바드 **스킬** 사용 | 글로벌 5초. **Song 은 이것을 세우지 않는다** |
| `cooldown "disco"` | Disco | 단독 슬롯 5초 |
| `cooldown "peace/provo"` | Peace 와 Provo | **공유 슬롯 10초.** 합친 항목 하나 |
| **Barding Song 쿨** | 3곡 전체 | **별도 계열. `cooldown "music"` 이 아니다.** 세 곡이 공유 |
| Unholy Symbol | Blood Oath(4), Corpse Skin(2), Evil Omen(2), Vampiric Embrace(3) | 5초당 1개, 최대 Effective Necro/10 = **10** |
| 마나 | 버프 + 오프닝 + 스팸 + 필러 | 메디가 없어 가장 빡빡하다 |

**자원이 독립이어도 행동 슬롯은 하나다.** 교전 중 블록의 전체 가드는 이렇다.

```
if not targetexists and not casting and not warmode and find var__combat_target ground -1 -1 12 as alias__target
```

### 바드 쿨 모델 (확정)

**Song 은 스킬을 백팩에 타겟한 것이다.** 별도 명령이 아니다.

```
useskill 'Peacemaking'
waitfortarget wait__target
target backpack        <- Song (AoE, 15분)
target lasttarget      <- Skill (단일 대상)
target ground          <- 짧은 광역
```

```
Song    요구:  Music = 0   AND   Song = 0   AND   <그 곡의 슬롯> = 0
        설정:  Song 11초만.   Music 도 슬롯도 세우지 않는다

Skill   요구:  Music = 0   AND   <그 스킬의 슬롯> = 0
        설정:  Music 5초   +   <그 스킬의 슬롯>

슬롯:   cooldown "disco"       5초   단독
        cooldown "peace/provo"   10초  Peace 와 Provo 가 공유
```

**읽는 조건은 거의 같고, 다른 것은 무엇을 세우느냐뿐이다.**
한 줄로 줄이면 **"송은 스킬을 빌려 쓰되 소모하지 않는다."**
차단 메시지 세 종류와 실측 로그는 `bard-mechanics.md` 참조.

**Peace 와 Provo 는 서버에서 슬롯을 공유한다.**
`cooldowns.xml` 에서 **`peace/provo` 한 항목으로 합쳤다.**

**차단된 시도도 `music` 을 태운다.** 송 쿨에 막힌 시전이 스킬 쿨을 소비하므로,
실패한 송 뒤에 스킬을 바로 밀어넣으면 그 스킬도 막힌다.

#### 루프 규칙 하나

**송은 전투 중에 부르지 않는다. 이동 중에만 부른다.**

전투 중에는 디스코와 피스가 `music` 을 5초씩 계속 세워서 송이 거의 안 나간다.
게다가 악기 연주는 시전을 끊어서 프록 주문을 날려먹는다.
반대로 이동 구간(10~20초)에는 `music` 이 비어 있고 어차피 아무것도 안 하고 있다.

```
not targetexists and not casting and 근처에 몹 없음  ->  송 한 곡
```

#### `cooldowns.xml` 은 이미 정리했다

`config/indian/classicuo/Qianshanmuxue/cooldowns.xml` 을 다섯 군데 고쳤다.
내역과 이유는 `bard-mechanics.md` 의 "이 저장소의 `cooldowns.xml` 최종 형태" 에 있다.

따라서 스크립트는 게임 값을 그대로 읽으면 된다. **자체 타이머가 하나도 필요 없다.**

```
Disco 송    cooldown "music" = 0 and cooldown "song" = 0 and cooldown "disco" = 0
Peace 송    cooldown "music" = 0 and cooldown "song" = 0 and cooldown "peace/provo" = 0
Disco 스킬  cooldown "music" = 0 and cooldown "disco" = 0
Peace 스킬  cooldown "music" = 0 and cooldown "peace/provo" = 0
프록 스펠   cooldown "magic arrow" / "harm" / "fireball" / "lightning" = 0
필러        mana > config__filler_floor
```

**바드 외 스킬을 루프에 넣게 되면 `music` 대신 `skill` 을 봐야 한다.**
서버 스킬 게이트가 하나라 Animal Lore 같은 것도 같은 타이머를 쓴다.

Lyric Aspect 방어구의 리셋 프록이 `music` / 스킬 슬롯 / `song` 을 전부 0으로 만드는데,
게임 값을 직접 읽으므로 그 이득이 자동으로 따라온다.


### Song 버프 감지

```
findbuff "song of discordance"
findbuff "song of provocation"
findbuff "song of peacemaking"
```

15분 만료를 직접 세지 않는다. 저장소 기존 구현(`bard-mace.razor:494`)이 이 방식이다.

## 마나 예산

| 주문 | 서클 | 마나 |
|---|---|---|
| Magic Arrow | 1 | 4 |
| Harm | 2 | 6 |
| Fireball | 3 | 9 |
| Lightning | 4 | 11 |
| Curse | 4 | 11 |
| Mana Drain | 4 | 11 |
| **Energy Bolt** | 6 | 20. T3 는 **볼트 뒤 5초 안에 대상이 죽을 때만** 15 를 돌려준다 |
| Create Food | 1 | 4 |

**15초 창을 시전 시간으로 정확히 나눈다** (시전 + 회복 0.2초):

```
Magic Arrow   1서클  0.50 + 0.2 = 0.70
Harm          2서클  0.75 + 0.2 = 0.95
Fireball      3서클  1.00 + 0.2 = 1.20
Lightning     4서클  1.25 + 0.2 = 1.45
                              ------
                프록 코어 합    4.30초

15 - 4.30 = 10.70초가 비어 있었다

Energy Bolt   6서클  1.75 + 0.2 = 1.95
10.70 / 1.95 = 5.4  ->  필러 5방
```

**15초당 시전 4회 -> 9회. 2.25배다.** 이것이 `Bless` 를 버리고 `Energy Bolt` 를 넣은 근거다.

```
오프닝 (몹 1마리당)   Mana Drain 11 + Curse 11          =  22
프록 코어 (15초)      4 + 6 + 9 + 11                    =  30
필러 (15초)           Energy Bolt x5, 20씩 (마무리면 5)      = 100 (~25)
                                                       -----
                                          15초당     152 (~55)

1분 교전
  코어 120 + 오프닝 22 = 142         환급 56% 적용 -> 62
  필러 20방 x 20, 환급 56% 적용 (마무리면 x 5)       -> 176 (~100)
                                                       ----
                          실질 약 238/분 = 4.0 마나/초 (전부 마무리면 2.7)
```

**이동 10~20초 구간은 소모 0** 이고 거기에 Avarhide double mana regen 60%,
`Create Food` 버섯 분당 25 가 얹힌다. 그래도 **메디 없이 2.7~4.0/초는 버겁다.**

> `Energy Bolt` 의 15 마나는 **볼트 뒤 5초 안에 대상이 죽을 때만** 돌아온다 (Grimoire 원문, `bard-mechanics.md`).
> 잡몹 마무리에서만 실질 5 고, 체력 큰 몹에는 20 그대로다. 위 표의 괄호가 전부 마무리인 경우다.

여기에 **이동 10~20초 동안 소모 0** 과 Avarhide double mana regen 60%,
`Create Food` 버섯 분당 25 가 얹힌다.

> **미확인 두 가지**
> 1. Eldritch 환급과 Grimoire 환급이 합산인지 각각 굴리는지. 각각이면 실효 `48%`.
> 2. (해결) `Energy Bolt` 의 15 마나는 5초 안에 죽을 때만 돌아온다. 환급 확률과 중첩되는지는 아직 모른다.

**프록 쿨다운이 더 이상 마나 조절기가 아니다.** 빈 10.7초가 사라졌으니
이제 마나가 실제 상한이다. **필러 5방은 이론치고, 실제로는 마나가 허락하는 만큼만 나간다.**

```
프록 4종      마나가 남는 한 항상.  창당 30마나
Energy Bolt   mana > config__filler_floor 일 때만       <- 여기서 먼저 잘린다
```

`config__filler_floor` 를 오프닝 22 + 프록 코어 30 = **52 이상**으로 둔다.
그래야 필러가 마나를 다 먹어서 다음 몹의 오프닝을 못 거는 일이 없다.

## Wizard's Grimoire 40점

```
Magic Arrow    5    15초마다 첫 시전 +250%
Harm           5    15초마다 첫 시전 +250%
Fireball       5    15초마다 첫 시전 +250% DoT
Lightning      5    15초마다 첫 시전 +200% + 힌더 2.5초
Curse          5    대상에게 60초간 내 모든 주문 +30%
Mana Drain     5    대상에게 60초간 적대주문 환급 +30%
Create Food    5    버섯 25마나 / 60초
Energy Bolt    5    +30% 데미지, 5초 안에 죽으면 15마나 회수
              ----
               40
```

### Bless 를 빼고 Energy Bolt 를 넣은 것이 맞다

| | Bless 3 | Energy Bolt 5 |
|---|---|---|
| 얻는 것 | 팔로워 근접뎀/주문뎀/공속 각 **5%** | 6서클 주문 **+30%**, 마무리 때 실질 5마나 |
| 전체 딜 기여 | 주문뎀 5% x 소환수 63% = **약 +3.2%** | 15초 창마다 시전 횟수가 **약 2배** |
| 비용 | 9마나 / 2분 + 행동 슬롯 1 | 빈 시간을 메운다. 추가 행동 슬롯 없음 |

**프록 4종은 15초 창에 약 6초만 쓴다.** 남는 9초가 그냥 버려지고 있었다.
`Energy Bolt` 가 그 9초를 6서클 주문 +30% 로 채운다는 것이 `Bless` 의 `+3.2%` 와 비교가 안 된다.
실질 5 마나는 마무리 때만이지만, 20 을 다 내도 결론은 같다.

### 필러는 Energy Bolt 지 Flamestrike 가 아니다

Magery 100, Eval 80 (`0.75 + 0.75 x 0.8 = 1.35`), 위키 PvM 공식.

| | Energy Bolt (Grimoire 5) | Flamestrike (Grimoire 0) |
|---|---|---|
| 마나 | 20 (마무리면 5) | 40 |
| 피해 | 32~44 x 1.35 x 1.30 = **56~77**, 평균 67 | 72~96 x 1.35 = **97~130**, 평균 113 |
| 시전 | 1.75 + 0.2 | 2.00 + 0.2 (+ 피해 딜레이 0.5) |
| 마나당 피해 | **3.3** (마무리면 13) | 2.8 |
| 초당 피해 | 34 | **51** |

이 루프는 마나가 먼저 바닥나는 루프다 (`config__filler_floor` 에서 잘린다). 그러면 **마나당 피해**가 기준이고 EB 가 이긴다.
Flamestrike 는 시간당으로는 1.5배지만 마나를 1.8배 빨리 태우고, Grimoire 5 를 EB 에서 빼 와야 DoT 35% 가 붙는다.
잡몹 마무리에서는 EB 가 15 를 돌려받아 마나당 13 으로 벌어진다. **필러는 EB 로 둔다.**
Flamestrike 를 쓰고 싶으면 "마나가 높을 때만 (예: 80 이상) 체력 큰 몹에 한 방" 이라는 별도 분기여야지, 필러 교체가 아니다.


`Magic Reflect` / `Protection` / `Greater Heal` / `Cure` 를 전부 0으로 둔 것도 맞다.
기본 주문은 포인트 없이도 시전되고, 큐어는 쿨 없는 포션이 우선이다.

## Bard Codex 20점 -- 지금 배분이 맞다

```
Self Taught     3    Musicianship 80 대체.  T3(120점)는 낭비 -- printed 가 80뿐
Perfect Pitch   5    성공률 56.1% -> 72.9%
Refrain         5    Barding Break 20% 무시
Ensemble        3    +24%
Reverb          3    +12%
Virtuoso        1    +4%
               ----
                20
```

**이전 판의 `Refrain 5 -> 1` 권고는 철회한다.** 근거가 틀렸다.

`Ensemble` 의 실제 조건은 **`Discord AND (Peace OR Provo)`** 다. 디스코 하나로는 안 켜진다.
Discordance 자체는 브레이크에 안 끊기지만 **Peace / Provo 는 끊긴다.**
따라서 `Refrain` 은 Peace 를 지키는 동시에 **`Ensemble` 가동률을 지킨다.**

### Ensemble 3 -> 5 로 올릴 가치는 거의 없다

난이도 400, Lyric 방어구 무시 42.5% + `Refrain` T3 20% 로 계산하면 Peace 가동률은 약 **62%** 다.

| 2점 이동 | 효과 |
|---|---|
| `Ensemble 3 -> 5` | `+24% -> +40%`, 가동률 62% -> 실효 **+9.9** |
| `Reverb 3 -> 1` | `+12% -> +4%`, 가동률 거의 100% -> 실효 **-8.0** |
| 합 | **+1.9** 본체 데미지 = 전체 약 **+0.7%** |

**움직일 값이 아니다.** 지금 배분을 유지한다.

### 진짜 문제는 배분이 아니라 Peace 가동률이다

`Ensemble` 3점이 값을 하려면 **Peace 가 계속 걸려 있어야 한다.**
난이도 300+ 에서 Peace 지속은 최소값 `15 x 0.8 = 12초` 이고 자기 쿨은 10초다.
**즉 12초마다 다시 걸면 끊김 없이 유지된다.** 이것이 루프에 반드시 들어가야 한다.

Peace 를 가끔 쓰는 제어 수단으로만 다루면 `Ensemble` + `Virtuoso` 4점이 대부분 놀게 된다.

**브레이크가 걸린 대상에게는 Peace 도 Provo 도 못 건다** (인게임 확인됨).
한쪽으로 다른 쪽을 대신할 수 없으므로, 브레이크가 뜨면 난이도 400 기준
**40초 동안 `Ensemble` 과 `Virtuoso` 가 통째로 꺼진다.** `Refrain` 이 막아주는 것이 바로 이 40초다.

## Unholy Symbol 경제

5초당 1개, 최대 `Effective Necro / 10` = **10개**. 30초 사이클에 6개가 차는데
전투용 세 개(4 + 2 + 2 = 8)를 다 쓰면 **사이클당 2개씩 마이너스**다.
그래서 개수만 되면 바로 쓰지 않고, **위에 있는 능력 몫을 남기고** 쓴다.

| 능력 | 비용 | 발동 조건 | 남겨두는 것 |
|---|---|---|---|
| **Blood Oath** | 4 | `>= 4` | 없음. 최우선 |
| **Corpse Skin** | 2 | `>= 4` | 없음. Blood Oath 와 같은 4 라 체인 순서가 우선순위 |
| Evil Omen | 2 | `>= 4` | 없음. 위 둘이 30초에 6개를 다 쓰니 사실상 이동 잉여에서만 |
| Poison Strike | 1 | `>= 1`, Corpse Skin 켜진 동안 + 오프너 뒤 | 없음. 필러 자리라 위는 이미 썼다 |
| Vampiric Embrace | 3 | `>= 9`, 이동 중만 | 6 |

2026-09-27 에 6/8/9/7 → 4/4/1/9. 은행이 늘 차 있어서 Evil Omen 과 Poison Strike 가 거의 안 나가던 것, 그리고 Poison Strike 가 Corpse Skin 을 기다리는 시간을 줄이려고.

전부 `config__symbols_*` 라 사냥터에 맞춰 조정한다. 전투가 짧고 이동이 길면 올리고, 은행이 늘 차 있으면 내린다.

**우선순위 근거** (Necro 100):

| | 효과 | 전체 딜 기여 |
|---|---|---|
| Blood Oath | 팔로워 딜 **+30%** | 63% × 30% = **+18.9%** |
| Corpse Skin | 모든 주문에 25% 질병 DoT | 37% × 25% = +9.3%, **자해 없음** |
| Evil Omen | 주문 +20%, 주문당 25% 확률로 마나/2 자해 | 37% × 20% = +7.4%, 자해 있음 |

**Corpse Skin 이 Evil Omen 보다 위다.** 보너스가 크고 대가가 없다. **둘은 동시에 유지된다** (인게임 확인됨).

**Poison Strike** 는 Corpse Skin 이 깔아둔 질병 틱을 최대 8개 한 번에 터뜨린다. 곧 죽을 몹에서는
같이 사라졌을 딜을 회수하는 셈이라 값을 하고, 마나가 안 들어 **필러 자리**를 쓴다.

**Necro 100 의 실제 순환은 Blood Oath + Corpse Skin 이다.** 30초에 6개가 차고 그 둘이 정확히 6개를 쓴다.
셋이 전부 4 에서 나가므로 체인 순서(Blood Oath → Corpse Skin → Evil Omen)가 곧 우선순위다. Blood Oath 뒤
20초면 Corpse Skin 이 나가고 그때부터 Poison Strike 가 열린다. Evil Omen 은 이동 중 쌓인 잉여로만 돈다.

**안 넣은 것**: Strangle(4)은 Blood Oath 와 심볼을 다투고 모든 딜을 5초 지연시킨다.
Wither(5)는 비공격 주문용 마나만 준다. Pain Spike(5)는 **다음 몹 옆에** 시체가 있어야 한다.

**핫바 Auto-Renew 는 전부 끈다.** 게임이 같은 심볼을 쓰고, 우선순위가 **"least expensive first"** 라
이 빌드엔 정반대다 — Blood Oath 가 맨 마지막에 돈다.

**심볼 개수는 `ingump` 로 숫자로 읽는다.** `"<have>/<max>"` 형식이고 `ingump` 가 부분문자열 매칭이라
`"1/"` 이 `"11/20"` 안에도 잡히므로 **20부터 내려오는 체인**으로 읽는다. 0~20 전수 시뮬레이션으로 검증했다.

## 오프닝은 대상마다 다시 건다

> Curse T3: "Spells cast by caster **against target** have their damage increased by 30%"
> Mana Drain T3: "Increases mana refund chance by 30% for caster's hostile spells **cast against target**"

**둘 다 대상에 걸리는 디버프다.** 몹을 바꾸면 따라오지 않는다. Discordance / Peace 도 마찬가지다.

### 지속시간이 어긋난다

```
베이스 디버프   2분    Curse -5%,  Mana Drain -20 Magic Resist
그리모어 라이더  60초   +30% 데미지,  +30% 환급
```

**디버프 아이콘이 남아 있어도 +30% 두 개는 이미 꺼져 있다.** `getlabel` 로 판정할 수 없다.

### 리스트 두 개로 상태를 표현한다

```
list 'magic_drained_targets'    Mana Drain 완료 serial
list 'magic_cursed_targets'     Curse 완료 serial
timer__magic_window             마지막 Curse 안착 이후 경과

if timer "timer__magic_window" >= cooldown__magic_window        60000
	clearlist 'magic_drained_targets'
	clearlist 'magic_cursed_targets'
	settimer "timer__magic_window" 0
endif

not inlist drained                  -> Mana Drain
inlist drained, not inlist cursed   -> Curse   (안착하면 settimer 0)
inlist cursed                       -> 프록 코어
```

타이머는 **Curse 가 안착할 때마다 0으로** 돌아간다. 한 마리와 싸우는 보통의 경우 만료가 정확히
60초에 맞고, 두 마리면 먼저 건 쪽이 몇 초 일찍 sweep 된다. 주기적 sweep 보다 낫다.

분기 자체가 상태라 `var_magic_stage` 같은 단계 변수가 필요 없다.

**이 두 리스트는 구식 `bard-necro.razor` 에서 가져온 것이다.** 그 파일은 지웠고 (git 이력),
같은 두 리스트가 `bard-necro-enhanced.razor` 의 `OPENER` 에 그대로 산다.

**트레이드오프**: sweep 이 전역이라 방금 건 대상까지 지운다. 동시 교전 1~2마리면 가끔 22마나 손해다.
**대상별 타임스탬프는 산술이 필요해서 못 쓴다.**

**막힘 방지**: 타이머가 아니라 **조건**으로 푼다. Curse 시약이 없거나 4서클 마나가 안 되면
`var__opener_done` 이 그냥 1이 되어 프록과 필러가 라이더 없이 나간다.
살아있는 몹 앞에서 스크립트가 서 있는 것보다 30% 덜 아프게 때리는 쪽이 낫다.

```
var__opener_done = 1  <-  inlist cursed
                     or  var__regs_curse = 0
                     or  mana < config__mana_4th
```

### 구식 스크립트의 버그 (반복하지 말 것)

**두 구식 스크립트가 같은 버그를 갖고 있었다** (둘 다 지웠다, git 이력). `clearlist` 가
**전투 대상이 사라지고 조용해졌을 때만** 돌았다.

한 마리와 60초 넘게 싸우면 Curse 의 `+30%` 가 꺼졌는데도 리스트가 "걸려 있음" 이라고 답해서
**영영 재시전하지 않는다.** 난이도 300~500 몹은 대부분 여기 걸린다.
**만료는 교전 종료가 아니라 시간으로 재야 한다.**

## 꼬이는 지점

| 조합 | 꼬이나 | 이유 |
|---|---|---|
| 디스코 x Curse x Mana Drain | 안 꼬임 | 효과가 전부 다르고 중첩된다 |
| 디스코 x Barding Break | 안 꼬임 | **디스코는 브레이크로 안 끊긴다** |
| **Peace x Barding Break** | **꼬임** | 끊기면 `Ensemble` 조건이 같이 꺼진다. `Refrain` 이 이걸 막는다 |
| 피스 x 공격 | 안 꼬임 | **피스는 데미지로 안 풀린다.** 걸어두고 때려도 된다 |
| **Song x Song** | **꼬임** | **세 곡이 쿨 하나를 공유한다.** 3곡 연창은 곡당 11초씩 걸린다 |
| **Skill -> Song** | **꼬임** | 스킬이 `music` 5초를 세워 송을 밀어낸다. 송이 급하면 스킬을 참는다 |
| Song -> Skill | 안 꼬임 | 송은 `music` 도 스킬 슬롯도 안 세운다. 1.5초 뒤 디스코가 나간다 |
| `clearsysmsg` x `insysmsg` | 위험 | 한 패스 안에서 시전->판정을 끝낸다 |
| 송 x 시전 | **꼬임** | 악기 연주가 시전을 끊는다. `not casting` 필수. 그래서 전투 중엔 안 부른다 |
| **Peace 스킬 x Peace/Provo 송** | **꼬임** | 슬롯 공유. 전투 직후 10초간 두 곡이 막힌다 |
| Peace x Provo | **꼬임** | 서버가 슬롯을 공유한다. 둘 다 쓰려면 10초씩 번갈아야 한다 |

## 설계 결정

**재소환 감지를 하지 않는다. 이동 중에 계속 갱신한다.**

송 쿨이 약 11초뿐이고 전투 사이클마다 이동이 10~20초 있으므로,
이동할 때마다 라운드로빈으로 한 곡씩 부르면 **세 곡이 늘 최근 상태로 유지된다.**
소환수를 언제 다시 뽑든 다음 이동 구간에서 자동으로 버프를 받는다.

이 결정 하나로 아래가 전부 사라진다.

| 없앤 것 | 이유 |
|---|---|
| `list 'sung_followers'` serial 명부 | 추적할 필요가 없다 |
| `findtype` 소환수 훑기 + `noto` 필터 | 적 Lich 오인 문제 자체가 사라진다 |
| `var__resing` 플래그와 우선순위 예외 | 송이 상시 갱신이라 "급한 재시전" 이 없다 |
| 전투 중 3곡 몰아부르기 (약 22초) | 전투 중에는 아예 안 부른다 |

**대가**: 소환수가 전투 중에 죽고 다시 뽑히면 **그 전투가 끝날 때까지는 송 버프가 없다.**
세 곡 각 8.5% 이므로 한 판의 일부 구간에서 그만큼 손해다.
위의 복잡도 전부와 바꿀 만하다.

**라운드로빈은 산술 없이 리터럴 상태값으로 돈다.**

```
if var__song_next = 1
	useskill 'Discordance'
	@setvar! var__song_next 2
elseif var__song_next = 2
	useskill 'Peacemaking'
	@setvar! var__song_next 3
else
	useskill 'Provocation'
	@setvar! var__song_next 1
endif
```

`findbuff "song of ..."` 로 게이트하지 않는다. 15분 버프라 늘 참이어서 갱신이 영영 안 돈다.
**`cooldown "song" = 0` 을 보고 다음 곡을 부른다.**

다만 **곡마다 자기 슬롯을 함께 봐야 한다.** 전투가 막 끝났으면 Peace 슬롯이 10초 남아 있어서
Peace 송과 Provo 송이 둘 다 막힌다. 그때는 그 패스를 거르고 다음 패스에 다시 온다.

```
if cooldown "music" = 0 and cooldown "song" = 0
	if var__song_next = 1 and cooldown "disco" = 0
		... Disco 송 ...   @setvar! var__song_next 2
	elseif var__song_next = 2 and cooldown "peace/provo" = 0
		... Peace 송 ...   @setvar! var__song_next 3
	elseif var__song_next = 3 and cooldown "peace/provo" = 0
		... Provo 송 ...   @setvar! var__song_next 1
	endif
endif
```

이동 구간이 10~20초라 슬롯은 대개 그 안에 풀린다. 못 부른 곡은 다음 이동 때 잡힌다.

**재소환해도 Bless 는 다시 안 건다.** 애초에 Grimoire 에서 뺐다.

## 재소환 -- 설계만, 구현 보류

소환수가 죽으면 딜의 63%가 빠진다. 그런데 사실을 다 모으니 **자동화의 값이 생각보다 작다.**

### 확정 사실 (`bard-mechanics.md`)

- 언데드는 **Vengeful Spirit(심볼 1) 을 켠 뒤** 소환해야 나온다. Fire -> Lich, Earth -> Mummy, Daemon -> Vampire
- 8서클: **마나 50, 시전 6초**, Bloodmoss 필요
- 소환수는 **10초마다 최대 체력 1% 씩 썩어** 맞지 않아도 죽는다. 즉 재소환은 반응이 아니라 **주기 정비**다
- `followers` 는 슬롯 수. Lich 2 = 4

### 판단: 지금은 수동

| 근거 | 내용 |
|---|---|
| **한 세트가 VS + 6초 + 6초, 마나 101** | 교전 중엔 로테이션이 12초 서고 긴급 힐이 끊으면 50 씩 날아간다. 이동 중엔 서 있어야 하므로(`cooldown "walk"`) 다음 몹 앞에 멈춘 순간에만 나간다 -- 수동과 같은 타이밍이다 |
| **뭘 뽑을지는 상황이 정한다** | 듀오 Lich 2 / 솔플 Mummy + Lich / 고 MR Mummy + Air. 스크립트는 파티 구성을 모른다 |
| **썩는 속도가 결정을 사람에게 준다** | 1%/10초면 체력 반이 되는 데 8분이다. "언제 갈아끼울지"는 남은 체력과 다음 몹을 보고 정하는 문제라 임계값 하나로 대신하기 어렵다 |
| **없을 때의 뒷정리는 이미 자동이다** | 송은 다음 이동에서 다시 걸리고, Blood Oath / Vampiric Embrace 는 `followers > 0` 으로 선다. 본체 로테이션은 그대로 돈다 |

구식 두 스크립트도 재소환을 안 했다.

### 나중에 넣는다면 이 모양

이동 중 전용, 소환 종류는 config, VS 를 먼저 켠다.

```
config__resummon 0                      기본 꺼짐
config__summon_spell 'Fire Elemental'
config__followers_want 4                슬롯 수. Lich 2마리

RESUMMON   [MUSHROOM 뒤, BARD SONG 앞]
  var__engaged = 0 and followers < config__followers_want
    mana >= 50 and var__regs_summon = 1          bloodmoss, mandrake, silk, ash
      not targetexists and not casting and cooldown "walk" = 0
        timer "timer__vengeful_spirit" >= 30000  -> hotkey 'Vengeful Spirit', 메시지 확인
        else                                     -> cast config__summon_spell, for 70 폴링, target
```

Bloodmoss 플래그 하나와 `Vengeful Spirit` 핫키(목록에 있음)만 추가하면 된다. 남은 미확인은 **소환 커서가
지점 지정인지 자동 배치인지** 하나뿐이다.

## 쓸 수 있는 구문 (전부 저장소에 선례 있음)

| 구문 | 선례 |
|---|---|
| `not inlist '이름' alias` | `bard-necro-enhanced.razor` OPENER |
| `magic_drained_targets` + `magic_cursed_targets` 2단 오프닝 | `bard-necro-enhanced.razor` OPENER |
| `createlist` / `removelist` / `clearlist` / `pushlist` | 여러 파일 |
| `while findtype ... backpack as` + `@ignore` | `bard-necro-enhanced.razor` INSTRUMENT |
| `not dead X and noto X != "hostile" ...` | `bard-necro-enhanced.razor` COMBAT TARGET CACHE |
| `findbuff "song of discordance"` | `bard-mace.razor:494` |
| `useskill` -> `waitfortarget` -> `target backpack` | `bard-mace.razor:518` |
| `stop` | `bard-necro-enhanced.razor` INSTRUMENT |
| `cooldown "magic arrow" = 0` | `cooldowns.xml` 에 항목 존재 |
| `for 25` + `break` 로 커서 폴링 | `bard-necro-enhanced.razor` PROC CORE, 레퍼런스 `auto-mage.razor:1160` |
| `hotkey 'Vampiric Embrace'` + `hotkey 'Target Self'` | 위키: 자신을 타겟하면 주변 시체를 자동 탐색. **인게임 확인됨** |
| `hotkey 'Drink Heal'` 등 포션 핫키 | Razor 핫키 목록 Potions 항목. 이름 그대로 |
| `hotkey "> Interrupt"` | 휠다운에 물려 쓰던 것. 시전 폴링 안에서 긴급 힐용 |

## 쓰면 안 되는 구문 (선례 없음, 실제로 깨졌던 것들)

- **변수끼리, 또는 변수와 숫자의 크기 비교** (`var__symbols >= config__symbols_blood_oath`). 조건에서 변수는 `=` 만 된다.
  네크로가 한 번도 안 나가던 원인. 수를 세려면 옛 스크립트처럼 **리스트에 항목을 밀어 넣고 `list 'name' >= n`** 으로 비교한다.
  `mana >= config__x` 처럼 **내장 식이 왼쪽**이면 된다.

- 산술 `@setvar! var__n var__n + 1`
- `while <스크립트 변수> <`
- `menu <serial> <변수>` -- 인덱스는 반드시 리터럴
- 조건 안의 괄호
- 주석 안의 세미콜론
- 미선언 변수 (`check.sh` 가 못 잡는다)

## 인게임에서 확인할 것

확인 끝난 것:

- **Effective Barding = 170** (송 메시지 8.5% 실측)
- **Discordance 는 barding break 로 안 끊긴다**
- **Peacemaking 은 데미지로 안 풀린다.** 브레이크로만 풀린다
- **Peace 와 Provo 는 슬롯을 공유한다.** `peace/provo` 한 항목으로 합쳤다
- **Song = 스킬을 백팩에 타겟.** Music 도 슬롯도 세우지 않고, 읽기만 한다
- **Ensemble 조건은 `Discord AND (Peace OR Provo)`**
- **"Your barding skill cooldowns reset." 프록이 존재한다**

추가로 확인된 것:

- **리셋 프록의 출처는 Lyric Aspect 방어구다.** 쿨 측정할 때는 벗는다
- **브레이크 대상에는 Peace / Provo 둘 다 못 건다**
- **시전 시간은 서클별 고정** (1서클 0.50 ~ 8서클 2.50, 회복 0.2초)
- **Song 쿨은 세 곡이 공유하는 별도 계열이다.** `cooldown "music"` 이 아니다

**코드 작성 전에 먼저 할 일**

1. **`cooldowns.xml` 의 `music` 항목을 고친다** (게임 끄고).
   송 트리거를 빼고 `song` 항목을 신설한다. 이걸 안 하면 게이트가 애초에 틀린 값을 읽는다.
2. **`fireball` 항목에 발동 트리거를 넣는다.** 지금은 "다시 준비됨" 메시지만 있어서
   바가 채워지지 않는다. 인게임에서 Fireball 프록이 터질 때 나오는 문구를 받아 적는다.

**남은 측정**

3. **Song 이 바드 스킬 슬롯까지 잠그는가.**
   probe 스크립트는 답을 얻고 지웠다 (git 이력). 다시 재려면 `bard-mechanics.md` 의 테스트 절차대로
   **Lyric 방어구 벗고** 한 번 돌린다.
   실행 중 수동 조작을 하지 않는다 -- 지난 로그가 그것 때문에 오염됐다.
4. **Song 쿨의 정확한 길이.** 위 probe 4단계(약 11초 후 시도)가 답한다.
5. **`Energy Bolt` 의 15마나 회수(5초 안 마무리 때만)가 환급 확률과 중첩되는지.**
   마나 예산이 2.7/초냐 그보다 훨씬 낮냐가 여기서 갈린다.
6. **`Ensemble` / `Reverb` / `Virtuoso` 가 정말 본체 전용인가.**
   포인트 변경 전후로 데미지 트래커의 **소환수 딜 절대값**을 비교한다.

### 확인 대기 (2026-09-27)

- **SELF BUFFS.** 몹이 없고 서 있을 때 (`var__engaged = 0`, `cooldown "walk" = 0`) Reactive Armor 와 Magic Reflection 을 건다.
  통과: 사냥 사이에 버프바에 둘이 붙고, 붙어 있는 동안은 다시 걸지 않는다. 실패: 매 패스 다시 건다 → `findbuff` 이름이 다른 것.
  리플렉트가 소모되면 `[ reflect, off ]` 와 `reflect` 바 30초, 바가 꺼진 뒤 다음 정지 구간에 다시 건다.
- **loadout 배치.** 우하단 한 자리에 새첼 → 루팅 파우치 → 트랩 파우치 5개(x 120~140) 순으로 쌓인다.
  새첼이나 루팅 파우치가 삐져나오면 `loadout.razor` 의 좌표만 조정 (`y 200`, `x 120~140` 은 감으로 잡은 값).

## 참고 링크

- [Magery](https://wiki.uooutlands.com/Magery)
- [Wizard's Grimoire](https://wiki.uooutlands.com/Wizard%27s_Grimoire)
- [Bard Codex](https://wiki.uooutlands.com/Bard_Codex)
