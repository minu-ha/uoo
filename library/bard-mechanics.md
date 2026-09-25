# 바드 메커니즘 레퍼런스

**추측 금지 문서.** 바드 관련 숫자가 필요하면 여기서 인용한다. 여기 없으면 위키를 읽고 여기에 추가한다.
모든 인용문은 위키 원문이다. 해석은 인용문 아래에 따로 적는다.

## 스킬 사용 쿨다운

| | 쿨다운 | 출처 |
|---|---|---|
| **Music (글로벌)** | 5초 | "A player may alternate between using Peacemaking or Provoking and Discordance every 5 seconds" |
| Discordance | 5초 (성공/실패 동일) | "Skill usage cooldown is 5 seconds on both success and failure" |
| Peacemaking | **10초 성공 / 5초 실패** | "Skill usage cooldown is 10 seconds on success and 5 seconds on failure" |
| Provocation | **10초 성공 / 5초 실패** | "Skill usage cooldown is 10 seconds on success and 5 seconds on failure" |
| Barding Song | 10초 | "Casting a Barding Song has a 10 second cooldown that is independent of normal bard skill usage" |

**Peace 와 Provo 는 쿨다운을 공유하지 않는다** (probe 확인. 아래 참조).

**글로벌과 개별은 AND 조건이다.** Music 5초가 지나도 Peace 자기 쿨 10초가 안 지났으면 못 쓴다.

```
if cooldown "Music" = 0 and cooldown "Peace" = 0
```

가능한 사이클:

```
t=0   Discordance      Music 0->5,  Disco 0->5
t=5   Peacemaking      Music 0->5,  Peace/Provo 0->10
t=10  Discordance      Music 0->5,  Disco 0->5
t=15  Provocation      Peace/Provo 쿨이 그때 풀린다
```

### Song 은 스킬을 백팩에 쓴 것이다

별도 명령이 아니다. **바드 스킬을 자기 자신(백팩)에 타겟하면 Song 이다.**

> "What do you wish to pacify? (you may target **yourself for an area effect** or the **ground for a group effect**)"

```
useskill 'Peacemaking'
waitfortarget wait__target
target backpack          <- Song (AoE)
target lasttarget        <- Skill (단일 대상 디버프)
```

저장소의 기존 구현이 이미 이 형태다 (`bard-mace.razor:518`, `bard-archer.razor:228`).

### 세 가지 쿨다운 계열

차단 메시지가 어느 계열인지 알려준다. **이 구분이 모델의 열쇠다.**

| 계열 | 차단 메시지 | 범위 |
|---|---|---|
| **Music 글로벌** | "You must wait a few moments to **use another skill**." | 모든 바드 스킬. 5초 |
| **Barding Song** | "You must wait a few moments before performing **another barding song**." | **세 곡 전체가 공유.** 11초 |
| **Peace / Provo 슬롯** | "You must wait a few moments before you may **provoke or pacify another creature**." | **공유.** 10초. `cooldowns.xml` 에서 `Peace/Provo` 한 항목으로 합쳤다 |

Discordance 는 자기 슬롯 5초를 따로 쓴다 (전용 차단 메시지는 확인되지 않았다).

`Peace Song -> Disco Skill -> Disco Song` 에서 마지막이 "another barding song" 으로 막혔다.
**다른 곡이 다른 곡을 막는다 = 곡끼리 하나의 쿨을 공유한다.**

### `cooldown "..."` 은 서버 값이 아니다

`config/<이름>/classicuo/<캐릭터>/cooldowns.xml` 에 **직접 정의한 메시지 트리거 타이머**다.
`cooldown "Music"` 이 알려주는 것은 서버 쿨이 아니라 **내가 설정한 값**이다.
숫자가 이상하면 서버가 아니라 이 파일을 의심한다.

**파일은 게임 종료 시 덮어쓰기 되므로 게임을 끈 상태에서만 수정한다.**

#### 현재 `Music` 엔트리에 버그가 있다

```xml
<cooldownentry name="Music" ...>
  <trigger duration="5"  triggertext="play successfully" />        <- 바드 스킬 성공
  <trigger duration="5"  triggertext="fail to incite anger" />
  <trigger duration="5"  triggertext="fail to discord" />
  <trigger duration="10" triggertext="under the effect of a song" />   <- SONG
  <trigger duration="5"  triggertext="fail to pacify" />
  <trigger duration="0"  triggertext="Your barding skill cooldowns" /> <- Lyric 리셋
</cooldownentry>
```

**스킬 글로벌(5초)과 송 쿨(10초)이 한 항목에 섞여 있다.**
나중에 온 스킬 트리거가 송의 남은 시간을 5초로 **덮어쓴다.**

```
t=0   Song          "under the effect of a song"  -> Music = 10초 (t=0~10)
t=1   Disco Skill   "play successfully"           -> Music =  5초 (t=1~6)   <- 덮어씀
t=6   Music = 0     그런데 실제 송 쿨은 t=10 까지 남아 있다
t=6   Song 시도     -> "another barding song"      X
```

**"Music 이 0인데 송이 안 나간다" 의 원인이 정확히 이것이다.**

반대 방향 피해도 있다. 송을 부르면 `Music` 이 10초 잡히므로,
`cooldown "Music" = 0` 으로 게이트한 스크립트는 **서버가 허용하는 바드 스킬을 10초 동안 참는다.**

#### 고칠 형태 (게임 끄고 수정)

`Music` 에서 송 트리거를 빼고, 송 전용 항목을 새로 만든다.

```xml
<!-- Music 에서 이 줄을 삭제 -->
<trigger triggertype="SysMessage" duration="10" triggertext="under the effect of a song" />

<!-- 새 항목 추가 -->
<cooldownentry name="Song" defaultcooldown="0" cooldownbartype="Regular" hue="53" hidewheninactive="False">
  <trigger triggertype="SysMessage" duration="11" triggertext="under the effect of a song" />
</cooldownentry>
```

결과:

```
cooldown "Music"   바드 스킬 글로벌 5초만
cooldown "Song"    세 곡이 공유하는 11초
```

`Song` 에 Lyric 리셋 트리거(`"Your barding skill cooldowns"`)를 **넣지 않는다.**
메시지가 "barding **skill** cooldowns" 라 송까지 리셋하는지 확인되지 않았다.
넣지 않으면 가끔 조금 더 기다릴 뿐이고, 잘못 넣으면 매번 헛시전한다.

#### 개별 스킬 항목의 송 트리거는 보류

`Discord` / `Peace` / `Provo` 에는 각각 자기 곡 트리거가 11초로 들어가 있다.

```xml
<trigger duration="11" triggertext="effect of a song of discordance" />
```

이것은 **"Disco 송이 Disco 스킬을 11초 잠근다"** 는 가정인데 아직 확인되지 않았다.
사실이 아니면 Disco 를 11초 동안 헛되이 참게 되고, 그만큼 `Ensemble` 가동률이 깎인다.
**probe 3단계가 답할 때까지 그대로 둔다** (보수적).

### 쿨다운 모델 (확정)

```
Song    요구:  Music = 0   AND   Song = 0   AND   <그 곡의 슬롯> = 0
        설정:  Song 11초만.   Music 도 슬롯도 세우지 않는다

Skill   요구:  Music = 0   AND   <그 스킬의 슬롯> = 0
        설정:  Music 5초   +   <그 스킬의 슬롯>

슬롯:   Discord         5초   단독
        Peace / Provo   10초  **공유**
```

### 한 문장으로

**모든 바딩 행동이 같은 관문 하나를 통과한다.**

```
Music = 0   AND   <그 스킬의 슬롯> = 0
```

**송만 여기에 `Song = 0` 을 하나 더 본다.**
읽는 조건은 거의 같고, **다른 것은 무엇을 세우느냐뿐이다.**

```
Skill  ->  Music 5초  +  슬롯을 세운다
Song   ->  Song 11초만 세운다        <- Music 도 슬롯도 건드리지 않는다
```

**"송은 스킬을 빌려 쓰되 소모하지 않는다."**

- 스킬이 Music 을 세우므로 **스킬 -> 송이 막힌다**
- 송은 Music 을 안 세우므로 **송 -> 스킬은 통과한다**
- 스킬이 슬롯을 세우므로 **Peace 스킬 -> Peace 송이 막힌다**
- 송은 슬롯을 안 세우므로 **Peace 송 -> Peace 스킬은 통과한다**

#### 근거 (전부 인게임 실측)

| 시퀀스 | 결과 | 설명 |
|---|---|---|
| Song -> Disco Skill (1.5초 후) | **성공** | 송이 Music 도 슬롯도 안 세운다. same/other 둘 다 통과 |
| Song -> Peace Skill | **성공** | 같음 |
| Song -> Song (즉시) | "another barding song" | Song 쿨 공유 |
| Disco Skill -> Song (즉시) | "use another skill" | **송이 Music 을 본다** |
| Song(t=0) -> Disco Skill(t=9) -> Song(t=11) | 차단 | Song 은 풀렸지만 Disco 가 세운 Music 이 t=14 까지 |
| **Peace Skill -> Peace Song** (Music 풀린 뒤) | **"provoke or pacify another creature"** | **송이 자기 슬롯을 읽는다** |
| **Peace Skill -> Disco Song** | **성공** | 슬롯이 다르면 통과 |
| **Peace Song -> Peace Skill** | **성공** | **송은 슬롯을 세우지 않는다** |
| Song -> 차단된 Song -> Peace Skill | 차단 | **차단된 시도도 Music 을 태운다** |

**마지막 줄이 함정이다.** 송 쿨에 막힌 시도가 스킬 쿨을 소비하기 때문에,
"차단된 송 바로 다음의 스킬 판정" 을 보고 "송이 스킬을 잠근다" 고 오독하기 쉽다. 실제로 한 번 틀렸다.

#### 루프에 주는 규칙

**송을 불러야 하는 상황에서는 바드 스킬을 참는다.**
송 쿨이 풀리기 직전에 디스코를 쓰면 Music 5초가 걸려 송이 그만큼 더 밀린다.
재소환 감지로 3곡을 다시 불러야 할 때가 정확히 이 경우다.

```
var__resing = 1 이면  ->  Song 블록만 돌리고 바드 스킬 블록은 건너뛴다
```

### Peace 와 Provo 는 슬롯을 공유한다

전용 차단 메시지가 있다.

> "You must wait a few moments before you may **provoke or pacify another creature**."

한때 이 문서가 "공유하지 않는다" 고 적었던 것은 **로컬 Razor 엔트리만 보고 내린 결론**이었다.
`Provo` 엔트리가 Peace 메시지에 반응하지 않으니 `provo READY` 로 보였을 뿐, **서버는 막는다.**
위키의 원래 서술이 맞았다.

**`cooldowns.xml` 에서 `Peace/Provo` 한 항목으로 합쳤다.** 서버가 타이머 하나를 쓰는데
칸을 둘로 두면 화면만 차지하고 값도 틀린다.

합치기 전에는 기존 스크립트가 **틀린 값을 읽고 있었다** -- 직전에 Peace 를 썼는데
`Provo` 가 READY 로 나와서 헛시전하고 `Music` 만 태웠다.
`script/` 전체의 `cooldown "Peace"` / `cooldown "Provo"` 30곳을 `cooldown "Peace/Provo"` 로 바꿨다.

### "Your barding skill cooldowns reset."

**출처는 Lyric Aspect 방어구다.** 모든 바드 쿨다운을 즉시 초기화한다.

**Song 쿨도 같이 초기화된다** (인게임 확인됨). `song song disco` 가 가능하다.

**쿨다운을 측정할 때는 Lyric 방어구를 벗는다.** 착용 중이면 리셋이 끼어들어 실제 길이가 안 보인다.
송 메시지가 그대로 알려준다 -- **`8.5%` 면 착용 중, `6.8%` 면 벗은 상태.**

**스크립트에 주는 영향**: 쿨다운이 예고 없이 0이 될 수 있다.
따라서 **자체 `timer__` 로 바드 쿨을 흉내내지 않는다.** 게임이 주는 `cooldown "..."` 을 직접 읽어야
리셋 프록의 이득을 가져간다.

### Song 버프 감지

```
findbuff "song of discordance"
findbuff "song of provocation"
findbuff "song of peacemaking"
```

15분 만료를 직접 세지 않는다. 저장소 기존 구현(`bard-mace.razor:494`)이 이 방식이다.

### 이 저장소의 `cooldowns.xml` 최종 형태

```
Skill        일반 스킬 전부 + 바드 5초 트리거 4개 + 리셋
Music     5s play successfully / fail to incite anger / fail to discord / fail to pacify
          0s Your barding skill cooldowns
Discord   5s successfully, disrupting your opponent / fail to discord / briefly discording
          0s Your barding skill cooldowns
Peace/Provo
         11s pacifying your target / successfully, briefly pacifying / play successfully, provoking
          5s fail to pacify any nearby creatures / fail to pacify your opponent / fail to incite anger
          0s Your barding skill cooldowns
Song     11s under the effect of a song
          0s Your barding skill cooldowns
```

항목 순서는 **바가 자주 뜨는 순서**로 정렬했다.
`Skill` -> `Music` -> `Discord` -> `Peace/Provo` -> `Song`.

### `Skill` 과 `Music` 의 관계

**서버는 스킬 게이트가 하나다.** `Music` 은 그중 바드 부분만 따로 보는 이름일 뿐이다.
실제로 **Music 이 도는 동안 Animal Lore 같은 다른 스킬도 안 먹는다.**

그래서 `Skill` 항목에도 바드 5초 트리거 네 개와 리셋을 넣었다.

```
cooldown "Skill"   아무 스킬이라도 쿨이면 1
cooldown "Music"   바드 때문에 쿨이면 1      <- 전투 루프가 쓰는 것
```

전투 루프는 바드 외 스킬을 안 쓰므로 `Music` 으로 충분하다.
**루프에 Animal Lore 나 Herding 크룩 같은 비바드 스킬을 넣게 되면 `Skill` 로 바꿔야 한다.**

고친 내역과 이유:

- `Music` 에서 `"under the effect of a song" 10초` 를 **뺐다.** 스킬 글로벌 항목에 송 쿨 값이
  들어가 있어서, 뒤따르는 5초 스킬 트리거와 서로 덮어썼다.
  이것이 "Music 이 0인데 송이 안 나간다" 의 원인이었다.
- `Song` 을 **신설했다.** 곡끼리 공유하는 11초 + Lyric 리셋.
- `Discord` / `Peace` / `Provo` 에서 각자의 `"effect of a song of ..." 11초` 를 **뺐다.**
  송은 자기 스킬을 잠그지 않는다. 두면 서버가 1.5초에 허용하는 것을 11초 참는다.
- `Peace` 에서 `"You play successfully, briefly pacifying one or more nearby creatures." 5초` 를 **뺐다.**
  같은 메시지에 `"successfully, briefly pacifying" 11초` 가 이미 걸려 있어 둘이 충돌했다.
- `Peace` 와 `Provo` 를 **`Peace/Provo` 한 항목으로 합쳤다.** 서버가 슬롯을 공유한다.
  `script/` 의 참조 30곳도 같이 바꿨다.
- **`Skill` 에 바드 5초 트리거를 넣었다.** 서버 스킬 게이트가 하나라
  바드가 도는 동안 다른 스킬도 막힌다.
- 바가 자주 뜨는 순서로 **재정렬했다**: `Skill` -> `Music` -> `Discord` -> `Peace/Provo` -> `Song`.

**이 파일은 게임 종료 시 덮어쓰기 된다. 반드시 게임을 끈 상태에서 수정한다.**
켜둔 채로 고치면 종료할 때 통째로 날아간다 (실제로 한 번 날아갔다).


## Barding Song (AoE 버프)

세 곡 전부 **"Players and their Followers"** 에 걸린다. 소환수가 받는다.

| 곡 | 효과 | 출처 |
|---|---|---|
| Discordance | `5% x (Effective Barding / 100)` **Damage Resistance** | "Provides a (5% * (Effective Barding Skill / 100)) Damage Resistance bonus to Players and their Followers" |
| Peacemaking | `5% x (Effective Barding / 100)` **Healing Received** | "Provides a (5% * (Effective Barding Skill / 100)) Healing Amounts Received Bonus to Players and their Followers" |
| Provocation | `5% x (Effective Barding / 100)` **Damage Bonus** | "Provides a (5% * (Effective Barding Skill / 100)) Damage Bonus to Players and their Followers" |

- 지속: **15분** -- "All AoE Barding Song Buffs durations are 15 minutes"
- **재소환한 소환수에는 안 걸려 있다.** 다시 불러야 한다 (인게임 확인됨).
- 스킬 사용(디스코/피스/프로보)과는 다른 것이다. 혼동하지 말 것.

## Discordance 디버프

> "The Discorded debuff increases damage taken from all sources by 25%, and reduces damage done by 25%."
> 스케일: "(Bard's Printed Discordance Skill / 120) * 25 as %"

**printed 스킬 기준이다.** Effective 가 아니다. 디스코 80이면 `80/120 x 25 = 16.7%`.

## Effective Barding Skill

> "A player's Effective Discordance Skill is their (Discordance Skill + Instrument Skill Bonuses + Applicable Instrument Slayer Bonuses + Supplemental Skill Bonuses + Lyric Aspect Armor Bonus)."
> "total bonuses from these sources cannot exceed the player's **Musicianship skill level**"

**보너스 합계의 상한이 Musicianship 이다.** 이것이 Musicianship 을 버릴 수 없는 이유다.

**`Self Taught` 의 대체값이 이 상한에도 적용된다** (인게임 확인됨).

### 실측값: Effective Barding = 170

Song 시전 메시지가 값을 그대로 알려준다. 송 공식이 `5% x (Effective Barding / 100)` 이므로
표시된 퍼센트에 20 을 곱하면 Effective Barding 이다.

| 장비 | 송 표시 | Effective Barding |
|---|---|---|
| Lyric Aspect 방어구 착용 | `8.5%` | **170** |
| Lyric 벗음 | `6.8%` | 136 |

차이 **34** 가 Lyric Aspect Armor Bonus 다. **실전값은 170 을 쓴다.**
`80 printed + 80 cap = 160` 이라는 계산보다 높은데, 상한이 정확히 어떻게 잡히는지는
확인되지 않았다. **추론값 대신 이 실측값을 쓴다.** 장비를 바꾸면 송 메시지를 다시 읽는다.

## 바딩 지속시간

| 스킬 | 공식 |
|---|---|
| Peacemaking | `(60초 - 몹 난이도) x (Effective Barding / 100)`, 최소 `15 x (Musicianship / 100)` 초 |
| Provocation | `(60초 - 최고 몹 난이도) x (Effective Barding / 100)`, 최소 `15 x (Musicianship / 100)` 초 |

**난이도 300~500 구간에서는 앞 항이 음수라 최소값이 지배한다.**
Musicianship 80 이면 `15 x 0.8 = 12초`. Musicianship 을 120으로 올려도 18초다.
**이 구간에서 Musicianship 을 올려 얻는 지속시간은 6초뿐이다.**

## Barding Break

> "for every 1 second that passes there is a ((CreatureDifficulty / 100) * 1%) chance they will suffer a 'Barding Break'"
> "that will last for (CreatureDifficulty / 10) seconds"

난이도 400 기준: **초당 4% 확률**, 걸리면 **40초** 지속.

무엇을 끊는가:

- Peacemaking: "Pacified creatures may suffer a barding break, **ending the pacify effect prematurely**, and temporarily preventing them from being pacified again for a limited time."
- Provocation: "Provoked creatures may suffer a barding break, **ending the provocation effect prematurely**"
- Discordance: **끊기지 않는다. 한 번 걸면 계속 걸려 있다** (인게임 확인됨).
  위키 Discordance 문서에 barding break 언급이 없는 것과 일치한다.

**`Ensemble` 은 그래도 브레이크에 걸린다.** 조건이 `Discord AND (Peace OR Provo)` 라서,
디스코가 살아 있어도 **Peace / Provo 가 끊기면 Ensemble 이 꺼진다.**
따라서 `Refrain`(브레이크 무시)은 Peace / Provo 를 지키는 동시에 **Ensemble 가동률을 지킨다.**

**브레이크가 걸린 대상에게는 Peace 도 Provo 도 걸 수 없다** (인게임 확인됨).
한쪽으로 다른 쪽을 대신할 수 없다. 난이도 400 기준 **40초 동안 Ensemble 이 완전히 꺼진다.**

## Peacemaking 이 하는 일

> "Pacified creatures will not move, perform melee attacks, cast spells, or use most abilities"

**데미지를 받아도 안 풀린다.** 풀리는 것은 **Barding Break 뿐**이다.
(위키 어디에도 "damage breaks pacify" 가 없다. 클래식 UO 규칙을 여기에 적용하지 말 것.)

따라서 **피스를 걸어두고 때려도 된다.** 소환수가 때려도 안 풀린다.
피스와 공격 로직을 배타로 만들 이유가 없다.

## Bard Codex

> 요구조건: "Players must have 2 or more skills of at least 80 Musicianship, Peacemaking, Provocation, Discordance skill or above"

**총 20 포인트.** 티어 비용은 증분 `1/2/2` = 누적 **`T1=1 / T2=3 / T3=5`**.

| 업그레이드 | 효과 (T1 / T2 / T3) | 팔로워 적용 |
|---|---|---|
| **Sing Your Own Praises** | "Your bard song effects are increased by (40% / 120% / 200%) of normal **for you and your followers** but are reduced by (20% / 60% / 100%) **for others**" | **O** |
| Ensemble | "Gain Damage Bonus of (8% / 24% / 40%) towards creatures that you have Discorded" -- **실제 조건은 Discord **AND** (Peace **OR** Provo). 두 개가 걸려 있어야 한다** (인게임 확인됨) | 언급 없음 |
| Reverb | "Gain Damage Bonus of (4% / 12% / 20%) towards the target or targets of your most recent successful barding skill usage" | 언급 없음 |
| Virtuoso | "Damage Bonus and Damage Resistance against Barded Creatures" -- `5% / 15% / 25%` x (lowest skill / 100) | 언급 없음 |
| Perfect Pitch | "Increases barding success chances by (6% / 18% / 30%) of normal" | -- |
| Refrain | "Your barding effects have a (4% / 12% / 20%) chance to ignore any Barding Breaks" | -- |
| Revolution Song | "Your provoked creatures inflict (40% / 120% / 200%) more damage" | -- |
| Self Taught | "Player can use up to (40 / 80 / 120) points of their **lowest printed skill** amongst Discordance, Peacemaking, Provocation to replace Musicianship requirements" | -- |

**팔로워에게 적용된다고 명시된 코덱스는 `Sing Your Own Praises` 하나뿐이다.**
`Ensemble` / `Reverb` / `Virtuoso` 는 "you" / "the player" 로만 쓰여 있다.
소환수가 딜의 60% 이상인 빌드에서는 이 구분이 배분을 뒤집는다.

**`Sing Your Own Praises` 의 `for others` 페널티**: 다른 플레이어와 **그 사람의 팔로워**가
내 송에서 받는 효과를 깎는다. 테이머 듀오면 테이머 펫이 여기 걸린다.
T3 는 `-100%` 라 테이머 쪽이 내 송을 전혀 못 받는다.

**`Self Taught` 상한**: "lowest printed skill" 이 기준이다.
Disco/Peace/Provo 가 전부 80이면 T3(120점)를 찍어도 **80밖에 못 쓴다.** T2(3점)가 상한이다.

## 바딩 성공률

> "Increases barding success chances by (6% / 18% / 30%) of normal" -- Perfect Pitch

최소 성공률 `33% x (Effective Barding / 100)`. Effective 170 이면 `56.1%`.
`Perfect Pitch` T3 를 얹으면 `56.1% x 1.3 = 72.9%`.

## 이 캐릭터의 확정 수치 (Effective Barding 170)

| 항목 | 값 | 출처 |
|---|---|---|
| Barding Song 세 곡 각각 | **8.5%** (나 + 팔로워) | 송 메시지 실측 |
| Discordance 디버프 | printed 80 -> `80/120 x 25 = ` **16.7%** | printed 기준 |
| Discordance 지속 | **1분 21초 ~ 1분 57초** | 실측. 장비/대상에 따라 변동 |
| Peace / Provo 최소 지속 | `15 x 0.8 = ` **12초** | 난이도 300+ 에서 이 값이 지배 |
| 바딩 최소 성공률 | **56.1%**, Perfect Pitch T3 포함 **72.9%** | |
| Barding Break (난이도 400) | 초당 **4%**, 걸리면 **40초** | **Peace / Provo 만** 끊는다 |

## Magery 프록은 게임이 메시지로 알려준다

`cooldowns.xml` 에 이미 잡혀 있다. **자체 `timer__` 로 15초를 세지 않는다.**

| 항목 | 프록 발동 | 다시 준비됨 |
|---|---|---|
| `MagicArrow` | "magic arrow activated" | "cast a wizardry magic arrow spell again" |
| `Harm` | "harm activated" | "cast a wizardry harm spell again" |
| `Lightning` | "lightning spell hinders" | "cast a wizardry lightning spell again" |
| `Fireball` | **트리거 없음** | "You may now cast a wizardy fireball spell" (게임 원문의 오타 그대로) |

스크립트는 `cooldown "MagicArrow" = 0` 처럼 바로 읽으면 된다.

> **`Fireball` 항목이 불완전하다.** 발동 메시지 트리거가 없어서 바가 채워지지 않는다.
> 인게임에서 Fireball 프록이 터질 때 나오는 문구를 받아 적어 트리거로 넣어야 한다.

**`Energy Bolt` 는 쿨다운 항목이 필요 없다.** 업그레이드가
"Damage increased by 30%, recovers 15 mana" 로 **조건 없는 상시 효과**다.
15초 창 같은 것이 없어서 순수 필러로 쓸 수 있다.

## Magery 시전 시간 (마나 예산 계산용)

| 서클 | 시전 | 서클 | 시전 |
|---|---|---|---|
| 1 | 0.50초 | 5 | 1.50초 |
| 2 | 0.75초 | 6 | 1.75초 |
| 3 | 1.00초 | 7 | 2.00초 |
| 4 | 1.25초 | 8 | 2.50초 |

> "Casting recovery time is **0.2 seconds**" -- 시전 사이 고정 딜레이

## 자주 틀렸던 것

| 틀린 생각 | 사실 |
|---|---|
| 피스는 데미지를 받으면 풀린다 | **아니다.** Barding Break 로만 풀린다 |
| Provocation 은 안 찍었다 | **찍었다.** Self Taught 가 Musicianship 을 대체해서 Disco/Peace/Provo 80/80/80 구성이다 |
| Musicianship 은 Self Taught 로 완전히 대체된다 | **"requirements" 대체다.** 보너스 상한에도 적용되는지 미확인 |
| Vampire Thrall 은 근접딜러다 | **주문딜러다.** "Spell Damage: 26 - 32" |
| Fury 는 분당 5% | **30초당 5%, 최대 +30%** -- 3분이면 캡 |
| Music 쿨만 보면 된다 | **글로벌 5초 + 개별 쿨의 AND 조건이다** |
| Discordance 는 Effective 로 스케일 | **printed 스킬로 스케일한다** (`printed / 120 x 25%`) |
| 소환수도 Virtuoso / Ensemble 을 받는다 | **팔로워 명시는 `Sing Your Own Praises` 뿐이다** |
| 송은 스킬 쿨과 완전히 무관하다 | **단방향이다.** 송->스킬은 되고 스킬->송은 안 된다 |
| Discordance 도 barding break 로 끊긴다 | **안 끊긴다.** 브레이크는 Peace / Provo 만 끊는다 |
| Self Taught 는 요구조건만 대체한다 | **Effective Barding 보너스 상한에도 적용된다.** 실측 170 |
| Peace 와 Provo 는 쿨을 공유한다 | **공유하지 않는다.** Peace 성공 직후에도 provo READY |
| Song 은 별도 명령이다 | **스킬을 백팩에 타겟한 것이다.** 땅에 타겟하면 group effect |
| Song 과 Skill 은 서로 막는다 | **비대칭이다.** 송은 Music 과 슬롯을 읽기만 하고 쓰지 않는다 |
| Peace 와 Provo 는 슬롯이 따로다 | **공유한다.** 로컬 엔트리가 서로를 반영하지 않아 착각했다 |
| 차단된 시도는 아무 쿨도 안 태운다 | **Music 을 태운다.** 차단된 송 다음의 스킬 판정을 믿지 말 것 |
| Ensemble 은 디스코만 있으면 된다 | **Discord AND (Peace OR Provo).** 두 개가 걸려야 한다 |
| 바드 쿨은 예측 가능하다 | **"Your barding skill cooldowns reset." 프록이 있다** (Lyric 방어구). 측정할 땐 벗는다 |
| Song 쿨은 `cooldown "Music"` 이다 | **아니다. 별도 계열이다.** 지금 `Music` 항목이 둘을 섞어서 덮어쓰기 버그가 있다 |
| `cooldown "..."` 은 서버 값이다 | **아니다. `cooldowns.xml` 의 내 메시지 트리거다.** 숫자가 이상하면 이 파일을 본다 |
| 프록 15초는 타이머로 센다 | **게임이 메시지로 알려준다.** `cooldown "MagicArrow"` 등을 읽는다 |
| 브레이크 중엔 Provo 로 Ensemble 을 살린다 | **못 한다.** 브레이크 대상엔 Peace 도 Provo 도 안 걸린다 |

## 참고 링크

- [Musicianship](https://wiki.uooutlands.com/Musicianship) -- Barding Song, barding break 공식
- [Discordance](https://wiki.uooutlands.com/Discordance) -- 디버프 공식, Effective Barding 정의
- [Peacemaking](https://wiki.uooutlands.com/Peacemaking) -- 지속시간, 쿨다운
- [Provocation](https://wiki.uooutlands.com/Provocation)
- [Bard Codex](https://wiki.uooutlands.com/Bard_Codex)
