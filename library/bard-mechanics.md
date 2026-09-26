# 바드 메커니즘 레퍼런스

**추측 금지 문서.** 바드 관련 숫자가 필요하면 여기서 인용한다. 여기 없으면 위키를 읽고 여기에 추가한다.
모든 인용문은 위키 또는 공식 패치노트 원문이다. 해석은 인용문 아래에 따로 적는다.

## 스킬 사용 쿨다운

| | 쿨다운 | 출처 |
|---|---|---|
| **Music (글로벌)** | 5초 | "A player may alternate between using Peacemaking or Provoking and Discordance every 5 seconds" |
| Discordance | 5초 (성공/실패 동일) | "Skill usage cooldown is 5 seconds on both success and failure" |
| Peacemaking | **10초 성공 / 5초 실패** | "Skill usage cooldown is 10 seconds on success and 5 seconds on failure" |
| Provocation | **10초 성공 / 5초 실패** | "Skill usage cooldown is 10 seconds on success and 5 seconds on failure" |
| Barding Song | 10초 | "Casting a Barding Song has a 10 second cooldown that is independent of normal bard skill usage" |

**Peace 와 Provo 는 슬롯을 공유한다.** `cooldowns.xml` 에서 `peace/provo` 한 항목으로 합쳤다.

**글로벌과 개별은 AND 조건이다.** Music 5초가 지나도 Peace 자기 쿨 10초가 안 지났으면 못 쓴다.

```
if cooldown "music" = 0 and cooldown "peace/provo" = 0
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

저장소의 기존 구현이 이미 이 형태다 (`bard-mace.razor:518`, `bard-necro-enhanced.razor` BARD SONG).

### 세 가지 쿨다운 계열

차단 메시지가 어느 계열인지 알려준다. **이 구분이 모델의 열쇠다.**

| 계열 | 차단 메시지 | 범위 |
|---|---|---|
| **Music 글로벌** | "You must wait a few moments to **use another skill**." | 모든 바드 스킬. 5초 |
| **Barding Song** | "You must wait a few moments before performing **another barding song**." | **세 곡 전체가 공유.** 11초 |
| **Peace / Provo 슬롯** | "You must wait a few moments before you may **provoke or pacify another creature**." | **공유.** 10초. `cooldowns.xml` 에서 `peace/provo` 한 항목으로 합쳤다 |

Discordance 는 자기 슬롯 5초를 따로 쓴다 (전용 차단 메시지는 확인되지 않았다).

`Peace Song -> Disco Skill -> Disco Song` 에서 마지막이 "another barding song" 으로 막혔다.
**다른 곡이 다른 곡을 막는다 = 곡끼리 하나의 쿨을 공유한다.**

### `cooldown "..."` 은 서버 값이 아니다

`config/<이름>/classicuo/<캐릭터>/cooldowns.xml` 에 **직접 정의한 메시지 트리거 타이머**다.
`cooldown "music"` 이 알려주는 것은 서버 쿨이 아니라 **내가 설정한 값**이다.
숫자가 이상하면 서버가 아니라 이 파일을 의심한다.

**파일은 게임 종료 시 덮어쓰기 되므로 게임을 끈 상태에서만 수정한다.**

#### 현재 `music` 엔트리에 버그가 있다

```xml
<cooldownentry name="music" ...>
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

반대 방향 피해도 있다. 송을 부르면 `music` 이 10초 잡히므로,
`cooldown "music" = 0` 으로 게이트한 스크립트는 **서버가 허용하는 바드 스킬을 10초 동안 참는다.**

#### 고칠 형태 (게임 끄고 수정)

`music` 에서 송 트리거를 빼고, 송 전용 항목을 새로 만든다.

```xml
<!-- Music 에서 이 줄을 삭제 -->
<trigger triggertype="SysMessage" duration="10" triggertext="under the effect of a song" />

<!-- 새 항목 추가 -->
<cooldownentry name="song" defaultcooldown="0" cooldownbartype="Regular" hue="53" hidewheninactive="False">
  <trigger triggertype="SysMessage" duration="11" triggertext="under the effect of a song" />
</cooldownentry>
```

결과:

```
cooldown "music"   바드 스킬 글로벌 5초만
cooldown "song"    세 곡이 공유하는 11초
```

`song` 에 Lyric 리셋 트리거(`"Your barding skill cooldowns"`)를 **넣지 않는다.**
메시지가 "barding **skill** cooldowns" 라 송까지 리셋하는지 확인되지 않았다.
넣지 않으면 가끔 조금 더 기다릴 뿐이고, 잘못 넣으면 매번 헛시전한다.

#### 개별 스킬 항목의 송 트리거는 보류

`disco` / `Peace` / `Provo` 에는 각각 자기 곡 트리거가 11초로 들어가 있다.

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

**전투 중에는 송이 거의 안 나간다.** 디스코와 피스가 `music` 을 5초씩 계속 세우기 때문이다.
게다가 악기 연주는 시전을 끊어 주문을 날려먹는다.

그래서 `bard-necro-enhanced` 는 **송을 이동 구간에서만 부른다.**
이동 10~20초 동안 `music` 이 비어 있고 어차피 아무것도 안 하고 있다.

### Peace 와 Provo 는 슬롯을 공유한다

전용 차단 메시지가 있다.

> "You must wait a few moments before you may **provoke or pacify another creature**."

한때 이 문서가 "공유하지 않는다" 고 적었던 것은 **로컬 Razor 엔트리만 보고 내린 결론**이었다.
`Provo` 엔트리가 Peace 메시지에 반응하지 않으니 `provo READY` 로 보였을 뿐, **서버는 막는다.**
위키의 원래 서술이 맞았다.

**`cooldowns.xml` 에서 `peace/provo` 한 항목으로 합쳤다.** 서버가 타이머 하나를 쓰는데
칸을 둘로 두면 화면만 차지하고 값도 틀린다.

합치기 전에는 기존 스크립트가 **틀린 값을 읽고 있었다** -- 직전에 Peace 를 썼는데
`Provo` 가 READY 로 나와서 헛시전하고 `music` 만 태웠다.
`script/` 전체의 `cooldown "Peace"` / `cooldown "Provo"` 30곳을 `cooldown "peace/provo"` 로 바꿨다.

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
`skill` -> `music` -> `disco` -> `peace/provo` -> `song`, 그 뒤에 이 루프가 읽는 바 순서로 `magic arrow` -> `harm` -> `fireball` -> `lightning` -> `mush` -> `heal pot`.

### `skill` 과 `music` 의 관계

**서버는 스킬 게이트가 하나다.** `music` 은 그중 바드 부분만 따로 보는 이름일 뿐이다.
실제로 **Music 이 도는 동안 Animal Lore 같은 다른 스킬도 안 먹는다.**

그래서 `skill` 항목에도 바드 5초 트리거 네 개와 리셋을 넣었다.

```
cooldown "skill"   아무 스킬이라도 쿨이면 1
cooldown "music"   바드 때문에 쿨이면 1      <- 전투 루프가 쓰는 것
```

전투 루프는 바드 외 스킬을 안 쓰므로 `music` 으로 충분하다.
**루프에 Animal Lore 나 Herding 크룩 같은 비바드 스킬을 넣게 되면 `skill` 로 바꿔야 한다.**

고친 내역과 이유:

- `music` 에서 `"under the effect of a song" 10초` 를 **뺐다.** 스킬 글로벌 항목에 송 쿨 값이
  들어가 있어서, 뒤따르는 5초 스킬 트리거와 서로 덮어썼다.
  이것이 "Music 이 0인데 송이 안 나간다" 의 원인이었다.
- `song` 을 **신설했다.** 곡끼리 공유하는 11초 + Lyric 리셋.
- `disco` / `Peace` / `Provo` 에서 각자의 `"effect of a song of ..." 11초` 를 **뺐다.**
  송은 자기 스킬을 잠그지 않는다. 두면 서버가 1.5초에 허용하는 것을 11초 참는다.
- `Peace` 에서 `"You play successfully, briefly pacifying one or more nearby creatures." 5초` 를 **뺐다.**
  같은 메시지에 `"successfully, briefly pacifying" 11초` 가 이미 걸려 있어 둘이 충돌했다.
- `Peace` 와 `Provo` 를 **`peace/provo` 한 항목으로 합쳤다.** 서버가 슬롯을 공유한다.
  `script/` 의 참조 30곳도 같이 바꿨다.
- **`skill` 에 바드 5초 트리거를 넣었다.** 서버 스킬 게이트가 하나라
  바드가 도는 동안 다른 스킬도 막힌다.
- 항목 이름을 **전부 PascalCase 로** 맞췄다 (49개). 스크립트가 참조하는 건 `peace/provo` 와 `heal pot` 둘이고,
  `heal pot` 은 원래 XML 이 `Heal Pot`, 스크립트 11개가 `heal pot` 으로 **서로 어긋나 있던 것**을 맞춘 것이다.
  임시 쿨다운으로 동작은 했지만 바는 안 뜨고 있었다.
- `fireball` 에 발동 트리거 `"fireball activated"` 를 넣었다. 실측 메시지는 "Wizardry fireball activated."
  이게 없어서 바가 채워지지 않았고, 그대로 두면 프록 게이트가 매 패스 통과했다.
- 바가 자주 뜨는 순서로 **재정렬했다**: `skill` -> `music` -> `disco` -> `peace/provo` -> `song`, 그 뒤에 이 루프가 읽는 바 순서로 `magic arrow` -> `harm` -> `fireball` -> `lightning` -> `mush` -> `heal pot`.

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

## 네크로 소환 (Vengeful Spirit)

**언데드 소환수는 `Vengeful Spirit` 을 켠 뒤에 소환 주문을 시전해야 나온다.** Spirit Speak 만으로는 안 된다.

> "For next 30 seconds all summon spells cast will instead create an Undead follower that loses 1% health &
> max health every 10 seconds but has damage increased by (20% * (Necromancy / 100))"

| Magery 소환 | 언데드 |
|---|---|
| Fire Elemental | **Lich** |
| Earth Elemental | **Ancient Mummy** |
| Air Elemental | Skeletal Fiend |
| Water Elemental | Rag Witch |
| Summon Daemon | **Vampire Thrall** |
| Blade Spirits | Skeletal Husk |
| Energy Vortex | Jackal Spirit |
| Summon Creature | 무작위 언데드 |

- 8서클 소환 전부 **마나 50, 시전 6.00초**, 시약에 **Bloodmoss** 포함 (`item-list.razor`)
- **타이머는 없지만 최대 체력이 10초마다 1% 깎여 결국 죽는다.** 재소환은 "죽었을 때"가 아니라 주기적 정비다
- **`followers` 는 컨트롤 슬롯 수다.** 위 소환수는 각 **2**, Summon Creature 는 1 (인게임 확인됨)
- Vengeful Spirit 은 심볼 1, 30초. 소환 둘을 뽑으려면 VS -> 소환 -> 소환 을 30초 안에

## Magery 프록은 게임이 메시지로 알려준다

`cooldowns.xml` 에 이미 잡혀 있다. **자체 `timer__` 로 15초를 세지 않는다.**

| 항목 | 프록 발동 | 다시 준비됨 |
|---|---|---|
| `magic arrow` | "magic arrow activated" | "cast a wizardry magic arrow spell again" |
| `harm` | "harm activated" | "cast a wizardry harm spell again" |
| `lightning` | "lightning spell hinders" | "cast a wizardry lightning spell again" |
| `fireball` | **트리거 없음** | "You may now cast a wizardy fireball spell" (게임 원문의 오타 그대로) |

스크립트는 `cooldown "magic arrow" = 0` 처럼 바로 읽으면 된다.

> **`fireball` 항목이 불완전하다.** 발동 메시지 트리거가 없어서 바가 채워지지 않는다.
> 인게임에서 Fireball 프록이 터질 때 나오는 문구를 받아 적어 트리거로 넣어야 한다.

**`Energy Bolt` 는 쿨다운 항목이 필요 없다.** 15초 창 같은 것이 없어서 순수 필러로 쓸 수 있다. 다만 환급은 조건부다.

> "Damage increased by (6% / 18% / 30%). Player recovers (3 / 9 / 15) mana **if target is killed within next 5 seconds**" -- Wizard's Grimoire, Energy Bolt
> "Inflicts an additional (7%, 21%, 35%) of final spell damage to target over 15 seconds" -- Wizard's Grimoire, Flamestrike

- 15 마나는 **볼트 뒤 5초 안에 대상이 죽을 때만** 돌아온다. 잡몹 마무리에는 거의 공짜, 체력 큰 몹에는 20 그대로다.
- 이전 판의 "조건 없는 상시 효과" 는 틀렸다. `bard-necro-combat-design.md` 의 마나 예산도 이 조건으로 고쳤다.

## Magery 시전 시간 (마나 예산 계산용)

| 서클 | 시전 | 서클 | 시전 |
|---|---|---|---|
| 1 | 0.50초 | 5 | 1.50초 |
| 2 | 0.75초 | 6 | 1.75초 |
| 3 | 1.00초 | 7 | 2.00초 |
| 4 | 1.25초 | 8 | 2.50초 |

> "Casting recovery time is **0.2 seconds**" -- 시전 사이 고정 딜레이

## PvP

**바드의 PvP 방어와 도주는 한 조건에 묶여 있다. 다른 플레이어에게 공격적 행동을 하지 않는 것이다.**
먼저 손을 쓰면 Defensive Barding 과 리콜을 같이 잃는다. 이 절의 숫자는 전부 이 조건에서 갈린다.

### Defensive Barding

> "Defensive Barding will ONLY apply while a player is Flagged in PvP"
> "Players will receive Defensive Barding if they do not have Heat of Battle in effect (i.e. they have not made an aggressive action against another player recently)"
> "When Defensive Barding activates the player will automatically receive an Effective Wrestling skill value and Effective Magic Resist skill value, but only for the purposes of defending against attacks/spells, based on their barding skill values"
> "Effective Wrestling skill value of ((Discordance Skill + Peacemaking Skill + Provocation Skill) / 2) up to a maximum of 100 Skill value"
> "Effective Magic Resist skill value of ((Discordance Skill + Peacemaking Skill + Provocation Skill) / 2) up to a maximum of 100 Skill value"
> "If a player already has a printed Wrestling or Magic Resist skill for their character at a higher amount than the Effective Barding skill received for that skill, the player's printed skill will always take priority."
> "The Wrestling/Magic Resist received from Defensive Barding will NOT count towards meeting any Skill Requirements needed for Codexes/Grimoires/etc and players will NOT receive any unique PvM bonuses from Wrestling / Magic Resist (such as Wrestling Mana Refund Chance or Magic Resist Siphon Spell Damage)"

- Disco/Peace/Provo 80/80/80 이면 `240 / 2 = 120` -> 상한 **100**. Wrestling 과 Magic Resist 둘 다.
- **방어에만 쓰인다.** 내가 칠 때의 명중 판정에는 안 들어간다.
- printed 가 **더 높을 때만** printed 를 쓴다. 켜져 있는 동안 printed Wrestling 80 / Resist 80 은 하는 일이 없다.
- **Heat of Battle 이 켜지면 통째로 꺼진다.** 그때는 printed 값만 남는다.

처음 들어온 패치(2020-09-28) 원문은 지금 위키와 두 군데가 다르다.

> "Effective Wrestling skill value of ((Discordance Skill + Peacemaking Skill + Provocation Skill) / 2) up to a maximum of 100 Skill value, when defending against creatures and other players while unarmed"
> "Effective Magic Resist skill value of ((Discordance Skill + Peacemaking Skill + Provocation Skill) / 3) up to a maximum of 100 Skill value"

| | 2020 패치 | 지금 위키 |
|---|---|---|
| Magic Resist | `/ 3` -> 80/80/80 이면 **80** | `/ 2` -> **100** |
| Wrestling 적용 범위 | "**while unarmed**" | 언급 없음 |
| PvP 플래그 조건 | 없음 | "ONLY apply while a player is Flagged in PvP" |

확인되지 않은 것:

- 어느 Resist 공식이 지금 서버 값인지. `/ 3` 이어도 printed 80 과 같으므로 printed 가 더 주는 것은 없다.
- **레슬링 무기를 들었을 때도 Effective Wrestling 이 적용되는지.** 2020 원문은 "while unarmed" 다.
- "Flagged in PvP" 가 무엇인지. 위키에 정의가 없다.

### Heat of Battle

> "Heat of Battle will be triggered by performing an aggressive action against another player regardless of notoriety, or when interacting with various faction content events or wayposts."
> "Aggressive actions include attacking or stealing from a player"
> "Aggressive actions do not include retaliatory empty-handed wrestling attacks or weapon swings your character makes when someone attacks you"
> "However, it is an aggressive action to re-target your attacker (for example, to avoid attacking monsters instead of the attacking player)"
> "Note also that using harmful spells (such as Weaken, Telekinesis, or Energy Bolt) will trigger Heat of Battle, even when used against an attacker"
> "Heat of battle will prevent the player from utilizing any moongates, recalling, or entering an inn room while it is active"

지속시간은 위키 문서에 없고 2020-09-28 패치 원문에 있다.

> "When any player commits a hostile action (including stealing) to another player, but the action is not considered a criminal action (such as attacking or stealing from a Red, Grey, or Orange player) they will have a 30 second Heat of Battle timer started"
> "When any player commits any Criminal action, they have will have a 2 minute Heat of Battle timer started that matches their Criminal Timer duration"
> "Heat of Battle now has a maximum duration of 5 minutes, regardless of circumstance"

| 내 행동 | Heat of Battle |
|---|---|
| PK 가 나를 칠 때 내 캐릭터가 자동으로 되받아치는 스윙 | **안 켜짐** |
| 몹을 치던 중 PK 로 타겟을 바꿈 | **켜짐.** 위키 예시가 이 경우다 |
| 해로운 주문 (Energy Bolt, Weaken, Telekinesis ...) | **켜짐.** 상대가 먼저 쳤어도 |
| 빨강 / 회색 / 주황 플레이어에게 공격적 행동 | 켜짐, 할 때마다 **30초** 타이머 |
| 파랑 공격 (Criminal) | 켜짐, **2분** |
| 햄스트링을 켜 둔 자동 반격 스윙 | 확인되지 않았다 |

**"반격은 안 켜진다" 는 자동 스윙에만 맞다.** 사냥 중에는 몹을 치고 있으므로 PK 를 치려면 타겟을 바꿔야 하고,
그 순간 켜진다. 거리를 두고 주문을 쓰는 메이지 PK 에게는 자동 스윙이 나갈 일 자체가 없다.

#### 도주인가 반격인가

| | 도주 (공격적 행동 없음) | 반격 (Heat of Battle) |
|---|---|---|
| 맨손 근접 방어 | Effective Wrestling **100** | printed Wrestling |
| 마법 방어 | Effective Resist **100** (`/ 3` 이면 80) | printed Resist |
| 리콜·문게이트 | 가능 | **막힘** |
| printed Wrestling / Resist 80 | 하는 일 없음 | **유일한 방어** |

**printed Resisting Spells 는 도주 플랜에서는 0, 반격 플랜에서는 유일한 마법 방어다.**
PK 를 어떻게 상대할지가 템플릿에 Resist 를 넣을지를 정한다.

#### 던전에서는 리콜로 도주할 수 없다

> "Within dungeons, players may only cast Recall within 8 tiles of a Golden Moongate" -- Magery (Recall)
> "Any character can cast this spell from a scroll in a rune book or rune tome, or from a scroll onto a loose marked rune, even with 0 Magery skill" -- Magery (Recall)
> "When a player is in the Heat of Battle they are unable to cast Recall, Gate, or use any Moongates" -- Magery

- 룬북 리콜은 Magery 0 이어도 된다. 하지만 **던전 안에서는 Golden Moongate 8타일 안에서만 된다.**
- 던전에서 PK 를 만나면 도주 플랜은 "문게이트까지 뛰기" 다. 그 사이에 맞으면 **printed 방어로 버텨야 한다.**

### 명중률

> "The chance to hit with a mace class weapon is equal to (attacker's mace fighting skill + 50) / ((defender's weapon or wrestling skill + 50) * 2) plus any relevant accuracy bonuses" -- Mace Fighting
> "The chance to hit and defend with fists (avoiding interrupts while casting) is equal to (attacker's wrestling skill + 50) / ((defender's weapon or wrestling skill + 50) * 2) plus any relevant accuracy bonuses." -- Wrestling
> "Due to Wrestling's defense bonus being active when unarmed (or when holding a spellbook) it can be used to defend against melee attacks while casting spells." -- Wrestling

Swordsmanship 도 같은 형태다.

```
명중률 = (공격자 스킬 + 50) / ((방어자 스킬 + 50) x 2)
```

**양쪽 다 지금 손에 든 것의 스킬 하나만 쓴다.** 가진 다른 스킬은 판정에 안 들어간다.

| | 쓰이는 스킬 |
|---|---|
| 공격자 | 든 무기의 스킬. 맨손·레슬링 무기일 때만 Wrestling |
| 방어자 | 든 무기의 스킬. 맨손·스펠북이면 Wrestling |

#### 스킬 대 스킬 (명중 보너스 0)

| 공격 \ 방어 | 0 | 50 | 80 | 100 |
|---|---|---|---|---|
| **0** | 50% | 25% | 19.2% | 16.7% |
| **50** | 100% | 50% | 38.5% | 33.3% |
| **80** | 100% | 65% | 50% | 43.3% |
| **100** | 100% | 75% | 57.7% | 50% |

- **같은 숫자끼리는 항상 50%.**
- 방어 0 에 공격 50 이상은 공식값이 1 을 넘는다 (130%, 150%). 100% 로 적었다.

#### 내가 칠 때

| 나 (손에 든 것) | 상대 (손에 든 것) | 계산 | 명중 |
|---|---|---|---|
| 메이스 100 | 무기 100 | 150 / 300 | 50% |
| 맨손, 레슬링 100 | 맨손, 레슬링 100 | 150 / 300 | 50% |
| 맨손, 레슬링 0 | 맨손, 레슬링 100 | 50 / 300 | 16.7% |
| 맨손, 레슬링 100 | 맨손, 레슬링 0 | 150 / 100 | 100% |
| 맨손, 레슬링 0 | 무기 100 | 50 / 300 | 16.7% |
| 레슬링 무기, 레슬링 80 | 메이지 PK (스펠북, 레슬링 100, 무기 0) | 130 / 300 | **43.3%** |
| 메이스 100, 레슬링 0 | 메이지 PK (스펠북, 레슬링 100) | 150 / 300 | **50%** |
| 메이스 80 | 메이지 PK (스펠북, 레슬링 100) | 130 / 300 | **43.3%** |
| 메이스 100 | 무기 100 + 레슬링 100, **무기를 든 상태** | 150 / 300 | 50%. 상대 레슬링은 안 쓰인다 |
| 메이스 100 | 무기 100 + 레슬링 100, **스펠북을 든 상태** | 150 / 300 | 50% |
| 메이스 100 | 무기 100 + 레슬링 0, **스펠북을 든 상태** | 150 / 100 | 100% |

- **메이지 PK 상대 명중률은 내 무기 스킬만 정한다.** 내 레슬링은 내가 레슬링으로 칠 때만 들어간다.
- 80 으로 치면 메이스든 레슬링 무기든 똑같이 43.3% 다.
- 무기와 레슬링을 둘 다 가진 상대는 **지금 든 쪽**으로 방어한다.

#### PK 가 나를 칠 때 (PK 무기 100)

| 내 손 | Defensive Barding 켜짐 | Heat of Battle 중 |
|---|---|---|
| 맨손, printed 레슬링 0 | 50% (Effective 100) | **100%** |
| 맨손, printed 레슬링 80 | 50% (Effective 100) | 57.7% |
| 레슬링 무기, printed 레슬링 80 | 확인되지 않았다 ("while unarmed") | 57.7% |
| 메이스 80 | 57.7% | 57.7% |
| 메이스 100 | 50% | 50% |

무기를 들면 방어는 그 무기의 스킬이다. **Effective Wrestling 이 끼어드는 것은 맨손일 때다.**

#### 명중 보너스

> "Accuracy bonuses to melee weapons from items (Colored Materials, Magical Properties, Aspects, Mastery Chains, etc) are now capped by a player's base melee skill for that weapon." -- Armor & Weapons
> "Players will receive bonuses against creatures based on what "setup" they have for weapons/shields occupying their hands" -- Wrestling

- 위 표는 보너스 0 기준이다. **보너스가 곱해지는지 더해지는지는 위키에 없다.**
- Weapon Setup 보너스(한손 무방패 Accuracy 등)는 크리처 상대 보너스라서 PvP 에는 안 붙는다.

#### 메이지가 레슬링을 드는 이유

> "Wrestling is very important to mage-types, as taking a melee hit will interrupt a spellcast in progress." -- Wrestling

**메이지 PK 는 한 대 맞으면 시전이 끊긴다.** 메이지가 레슬링 100 을 드는 이유이고, 이쪽이 무기 스킬을 올려야 하는 이유다.

Arcane Staff 를 든 메이지는 방어 스킬이 다르다.

> "A players chance to hit/defend with an Arcane Staff is based on their Arcane skill, but is also capped by the lower printed value of Magery or Wrestling" -- Arcane Staff
> "PvP-based interrupts while casting with an Arcane Staff equipped will be resolved as normal using the player's Wrestling skill" -- Arcane Staff

### Hamstring

PvP 요구조건. 첫 줄을 채우고 나머지 둘 중 하나를 채운다.

> "80.0 or higher attacking weapon skill in Dual Wielding, Fencing, Mace Fighting, Swordsmanship, or Wrestling"
> "two of the following skills at 80.0 or higher; Anatomy, Arms Lore, Chivalry, Forensic Evaluation, Tracking, Wrestling"
> "two of the following weapon skills at 80.0 or higher (including attacking weapon skill); Archery, Dual Wielding, Fencing, Mace Fighting, Swordsmanship"

> "if Hamstring is toggled for a player, on a missed attack they will not be able to make another Hamstring attempt for 15 seconds"
> "On a successful hit when Hamstring is toggled, a player will have a cooldown of 30-53 seconds (100-25 dex) before they may make another Hamstring attempt to any target"
> "When a player is hit by a Hamstring effect, they will be reduced to 0 Stamina for 3 seconds (forcing them to walk), after which their stamina will return to its previous amount"
> "Once hamstrung, a player or creature cannot be affected by another hamstring effect for another 30 seconds"

- **빗나가면 15초 잠긴다.** 햄스트링을 켠 첫 스윙의 명중률이 곧 성공률이다. 레슬링 100 메이지 상대로 무기 80 이면 43.3%, 100 이면 50%.
- 걸려도 3초이고 다음 시도는 30~53초 뒤다. **한 교전에 한 번**이라고 보는 게 맞다.
- Wrestling 80 + Anatomy 80 은 두 번째 줄(목록에서 두 개)을 채운다. 공격 스킬인 Wrestling 을 목록에서 다시 세지 말라는 문구는 없다.
- 메이스로 하려면 Mace 80 + 목록에서 두 개. Anatomy + Tracking 도 된다.
- 세 번째 줄(무기 두 개)의 PvP 목록에는 Wrestling 이 없다. PvM 목록에는 있다.

### Telekinesis + Explosion Potion

메이지 PK 의 흔한 진입이다. 규칙은 2020-09-28 패치 원문에 있고, 위키 Alchemy 문서에는
"Telekinesis is always required for sticking explosion potions to players regardless of skill level" 만 남아 있다.

> "If a player casts Telekinesis and successfully targets another player, it will apply a "Sticky" effect to the target player lasting 30 seconds"
> "If the same player that casted Telekinesis against a player throws an Explosive Potion at them within 30 seconds of the spellcast, the explosion potion will follow the movement of the target player, and when exploding will only damage the target player (and not other nearby players or creatures)"
> "If a "Stuck" potion on a player explodes, and both the thrower and the target player are within the radius of the blast, the damage from the potion will be split equally between the two players, instead of being dealt entirely to the target"
> "In some cases, players "stuck" with a explosive potion should consider "running the potion back" to the target to trigger the Splashback mechanic, both to reduce the damage on the explosion potion, but to also damage the thrower and potentially interrupt a spellcast if the thrower is currently casting"
> "Players can also cast Telekinesis on themselves as a defensive measure, since once Telekinesis is cast onto a player, no other player will be able to cast the spell on them for 30 seconds, and only the caster of the spell is allowed to stick potions onto a target that has Telekinesis active on them"
> "Telekinesis is a 3rd circle spell, requiring a minimum of 30 Magery to cast and 50 Magery to cast with 100% success"

위키 Explosion Potion 문서 (삭제 표시가 붙어 있다):

> "Explosion Potions stuck to another player with Telekinesis will now follow their target even if they change regions, such as crossing dungeon levels, exiting dungeons, recalling/gating/hiking, or using moongates"

- **붙은 포션은 리콜해도 따라온다.** 리콜로 이 콤보를 피할 수 없다.
- **던진 사람 곁에서 터지면 데미지가 반으로 나뉘고, 상대 시전이 끊길 수 있다.** 붙어서 싸우는 플랜과 방향이 같다.
- 자기 자신에게 TK 를 거는 방어는 Magery 30 이 있어야 한다.

지금 위키 Magery 주문표도 자기 TK 방어를 적고 있다.

> "Players can cast the Telekinesis spell onto another player (PvP) to make the player "Sticky" for explosion potions for the next 30 seconds" -- Magery (Telekinesis)
> "or on themselves to block it from being cast on them." -- Magery (Telekinesis)

TK 쿨다운 제약 (2020-09-28 패치 원문. 지금 위키에는 없다):

> "Each player has a global cooldown for casting Telekinesis in PvP, and can only successfuly apply it at most once every 30 seconds to any player (similar to Wall of Stone casting cooldowns)"
> "A player can only be hit by the Telekinesis spell (from all players) at most once every 30 seconds"
> "Whenever an Explosion Potion is "stuck" to a player, it immediately resets the 30 second Telekinesis casting cooldown against them (i.e other players cannot cast Telekinesis against that player for another 30 seconds after that point)"

- **자기 TK 는 상대 TK 보다 먼저 걸려야 한다.** 상대 TK 가 먼저 맞으면 30초 동안 Sticky 이고, 그동안은 내 TK 도 나에게 안 걸린다.
- 자기 TK 가 막는 것은 **붙는 것**이다. 던지는 것 자체는 막지 않는다. 안 붙은 포션은 나를 따라오지 않는다.
- **자기 TK 와 역콤보 TK 는 30초 안에 둘 다 못 쓸 수 있다.** "to any player" 에 자기 자신이 들어가는지는 확인되지 않았다.
- **상대가 자기 TK 를 걸어 두었으면 내 TK 는 안 걸린다.** 걸려 있는 동안 포션을 붙일 수 있는 것은 건 사람뿐이다.
- 자기에게 거는 TK 는 "against another player" 가 아니므로 위키 정의상 Heat of Battle 조건이 아니다. 인게임 확인은 안 됐다.

### Magery 로 싸울 때

바드 메이지 템플릿을 PvP 기준으로 볼 때 필요한 숫자다.

> "All hostile spells from 4th, 5th, 6th, 7th, and 8th circles will interrupt other players 100% of the time" -- Magery
> "Casting a hostile 1st circle spell against another player will at first have an interrupt chance of 100%" -- Magery
> "Afterwards, a 5 second window starts where all subsequent 1st circle hostile spells against the target have a 0% interrupt chance" -- Magery

2서클과 3서클도 같은 규칙이고, 창은 서클마다 따로 돈다.

> "PvP - Deals ((28 to 36) * (Magery / 100) * (.75 + (.375 * (Eval Int / 100)))) damage to target player" -- Energy Bolt, Explosion 공통
> "Modifies base spell damage against players by (0.75 + (0.375 * (Eval/100)))" -- Evaluating Intelligence
> "There is a 10% spell damage cap on supplemental skills (Tracking, Camping, Inscription, etc)" -- Evaluating Intelligence

| Eval | PvP 배율 | Energy Bolt / Explosion (Magery 100) |
|---|---|---|
| 80 | x1.05 | 29.4 ~ 37.8 |
| 100 | x1.125 | 31.5 ~ 40.5 |

- Explosion 은 "damage delay of 2.5 seconds", Energy Bolt 는 0.5초다.

**레슬링:**

- 메이지는 근접 한 대에 시전이 끊긴다 (위 "메이지가 레슬링을 드는 이유").
- **바드 메이지의 레슬링은 도주할 때만 Defensive Barding 이 채운다.** 첫 공격 주문을 쏘는 순간 Heat of Battle 이 켜지고 printed 값이 된다.
- printed 0 이면 무기 100 PK 의 근접은 **100%** 맞고, 한 대마다 시전이 끊긴다.

> "Wrestling will provide a (15% * (Wrestling Skill / 100)) Mana Refund chance when casting spells" -- Wrestling (PvM)

**Magic Reflection 과 Inscription:**

> "PvP - Has a (35% * (Inscription / 100)) chance to stay active and reflect a single additional spell before being nullified" -- Magery (Magic Reflection)
> "Will at most ever reflect 2 spells during PvP" -- Magery (Magic Reflection)
> "Players using a scroll to cast a spell will receive a (10% * (Inscription Skill / 100)) damage bonus against other players (PvP Spell Supplemental Damage Cap 10%)" -- Inscription
> "Increases certain spell's buff durations. Normal duration is 2 minutes and are increased by (400% * (Inscription Skill / 100)), including:" -- Inscription (Protection, Arch Protection, Bless, Invisibility)

- Inscription 120 의 PvP 몫은 **리플렉트가 한 번 더 남을 확률 42%** 와 스크롤 시전 딜 +10% (상한) 정도다.
- 나머지는 PvM 이다. 버프 지속 2분 -> 11.6분, 스크롤 환급, Reactive Armor.

**Alchemy (PvP):**

> "Increases Explosion Potion damage by (50% * (Alchemy Skill / 100))" -- Alchemy
> "Increases Healing Potion effectiveness by (25% * (Alchemy Skill / 100))" -- Alchemy
> "Increases Cure Potion chances by (12.5% * (Alchemy Skill / 100))" -- Alchemy
> "In PvP the base damage range is 15-25, scaled with a player's alchemy skill" -- Alchemy (Greater Explosion)

- 80 이면 폭발 포션 +40%, 힐 포션 +20%, 큐어 포션 +10%. Greater Explosion 쿨다운은 15초 (위키 포션표).

**마나:**

> "The baseline Mana Regen rate is 1 mana restored every 2 seconds (i.e., 0.5 mana per second)." -- Meditation
> "The Mana Regen rate is increased by (100% * (Meditation skill / 100))" -- Meditation

- Meditation 0 이면 초당 0.5 다. PvP 에서 오래 싸우는 구성이 아니다.

**PvM 에서 인터럽트:**

> "Provides players with a (Effective Magic Resist Skill / 100%)) chance to avoid Spell Interruption from Creature/Environment Damage" -- Resisting Spells
> "Players will have an (Effective Inscription Skill / 100%)) chance to avoid Spell Interruption from Creature/Environment Damage" -- Inscription

- 크리처 인터럽트 회피가 Resist 와 Inscription 에 같은 형태로 있다. 둘이 합산되는지는 확인되지 않았다. **Resist 100 이면 이것만으로 100% 다.**
- Defensive Barding 은 PvM 보너스를 주지 않으므로 이 효과는 printed Resist 로만 받는다.

Wizard's Grimoire:

> "Players must have at least 80 Magery skill and at least 80 Meditation or 80 Eval Int skill to benefit from the Wizard's Grimoire" -- Wizard's Grimoire

### 소환수로 싸울 때

**"소환수는 PvP 에서 약하다" 에는 근거가 있다.** PvM 에서 받던 강화가 PvP 에서 빠진다.

> "If a player gets PvP flagged their summons' stats and skills will be automatically adjusted to their printed spirit speak skill" -- Spirit Speak
> "Additionally Summoner Tome upgrades will not apply against players" -- Spirit Speak
> "Necromancy Abilities will NOT work in PvP" -- Necromancy
> "Abilities that increase the Health and Damage of Summoned Followers will follow the same handling that bonuses earned from Spirit Speak follow in PvP" -- Necromancy
> "When a player attempts to Dispel another player's summoned follower (with the Dispel or Mass Dispel spell) there is a (50% * (Controller's Printed Spirit Speak Skill / 100)) chance the Summoned Follower will ignore the dispel attempt (this applies to normal and Undead summons)" -- Spirit Speak
> "Summoning Spells take 5 seconds to cast" -- Spirit Speak
> "Players cannot receive Mana Refunds from casting any Summoning Spells" -- Spirit Speak
> "Magic Resist potions work against pets in PvP" -- Alchemy
> "Lesser, Regular, and Greater Magic Resist potions reduce spell damage taken from creatures by 10/20/30% for 2 minutes" -- Alchemy

| 항목 | PvM | PvP |
|---|---|---|
| 소환수 스탯 | Effective Spirit Speak (장비 보너스 포함) | **printed Spirit Speak 만** |
| Summoner's Tome 업그레이드 | 적용 | **플레이어 상대로 안 됨** |
| Necromancy 어빌리티 | 적용 | **안 됨** |
| 소환수 주문 데미지 | 그대로 | PK 가 Magic Resist 포션을 마시면 **-10 / 20 / 30%** |
| 상대 Dispel | -- | Spirit Speak 120 이면 **60% 무시, 40% 로 지워진다** |
| 다시 부르기 | -- | 5초 시전 (`item-list.razor` 는 6.00초), 마나 환급 없음, 상대 4서클+ 주문에 끊긴다 |

Herding 과 Necromancy 가 PvP 에서 대신 주는 것:

> "Tamed and summoned creatures deal (11% * (Effective Herding Skill / 100)) additional damage against players while their controller has an active shepherd's crook." -- Herding
> "Tamed and summoned receive (5.5% * (Effective Herding Skill)) Damage Resistance against all players" -- Herding
> "Instead, having the Necromancy skill during PvP will provide the player with a (10% * (Necromancy Skill / 100)) Supplemental PvP Spell Damage bonus" -- Necromancy
> "However, you could have 100 Evaluating Intelligence and 100 Tracking and gain 22.5% spell damage increase" -- Evaluating Intelligence

- Herding 80 이면 소환수 딜 +8.8%. 저항 공식은 원문에 `/ 100` 이 빠져 있어 값을 그대로 읽을 수 없다.
- Eval 과 보조 스킬 보너스는 **더해진다** (위키 예시: 12.5% + 10% = 22.5%).

| 구성 | Eval 배율 | 보조 스킬 (상한 10%) | PvP 주문 합계 |
|---|---|---|---|
| Bard Necro (Eval 80, Necro 100) | +5% | +10% (Necromancy) | **+15%** |
| Bard Mage (Eval 100, 보조 없음) | +12.5% | 0 | +12.5% |
| Bard Mage (Eval 100, Inscription 120, 스크롤 시전) | +12.5% | +10% (Inscription, 스크롤만) | +22.5% |

**확인되지 않은 것:**

- **소환수가 PK 를 치면 내 Heat of Battle 이 켜지는지.** 위키 정의는 "performing an aggressive action against another player" 뿐이다.
  켜지지 않는다면 "소환수가 싸우고 나는 자기 대상 주문(자기 TK, 힐, 큐어)만 쓴다" 는 플랜이 Defensive Barding 과 리콜을 지킨다.
  Heat of Battle 은 버프바에 뜨므로 ("The Heat of Battle flag is now a visible buff on players in the Buff Bar") 실전에서 소환수가 공격을 시작한 직후 버프바를 보면 확인된다.
- **소환수 데미지가 Resisting Spells 의 "Creature/Environment Damage" 에 들어가는지.** 들어간다면 Resist 100 PK 는 소환수에게 맞아도 시전이 끊기지 않는다. 그러면 PK 의 콤보를 끊는 것은 **내 주문뿐**이다.

#### Herding 을 Resist 로 바꿀 것인가

Bard Necro 기준으로 Herding 80 -> Resisting Spells 80 을 따져 본 결과다.

- 잃는 것은 **상시**다. 팔로워 딜 +17.6% (위 설계 문서 값). 소환수가 딜의 63.4% 이므로 전체 딜 약 -9.5% (추정: `36.6 + 63.4 / 1.176`).
- 얻는 것은 **반격할 때만**이다. 도주하는 동안에는 Defensive Barding 이 이미 Resist 를 준다.
- **사냥이 본업이고 PK 가 가끔이면 Herding 을 유지한다.** PK 는 아래 순서로 대응한다.

| 순서 | 행동 | 근거 |
|---|---|---|
| 1 | 빨강이 보이면 **자기 TK** | 상대 TK 보다 먼저여야 한다 |
| 2 | 해로운 주문을 쏘지 않는다. 힐·큐어만 | Defensive Barding (Resist) 과 리콜을 지킨다 |
| 3 | Golden Moongate 8타일 안이면 리콜 | 던전 리콜 제한 |
| 4 | 싸울 거면 그때 공격 | 이 순간부터 Heat of Battle. Bard Necro 는 Resist 0 |

### Parrying

> "Players may parry melee attacks with shields, two-handed weapons, paired weapons (wrestling/dual wielding) and parry daggers."
> "Chance to parry a melee attack is (50% * (Parrying Skill / 100))"
> "Successfully parrying an attack from another player or creature will reduce its damage by 75%"
> "Successfully parrying an attack from another player, while wielding a two-handed weapon, will reduce its damage by only 50% however"
> "You cannot parry spells in PVP"
> "Provides a (50% * (Effective Parry Skill / 100)) reduction to Stamina losses that occur due to taking damage"

| Parrying | 근접 막기 | 막으면 | 피격 스태미나 손실 |
|---|---|---|---|
| 80 | 40% | -75% (양손 무기면 -50%) | -40% |
| 100 | 50% | 같음 | -50% |

- **PvP 주문은 못 막는다.** 메이지 PK 상대로 남는 것은 스태미나 손실 감소뿐이다.
- 레슬링 무기는 무기표에 **2H** 로 적혀 있다. PvP 패링 감소가 -50% 로 줄어드는지는 확인되지 않았다.

PvP 근접 데미지 기대 감소 = 막을 확률 x 감소율.

| Parrying | 방패 · paired | 양손 무기 |
|---|---|---|
| 80 | `40% x 75% =` **30%** | `40% x 50% =` 20% |
| 100 | `50% x 75% =` **37.5%** | `50% x 50% =` 25% |

#### 패리 메이지가 있는 이유

주문 방어가 아니라 **근접 방어와 방패**다.

> "Players with both 80 Magery and 80 Parrying or greater may cast spells and meditate with a shield (meditation rate will still be affected by the shield's meditation penalty)" -- Parrying
> "Armor rating provided from shields is (50% * Shield Base AR) + (50% * Shield Base AR * (Parrying Skill / 100))" -- Parrying
> "Hits from a Macing-skill weapon against another player have a (100% * (Damage / 50)) chance to cause the player to lose 5 Stamina" -- Mace Fighting
> "Dexterity Penalties have been removed from armor and shields and replaced with a Stamina Fatigue Penalty that increases the amount of stamina the player loses when taking damage" -- Armor & Weapons

- 메이지는 **Magery 80 + Parrying 80 이 있어야 방패를 든 채 시전한다.** 방패 AR 도 Parrying 에 비례한다.
- PvP 에서 하는 일은 덱서의 근접을 막고, 맞을 때 잃는 스태미나를 줄이는 것이다.
  스태미나가 0 이면 걷게 된다 (Hamstring 원문 "reduced to 0 Stamina ... forcing them to walk").
- PvM 에서 하는 일이 더 많다. 크리처 주문 패링 (`25% x (Parrying / 100)`, -75%), Taunt, Parry Codex.
- Parry Codex 에는 Mirror ("reduces Spell Damage taken by 6% per rank") 같은 스탠스가 있다.
  하지만 Codex 문서 분류는 PvM 이고 XP 도 크리처를 잡아야 오른다. **PvP 에 적용되는지는 적혀 있지 않다.**
- 위키 메이지 템플릿 페이지에 패리 메이지는 없다. Parry Codex 를 요구하는 메이지는 New Player 페이지의 Arcane Mage 하나다.

**메이지 PK 상대로 패링이 막는 것은 없다.** 근접 PK 나 무기를 든 하이브리드 상대로는 위 30% 가 그대로 산다.

### Resisting Spells

> "Spell damage taken is reduced by a minimum of (12.5% * (Magic Resist Skill / 100)) (PvM/PvP)"
> "Spell damage taken is reduced by a maximum of (37.5% * (Magic Resist Skill / 100)) (PvM/PvP)"
> "The chance to resist any hostile spell with a non-damaging effect such as Curse or Poison is ((40% - (Spell Circle * 5%)) * (Magic Resist Skill / 100))"

위키 표 (발췌). 서클 칸은 비데미지 주문 저항 확률이다.

| Resist | 데미지 감소 | 1서클 | 2서클 | 3서클 | 4서클 | 5서클 | 6서클 | 7서클 | 8서클 |
|---|---|---|---|---|---|---|---|---|---|
| 80 | 10 ~ 30% | 28% | 24% | N/A | 16% | 12% | 8% | 4% | N/A |
| 100 | 12.5 ~ 37.5% | 35% | 30% | N/A | 20% | 15% | 10% | 5% | N/A |

- 서클 (위키 Magery 주문표): Weaken 1, **Poison · Telekinesis 3**, Curse 4, Paralyze 5, **Energy Bolt · Explosion 6**, Mana Vampire 7.
- 위키 표는 3서클을 N/A 로 적는데 본문은 3서클인 Poison 을 예로 든다. 서로 맞지 않는다. 확인되지 않았다.
- **Defensive Barding 이 켜져 있으면 100 행, Heat of Battle 중이면 printed 행이다.**

### 반격력

> "Unarmed Wrestling base damage against players is 1-4" -- Wrestling
> "Damage from Wrestling Weapons in PvP will scale based on the player's Raw Dex stat as a % (without any adjustments for Dex bonuses or penalties from Potions, Bless, Weaken, other effects)" -- Wrestling
> "Wrestling Weapons can be disarmed, which will result in the player dealing standard "Unarmed" 1-2 damage during that time" -- Wrestling
> "Wrestling Weapons receive a +20% Melee Damage bonus towards creatures that is applied to Two-Handed Weapons (since players cannot equip shields while using Wrestling Weapons)" -- Wrestling

위키 무기표의 Grinding (Light) 행:

| 계열 | 초/스윙 | 데미지 | 평균 | DPS | 무기 |
|---|---|---|---|---|---|
| Wrestling | 1.67 | 13 ~ 31 | 22 | **13.17** | Martial Manual, Cestus, Fistblade |
| Swordsmanship | 1.56 | 13 ~ 23 | 18 | 11.54 | Longswords, Broadsword, Viking Sword, Norse Axe |
| Mace Fighting | 1.63 | 12 ~ 24 | 18 | 11.04 | Mace, Maul, War Mace, Flanged Mace, Flail |
| Throwing | 1.88 | 14 ~ 24 | 19 | 10.11 | Throwing Dagger, Throwing Star |
| Archery | 2.21 | 13 ~ 25 | 19 | 8.6 | Bow, Hunting Bow, Recurve Bow |

- **맨손은 PvP 에서 1~4 다.** 레슬링으로 싸우려면 레슬링 무기가 전제다.
- 레슬링 무기의 PvP 데미지는 **raw Dex 비율**이다. raw Dex 100 이면 100%, 50 이면 50%. 포션·Bless 는 안 친다.
- 레슬링 무기는 방패를 못 든다. 패링은 무기 자체로 한다 (위 Parrying).
- 위키 Discordance / Peacemaking / Provocation 문서는 크리처 대상 효과만 적는다. 바드 스킬로 PK 를 누르는 수단은 문서에 없다.

### Tracking

> "A downside of Bard Templates is clear lack to fight back Pks / Griefers. Through Defensive Barding they are tough to kill but lack the offensive to fight back." -- TemplatesBard
> "Consider squeezing 80-100 Tracking into a template to passively track hostile players (PK's) so you can avoid them." -- TemplatesBard
> "On a successful tracking attempt, players can see a list of non-hidden targets within (20 + (80 * (Tracking Skill / 100))) tiles"
> "Inside dungeons, this tracking distance is halved (20 + (80 * (Tracking Skill / 100))) / 2 tiles"
> "Increases Effective Barding skill by (10 * (Tracking Skill / 100))"
> "When attacking any creature add Base Weapon Damage * (25% * (Tracking Skill / 100)) supplemental bonus damage per weapon hit."
> "When attacking any player, add Base Weapon Damage * (10% * (Tracking Skill / 100)) supplemental bonus damage per weapon hit"

| Tracking | 탐지 거리 야외 / 던전 | Effective Barding | 무기 딜 PvM / PvP |
|---|---|---|---|
| 80 | 84 / 42 타일 | +8 | +20% / +8% |
| 100 | 100 / 50 타일 | +10 | +25% / +10% |

- Effective Barding 보너스는 Musicianship(또는 Self Taught 대체값) 상한 안에서만 붙는다 (위 "Effective Barding Skill").
- Hunting 모드를 "Murderer Players" 로 켜는 코드가 이미 있다: `script/gather/mining.razor:195`.
- Hamstring 두 번째 줄 목록에 들어 있다.

#### Hunting 모드와 바드 스킬 쿨

> "Players can activate and deactivate a "Hunting" mode from the Tracking window to automatically make Tracking skill checks at various intervals (still requiring the normal 5 second skill cooldown) against a specific type of player/creature"
> "Players will always receive their bonuses to Damage and Barding Skill from the Tracking skill even if they are not currently Hunting"
> "Tracking success chance is (100% * (Tracking Skill / 100))"

- **딜·바딩 보너스는 Hunting 을 안 켜도 붙는다.** PK 조기 발견에만 Hunting 이 필요하다.
- 판정 한 번의 성공률은 Tracking 80 이면 80% 다.
- **Hunting 의 자동 판정도 5초 스킬 쿨을 쓴다.** 위 "`skill` 과 `music` 의 관계" 대로 서버 스킬 게이트가 하나라면,
  사냥 중 Hunting 이 바드 스킬을 "use another skill" 로 막을 수 있다. **확인되지 않았다.**
- 판정 빈도는 Hunt Frequency 로 고른다. "New When No Arrow" 와 "New When No Target" 은 화살표가 없을 때만 판정한다.
  주변에 Murderer 가 없으면 화살표가 없으므로 계속 판정한다.

## 자주 틀렸던 것

| 틀린 생각 | 사실 |
|---|---|
| 피스는 데미지를 받으면 풀린다 | **아니다.** Barding Break 로만 풀린다 |
| Provocation 은 안 찍었다 | **찍었다.** Self Taught 가 Musicianship 을 대체해서 Disco/Peace/Provo 80/80/80 구성이다 |
| Vampire Thrall 은 근접딜러다 | **주문딜러다.** "Spell Damage: 26 - 32" |
| Fury 는 분당 5% | **30초당 5%, 최대 +30%** -- 3분이면 캡 |
| Music 쿨만 보면 된다 | **글로벌 5초 + 개별 쿨의 AND 조건이다** |
| Discordance 는 Effective 로 스케일 | **printed 스킬로 스케일한다** (`printed / 120 x 25%`) |
| 소환수도 Virtuoso / Ensemble 을 받는다 | **팔로워 명시는 `Sing Your Own Praises` 뿐이다** |
| Discordance 도 barding break 로 끊긴다 | **안 끊긴다.** 브레이크는 Peace / Provo 만 끊는다 |
| Self Taught 는 요구조건만 대체한다 | **Effective Barding 보너스 상한에도 적용된다.** 실측 170 |
| Song 은 별도 명령이다 | **스킬을 백팩에 타겟한 것이다.** 땅에 타겟하면 group effect |
| Song 과 Skill 은 서로 막는다 | **비대칭이다.** 송은 Music 과 슬롯을 읽기만 하고 쓰지 않는다 |
| Peace 와 Provo 는 슬롯이 따로다 | **공유한다.** 로컬 엔트리가 서로를 반영하지 않아 한 번 착각했다 |
| 차단된 시도는 아무 쿨도 안 태운다 | **Music 을 태운다.** 차단된 송 다음의 스킬 판정을 믿지 말 것 |
| Ensemble 은 디스코만 있으면 된다 | **Discord AND (Peace OR Provo).** 두 개가 걸려야 한다 |
| 바드 쿨은 예측 가능하다 | **"Your barding skill cooldowns reset." 프록이 있다** (Lyric 방어구). 측정할 땐 벗는다 |
| Song 쿨은 `cooldown "music"` 이다 | **아니다. 별도 계열이다.** `music` 이 둘을 섞어 덮어쓰던 버그는 고쳤다 |
| `cooldown "..."` 은 서버 값이다 | **아니다. `cooldowns.xml` 의 내 메시지 트리거다.** 숫자가 이상하면 이 파일을 본다 |
| 프록 15초는 타이머로 센다 | **게임이 메시지로 알려준다.** `cooldown "magic arrow"` 등을 읽는다 |
| Energy Bolt 는 시전마다 15 마나가 돌아온다 | **5초 안에 대상이 죽을 때만.** 잡몹에서만 실질 5 다 |
| 브레이크 중엔 Provo 로 Ensemble 을 살린다 | **못 한다.** 브레이크 대상엔 Peace 도 Provo 도 안 걸린다 |
| Spirit Speak 만 있으면 언데드 소환이 나온다 | **Vengeful Spirit 을 먼저 켜야 한다.** 매핑은 위 표 |
| `followers` 는 소환수 마릿수다 | **컨트롤 슬롯 수다.** Lich 2마리 = 4 |
| 소환수는 안 맞으면 안 죽는다 | **10초마다 최대 체력 1% 씩 썩는다.** 재소환은 주기적이다 |
| 레슬링이 0 이면 PvP 에서 못 때린다 | **아니다.** 공격은 든 무기의 스킬로 판정한다. 레슬링은 맨손·레슬링 무기로 칠 때만 쓴다 |
| 레슬링 100 이면 명중 50% | **스킬이 같으면 50% 다.** 100 대 100 이라서 50% 다 |
| 메이지 PK 를 맞히려면 내 레슬링이 필요하다 | **내 무기 스킬 대 상대 레슬링이다.** 메이스 100 이면 50%, 80 이면 43.3% |
| 바드에게 printed Resist 는 PvP 에서 쓸모없다 | **도주할 때만 맞다.** 반격하면 Heat of Battle 이 Defensive Barding 을 끈다 |
| PK 가 먼저 쳤으면 반격해도 Heat of Battle 이 안 켜진다 | **자동 반격 스윙만 예외다.** 타겟을 바꾸거나 해로운 주문을 쓰면 켜진다 |
| 레슬링 무기 데미지는 4~13 이다 | **13~31, 평균 22.** 무기표의 DiceMax(4) 와 MinDmg(13) 칸을 데미지로 잘못 읽은 값이었다 |
| 붙은 폭발 포션은 리콜로 피한다 | **따라온다.** 던진 사람 곁으로 가면 데미지가 반으로 나뉜다 |
| 패링으로 PK 의 주문을 막는다 | **못 막는다.** "You cannot parry spells in PVP". 패리 메이지의 이유는 근접 방어와 방패 시전이다 |
| 바드 메이지는 Defensive Barding 이 있어 레슬링이 필요 없다 | **도주할 때만 맞다.** 첫 공격 주문에 Heat of Battle 이 켜지고 printed 0 이 된다 |
| 던전에서도 룬북으로 도망친다 | **Golden Moongate 8타일 안에서만 리콜된다** |
| Summoner's Tome 투자는 PvP 에서도 소환수를 세게 한다 | **안 한다.** "Summoner Tome upgrades will not apply against players". 스탯도 printed Spirit Speak 로 돌아간다 |
| 자기 TK 는 PK 가 나타난 뒤 아무 때나 걸면 된다 | **상대 TK 보다 먼저여야 한다.** 한 사람은 30초에 한 번만 TK 에 맞는다 |

## 참고 링크

- [Musicianship](https://wiki.uooutlands.com/Musicianship) -- Barding Song, barding break 공식, Defensive Barding
- [Discordance](https://wiki.uooutlands.com/Discordance) -- 디버프 공식, Effective Barding 정의
- [Peacemaking](https://wiki.uooutlands.com/Peacemaking) -- 지속시간, 쿨다운
- [Provocation](https://wiki.uooutlands.com/Provocation)
- [Bard Codex](https://wiki.uooutlands.com/Bard_Codex)
- [Heat of Battle](https://wiki.uooutlands.com/Heat_of_Battle) -- 공격적 행동의 정의, 자동 반격 예외
- [PATCH: Murderer and PvP Overhaul (2020-09-28)](https://forums.uooutlands.com/index.php?threads/patch-murderer-and-pvp-overhaul-general-changes.3232/) -- Heat of Battle 지속시간, Defensive Barding 원래 공식, Telekinesis 포션
- [Wrestling](https://wiki.uooutlands.com/Wrestling) / [Mace Fighting](https://wiki.uooutlands.com/Mace_Fighting) -- 명중 공식, 레슬링 무기
- [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons) -- 무기표, 명중 보너스 상한
- [Hamstring](https://wiki.uooutlands.com/Hamstring)
- [Parrying](https://wiki.uooutlands.com/Parrying)
- [Resisting Spells](https://wiki.uooutlands.com/Resisting_Spells)
- [Tracking](https://wiki.uooutlands.com/Tracking)
- [TemplatesBard](https://wiki.uooutlands.com/TemplatesBard)
- [Alchemy](https://wiki.uooutlands.com/Alchemy) -- Sticky Potions
- [Arcane Staff](https://wiki.uooutlands.com/Arcane_Staff)
