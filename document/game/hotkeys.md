---
name: Hotkeys
label: 핫키 배치
group: Game reference
order: 20
---

모든 캐릭터가 **같은 자리에 같은 역할**을 둔다. 배치는 두 유형이고, Razor 프로필 하나가 유형 하나다.

| 유형 | 누구 | Razor 프로필 |
| --- | --- | --- |
| summoner | 소환수와 펫을 부리는 캐릭터 | `summoner` |
| basic | 그 밖의 캐릭터(기본형) | `default` |

두 유형이 다른 칸은 아랫줄(01.E절)뿐이다. 템플릿마다 채우는 칸은 `1 2 3`, `F1`, `F4`, Alt 줄이다(03절).
바인딩의 정본은 Razor 프로필 xml과 ClassicUO의 `macros.xml`, `profile.json`이다(02.C절). 이 문서는 그 파일들을 사람이 읽을 수 있게 그린 배치도다.

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | 키마다 무엇이 걸려 있나 |
| [02](#02) | 층은 어떻게 나누나. Mac에서 막히는 키는 무엇이고, Razor와 ClassicUO 가운데 어디에 거나 |
| [03](#03) | 템플릿이 채우는 칸은 캐릭터마다 무엇인가 |
| [04](#04) | 상황마다 어떤 순서로 누르나 |
| [05](#05) | 프로필의 L 번호는 Razor의 어느 이름인가 |
| [06](#06) | 주문 데미지는 얼마인가 |
| [07](#07) | 확인하지 못한 것 |

이 문서에 걸린 질문은 [Open items](../questions/open-items.md)에 모았다.

::part[배치]

## <a id="01"></a>01 키 배치

키보드 줄마다 표가 하나다. —는 빈칸이고, (예정)은 자리만 정하고 아직 걸지 않은 칸이다.

Mac에서는 Wine이 `Cmd → Ctrl`, `Option → Alt`로 넘긴다(`prefix/user.reg`의 `LeftCommandIsCtrl`, `LeftOptionIsAlt`).
그래서 이 문서의 **Ctrl은 엄지로 누르는 Cmd**이고, Alt는 Option이다.

### <a id="01.A"></a>01.A 펑션줄

|  | Esc | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 무수정 | 스크립트 정지 | **전투 루프** | cancel-target | recycle | **PvP 루프** | 이름 표시 | 투명 | 하이드 | 명상 | — | share-loot | claim-loot | loadout |
| Shift | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Ctrl | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Alt | — | — | — | — | — | — | — | — | — | — | — | — | — |

### <a id="01.B"></a>01.B 숫자줄

|  | `` ` `` | 1 | 2 | 3 | 4 | 5 | 6 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 무수정 | **Smart Heal/Cure** | 시그니처 ① | 시그니처 ② | 시그니처 ③ | Explosion | Energy Bolt | Paralyze | Night Sight |
| Shift | — | — | — | — | — | — | — | — |
| Ctrl | **Greater Heal** (커서 → 펫, 동료) | 힐 포션 | 큐어 포션 | 리프 포션 | 힘 포션 | 민 포션 | 레지 포션 | — |
| Alt | — | **Vengeful Spirit** | Fire El → Lich | Water El → Rag Witch | Earth El → Mummy | Daemon → Vampire | Summon Creature | dress |

Alt 줄에서 → 뒤의 이름은 Vengeful Spirit(`Alt+1`)을 켜고 부르면 나오는 언데드다([Bard Necro](../templates/bard-necro.md#03.C) 03.C절).
Alt 줄에는 템플릿이 쓰는 소환만 건다(03절). `Alt+0`의 dress는 소환이 아니지만, 자주 누르지 않으니 Alt 줄 끝에 두었다.
비어 있는 `7`\~`9`는 표에서 뺐다.

### <a id="01.C"></a>01.C 윗줄

|  | Tab | Q | W | E | R | T | Y | U |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 무수정 | — | 셋 라타 | ↑ | **라타 발사** | Teleport | Telekinesis | — | — |
| Shift | — | Harm | Magic Arrow | Fireball | Lightning | Mind Blast | Poison | — |
| Ctrl | — | Reactive Armor | Magic Reflection | Protection | Bless | **Cure** (커서 → 펫, 동료) | **Resurrection** (커서 → 동료) | — |
| Alt | — | — | — | — | — | — | — | — |

라타는 last target이다. `Q`로 대상을 잡고, 주문 커서가 뜨면 `E`로 라타에 쏜다.

### <a id="01.D"></a>01.D 홈줄

|  | A | S | D | F | G | H | J |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 무수정 | ← | ↓ | → | 로프 | 폭발 포션 | **Chain Lightning** | — |
| Shift | — | — | — | — | — | — | — |
| Ctrl | — | — | — | — | — | — | — |
| Alt | — | — | — | — | — | — | — |

`F`의 로프는 `[rope`를 말하는 매크로라서 `macros.xml`에 건다(02.C절). 여섯 캐릭터 모두 같은 자리다.

### <a id="01.E"></a>01.E 아랫줄

**`Z → V`가 공격이다.** 어느 유형이든 `Z`로 시작해서 `V`로 끝낸다. 유형마다 키의 뜻은 달라도, 두 키를 이어 누르면 똑같이 가장 가까운 몹을 친다.
이 줄에서 유형마다 다른 칸은 `Z X C V`의 무수정과 Shift뿐이다.

|  | Z | X | C | V | B | N |
| --- | --- | --- | --- | --- | --- | --- |
| 무수정 (summoner) | **All Kill** (커서) | All Follow Me | All Guard Me | **가장 가까운 몹 타겟** | moongate | home |
| 무수정 (basic) | **가장 가까운 몹 타겟** | 이전 플레이어 | 다음 플레이어 | **Attack Last Target** | moongate | home |
| Shift (summoner) | — | 이전 플레이어 | 다음 플레이어 | Attack Last Target | — | — |
| Shift (basic) | 햄스트링 토글 (예정) | 디스암 토글 (예정) | — | — | — | — |
| Ctrl | Wall of Stone | Dispel Field | Invisibility | Reveal | — | — |
| Alt | — | — | — | — | — | — |

- summoner는 `Z`가 All Kill 커서를 띄우고, `V`가 그 커서를 가장 가까운 몹으로 채운다. 커서가 없을 때 `V`는 라타만 잡는다.
- basic은 `Z`로 라타를 잡고 `V`로 친다. PvP에서는 `X`나 `C`로 플레이어를 잡고 `V`를 누른다.
- 플레이어 순환은 summoner가 `Shift+X/C`, basic이 무수정 `X/C`다. 키 하나에는 바인딩이 하나만 걸리는데, summoner는 무수정 `X`와 `C`를 펫 명령에 쓰기 때문이다.
- summoner는 Follow를 `X`, Guard를 `C`에 둔다. `C`는 가장 자주 누르는 `V` 바로 옆이라 잘못 누르기 쉽다.
  Guard는 잘못 눌러도 펫이 싸움을 이어 가지만, Follow를 누르면 펫이 싸움을 멈춘다.
- 햄스트링과 디스암은 평소 켜 둔다. basic의 `Shift+Z`와 `Shift+X`는 상황에 따라 끄고 켜는 자리다(예정, 07절).
  끄고 켜면 프로필 오버헤드 `[ hams mode, on/off ]`와 `[ disarm mode, on/off ]`가 뜬다([Overheads](../scripting/overheads.md#07) 07절).
- 무기 스왑(`hotkey/weapon-*`)은 스크립트라서, 누르면 돌던 전투 루프가 멈춘다. 그래서 이 줄에 넣지 않는다.

### <a id="01.F"></a>01.F 마우스와 기타

|  | Space | 휠 위 | 휠 아래 | 사이드 위 (`-5`) | 사이드 아래 (`-4`) |
| --- | --- | --- | --- | --- | --- |
| 무수정 | 자기 타겟 | — | **Interrupt** | 타겟 취소 | **Pouch** (마비 해제) |
| Shift | — | 다음 아군 플레이어 | 이전 아군 플레이어 | — | — |
| Ctrl | — | — | — | — | — |
| Alt | — | — | — | — | — |

## <a id="02"></a>02 규칙

### <a id="02.A"></a>02.A 층

| 층 | 뜻 | 줄별 |
| --- | --- | --- |
| 무수정 | 손에 익어야 하는 것 | 이동, 타겟, 펫, 핵심 콤보, 도주, 긴급 |
| Shift | 밖으로 던지는 것 | 윗줄 공격 주문 6, 아랫줄 교전(summoner는 플레이어 순환, basic은 햄스트링과 디스암) |
| Ctrl | 나와 내 편에 좋은 것 | 숫자줄 포션 6, 윗줄 버프 4와 펫 큐어와 동료 부활, 아랫줄 필드와 유틸 4, `` ` `` 펫 힐 |
| Alt | 소환만 | `1` VS → `2`\~`6`. 예외는 `0` dress 하나다(01.B절). 전투 밖에서 천천히 누른다 |

### <a id="02.B"></a>02.B Mac에서 막히는 키

Ctrl은 Cmd로, Alt는 Option으로 누른다(01절). 그래서 macOS가 먼저 가져가는 키가 있다.

| 키 | 무엇이 막나 | 대처 |
| --- | --- | --- |
| `Ctrl+Space` | macOS가 가져간다 | 쓰지 않는다 |
| `` Ctrl+` `` | macOS 기본 단축키 "다음 윈도우로 초점 이동"이 가져간다 | 시스템 설정 → 키보드 → 키보드 단축키 → 키보드에서 그 항목을 끄고 쓴다 |
| `` Alt+` `` | `` Option+` ``은 악센트 dead key라서 게임에 들어오지 않는다 | 쓰지 않는다. Alt 줄은 `1`부터 쓴다 |

### <a id="02.C"></a>02.C 어디에 거는가

| 어디 | 무엇 | 메모 |
| --- | --- | --- |
| Razor 프로필 `<hotkeys>` | Razor 핫키로 되는 것 전부. 주문, 네크로 능력, 스킬, 타겟, 펫, 포션, Pouch, 힐, 스크립트 | 프로필 하나가 유형 하나라서, 한 파일만 고치면 그 유형의 캐릭터 모두에 적용된다 |
| ClassicUO `macros.xml` | Razor에 없는 것만. 말하기(`bank guards`, `[recallcharge Houseboat`, `[vendor`, `all release`), 클라이언트 UI(F5 이름 표시, F6 투명, Set Bag), 화면에서 클릭해 쓰는 하이드와 명상(키 없음) | 캐릭터마다 따로다. 되도록 적게, 캐릭터끼리 같게 둔다 |
| ClassicUO `profile.json` | 이동 키 `W A S D`(`walk_up_key` 같은 항목) | 캐릭터마다 따로다 |
| 인게임 카운터와 핫바 | 걸지 않는다 | 파일에 없는 바인딩은 저장소가 지킬 수 없다 |

프로필이 `HotKeyStop=True`라서 Razor에 걸린 키는 ClassicUO로 넘어가지 않는다. 같은 키를 양쪽에 걸면 ClassicUO 쪽 매크로는 조용히 죽는다.

::part[쓰는 법]

## <a id="03"></a>03 템플릿이 채우는 칸

| 캐릭터, 템플릿 (유형) | 1 2 3 | F1 | F4 | Alt 줄 |
| --- | --- | --- | --- | --- |
| nomeehej, Bard Necro (summoner) | Disco, Peace, Provo | bard-necro-enhanced | pvp | 소환 5와 VS |
| nomeehui (옛 xuezhonglian), PK 메이지 (default) | Feeblemind, Weaken, Clumsy | skinning-enhanced (현재 연결) | pvp | Water El과 Earth El만 (`Alt+3`, `Alt+4`) |

## <a id="04"></a>04 손에 잡히는 흐름

| 상황 | 키 | 메모 |
| --- | --- | --- |
| 소환 | `Alt+1` → `Alt+2` → `Alt+2`, 솔플은 `Alt+1` → `Alt+3` → `Alt+2` | Vengeful Spirit을 켜고, 듀오는 Lich 둘, 솔플은 Rag Witch와 Lich를 부른다([Bard Necro](../templates/bard-necro.md#04.B) 04.B절) |
| PvE 공격 | `Z` → `V` | summoner는 펫이, basic은 내가 가장 가까운 몹을 친다(01.E절) |
| PvE 주문 | `V`(summoner)로 라타 → `1 E` `2 E` → `4 E` `5 E` | `1`과 `2`는 시그니처 칸이다(03절) |
| PvP 시작 | `F4` | 전투 루프가 멈추고 PvP 루프가 돈다. 펫 공격은 루프가 15초마다 `all kill`로 한다. `F1`로 돌아온다 |
| PvP 타겟 | `Q`, summoner는 `Shift+X/C`, basic은 `X/C` | 라타 하나만 친다. 가장 가까운 플레이어를 잡는 타겟은 서버가 막아 두었고, 플레이어는 순환으로만 잡는다 |
| PvP 주문 | 라타를 잡고 → `6 E` → `4 E` `5 E` |   |
| 폭탄 | `T` `E` → `G` `E` | Telekinesis가 먼저다. 상대가 30초 동안 끈끈이가 된다([PvP](pvp.md#04) 04절) |
| 긴급 | `` ` `` 힐(새끼손가락), 사이드 아래 Pouch(엄지), `Ctrl+1` 힐 포션(엄지와 약지) | 손을 옮기지 않고 누른다 |
| 펫 돌보기 | `` Ctrl+` `` → 펫 클릭(Greater Heal), `Ctrl+T` → 펫 클릭(Cure) |   |

#### 지금 연결된 것

- 저장소의 default 프로필과 summoner 프로필은 F4를 `Play Script: combat\pvp`에 연결한다.
  2026-10-05 템플릿별 PvP 스크립트를 지우고 `combat/pvp` 하나로 합쳤다.
- default의 현재 연결은 `F1=skinning-enhanced`, `F4=pvp`, `T=Telekinesis`다. 2026-10-09 게임에서 lumberjack-enhanced에서 다시 바꿨다.
- 진단 파일은 `debug\...` 경로로 연결한다. 프로필 원본을 고칠 때는 게임을 먼저 끈다([Workflow](../working/workflow.md#04.C) 04.C절).
- 2026-10-05 `xuezhonglian`을 `nomeehui`로 바꿨다. ClassicUO 설정의 정본은 `config/indian/classicuo/nomeehui/`이고, 게임의 새 이름 폴더를 여기에 연결했다.
  캐릭터 serial은 그대로라서 `chars.lst`의 `default` 선택도 그대로다.
- 저장된 연결과 게임의 반응이 다르면, 게임을 완전히 끈 뒤 다시 실행하고 Razor Profile이 `default`인지 확인한다.
  실제로 키가 도는지는 다시 실행한 뒤 인게임에서 확인해야 한다.

::part[자료]

## <a id="05"></a>05 Razor 내장 이름과 L 번호

프로필의 `L:번호`는 `Assistant/Language/Razor_lang.enu`에서 찾는다. 아래는 지금 프로필에 걸린 번호다.

| 번호 | 이름 | 번호 | 이름 |
| --- | --- | --- | --- |
| 1028 \~ 1034 | Drink Heal, Cure, Refresh, Magic Resist, Explosion, Strength, Agility | 1058 | Last Target |
| 1059 | Target Self | 1060 | Set Last Target |
| 1332 | Cancel Current Target | 1391 | > Smart Heal/Cure Self |
| 1395 | Attack Last Target | 1994 | > Interrupt |
| 2013 | Target Closest Non-Friendly Monster | 2022, 2024, 2026 | All Follow Me, All Guard Me, All Kill |
| 2052, 2055 | Next Friendly Player Target, Previous Friendly Player Target | 2054, 2057 | Next Non-Friendly Player Target, Previous Non-Friendly Player Target |
| 2101 | > Stop Current Script | 2527 | Pouch |
| 1044060 + 스킬번호 | 스킬 사용(Disco 1044075, Peace 1044069, Hiding 1044081, Provo 1044082, Meditation 1044106) | 1060522 | Vengeful Spirit. Razor Hotkeys 탭에서 건 번호다. 손으로 넣은 2124는 종료할 때 버려졌다 |

**Magery 주문**의 번호는 계산한다. Razor CE `Spells.cs`의 규칙은 `3002011 + (서클 - 1) × 8 + (서클 안 번호 - 1)`이고, 순서는 CE `spells.def`와 같다.
ClassicUO 매크로의 `subcode`에서 바로 옮기려면 `3001949`를 더한다(`L = subcode + 3001949`, Clumsy `subcode 62` = `L:3002011`).

| 주문 | 번호 | 주문 | 번호 | 주문 | 번호 |
| --- | --- | --- | --- | --- | --- |
| Clumsy | 3002011 | Feeblemind | 3002013 | Magic Arrow | 3002015 |
| Night Sight | 3002016 | Reactive Armor | 3002017 | Weaken | 3002018 |
| Cure | 3002021 | Harm | 3002022 | Protection | 3002025 |
| Bless | 3002027 | Fireball | 3002028 | Poison | 3002030 |
| Telekinesis | 3002031 | Teleport | 3002032 | Wall of Stone | 3002034 |
| Greater Heal | 3002039 | Lightning | 3002040 | Dispel Field | 3002044 |
| Magic Reflection | 3002046 | Mind Blast | 3002047 | Paralyze | 3002048 |
| Summon Creature | 3002050 | Energy Bolt | 3002052 | Explosion | 3002053 |
| Invisibility | 3002054 | Reveal | 3002058 | Chain Lightning | 3002059 |
| Resurrection | 3002069 | Summon Daemon | 3002071 | Summon Earth El. | 3002072 |
| Summon Fire El. | 3002073 | Summon Water El. | 3002074 |   |   |

## <a id="06"></a>06 주문 데미지 메모

위키의 PvM 값이고, Magery 100 기준이다. 자세한 값은 위키 [Magery](https://wiki.uooutlands.com/Magery) 문서에 있다.

| 주문 | 피해 | 비고 |
| --- | --- | --- |
| Fireball | 14\~18 | 0.5초 딜레이 |
| Lightning | 16\~20 | 0.25초 딜레이 |
| Mind Blast | 20\~32 | 상대 AR만큼 늘어난다 |
| Energy Bolt | 32\~44 |   |
| Explosion | 34\~46 | 2.5초 딜레이 |
| Chain Lightning | 30\~42, 2타일 | 리플렉트를 벗긴다. 플레이어가 맞으면 30초 쿨 |
| Flamestrike | 72\~96 | PvP에서는 연속 시전마다 10% 피즐이 쌓인다 |
| Earthquake | 15\~25, 8타일 | PvP에서는 현재 HP의 50% |

::part[기록]

## <a id="07"></a>07 확인 안 된 것

- 인게임 카운터와 핫바에 남아 있던 포션, T, Y 바인딩을 풀었는지.
- default의 `2`와 `3`에 둔 Weaken, Clumsy가 실제 템플릿에 맞는지. 임시로 배정했다. `1`은 2026-10-09 사용자가 Feeblemind로 정했다.
- 사이드 위와 아래가 코드 `-5`, `-4`와 맞는지. 눌러 보고 반대면 두 줄을 맞바꾼다.
- macOS의 "다음 윈도우로 초점 이동"을 끈 뒤 `` Ctrl+` ``이 게임에 들어오는지.
- 아랫줄의 새 배치(`summoner.xml`, `default.xml`)가 게임에서 그대로 도는지.
- 햄스트링과 디스암 토글을 어떻게 거는지(Razor 핫키, 채팅 명령, 버튼). 위키 Hamstring 문서에서 확인하고 basic의 `Shift+Z`와 `Shift+X`에 건다.
- Razor로 옮긴 주문 핫키(`L:3002011` \~ `L:3002074`)가 Outlands에서 그대로 도는지. CE 규칙으로 계산한 번호라서 이 포크에서는 게임으로 확인하지 않았다.
  주문 매크로는 여섯 캐릭터의 `macros.xml`에서 이미 지웠다. 돌지 않는 키는 Razor Hotkeys 탭에서 다시 걸고, 게임을 꺼서 프로필에 저장한다.
