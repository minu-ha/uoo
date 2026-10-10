---
name: Open items
label: 확인할 것
group: Open questions
order: 10
---

작업하다가 사용자에게 물을 것으로 남긴 것을 모은 문서다. 스크립트나 설정을 바꿔야 하는 것, 출처가 없는 숫자, 해석이 갈리는 규칙, 스크립트마다 인게임에서 확인할 것이 여기 있다.
답이 정해지면 그대로 반영하고 이 문서에서 지운다.

## <a id="00"></a>00 한눈에

표마다 마지막 열이 물을 것이다. 답은 "01 drain: 지운다"처럼 절 번호와 항목 이름으로 알려 주면 된다.
새로 물을 것이 생기면 여기에 더한다([Workflow](../working/workflow.md#03) 03절).

먼저 답이 필요한 것은 셋이다.

1. **네 캐릭터의 옛 `cooldowns.xml`**(01절). 그 캐릭터로 스크립트를 돌리면 바를 하나도 읽지 못한다.
2. **뜨지 않는 바 14개**(01절). 지우든 트리거를 달든 정해야 바 목록이 실제와 같아진다.
3. **내가 나에게 건 TK나 받은 TK에도 켜지는 target 바**(08.B절). 내 공격 TK가 들어갔다고 잘못 판단해 포션을 점화할 수 있다.
   지금 루프는 포션을 자동으로 점화하지 않으므로, 자동 점화를 다시 넣기 전에 풀어야 한다.

| 절 | 무엇을 묻나 |
| --- | --- |
| [01](#01) | 뜨지 않거나 옛 형식인 쿨다운 바를 어떻게 할까 |
| [02](#02) | 머리 위 알림 규칙과 어긋난 줄을 어느 쪽으로 맞출까 |
| [03](#03) | 키 배치와 맞지 않는 캐릭터와 바인딩은 예외인가 |
| [04](#04) | 출처 없는 숫자와 사실의 근거는 무엇인가 |
| [05](#05) | 규칙과 다른 파일을 규칙에 맞출까, 규칙을 고칠까 |
| [06](#06) | 겹치거나 제자리가 아닌 문서 내용을 어디로 옮길까 |
| [07](#07) | 순서를 기다리는 일 |
| [08](#08) | 벌목과 PvP에서 자동화하기 전에 무엇을 실험할까 |
| [09](#09) | lumberjack-enhanced를 인게임에서 무엇으로 확인할까 |
| [10](#10) | 공통 pvp를 인게임에서 무엇으로 확인할까 |
| [11](#11) | skinning-enhanced를 인게임에서 무엇으로 확인할까 |
| [12](#12) | tamer-mage-enhanced를 인게임에서 무엇으로 확인할까 |
| [13](#13) | recycle이 루프로 돌아오는지 어떻게 확인할까 |
| [14](#14) | bard-necro-enhanced를 인게임에서 무엇으로 확인할까 |

::part[설정과 알림]

## <a id="01"></a>01 쿨다운 바

| 바 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot, kit, nom, pay 네 캐릭터의 `cooldowns.xml` | 옛 22항목 형식이다(`mushroom`, `CorpseSkin` 같은 이름). 지금 이름을 읽는 스크립트는 그 캐릭터에서 바를 찾지 못한다. nomeehui는 nomeehej와 같은 105항목이다 | nomeehej 파일로 맞출까 |
| `pain spike` `necrosis` `noble sacrifice` `holy light` `poison strike` `curse` `mass curse` `spyglass` `divine fury` `consecrate weapon` `spam` `crew heal` `quest` | 트리거도 없고 세우는 스크립트도 없어서 뜨지 않는다([Overheads](../scripting/overheads.md#06.C) 06.C절) | 지울까, 트리거 문장을 달까 |
| `drain` | 트리거가 머리 위 메시지 "MV ON" 하나인데, 이 메시지를 띄우는 곳이 없다 | 지울까, 다른 트리거를 달까 |

## <a id="02"></a>02 머리 위 메시지

규칙은 [Overheads](../scripting/overheads.md)에 있다. 아래는 그 규칙과 어긋난 채 남은 줄이다.

| 규칙 | 지금 | 정할 것 |
| --- | --- | --- |
| 22자 상한([Overheads](../scripting/overheads.md#02) 02절) | 프로필의 `[ magic arrow, target ]`이 23자다. loadout의 `[ trapped pouch, moved ]`는 24자, `[ alch satchel, moved ]`는 23자다 | 줄일까. `magic arrow`는 줄이지 않는다는 규칙과 부딪힌다 |
| 대상 위에 띄우는 줄은 1288([Overheads](../scripting/overheads.md#01.C) 01.C절) | moongate의 `[ moongate, set ]`은 290으로 게이트 위에, archive/backstab-mugging의 `[ range, out ]`은 254로 lasttarget 위에 뜬다 | 1288로 바꿀까, 예외로 적을까 |
| 한 대상에 한 낱말([Overheads](../scripting/overheads.md#04) 04절) | loadout의 `[ pouch, moved ]`는 looting pouch 줄인데, 글로서리는 `pouch`를 트랩 파우치에 쓴다(`loot pouch`가 맞다). 프로필의 `[ omen, target ]`과 스크립트의 `[ evil omen ]`, train/herding의 `[ herding, done ]`과 글로서리의 `herd`, 바 `cannons`와 `[ cannon, out ]`도 서로 다르다 | 어느 쪽으로 맞출까 |
| 대상만 쓰는 줄은 시전 알림([Overheads](../scripting/overheads.md#05) 05절) | 프로필의 `[ swing ]`(290)은 대상만 쓰는데 시전 알림이 아니다 | `[ swing, on ]`처럼 상태를 붙일까 |
| 고르라는 줄은 `pick` 255 | refill-runebook의 `[ chest, set ]`과 loadout의 `[ loot pouch, set ]`은 대상을 고르게 하는 줄인데 `set` 290이다 | `pick` 255로 바꿀까 |
| 글로서리 낱말 | `gheal` `invis` `tp`를 쓰는 줄이 없다 | 예약어로 둘까, 지울까 |

## <a id="03"></a>03 캐릭터와 핫키

| 무엇 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot | 키 배치를 따르지 않는다. 이동이 화살표 키이고, 매크로는 ClassicUO 기본 세트다(F1 Guards, F2 bank, 4 all stay, 6 Circle Trans). `chars.lst`에도 없다 | 예외로 두는 캐릭터인가 |
| `Shift`+휠 | 아군 순환이 Shift 층의 정의와 어긋난다. Shift 층은 "밖으로 던지는 것"이다([Hotkeys](../game/hotkeys.md#02.A) 02.A절) | 일부러 둔 예외인가 |
| 가장 가까운 플레이어 타겟 | "서버가 막아 놨다"([Hotkeys](../game/hotkeys.md#04) 04절)에 출처가 없다 | 맞다면 PvP 제약이니 [Razor](../scripting/razor.md#07) 07절로 옮길까 |
| "C and a click" | 지금은 없는 bard-necro-pvp의 주석에 있던 말이다. 어느 바인딩과도 맞지 않아서(summoner의 `C`는 All Guard Me) "Q or Shift+X/C"로 고쳤다 | 원래 뜻이 있었나 |
| 저장소 밖 파일 | L 이름과 `Razor_lang.enu`([Hotkeys](../game/hotkeys.md#05) 05절), Wine `user.reg` 키 이름(01절), Clumsy subcode 62(05절)를 대조하지 못했다 | 게임이 깔린 기계에서 대조할 수 있나 |

::part[근거]

## <a id="04"></a>04 출처 없는 숫자와 사실

숫자는 인용한다는 규칙([Workflow](../working/workflow.md#01.C) 01.C절)에 비추어 근거가 없는 것이다. 문서에는 그대로 두었거나 "확인되지 않았다"로 표시했다.

| 무엇 | 어디 | 물을 것 |
| --- | --- | --- |
| 캐릭터의 기본 STR과 DEX(스탯 포션 기준선) | 기준선이 bard-necro-enhanced와 tamer-mage-enhanced는 120과 45, pvp와 skinning-enhanced는 120과 100이다. archive의 bard-mace, bard-throwing, hally-mage는 120과 120이다 | 버프 없는 STR과 DEX가 얼마인가. 기준선은 그 값에 20을 더한 것이다([PvP](../game/pvp.md#09.D) 09.D절). bard-necro의 DEX 25는 사용자가 확인했다(2026-10-10, 포션을 마셔도 45). 그 전의 120은 예전 임계값 100에서 짐작한 값이었다. STR 100은 아직 짐작이다. pvp는 벌목과 skinning 템플릿의 100과 80을 따랐다. pvp는 summoner 프로필에서도 쓰므로, 그 캐릭터의 기본값이 다르면 실행 전에 바꾼다. 선이 높으면 포션이 도는 동안 5초마다 거절될 마시기가 나가고, 낮으면 포션을 아예 마시지 않는다 |
| Lyric 방어구 무시 42.5% | [Bard Necro](../templates/bard-necro.md#03.F) 03.F절 | 출처가 어디인가. Peace 가동률 62%가 이 숫자에서 나왔다 |
| Barding Break 동안 Virtuoso | [Bard Necro](../templates/bard-necro.md#03.F) 03.F절, `bard/peace` 모듈 | 정말 꺼지나. "Barded Creatures"에 디스코만 걸린 몹도 드는지 모른다 |
| PK의 Alchemy | [Bard Necro](../templates/bard-necro.md#06.C) 06.C절 | 80인가 100인가. 지금 숫자는 80 기준이다 |
| `song`과 `peace/provo` 바의 성공 쿨 | `cooldowns.xml`은 11초, 위키는 10초다([Bard Necro](../templates/bard-necro.md#02.C) 02.C절) | 1초를 일부러 더했나 |
| Vengeful Spirit의 마나 | [Bard Necro](../templates/bard-necro.md#04.A) 04.A절, 04.I절 | "마나 101"을 심볼 1과 마나 100으로 고쳤다. 마나가 따로 들지 않나 |
| `cooldown "…"`의 반환값 | [Razor](../scripting/razor.md) | 1인가, 남은 초인가 |
| `and`의 단락 평가 | [Bard Necro](../templates/bard-necro.md#05.H) 05.H절 | 버섯 `findtype`과 `counttype`을 서 있을 때만 읽는다는 설명이 이것에 기댄다. Razor 문서에는 없다 |
| `in`의 대소문자 구분 | [Conventions](../scripting/conventions.md#05) 05절 | 근거가 `dump-label.razor:11` 주석뿐이다. 인게임에서 봤다면 [Razor](../scripting/razor.md#03) 03절 함정 표에 넣는다 |
| Vampiric Embrace 확인 날짜 | [Razor](../scripting/razor.md#04) 04절 | 2026-09-25는 커밋 날짜에서 가져왔다. 실제로 본 날짜인가 |
| `auto-mage.razor:1160` 인용 | [Razor](../scripting/razor.md#04) 04절 | 저장소와 이력 어디에도 없는 파일이다. 어디 있나 |
| Overheads의 숫자 | [Overheads](../scripting/overheads.md#07) 07절, 09절 | 광역 바딩의 8타일과 5초, 2초. Resist 흡수 `25% x Resist/100`과 -75%(PvP의 Parrying 공식과 섞이지 않았나). siphon의 5분마다와 60분. reactive 25. drain의 레지 -10과 -20, 2분. Paralyze PvP 10초 |
| PvP의 주장 | [PvP](../game/pvp.md#02) 02절, 03절, 05절 | "Swordsmanship도 같은 형태다", 크리처 주문 패링 25%, Hamstring이 PvM 목록에는 있다는 말의 출처 |

::part[규칙과 문서]

## <a id="05"></a>05 규칙과 파일이 다른 곳

| 규칙 | 파일은 | 정할 것 |
| --- | --- | --- |
| 헤더는 설명 한 줄과 `Needs:`([Conventions](../scripting/conventions.md#02.C) 02.C절) | archive의 bard-throwing과 bard-mace는 배너 뒤에 "Naming convention" 블록이 온다. bard-necro-enhanced는 배너 없이 설명 한 줄, 설계 문서 안내, Needs가 오고 긴 메모가 이어진다. loadout은 헤더 없이 `clearall`로 시작한다 | 긴 루프의 헤더는 어떤 모양인가 |
| `cooldown` 명령은 기존 파일이 그 스타일일 때만 쓴다([Conventions](../scripting/conventions.md#04) 04절) | archive의 bard-throwing이 `cooldown "ability"`로 게이트를 세운다 | 규칙이 낡았나, 바가 보여야 해서 일부러 쓴 것인가 |
| 같은 성격이 3개 이상이면 폴더([Conventions](../scripting/conventions.md#01.C) 01.C절) | `gather/`와 `restock/`은 2개씩이다 | 규칙을 고칠까, 폴더를 합칠까 |
| 시작 4줄([Conventions](../scripting/conventions.md#02.D) 02.D절) | loadout, claim-loot, share-loot는 `clearall`, `clearsysmsg`, `cleardragdrop`, `clearignore` 순서다. archive의 bard-throwing과 bard-mace는 `clearsysmsg`, `clearall`, `clearignore`, `cleardragdrop` 순서다 | 순서가 중요한가 |
| 세션 값과 영속 값([Conventions](../scripting/conventions.md#03.B) 03.B절) | stock-vendor가 `setvar var__…`로 쓴다. 영속 값을 넣는 `setvar`인데 접두가 `var__`다. loadout은 지금 `setvar global__…`로 규칙에 맞는다 | stock-vendor를 규칙에 맞출까 |

## <a id="06"></a>06 문서 정리

옮길 곳을 정해야 하는 중복과 제자리가 아닌 내용이다. 한 사실은 한 곳에 둔다([Writing](../working/writing.md#08) 08절).

| 무엇 | 제안 |
| --- | --- |
| [Bard Necro](../templates/bard-necro.md#04.H) 04.H절이 되풀이하는 문법 사실 | [Razor](../scripting/razor.md#03) 03절 링크로 바꾼다 |
| "바드 쿨을 자기 타이머로 복사하지 않는다" | 세 문서에 있다. 한 곳을 정본으로 두고 나머지는 링크로 바꾼다 |
| Defensive Barding과 서버 스킬 게이트([Bard Necro](../templates/bard-necro.md#06.A) 06.A절) | 모든 바드 템플릿에 해당하니 [PvP](../game/pvp.md)로 옮긴다 |
| [Bard Necro](../templates/bard-necro.md#07) 07절의 "loadout 배치" 행 | 이 템플릿 이야기가 아니다. Conventions나 Hotkeys로 옮길까 |
| 2026-09-29에 바꾼 루프(교전과 이동 분기, 하우스키핑 시계, peace 대기, 한 줄로 접은 게이트) | 2026-10-10 모듈 조립 뒤의 인게임 확인 목록은 14절이다. 교전과 이동은 거기 있지만, 하우스키핑 시계와 peace 대기와 한 줄로 접은 게이트는 없다. 14절에 더할까 |

::part[보류]

## <a id="07"></a>07 미뤄 둔 것

사용자가 그대로 두라고 한 것이다(2026-09-29). 답을 기다리는 것이 아니라 순서를 기다린다.

| 무엇 | 남은 일 |
| --- | --- |
| archive/hally-mage | `[ cure pot, on ]`(290)을 아직 띄워서 프로필 줄과 겹친다. `[ pvp, on ]`이 234다(공통 pvp는 290). 읽는 무기 바 `Halberd` `Battle Axe` `Viking Sword` `Katana`가 어느 `cooldowns.xml`에도 없다. 2026-10-10에 archive로 옮겼으니 다시 쓸 때 고친다 |
| indian angus nom, kit, pay | [Hotkeys](../game/hotkeys.md#03) 03절에는 summoner 캐릭터가 nomeehej 하나뿐이다. gumps 파일의 serial로 보면 이 셋도 summoner다(추정). 그렇다면 Bard Necro 칸을 받는다. 1 2 3이 Disco, Peace, Provo이고, F1이 bard-necro-enhanced다 |

::part[벌목과 PvP 실험]

## <a id="08"></a>08 벌목과 PvP, 자동화 전에 확인할 것

2026-10-01의 후속 관찰과 근접 중심 설계를 반영했다. 확인된 자기 TK 공용 쿨과 두 클라이언트에서 본 것은 [PvP](../game/pvp.md#04) 04절에 반영했다.
아래는 그 결과로도 아직 정할 수 없거나 고쳐야 하는 부분이다.

### <a id="08.A"></a>08.A TK와 Reflect를 더 확인할 범위

이번 실험에서 TK로 Reflect가 사라지지 않았다는 결과는 다시 미확인으로 돌리지 않는다.
다만 화면에서 본 것을 서버 내부까지 넓히지 않는다. "어떤 조건에서도 반사 판정 자체를 완전히 건너뛴다"는 결론이나 포션 부착의 소유권은 화면만으로 정할 수 없다.

1. A가 공격자, B가 대상인 통제 시험에서 B의 Inscription 값과 Reflect 상태를 기록한다. 처음에는 A의 Reflect를 끄고, 양쪽 TK 제한이 끝난 상태에서 시작한다.
2. A가 B에게 TK를 건 직후 양쪽 Journal과 B의 Reflect를 함께 기록한다. A에게 TK를 받았다는 안내가 오는지, B에게 누가 걸었다고 뜨는지 본다.
3. 따로 한 시행에서 A가 B에게 포션을 던지고, B가 움직여서 실제로 붙었는지 본다. 반대 방향 시험은 새 시행으로 나누고, 모든 TK와 포션 제한이 끝난 뒤에 한다.
4. 비교군으로 Reflect가 없는 B와 A의 자기 TK를 각각 시험한다. 포션이 붙으면 대상 제한이 새로 시작되므로, 마지막으로 걸거나 붙인 때부터 시간을 센다.
5. Inscription 0인 경우와 높은 경우를 나눈다. "첫 반사 뒤에도 남음"을 "전혀 반사되지 않음"과 헷갈리지 않도록 양쪽 화면으로 확인한다.
6. 매번 화면 주인을 적고, 네 경우를 따로 시행한다. 자기 TK만, 내가 상대에게만, 상대가 나에게만, 양쪽이 동시에 거는 경우다.
   양쪽 Journal, 실제 대상 serial, 시도와 응답 시점을 함께 기록한다. 캐릭터 이름이 화면 주인의 이름인지 시전자의 이름인지 구분한다.
7. 취소, 실패, 대상 변경, 응답 지연, 남아 있는 옛 메시지, 수동 TK 핫키 개입을 하나씩 넣어서 거짓 성공이 나오는지 본다.

이 실험을 끝내기 전에도 운영 결론은 같다. TK를 Reflect를 없애거나 공짜로 자기 TK를 얻는 수단으로 쓰지 않는다.

### <a id="08.B"></a>08.B 자동화 전에 남은 것

#### 플레이어 조회 진단과 예전 Q 전투 버전

- 근거: 직접 serial을 쓴 alt TK와 Explosion에서 EB로 잇는 적용, 플레이어 find 실패, 변수 비교 방향 문제, 조회마다의 제한은 인게임 확인됨 2026-10-04.
  결과의 정본은 [Razor](../scripting/razor.md#03.A) 03.A절이다.
- 지금: 2026-10-05에 공격을 수동으로 바꾸고, 상대 조회와 자동 공격을 지금 루프에서 뺐다. 새 자기관리 루프의 확인은 10절에 있다.
  예전 자동 공격의 캐시와 후속 주문 시험은 지금 동작에 필요하지 않다.
- 확인할 것: 사용자는 실행 중 `Range check Last Target`이 ON이고 12타일이라고 확인했다.
  지금 Outlands에서 거리 밖에서 안으로 들어올 때 수동 Last Target이 커서를 쥐고 있다가 놓는지는 확인되지 않았다.
  검색이 플레이어를 빠뜨리는 내부 원인도 아직 모른다. 진단 핫키는 그대로 둔다.
  남은 진단은 셋이다. 바디 ID를 넣은 findtype 비교, 실제 거리를 기록하며 되풀이하는 검사, NPC getlabel에 label이 오지 않은 이유다.

#### 내가 나에게 건 TK나 받은 TK로 target 바가 켜진다

- 근거: 사용자의 후속 보고로는 적의 TK를 받아도 공통 안내와 me 바, target 바가 생길 수 있다.
- 확인할 것: 응답을 기다린 뒤 새 안내가 오고 대상이 같다는 것만으로 성공 처리하지 않는다. 받기만 한 시행에서 절대로 점화하지 않는지 검증한다.
  독립된 성공 신호를 찾지 못하면 자동 점화는 보류한다.
- 기록: 2026-10-04에 당시의 bard-necro-pvp에서 공통 바를 근거로 한 자동 점화 블록을 뺐다. 실제 포션은 손으로 던진다.

#### 나에게 걸린 TK를 누가 걸었나

- 근거: me 바는 `applied telekinesis to you`만 읽는다.
- 확인할 것: 화면 주인마다 고정 문구를 검사하는 방법과 name 표현식을 시험한다. 문자열을 동적으로 조합할 수 있는지는 아직 모른다.
  확인된 공격 TK를 me 바만 보고 취소하지 않는다. 동시에 걸어서 누구 것인지 모호하면 점화하지 않는지 검증한다.

#### 상대 Reflect가 마지막으로 소진됐나

- 근거: Harm 반사 피해와 Spell Siphon 표시는 소진만 알리는 신호가 아니다.
- 확인할 것: 첫 반사로 소진되는 경우, 첫 반사 뒤에도 남는 경우, 두 번째에 소진되는 경우로 나눠 공격자 Journal을 모은다.
  소진 전용 문구가 없으면 스크립트에서 확정 상태로 만들지 않는다.

#### Bless와 스탯 포션

- 근거: 공식으로 계산한 값과 실제 정수 처리, 중첩 처리를 구분해야 한다.
- 확인할 것: Magery 80에서 포션만, Bless만, 둘 다를 순서를 바꿔 가며 쓰고 STR, DEX, INT, 최댓값, 현재 마나를 기록한다.
  Bless 비용 9, 공식값 +8.8의 정수 처리, 스크롤로 꺼내려면 실제 마나 50이 필요한 조건을 구분한다.
- 기록: Magery 100의 Bless는 2026-10-09에 `changed by 11`로 +11이 확인됐다(12절).

#### 프리캐스트와 자동 회복

- 근거: 공식 설명으로는, 완료한 프리캐스트를 쥔 채 포션을 마시면 주문이 취소된다.
- 기록: v5는 보통의 수동 입력을 기다리고, 긴급 회복이 준비되면 수동 주문을 끊었다([PvP](../game/pvp.md#05.E) 05.E절). v6이 수동 입력 중단을 없앴다(10절).
- 확인할 것: 자체 자기 시전 도중에 새 수동 입력이 겹치는 경우는 10절에서 확인한다.

#### 출발 스탯과 무기 교체

- 근거: 벌목 핸드북의 표는 공식에 값을 넣어 계산한 것이다.
- 확인할 것: 지금 안은 100, 80, 45다. 포션을 마신 뒤 DEX 100에서 붕대 10초를, STA 100에서 GA 3초와 Norse 1.5625초를 확인한다.
  공유하는 마지막 스윙, 맞은 뒤 스태미나가 줄어드는 양, 가죽과 Meditation 0에서 30초 동안 재생되는 양도 기록한다.

#### 이동 중 짧은 견제

- 근거: 시전 시작 거리 6타일은 설계 초안이고, 최대 사거리가 아니다.
- 확인할 것: 이동 차단 옵션, LOS, 시전이 끝날 때의 거리, 상대 이동 속도, 실패 뒤 재시도를 확인한다. Harm이 5타일 이상에서 피해가 줄어드는 것과 접근 지연을 비교한다.

#### 피해 계산

- 근거: [Lumberjack PvP](../templates/lumberjack-pvp.md#07) 07절은 Tracking의 주문 보조를 뺀 비교 모델이다.
- 확인할 것: 같은 상대와 장비로 Eval 0과 100, Tracking 있음과 없음, RA 있음과 없음을 나눠 잰다. 계산 중간값을 실측 평균인 것처럼 적지 않는다.

#### Reflect 재시전 제한

- 근거: 2026 공식 패치는 PvP 플래그 중 60초라고 적었다.
- 확인할 것: 시전, 첫 반사, 마지막 소진 가운데 언제 제한이 시작되는지, 플래그 전환과 남은 시간 안내를 양쪽에서 기록한다.

### <a id="08.C"></a>08.C 포션 부착과 실패 복구

1. 30초 안내가 뜨는 플레이어 대상에게서 실제로 붙었다는 메시지, 이동 추적, 피해를 확인한다.
   60초 안내 화면에서 본 `Your explosion potion sticks to your target.`을 PvP에서도 받는지 검증한다.
2. 점화, 커서 생성, 투척, 부착, 폭발 시각을 따로 잰다. 화면의 5, 4, 3, 2만으로 정확한 퓨즈나 네트워크 여유 시간을 정하지 않는다.
3. 점화한 뒤 대상이 벗어나거나, LOS가 막히거나, 대상이 죽거나 바뀌는 상황을 만든다. 내 포션 커서가 남은 경우에만 땅에 던져 버리는 복구를 시험한다.
4. 땅에 던지기는 유효한 위치와 무효한 위치, 높이, 벽, 발밑, 이동 경로로 나눠 확인한다. 투척 완료 신호와 실제 폭발 위치, 반경을 함께 기록한다.
5. 커서 취소, 자동 회복 개입, 부착 메시지 누락을 넣는다. 다른 커서를 써 버리거나 같은 실패에서 포션을 또 점화하면 안 된다.
6. Splashback의 지금 피해 분담과 반경을 확인한다. 회수나 재타겟이 되더라도 퓨즈가 처음으로 돌아간다고 가정하지 않는다.

위 실험 전에는 완전 자동 공격 TK 확인이나 안전한 자동 폭탄 폐기가 구현됐다고 적지 않는다.
받은 TK만으로 점화되면 기능 실패다. 이미 확인된 공격 TK를 me 바 하나 때문에 취소하는 것도 별개의 판정 오류다.

::part[인게임 확인]

## <a id="09"></a>09 lumberjack-enhanced 인게임 확인

지금 버전은 v18이다. 설정, 상태, 타이머와 반영 절차의 정본은 [Lumberjack PvP](../templates/lumberjack-pvp.md#08) 08절이다.

v18(2026-10-10)은 housekeeping 주기를 없앴다. 리콜 블록이 자기 5초 주기로 책, Hunting, 무게를 점검하고, 음식과 목재 정리는 각자의 타이머를 패스마다 본다.
책과 Hunting 조건은 리콜 결정과 함께 `var__hold_gathering` 하나로 채집과 목재 정리를 세운다([Modules](../scripting/modules.md#08) 08절).

#### 기록

- **v8**: 사용자가 기본 채집이 정상으로 돈다고 보고했다(2026-10-05). 인게임 확인됨 2026-10-05.
- **v9**: 손이 비었는데 백팩 도끼를 장착하지 않는다는 보고를 받았다. 인게임 확인됨 2026-10-05.
  실제 검색 범위와 실패한 가드는 아직 모르므로 레이어 문법 오류로 단정하지 않는다.
- **v10**: 빈손이면 저장한 `var__my_hatchet`을 장착하고, 실제 왼손 serial이 같은지 확인하도록 바꿨다.
  - 목재 가공과 파우치 정리는 그대로 두고, 도끼 장착에는 책, Hunting, 무게 준비를 요구하지 않는다.
  - 도구 사용, 커서 대기, 자기 타깃은 같은 채집 블록에서 처리하고, 따로 pending 상태를 두지 않는다.
  - 리콜용 책, Hunting, 무게 점검은 기존 housekeeping 주기를 다시 쓰고, 시간이 지났다는 것만 알리던 응답 타이머와 안내 상태는 없앴다.
  - Tracking 시작 설정과 자동 리콜 판정은 계속 나눠 둔다.
- **v11**: 목재 가공과 파우치 이동 뒤 채집이 멈추고 Logs가 남는다는 보고를 받았다(인게임 보고 2026-10-05). 화면의 오류 문구와 줄 번호는 확인되지 않았다.
  v11은 목록과 foreach를 없애고, 작업 예산과 횟수를 제한한다. 순서를 생존, 자동 리콜, 채집, 자기 버프, housekeeping으로 정리하고, 집 문과 Stockpile 코드는 뺐다.
- **v12**: 네 겹의 채집 조건을 차단 사슬로 정리하고, 큐가 남아 있을 때만 기다리며, 진단 출력을 sysmsg로 나눈다.
  v12 화면에서도 BEGIN 뒤 convert만 계속 나온다는 보고를 받았다(인게임 보고 2026-10-05).
  CE 원본의 제어 흐름을 재현해 보니, if 안의 break가 반복문 범위를 남겨서 바깥 for 2를 Logs 단계로 되돌리는 경로가 있었다.
- **v13**: 목재 검색과 큐 대기를 조건으로 끝나는 while로 바꾸고, break와 continue를 없앴다. 새 상태나 타이머는 없다.
  기존 모의 검사가 엔진의 범위 처리를 놓쳤다는 점을 기록해 둔다. 실제 Outlands 내부에서 같은 동작인지는 확인되지 않았다.
  그 뒤 사용자 Journal에서 v13의 END와 채집 응답을 확인했다. 인게임 확인됨 2026-10-05.
- **v14**: 두 번 정리할 때 같은 Boards serial이 이동 대상으로 되풀이되고, 일부가 옮겨지지 않는다는 보고가 남았다.
  v14는 파우치에 든 것인지를 ignore 전에 가리고, 이미 보관한 Boards는 skip, 나머지는 move request로 기록한다.
  검색이 ignore를 적용하는 경우와 적용하지 않는 경우 모두, 병합과 다음 주기 재시도까지 모의 검사했다.
  지금 포크의 직접 serial 검색에 ignore가 적용되는지와 v14의 실제 이동 성공은 아직 확인되지 않았다.

#### 실제 Smart Harvest 경로

- Hatchet 하나만 준비하고, 손 슬롯 확인, Use item in hand, target self 순서로 채집이 되는지 본다.
- 빈손에서는 `var__my_hatchet`으로 백팩 도끼를 장착하고, 다음 시도에서 왼손 serial이 같은지 본다.
  sysmsg가 ON일 때 나오는 Hatchet equip requested 줄은 요청 기록일 뿐, 성공 증거가 아니다.
- 무게 한도에서도 빈손 장착이 되는지 본다. v18부터는 책이 필수인데 책이 없거나, 감지 리콜인데 Hunting이 없으면 장착도 기다려야 한다.
- 장착 거절, 도끼 파손, 교체, 이미 장착한 상태에서 다시 실행하는 경우도 시험한다. 백팩에만 도끼가 있는데 장착된 것으로 판정하면 실패다.
- 다른 왼손 장비만 비우고, 오른손 장비는 손으로 처리한다.
- 1초 뒤에 도착한 중립 커서도 3초 타임아웃 안에 같은 블록에서 처리해야 한다. 도구 큐가 남아 있어도 자기 타깃을 보내야 한다.
  3초 동안 응답이 없으면 자기 타깃을 보내지 않고, 다음 요청을 4초 더 미루는지 본다.
- 기존 커서가 있으면 새 채집 요청은 미루고 루프는 계속 돌아야 한다. 기다리는 동안 수동 입력과 중립 커서가 겹치는 경우도 시험한다.

#### v17 공용 회복 모듈

- 2026-10-10 v17은 모듈로 조립하면서 회복, 버프, 시약을 pvp와 같은 모듈로 바꿨다([Modules](../scripting/modules.md#08) 08절).
- 재시도 타이머가 없어도 같은 행동이 패스마다 되풀이되지 않아야 한다.
- 워모드를 켜면 회복 주문과 버프가 서고, 포션은 계속 나가야 한다. 리콜이 정해지면 버프가 서야 한다.
- 버프는 손실 15부터 시작하지 않고, 시전 중이면 끊긴다.
- 시약은 자동 리콜 뒤에 읽어서 Tracking 줄을 먼저 본다.
- `[ refresh, out ]`은 이제 뜨지 않는다.

#### v18 블록별 타이머와 채집 보류

- 2026-10-10 v18에서 housekeeping 주기를 없앴다. 먼저 `Lumberjack enhanced v18 loaded`가 뜨는지 본다.
- 음식은 60초마다, 목재 정리는 2분마다, 리콜의 책, Hunting, 무게 점검은 5초마다 각자의 타이머로 돌아야 한다.
- 음식은 다쳤거나, 독에 걸렸거나, 리콜을 정한 중에도 먹지만, 워모드에서는 쉰다.
- 책이 필수인데 책이 없거나, 감지 리콜인데 Hunting이 없으면 빈손 장착, 채집, 목재 정리가 모두 기다린다.
  책을 넣거나 Hunting을 켜면 다음 5초 점검 뒤 다시 시작해야 한다.
- 리콜을 정한 뒤에는 다시 실행하기 전까지 다시 시작하지 않는다.

#### 자원 없음 뒤 2초 재시도

- v15에서 주변 자원 없음 원문과 `[ harvest, out ]` 뒤 약 2초 지나 도구 요청이 나가는지 본다. 새 장소에서 요청하면 다음 간격은 기본 4초로 돌아가야 한다.
- 자원 없음이 되풀이되면 응답마다 2초를 센다.
- 기다리는 동안 회복은 계속하고, 기존 커서, 시전, 이동 바, 리콜 결정을 무시하지 않아야 한다.
- 여행 제한, 수확 실패, 채집 불가를 자원 없음으로 처리하면 실패다.
- 실제 간격과 응답 소비는 아직 인게임에서 확인되지 않았다.

#### 출력 설정 분리

- `config__chatty`와 `config__sysmsg`의 네 조합에서, 골라 켜는 오버헤드와 Journal 진단이 서로 따로 움직이는지 본다.
- 둘을 꺼도 도끼와 파우치 부족 경고, 프로필의 채집 결과는 남아야 한다.

#### 주기적 목재 가공과 파우치 정리

- `pack/lumber`를 넣은 조립과 뺀 조립, 2분과 3분 주기, 파우치를 처음 고를 때와 뺄 때와 용량이 모자랄 때를 시험한다.
- 일반 Logs와 특수 Logs가 Boards로 바뀌고, 기존 Boards와 합쳐져도 새 묶음을 옮겨야 한다. 이미 파우치 안에 있는 Boards는 빼고 센다.
- 가공이나 이동이 실패해도 되풀이 루프를 만들지 않고, 다음 주기까지 남겨 두는지 본다.
- 수동 커서, 시전, 피해, `var__hold_gathering`(리콜 결정, 책 없음, Hunting 없음)은 정리를 미룬다. 처리하는 도중에 상태가 바뀌면 다음 묶음 전에 양보해야 한다.
- 가공과 이동에 2.5초씩 준 예산이 끝나면, 남은 목재는 다음 주기로 넘기고 채집을 다시 하는지 본다.
- v18 loaded를 확인한 뒤 sysmsg의 Lumber pack BEGIN, convert와 skip과 move request, END, 큐와 커서 안내를 남긴다. 기존 파우치의 Boards는 skip만 기록돼야 한다.
- move request는 완료 증거가 아니므로 백팩과 파우치의 실제 묶음 수량을 본다.
  같은 hue로 합쳐진 뒤 다음 주기에 새 Boards만 들어 올리고, 거절된 이동은 다음 주기에 다시 시도하는지 본다.
- 한 번 정리할 때 BEGIN은 한 번이고, 다른 색, 큐 지연, 목재 없음, 이미 보관한 Boards에서도 END에 닿아야 한다.
- 실행이 Play로 돌아가면 Script Error, Line 번호, Script finished 문구도 함께 기록한다. 실제 서버의 인벤토리 갱신에 500ms 대기가 충분한지도 기록한다.

#### 리콜과 Tracking 블록을 뺀 조립

- `escape/tracking`이 있으면 확인한 Hunting을 다시 쓰고, 필요할 때만 시작 설정을 한다. 빼면 시작 설정도 없다.
- `escape/recall`은 Tracking 블록의 상태를 읽는다. 그래서 Tracking만 빼면 조립기가 멈춘다.
- `escape/recall`을 빼면 루프에 리콜용 감지, 책, 여유 무게 조회가 없어야 한다.
- 가까이에 red가 있어도 자기 회복, 버프, 채집은 계속한다.

#### 감지 리콜과 채집의 설정 조합

- recall_on_detection이 1이고 캐릭터에 Tracking이 있을 때만 Hunting 준비를 채집 조건으로 요구한다. 0이면 Hunting 때문에 채집을 미루지 않는다.
- `[ track, check ]`는 2026-10-10부터 `escape/tracking`이 띄운다. 그래서 recall_on_detection과 상관없이 Hunting이 꺼지면 뜨고, Tracking이 0이면 뜨지 않아야 한다.
- 이때도 무게 리콜과 책 필수 조건은 그대로다.

#### Tracking 초기 필터와 상태

- 기본은 red다. 지금 창의 필터를 확인하고, 세션의 색 캐시를 다시 쓴다.
- 바꿔야 하면 Hunting을 먼저 끄고, 최대 10개 필터를 돌며 맞춘다. 설정하는 동안 곰 같은 추적 문구를 비운 뒤 Hunting을 켠다.
- 다른 필터로 Hunting이 켜져 있을 때, Play를 되풀이할 때, 필터를 손으로 바꾼 뒤 Hunting을 껐을 때, 클라이언트를 다시 켰을 때를 각각 시험한다.
- 첫 응답이 빠지거나, 피해를 입거나, 손으로 시전하면 안전해진 뒤 다시 실행해서 준비 상태로 돌아간다.
- 감지 리콜이 ON이고 리콜을 정하기 전일 때만 리콜 블록의 5초 점검 주기로 상태를 보고, Hunting을 확인하지 못하면 채집을 미룬다.
- grey와 orange 확인 문장이 서버 문장과 맞는지도 기록한다.

#### Tracking 거리 오버헤드

- 사용자 요청으로 지금 매핑을 그대로 둔다. spaces to target가 든 서버 문장 전체를 받아서, 거리 숫자가 몇 번째 낱말인지 확인한다.
- 이름의 낱말 수가 달라질 때 고정된 {n}이 같은 숫자를 가리키는지도 본다.

#### 채집 전 리콜 판정과 메시지 순서

- 45 steps와 46 steps, 거리와 상관없는 옵션, 같은 패스의 무게 부족, 시약 부족과 시전 끊김 안내가 함께 도착하는 경우를 시험한다.
- 감지는 무게보다 먼저 읽고, 같은 패스부터 채집을 미룬다.
- 자기 시전, 최대 3초의 도구 커서 대기, 목재 정리 중의 판정 지연과 입력 충돌도 기록한다.
- sysmsg가 ON일 때 Recall trigger 로그로 실제 요청 원인이 Tracking인지 여유 무게인지 가린다.

#### 회복 에이전트, 시약, 수동 입력

- 독, 붕대, 회복 포션, 시약 부족, 프리캐스트를 조합해 보고, 자동 회복 직후의 커서 충돌을 본다.
- 첫 패스와 그 뒤 10초마다의 시약 갱신, 부족 안내를 읽은 패스의 즉시 재검색을 확인한다.

#### Home 리콜과 책 캐시

- 책 충전량, 룬 이름, 지연, 실패와 실행당 한 번의 요청을 본다.
- 사용자 화면의 집 접근 거절은 도착 성공이 아니다. Home 룬의 목적지와 집 권한을 확인하고, 실제 거절 안내가 뜨는지 기록한다.
- 책이 없을 때, 뺄 때, 새로 넣을 때와 책 필수 OFF를 나눠 확인한다.
- 정기 책과 무게 점검은 리콜 블록의 5초 점검 패스에서 채집 전에 한다. 요청 직전에 책이 사라졌으면 캐시를 0으로 바꾸고, 다음 점검까지 다시 찾지 않아야 한다.
- 준비용 Strength 포션과 Agility 포션은 쓰지 않는다.

#### 리콜 결정, 전송, 응답 지연

- 마나 부족, 기존 수동 커서, 이동 때문에 요청을 미뤄도 채집은 멈추고 회복은 계속한다.
- 보낸 뒤에는 늦은 거절을 알리되, 같은 실행에서 다시 보내거나 채집을 다시 시작하지 않아야 한다.
- 5초가 지났다는 것만으로 결과 안내나 도착 상태를 만들지 않는다. 새 요청은 다시 실행해서 시작한다.

#### Heat of Battle과 실제 서버 응답

- 버프만으로 명령 전송을 막지 않아야 한다. 공식 문서에는 Recall도 제한된다고 적혀 있으니, 실제로 허용되는지 거절되는지와 서버 문구를 확인한다.
- 규칙의 정본은 [PvP](../game/pvp.md#01) 01절이다.

#### 채집 결과, 스킬, 거절 프로필 안내

- default와 summoner 프로필에서 각각 일반 logs와 특수 목재의 종류 표시, 수확 실패, 두 배 수확을 확인한다.
  스킬 확률과 스킬 상승, 주변 자원 없음 줄은 summoner에만 있다([Overheads](../scripting/overheads.md#07) 07절).
- 재질은 You chop some으로 찾고, 서버 문장 전체의 {4}를 띄운다. 고갈 안내를 보면 다음 장소로 옮긴다. 확률 숫자를 실제 스킬 상승으로 읽지 않는다.
- 이동 제한, 주변 자원 없음, 채집 불가 안내도 한 번 떠야 한다.
- 실제로 이동한 뒤 서버의 60초 제한과 스크립트의 4초 명령 재시도 간격을 구분한다. 거절 메시지를 받은 때부터 새로 60초를 세지 않는다.
- 매핑의 정본은 [Overheads](../scripting/overheads.md#07) 07절이다.

#### 지금 캐릭터의 쿨다운 바

- heal pot, walk, reflect의 실제 트리거를 본다. 없거나 다르면 그 캐릭터만 나중에 고친다.

## <a id="10"></a>10 공통 pvp의 자기관리와 무기 장착 인게임 확인

`combat/pvp`는 지금 v9이고, 본문은 아직 인게임에서 확인되지 않았다. 설정, 변수, 타이머와 커서 처리의 정본은 [PvP](../game/pvp.md#05.E) 05.E절이다.

#### 기록

- 2026-10-05: `combat/pvp.razor`로 자기관리를 합치고, 예전 PvP 파일 둘은 지웠다.
- 2026-10-06 **v5**: 회복 선택, 긴급 수동 주문 중단, 자기관리 실행, 무기 장착 순서다. GH와 긴급 중단 기준을 손실 35로 맞추고, 시폰과 버섯 자동화, 양손과 슬롯 상태를 없앴다.
- 2026-10-08 **v6**: 각 블록이 지금 상태를 읽고 바로 행동하는 구조로 다시 썼다. 회복 주문은 에이전트가 맡고, 버프는 빠지면 바로 걸고, 스탯 포션은 켜 둔 동안 유지한다.
  수동 입력 중단, 주문의 이동 가드, 6초 시전 대기와 `[ cast, check ]` 정지, 재시도 타이머를 없앴다. 시약은 10초마다, 또는 시약 거절 직후 읽는다.
- 2026-10-09 **v7**: Strength 포션과 Agility 포션을 버프 대신 STR과 DEX 값으로 판정한다. 아군 Bless가 같은 아이콘을 띄워 포션을 막았기 때문이다([PvP](../game/pvp.md#09.D) 09.D절).
- 2026-10-10 **v8**: 가벼운 Heal을 붕대 옆에서도 쓸지 `config__use_light_heal`로 정한다(기본 0). 붕대를 쓸 수 없으면 옵션과 상관없이 대신 나간다.
- 같은 날 **v9**: 모듈로 조립한다. 동작은 v8과 같다([Modules](../scripting/modules.md#08) 08절).

#### 반영하는 법

Scripts 탭에서 Stop, Reload all scripts, Play 순서로 먼저 확인한다.
외부에서 고친 뒤 기존 핫키로 돌릴 때는 클라이언트를 다시 켠다([Workflow](../working/workflow.md#04.A) 04.A절).
게임을 끈 뒤 `git status --short`로 옛 본문이 덮어쓰지 않았는지 본다.

#### 마법과 무기 옵션, 붕대 옵션, 핫키 재연결

- 마법과 무기를 각각 0과 1로, 붕대를 0과 1로 CONFIG에서 바꿔 다시 실행한다. `[ pvp, on ]`과 `PvP sustain v9 loaded`가 떠야 한다.
- F4와 따로 둔 PvP 키는 `combat\pvp`로 다시 연결한다.
- 예전 프리셋이 설정을 덮어쓰거나, 꺼 둔 기능을 요청하면 실패다.

#### Q로 alt나 NPC 고르기, Q 바꾸기, Tab ON과 OFF

- 스크립트는 자동 TK, 공격 주문, 소환수 공격, 근접 공격 요청, Hamstring 토글을 보내지 않는다. 무기 옵션은 상대를 고르지 않아도 동작한다.
- 상대 find, dead, getlabel 제한 경고가 뜨면 실패다. 서버의 기존 자동공격과 수동 요청은 구분한다.

#### 피해, 독, 마비, 낮은 STA, 포션과 붕대와 시약 부족

- 순서는 파우치, Cure 포션, 힐 포션, GH 에이전트, 붕대, 가벼운 Heal이다. 기본 손실 35부터 포션을 쓰고, 포션이 나갈 수 없으면 GH를 쓴다.
- `use_light_heal`이 0인데 붕대가 도는 동안 가벼운 Heal이 나가면 실패다. 1이면 붕대와 함께 나가야 한다.
- Cure 포션이 하나라도 있으면 Cure 에이전트를 쓰지 않아야 한다.
- Healing이 없거나 붕대가 없으면 Heal 경로를 본다.
- 부족하면 `[ pouch, out ]`, `[ cure pot, out ]`, `[ heal pot, out ]`, `[ bandage, out ]`이 뜬다. 진행 중인 붕대를 되풀이해 시작하면 실패다.

#### Magery OFF, 붕대 OFF, 버프와 스탯 포션 옵션

- 꺼 둔 기능의 자동 요청이 없어야 한다. RA와 Reflect는 자기 버프다. 시폰, 버섯, 자기 MA의 자동 반복은 없어야 한다.
- Resist 포션은 버프가 빠진 다음 패스에, Strength 포션과 Agility 포션은 STR과 DEX가 기준선 아래로 내려간 다음 패스에 나가야 한다.
  RA와 Reflect는 빠지면 빈 창에서 바로 다시 나가야 한다.
- 스탯 포션 하나가 떨어져도 나머지는 계속 마셔야 한다.
- `config__str_potion`과 `config__dex_potion`을 실행하는 캐릭터의 기본값에 20을 더한 값으로 맞춘다.
  아군 Bless가 걸린 채 교전해도 힘 포션과 민첩 포션이 한 번씩 나가는지 본다. 마신 뒤 5초마다 다시 눌리면 선이 높은 것이다.
- 포션이 도는 동안 Curse, Weaken, Clumsy를 맞으면 거절 메시지가 5초에 한 번만 나와야 한다.
- 걷는 중에도 버프를 건다. 긴급 손실에서는 버프를 시작하지 않고, 시전 중에 그 선에 닿으면 끊는다.
- Resist 포션은 몹과 펫용이다. 적 플레이어의 주문 피해를 줄인다고 해석하지 않는다.

#### 시작하기 전에 수동 시전, 프리캐스트, 포션, 소환수 커서를 쥐고 있을 때

- 기존 커서를 지킨다. 시전 중이고 커서가 뜨기 전이면 포션이 나가고, 커서를 쥔 동안에는 마비 파우치 말고는 모두 기다린다.
- 커서가 끝난 것을 공격 성공으로 해석하면 실패다.

#### 긴급 HP에서의 수동 입력

- 손실 35 이상에서 손으로 시전 중이면 포션은 나가고, GH는 시전이 끝난 다음 패스에 나가야 한다.
- 완료한 공격 커서를 쥔 동안에는 포션과 GH 모두 기다리고, 커서를 놓은 다음 패스에 나가야 한다.
- 스크립트가 수동 시전이나 커서를 끊으면 실패다.
- 시전 중에 포션을 마셔도 주문이 실제로 끊기지 않는지, 커서를 쥔 채 마시면 주문이 취소되는지도 기록한다.

#### 자동 자기 시전 중의 끊김, 응답 지연, 새 수동 입력

- 에이전트, RA, Reflect는 `for 60` 폴링에서 시전이 끝나거나 끊김 줄이 보이면 다음으로 넘어간다.
- 스크립트는 커서에 답하지 않는다. 에이전트가 만피에서 남긴 beneficial 커서만 취소한다. 손으로 연 harmful이나 neutral 커서를 취소하거나 자기 타깃으로 쓰면 실패다.
- RA나 Reflect 시전 중에 긴급 HP가 되면 `> Interrupt` 뒤 다음 패스에 회복한다.
- 에이전트가 Q 선택과 수동 Last Target에 주는 영향도 본다.

#### 긴급 아이템 회복, 시약 소진과 보충, 빈 스탯 포션 시도

- 처음 실행할 때와 보급품을 채운 직후에도 필요한 마비 파우치, Cure 포션, 힐 포션을 먼저 시도해야 한다.
- Magery가 OFF이거나, 그 주문이 필요 없거나, 최소 마나에 못 미치면 시약을 조회하지 않아야 한다.
- 시약이 없는 상태에서 넣은 뒤 다음 회복이나 버프 점검에 반영되는지 본다.
  시약이 떨어지면 `More reagents are needed` 직후 플래그가 바뀌어 같은 주문을 되풀이하지 않아야 하고, 보충은 10초 안에 반영돼야 한다.
- 붕대를 빼거나 채운 직후에는 진행 중인 붕대를 유지하면서, 다음 점검의 Heal 대체 조건이 실제 재고를 따라야 한다.
- STR과 DEX가 기준선 이상이고 Resist가 있거나 포션이 없으면, 스탯 포션 블록에서 기다리지 않고 무기 단계로 가야 한다.

#### 자기 주문 선택과 마나 임계값

- 기존 기본값에서 Cure, 큰 피해의 GH, 붕대 대체 Heal 순서를 지킨다. 회복이 끝난 패스에서 스탯 포션, RA, Reflect가 차례로 나가야 한다.
- 각 `config__mana_*` 값의 바로 아래와 같은 값에서 시작 조건을 비교한다.
- 예비 마나 20을 반영한 GH 최소값 31에서는 마나 30에 요청하지 않고 31부터 가능해야 한다. 기본값은 예비 마나를 보장하지 않는다.
- GH의 시약만 모자랄 때 붕대 대체 조건을 채운 Heal을, RA의 시약만 모자랄 때 가능한 Reflect를 확인한다.
- 폴링이 끝난 것을 주문 성공으로 해석하면 실패다.

#### 무기 ON과 OFF, 네 슬롯 ID, 쓸 수 있는 무기가 없을 때

- OFF면 장착 명령이 없다. ON에서 슬롯을 하나씩 켜서 바 이름과 ID가 맞게 이어지는지 본다. ID 0은 건너뛴다.
- v6부터 준비된 슬롯의 무기가 백팩에 없으면 다음 슬롯으로 넘어가지 않고, 양손이 비면 `[ weapon, out ]`만 뜬다. 어느 경우에도 장착 없이 회복 루프가 계속돼야 한다.
- `dress serial`이 이 클라이언트에서 실제로 장착되는지도 본다([Razor](../scripting/razor.md#03) 03절의 dress 실패 기록).

#### 여러 스윙 바가 0일 때, 모두 진행 중일 때, 빈손일 때

- 준비된 슬롯 가운데 4, 3, 2, 1 순서로 고른다. Great 4가 진행 중이고 Norse 1만 0이면 Norse로 바꾼다.
- 모두 진행 중이면 지금 장비를 유지하고, 양손이 비면 1, 2, 3, 4 순서로 다시 들기만 한다.
- 모두 0인 동안 두 도끼를 되풀이해 바꾸거나, 장착을 명중으로 처리하면 실패다.

#### 이미 든 무기, 책, 방패와 같은 graphic의 여분

- Arm/Dress의 충돌 장비 자동 해제를 켜고 1H와 2H 사이 교체를 본다.
- 고른 serial이 손에 있으면 장착 요청을 되풀이하지 않는다.
- 찾는 도중에 새 수동 커서, 시전, 큐, 은신이 생기면 장착 요청 직전의 가드가 미뤄야 한다.
- 마지막으로 고른 물건이 손에 있는데 여분으로 되풀이해 바꾸면 실패다.
- `PvP weapon: equip requested`는 요청 표시일 뿐이니 실제 손 장비와 함께 본다.

#### 스윙 바의 타입과 시간, 지금 STA 변화와 실제 스윙

- 활성 캐릭터의 사용 슬롯에 `WeaponSwing` 바가 있는지 UI에서 본다.
- 바의 0만으로 설치 여부나 정확한 스윙 시간을 판정하지 않는다. STA를 바꿔 가며 계산식, 바, 실제 스윙을 비교한다.
- 스크립트가 스윙 바를 시작하거나 초기화하면, 또는 장착이나 Q 변경으로 실제 스윙을 확정하면 실패다.

#### Stop 뒤 다시 실행, 은신, 이동, 구조화 PvP, 필드 Heat of Battle

- 행동 재시도 타이머를 유지하고, 보급품 캐시와 주기적 초기 조회는 없다.
  시약 부족 점검 직후 Stop과 Play를 되풀이해도 회복과 버프의 재조회 간격이 지켜져야 한다.
- 은신 중에는 기다린다. v6부터 걷는 중에도 자동 주문을 시작하므로, 이동 중 시전이 서버에서 거절되거나 끊기는지 기록한다.
- 명령이 제한되면 `[ script, blocked ]` 뒤에 멈춘다. 필드 HoB만으로 같은 차단이 나면 구분에 실패한 것이다.

#### 조건부 전투 모형의 실측 입력

- [Lumberjack PvP](../templates/lumberjack-pvp.md#05.D) 05.D절의 결과는 실제 승률이 아니다.
- 시전을 시작할 때, 끝날 때, 방해받기 직전과 직후의 마나를 기록해서 중단 비용과 시전 중 재생을 확인한다.
- 근접 유지 시간, 양쪽 회복, 도끼 명중, 포션 시각을 함께 기록하고 모형 입력과 비교한다.
- 퓨즈와 Splashback 반경은 [08.C절](#08.C) 실험과 함께 확인한다.

#### 던전 첫 버스트와 회복 대기

- 2026-10-05에 사용자가 보고했다. 메이지 한 명, Reflect 없음, 몹에게 맞은 뒤 HP 약 100에서 약 10초 안에 죽었다.
- [Lumberjack PvP](../templates/lumberjack-pvp.md#05.E) 05.E절의 피해 범위는 설명할 수 있는 조건일 뿐이다. 실제 상대 스킬은 확인되지 않았다.
- TK 적용, 포션 부착, Explosion 방출, EB 시전, 각 피해, 회복 시각과 붕대 남은 시간을 기록한다.
- 시전 중에 포션을 마신 경우와 완료한 프리캐스트를 쥔 채 마신 경우를 나누고, 지금의 수동 입력 대기가 회복 요청을 미뤘는지 본다.
- 30초와 60초 모형의 낮은 사망 비율로 첫 버스트를 버틸 수 있는지 판단하지 않는다.

#### 만피에서 먼저 붕대 감기

- 서버가 만피 Bandage Self 요청을 받아 실제로 붕대를 감는지 본다. 지금 루프는 피해나 독이 있어야 요청한다.
- 이미 피해가 있으면 자기 MA 없이 시작되는지, 수동 커서나 시전이나 진행 중인 붕대가 요청을 막았는지 가린다.
- 자기 MA 자동 반복으로 마나를 쓰거나 진행 중인 붕대를 다시 시작하는 정책은 넣지 않는다.

## <a id="11"></a>11 skinning-enhanced 인게임 확인

`gather/skinning-enhanced`는 지금 v11이고, 본문은 아직 인게임에서 확인되지 않았다.
2026-10-06에 `gather/skinning-enhanced.razor`를 만들었다. Two-Handed Axe를 쓰는 Magery 80 덱서용 던전 근접 루프다.

- 템플릿은 Forensic Evaluation 120, Swordsmanship과 Tactics 100, Magery, Resisting Spells, Parrying, Anatomy, Healing 80, STR 100, DEX 80, INT 45다.
- bard-mace에서 바드를 빼고, lumberjack-enhanced의 자기 회복 주문, RA, Reflect와 시체 칼질을 넣었다.
- 워모드는 사용자가 Tab으로 직접 켠다. Z를 누르고 V를 눌러도 워모드는 바뀌지 않는다.
  싸우는 동안 워모드를 켜 두므로, 회복, 버프, 칼질 어느 것도 워모드를 보지 않는다.

#### 칼질 규칙

칼질은 위키 [Forensic Evaluation](https://wiki.uooutlands.com/Forensic_Evaluation)을 따른다.

> Players can target themselves or nearby ground to activate "Smart Harvest" which carves all grey notoriety corpses "within 2 tiles"

그래서 회색 시체만 깔 때는 `target self`를 쓰고, 회색과 파란 시체를 모두 깔 때는 시체 serial을 하나씩 직접 찍는다(`config__skin_unowned`).
스크립트는 시체 이름 색을 읽지 못하므로 회색 판정은 서버에 맡긴다.

#### 인게임에서 확인한 것

- 사용자 보고: 파란 시체에서 `[ loot, crim ]`이 뜨지만 아이템을 가져가야만 grey가 된다. 2칸 거리의 시체는 검색에 잡힌다.
  ignore한 시체는 clearignore 전까지 findtype에서 빠진다. 인게임 확인됨 2026-10-06.
- lasttarget이 바뀌어도 지금 치고 있는 대상은 바뀌지 않는다는 bard-mace 경험도 함께 보고했다. 칼질이 문제가 되는 것은 다음에 V를 누르는 한 번이다.
- 2026-10-07 v3 Journal에서 직접 타겟 칼질의 `You carve materials from the corpse.`를 확인했다.
- Sanctuary Dungeon의 파란 시체는 `Criminal actions are not permitted in the Sanctuary Dungeon.`으로 거절됐다.
  일반 던전에서는 아이템을 가져가야만 grey가 된다고 사용자가 보고했다. 인게임 확인됨 2026-10-07.
- 플레이어 시체는 다르다. v6이 파란 플레이어 시체 `the remains of Leap Day William`을 직접 찍자
  `You have committed a criminal act! (corpse carving onLeap Day William).`로 범죄 판정을 받았다. 인게임 확인됨 2026-10-07.
  몬스터 시체 이름은 `aged earth corpse`처럼 "…corpse"였다.
- v8은 직접 찍은 뒤의 응답을 읽는다. `That corpse has already been carved.`는 끝난 시체로,
  `That is too far away.`와 `You must wait to perform another action.`은 한 번 더 시도할 시체로 본다. 인게임 확인됨 2026-10-07.
- v3의 `setlasttarget` 복원은 Set Last Target 커서를 띄워 스크립트를 멈췄다. 인게임 확인됨 2026-10-07([Razor](../scripting/razor.md#03) 03절).

#### 기록

- **v5**: 복원을 빼고, 기억한 적이 없을 때만 칼질한다. 거절이 보이면 5분 동안 회색 시체만 깎는다.
- **v6**: sword codex 이름에 `sword_` 접두를 붙이고, 칼질 결과와 범죄 행위 거절을 프로필 오버헤드로 넘겼다.
  같은 날 오버헤드 팔레트의 채도를 낮췄다([Overheads](../scripting/overheads.md#05) 05절).
- **v7**: 직접 찍기 전에 라벨을 읽어서 "corpse"가 있고 "remains"가 없는 시체만 찍는다. 그래도 범죄 판정이 나오면 그 Play 동안 직접 찍기를 끈다.
  공개 스크립트 [forensics](https://outlands.uorazorscripts.com/skills/forensics/c8e4e8eb-743d-4a7f-9043-4c17d2cabb6a)도 `"the remains"`를 플레이어 시체로 보고 건너뛴다.
- 2026-10-09 **v9**: 힘 포션과 민첩 포션을 버프 대신 STR과 DEX 값으로 판정하고([PvP](../game/pvp.md#09.D) 09.D절), 세 스탯 포션을 따로 판정한다.
  v8은 `elseif` 사슬이라 힘 포션이 떨어지면 민첩과 저항 포션까지 막혔다.
- 2026-10-10 **v10**: 가벼운 Heal을 붕대 옆에서도 쓸지 `config__use_light_heal`로 정한다(기본 0). 붕대를 쓸 수 없을 때 대신 나가는 것은 그대로다.
- 같은 날 **v11**: 모듈로 조립하면서 회복, 포션, 버프, 시약을 pvp와 같은 core 블록으로 바꿨다. 바뀐 동작은 [Modules](../scripting/modules.md#08) 08절에 있다.
- Parry Codex는 랭크가 오를 때까지 Bulwark를 쓰고, 근접 밖에서 독, 출혈, 질병이 걸리면 Warding으로 바꾼다.
- 스탠스, 피니셔, 어빌리티는 Arms Lore가 없어서 무기 특수 확률이 기본 10%인 점을 반영해 고른다.
  근거는 `fight/sword-codex`와 `fight/weapon-ability` 모듈의 주석에 있다.
- `config__sysmsg`는 전투 대상 변화, 칼질 요청과 결과, codex 전환, 회복과 버프 시전, 도끼 장착, 골드와 가죽 정리를 Journal에 남긴다.

#### 반영하는 법

Scripts 탭에서 Reload all scripts, Play 순서로 먼저 확인한다. 핫키에 묶었다면 클라이언트를 다시 켠다([Workflow](../working/workflow.md#04.A) 04.A절).
Journal에 `Skinning enhanced v11 loaded`가 떠야 한다.

#### 전투 중 칼질 멈춤

- Z로 몹을 고른 뒤 V를 늦게 눌러도 그 사이에 `Carve request`가 없어야 하고, V가 그 몹을 쳐야 한다.
- 몹이 죽고 약 1.2초 뒤부터 주변 시체를 깎는다.
- 칼 커서가 떠 있을 때 Z를 누르면 커서가 취소되고, 시체는 전투가 끝난 뒤 다시 요청된다.
- `Target a new 'Last Target'` 커서가 뜨거나 V가 시체나 나를 치면 실패다.

#### 범죄 행위가 거절되는 지역

- Sanctuary Dungeon에서 파란 시체를 한 번 요청한 뒤 프로필의 `[ crim, blocked ]`와 Journal의 `Carve mode: grey corpses only`가 뜨고, 5분 동안 Smart Harvest만 써야 한다.
- 같은 파란 시체를 다시 요청하면 실패다. 일반 던전에서는 거절 없이 파란 시체도 깎여야 한다.

#### 칼질 결과 오버헤드

- 깎으면 `[ carve, done ]`, 이미 깎은 시체면 `[ corpse, carved ]`, Smart Harvest가 깎을 시체를 못 찾으면 `[ corpse, out ]`,
  범죄 판정이면 `[ crim, on ]`이 프로필에서 떠야 한다.
- 게임을 끈 상태에서 두 프로필에 넣는다. 스크립트가 같은 문장을 다시 띄우면 실패다.

#### 칼 커서의 종류와 도착

- 스크립트는 칼을 쓴 뒤 2초 안에 온 중립 커서에만 답한다.
- 칼 커서가 중립이 아니거나 2초 뒤에 오면 커서가 남아서 회복과 칼질이 모두 선다. 그러면 실패이고, 남은 커서는 직접 닫는다.

#### 시체 직접 타겟(skin_unowned 1)

- 시체마다 `Carve request: corpse=...` 한 줄과 서버 응답을 기록한다.
- 회색과 파란 몬스터 시체는 깎이고, 플레이어 시체는 `Carve skip: ... label=the remains of ...` 뒤 요청 없이 건너뛰어야 한다.
  플레이어 시체를 찍거나 `You have committed a criminal act`가 다시 뜨면 실패다.
- 인간 NPC 시체의 라벨과 건너뛴 몬스터 시체의 라벨도 기록한다. 라벨을 늦게 받아 비어 있으면 몬스터 시체도 건너뛴다.
- 요청마다 `Carve done`, `Carve miss`, `Carve refused`, `Carve no reply` 가운데 하나가 남아야 한다.
- 너무 멀거나 바쁜 시체는 한 번 더 요청하고(`One more try`), 두 번째도 실패하면 `Skipped`다. 같은 시체를 세 번 이상 찍으면 실패다.

#### Smart Harvest(skin_unowned 0)

- 회색 시체가 깎인 뒤 `worth carving`이 든 응답이 오면 2칸 안의 시체를 모두 건너뛰어야 한다. 파란 시체만 있으면 self를 한 번 쓴 뒤 건너뛴다.
- 위키는 한 번에 가장 가까운 시체라고도, 2칸 안의 회색 시체 전부라고도 적었다. 실제 동작을 기록한다.
- 응답 문구가 달라서 시체가 있는 동안 2초마다 self가 되풀이되면 실패다.

#### Two-Handed Axe 다시 들기

- 왼손을 비우면 저장한 도끼를 다시 든다. 저장한 것이 없으면 graphic 5187을 찾는다. 손에 든 도끼는 라벨의 `two-handed axe`로 한 번 저장한다.
- item-list의 5187이 아닌 다른 graphic의 도끼면 백팩 검색이 실패하니 `config__axe_graphic`을 바꾼다.
- 시전 중에는 장착하지 않아야 한다. 무장 해제 뒤 장착이 거절되면 2초마다 다시 시도하고, 장착 때문에 자기 주문이 끊기면 실패다.

#### Magery 자기 회복과 버프

- 워모드를 켜고 싸우는 중에도 손실 45부터 Greater Heal이 나가야 한다.
- 붕대가 있으면 가벼운 Heal은 쓰지 않는다. `config__use_light_heal`이 1이면 붕대 옆에서도 쓴다.
- 독이면 Cure 포션이 먼저다. 포션이 없을 때만 Smart Heal/Cure로 푼다. 포션과 주문이 같은 독에 함께 나가면 실패다.
- RA와 Reflect는 늘 유지한다. 마나가 RA 24, Reflect 34 이상이면 건다. 손실 35 이상이거나 독이면 시작하지 않고, 시전 중에 그렇게 되면 Interrupt로 끊는다.
- 버프를 시전하는 동안 근접 타격이 멈추는 시간도 기록한다. 시약이 없으면 10초(`interval__reagents`) 안에 다시 확인해야 한다.

#### v11 core 회복(모듈 조립)

- 재시도 타이머가 없어도 같은 행동이 패스마다 되풀이되지 않아야 한다.
- 순서는 큐어 포션, 힐 포션(35), Greater Heal(45, 그 패스에 포션이 안 나갔을 때), 붕대, Refresh(60 이하)다.
- 붕대가 우리 시전 중에도 시작되는지, 그때 시전이 끊기지 않는지 본다.
- 버프는 빠지면 바로 걸고, 독이거나 손실 35 이상이면 시작하지 않고 끊는다.
- 힐 포션 쿨 라벨, `[ refresh, out ]`, `[ str, out ]` 경고는 이제 뜨지 않는다. Journal에는 `Agent: …`와 `Buff: …`가 남는다.

#### 스탯 포션

- 기억한 적이 있을 때 STR 120, DEX 100 아래면 힘 포션과 민첩 포션을 5초에 한 번 마신다. 저항 버프가 빠지면 저항 포션을 마신다.
- 아군 Bless가 걸려 있어도 마셔야 하고, 힘 포션이 떨어져도 민첩과 저항은 계속 나가야 한다.

#### 골드 버리기

- 최대 무게를 넘으면 한 패스에 2000골드를 발밑에 버리고 `[ gold, dropped ]`가 뜬다. 버리는 사이에도 회복이 돌아야 한다.
- 골드가 없으면 `[ weight, over ]`만 뜬다. 무게를 넘지 않았는데 버리면 실패다.

#### 가죽 정리

- 칼질로 나온 가죽이 item-list의 `cut up leather` 4225인지 본다. 다른 graphic(hides 같은)이면 검색에 더한다.
- 기억한 적이 없을 때만 2분마다 돈다.
- 파우치 안의 묶음만 ignore하고 목록을 비우지 않는다. 그래서 정리 뒤 깎은 시체에 다시 요청하면 실패다. 이미 파우치에 든 가죽을 다시 옮겨도 실패다.
- 거절된 이동은 2.5초 예산 안에서 다시 시도한다.

#### 시체가 Last Target일 때

- 기억한 적이 없을 때 시체를 깎으면 Last Target이 바닥의 시체가 된다. 캐시는 `0x40000000 > serial`로 모빌만 `dead`와 `noto`에 넘긴다.
- Mobile not found나 Script Error로 멈추면 실패다.

#### Sword Codex 라벨

- `debug/dump-label`로 sword codex 라벨에 스탠스 이름과 `Execute`, `Bleed Out`이 보이는지 본다.
- 피를 60 넘게 잃으면 `[ sword, defensive ]`, 48 아래로 차면 `[ sword, warrior ]`가 돼야 한다.
- Bleed Out이 골라져 있으면 `[SwordsFinisher2`로 Execute로 바뀌는지, 피니셔가 꺼져 있으면 명령 없이 `[ execute, off ]`만 뜨는지 본다.
- 라벨에 스탠스 이름이 없으면 `[ sword stance, off ]`가 뜬다.

#### Parry Codex

- `debug/dump-label`로 shield codex 라벨에 스탠스 이름과 `Last Stand`, `Barrier`가 보이는지 본다.
- 기본은 Bulwark다. Testudo 랭크가 오르면 `config__parry_stance_main`을 `config__parry_stance_testudo`로 바꾼다.
- 기억한 적이 2칸 밖에 있거나 없을 때 독, 출혈, 질병이 걸리면 `[ parry, warding ]`, 풀리면 `[ parry, bulwark ]`가 떠야 한다. 2칸 안에서 싸우는 중에는 주 스탠스를 유지한다.
- 출혈이나 질병 중에 Warding으로 바뀌지 않으면 `findbuff "Bleed"`와 `"Disease"`의 버프 이름을 확인한다.
- 스탠스 이름이 없으면 명령 없이 `[ parry stance, off ]`만 뜨고, 이번 Play 동안 멈춘다. 같은 스탠스 명령이 3초마다 되풀이되면 실패다.

#### Chop 간격

- 기억한 적이 2칸 안에 있으면 `[ chop ]` 뒤 다음 타격에 나가는지 본다. Arms Lore가 없으니 60초 간격이 맞는지도 본다.

## <a id="12"></a>12 tamer-mage-enhanced 인게임 확인

`combat/tamer-mage-enhanced`는 지금 v6이다. 2026-10-10에 사용자가 지금 쓰지 않는다고 해서 `script/archive/`로 옮겼다가, 같은 날 레시피로 조립하면서 `script/combat/`으로 되돌렸다.
바뀐 동작은 [Modules](../scripting/modules.md#08.E) 08.E절에 있다.

#### 템플릿과 설계

- 2026-10-09에 `combat/tamer-mage-enhanced.razor` v1을 만들었다. Animal Lore, Animal Taming, Veterinary 120, Magery와 Tracking 100, Resisting Spells와 Meditation 80 템플릿용이다.
- bard-necro-enhanced의 생존, 전투 대상, 타겟 주문 모양과 lumberjack-enhanced의 Tracking 설정을 가져왔다.
- 펫 명령과 대상 지정은 손으로 한다. 워모드를 켜면 Flamestrike, Bless, Arch Protection, Create Food가 선다.
- 설계 근거는 위키다. 수의사 키트(Veterinary Supplies)는 붕대처럼 5초 뒤 2칸 안의 내 펫을 모두 치료한다.
  해독과 부활은 50%(펫이 하나면 75%)이고, 쓰면 진행 중인 붕대가 취소된다([Veterinary](https://wiki.uooutlands.com/Veterinary)). 사용자는 힐링 코덱스로 사거리를 3 늘려 5칸으로 쓴다.
- Bless는 9마나에 2분이고, Arch Protection은 11마나에 2분이다. Arch Protection은 6칸 안의 아군 모두의 AR을 올린다. Flamestrike는 40마나다([Magery](https://wiki.uooutlands.com/Magery)).
- Razor `diffhits`는 내 체력만 읽으므로, 펫 체력에 따른 자동 GH는 넣지 않았다.
- 주문 이름은 클라이언트 `spells.def`의 `Flamestrike`, `Bless`, `Arch Protection`, `Create Food`다.

#### 사용자가 확인한 것과 그에 따른 변경

- 같은 날 사용자가 버프 바를 확인했다. Bless는 `Strength`, `Agility`, `Cunning` 세 아이콘으로 뜨고, 시스템 메시지는 `Your strength/dexterity/intelligence has changed by 11`이다.
  Arch Protection은 `Protection`으로 뜬다.
- `Strength`와 `Agility`는 스탯 포션과 겹친다. 그래서 v2는 Bless를 `Cunning`으로, Arch Protection을 `Protection`으로 판정하고 시전 시각 타이머를 없앴다.
- 힘 포션과 민첩 포션도 버프 이름에 Potion이 없어서(사용자 확인) 버프로는 Bless와 구분되지 않는다. 위키 BuffIcons의 `Strength Potion Usage Cooldown`은 표의 라벨일 뿐이다.
- 그래서 포션은 스탯 값으로 판정한다. 포션을 마신 값(기본 + 20)을 `config__str_potion`과 `config__dex_potion`에 두고, 그보다 낮으면 마신다. Bless만 걸린 상태(기본 + 11)는 그보다 낮다.
- 거절된 마시기가 회복 포션과 같은 아이템 큐를 패스마다 차지하지 않도록 5초 재시도 간격을 둔다.
- 사용자는 수의사 키트가 나와 주변 팔로워를 함께 치료한다고 확인했다. 아무도 치료가 필요 없거나 팔로워가 멀면
  `You or your nearby followers do not require healing.`만 남기고 적용되지 않는다. 그래서 v3은 펫 지정과 거리 확인을 없애고 키트를 셀프 붕대로 쓴다.
- v4는 프로필 오버헤드에 등록된 `You begin using veterinary supplies`와 `You finish using veterinary supplies`로 키트가 도는 동안을 잡는다.
  도는 동안은 다시 쓰지 않는다. 다시 쓰면 진행 중인 치료가 취소된다. 피가 1이라도 빠지면 바로, 풀피면 끝난 직후와 거절 2초 뒤에 펫용으로 쓴다.
- v5는 가벼운 Heal 에이전트를 `config__use_light_heal`로 켜고 끄며, 기본은 끈다. 사용자가 너무 자주 나간다고 해서 회복은 키트, 힐 포션, GH만 쓴다.
  독일 때 큐어 포션이 없으면 쓰는 Smart Heal/Cure는 그대로다.
- 나머지 본문은 아직 인게임에서 확인되지 않았다.

#### 반영하는 법

새 파일이므로 Scripts 탭에서 Reload all scripts, Play 순서로 먼저 확인한다. 핫키에 묶었다면 클라이언트를 다시 켠다([Workflow](../working/workflow.md#04.A) 04.A절).
Journal에 `Tamer mage enhanced v6 loaded`가 떠야 한다. 핫키는 `Play Script: combat\tamer-mage-enhanced`다.

#### 수의사 키트

- 내 피가 1이라도 빠지면, 키트가 돌고 있지 않은 한 바로 `[ vet, on ]`이 떠야 한다.
- `[ vet, on ]`부터 `[ vet, done ]`까지는 다시 쓰지 않아야 하고, 끝나면 바로 다음 시도가 나간다.
- 아무도 다치지 않았으면 `You or your nearby followers do not require healing.`이 약 2초마다 한 번 남아야 한다. 더 잦거나 뜸하면 기록한다.
- 치료 중에 키트가 끊기면 실패다. 거절될 때 키트가 줄지 않는지, 키트 시간이 실제로 5초인지, 죽은 펫 부활 시도도 기록한다.
- 키트가 없으면 `[ vet kit, out ]`이 뜬다.

#### Bless와 Arch Protection

- 교전 중이 아니고(전투 대상이 10칸 밖이거나 없음) 워모드가 꺼져 있을 때 `Cunning`과 `Protection` 아이콘이 없으면, 커서에 자기 자신을 찍고 `Buff: Bless`와 `Buff: Arch Protection`이 남아야 한다.
  커서는 Bless가 beneficial, Arch Protection이 neutral이다.
- 아이콘이 뜬 다음 패스에서 같은 주문을 다시 시전하지 않아야 한다. 2분 뒤 아이콘이 사라지면 다시 시전하는지, 펫도 Arch Protection을 받는지 펫 상태에서 본다.

#### Bless와 스탯 포션

- `config__str_potion`과 `config__dex_potion`을 내 기본 힘과 민첩에 20을 더한 값으로 맞춘다. 이 루프의 값 120과 45는 이 템플릿의 STR 100, DEX 25, INT 100 기준이다.
- Bless가 걸린 채 전투에 들어가도 힘 포션과 민첩 포션이 한 번씩 나가고, 마신 뒤 5초마다 다시 눌리지 않아야 한다. 다시 눌리면 값이 높거나 포션이 +20이 아니다.
- 포션(+20)이 Bless(+11)를 덮어쓰는지(120) 쌓이는지(131), 포션이 끝난 뒤 `Cunning`이 남은 동안 Bless의 힘과 민첩이 살아 있는지도 본다.
  사라진다면 그동안은 Bless를 다시 걸지 않는다.
- 저항 포션은 아직 `findbuff "Magic Resist Potion"`으로 판정하므로, 버프 바에 그 이름이 뜨는지 확인한다.

#### Flamestrike

- 전투 대상이 10칸 안이고, 마나 51 이상이고, 워모드가 꺼져 있을 때만 시전한다.
- 시전 중에 다른 몹을 V로 고르면 커서가 취소되고, 다음 패스에 새 대상으로 나가야 한다. 대상이 죽으면 취소한다.
- 손실 35 이상이면 시작하지 않고, 시전 중이면 끊는다. aspect 발동 여부도 기록한다.

#### 버섯

- 마나 55 이하이고 쿨다운이 끝났으면 먹는다.
- 교전 중이 아니고 마나 70 이상이며 버섯이 2개 미만이면 Create Food를 시전한다. Create Food가 실제로 버섯을 만드는지(Grimoire 단계) 본다.

#### Tracking

- 설정한 색 필터로 Hunting이 켜지고, 감지는 프로필의 `[ track, … ]` 오버헤드로만 알린다.
- Hunting이 꺼지면 5초마다 `[ track, check ]`가 뜬다. 귀환은 하지 않는다.

#### 이동 가드

- bard-necro-enhanced처럼 시전 블록은 `walk` 바가 도는 동안 기다린다. 걷는 동안 회복 에이전트가 늦으면 기록한다. 포션은 걷는 중에도 나간다.

## <a id="13"></a>13 recycle 복귀 인게임 확인

2026-10-10부터 `loot/recycle`이 끝나면 마지막으로 Play한 사냥이나 채집 루프를 다시 켠다. 전에는 루프를 바꿀 때마다 마지막 줄의 `script "…"`를 손으로 고쳤다.

- recycle에는 원작자가 넣어 둔 같은 장치가 있었다. 아이템 ID를 못 해서 일찍 끝날 때 이전 스크립트 리스트의 항목을 `hotkey`로 실행한다.
  원작자 저장소에는 이 리스트를 읽는 스크립트만 있고 채우는 스크립트는 없어서, 쓰는 사람이 채운다.
- 그 리스트 이름을 저장소 규칙대로 `list__resume_script`로 바꾸고, recycle 마지막 줄도 같은 모양으로 바꿨다.
- bard-necro-enhanced, skinning-enhanced, lumberjack-enhanced, tamer-mage-enhanced, dexxer-basic이 Play할 때 자기 핫키 이름을 이 리스트에 넣는다.
  archive로 옮긴 bard-mace와 bard-throwing은 `Play Script: archive\…` 이름으로 넣는다. pvp는 싸울 때만 켜므로 넣지 않는다.
- 핫키 이름은 프로필 xml이 F1을 저장한 모양 `Play Script: gather\skinning-enhanced`를 따랐다.
  `hotkey`가 이 이름으로 스크립트를 켜는지, 따옴표 안의 `\`가 그대로 넘어가는지는 아직 확인되지 않았다.
- 변수는 단어를 `4294967295`로 읽으므로([Razor](../scripting/razor.md#03) 03절) 리스트에 넣는다.

#### 복귀

- skinning-enhanced를 Play한 뒤 F3 recycle을 돌리면, 끝나고 `Skinning enhanced v11 loaded`가 다시 떠야 한다. lumberjack-enhanced를 Play한 뒤에는 그쪽으로 돌아와야 한다.
- 아무것도 돌지 않으면 핫키 이름의 모양이 다른 것이다. Razor Hotkeys 탭의 스크립트 이름을 기록한다.

#### ID를 못 해서 일찍 끝날 때

- ID 스킬이나 완드가 없어 `Jase says: Not able to ID items..`가 뜰 때도 같은 루프로 돌아와야 한다.

#### 등록하기 전

- 클라이언트를 켠 뒤 루프를 한 번도 Play하지 않고 recycle을 돌리면 아무 스크립트도 돌지 않아야 한다.

#### pvp 중

- pvp 중에 recycle을 돌리면 마지막 사냥이나 채집 루프로 돌아간다. pvp로 돌아오길 바라면 기록한다.

#### 다시 쓴 recycle

- 2026-10-10에 저장소 규칙으로 다시 썼다. 변수 이름, 오버헤드, 대기 값, 시작 4줄을 바꿨고, 분류는 그대로여야 한다.
- Journal에 `Recycle check: …`가 아이템마다 남는다. 저장할 때는 `[ item, saving ]`과 `Recycle save: …`가 남고, 나머지는 분해된다.
- 링메일의 fortification, hardening, guarding, defense 스위치가 이제 먹고, studded 방어구는 studded 보관함으로 간다(지금은 둘 다 루트 파우치).
- 재질을 못 읽은 방어구는 루트 파우치로 간다. 재활용 도구가 없을 때도 루프로 돌아와야 한다.

## <a id="14"></a>14 bard-necro-enhanced 인게임 확인

2026-10-10에 `combat/bard-necro-enhanced`를 레시피로 조립하게 바꿨다. 바드, 네크로, 공격 주문 블록의 코드는 그대로다.
생존, 포션, 버프, 골드는 공용 모듈로 바뀌었고, 하우스키핑과 교전 및 이동 분기는 레시피 그룹이 만든다. 바뀐 동작은 [Modules](../scripting/modules.md#08.D) 08.D절에 있다.

#### 시작

- Play하면 악기를 찾고(없으면 `[ inst, pick ]`), `[ bard necro, on ]`이 뜬다.

#### 소환수 이름

- 소환한 뒤 5초 안에 `[ name, leech ]`처럼 이름이 뜨고 네임태그가 바뀌어야 한다. 바뀌지 않으면 Journal을 본다.
- `Summon name: no known kind in its label: …`이 뜨면 그 라벨을 기록한다. 아무것도 뜨지 않는데 오버헤드만 뜨면 `rename`이 거부된 것이다.
- 지금까지의 기록(2026-10-10): 종류를 읽은 판(`[ name, mummy ]`)은 서버가 `That name is unacceptable.`로 거절했다.
  종류 단어를 피한 철자로 바꾸자 `mumi`는 받아졌지만 `wytch`는 거절됐다. 한 글자 차이도 막는 것으로 보고 모든 이름을 두 글자 이상 떨어뜨렸다(`leech`, `vampa`, `wicca` 같은).
  새 이름이 받아지는지 본다.

#### Rag Witch 바디

- `mumi`는 바뀌었지만 rag witch는 바뀌지 않았다(2026-10-10). 바디 번호 740이 틀린 것으로 보고 기본 이름 `a rag witch`로도 찾게 했다.
  그다음 판은 rag witch를 찾아 이름을 붙이려 했다(`wytch`는 거절).
- Journal에 `a rag witch found by its name, not its body`가 뜨면 그 rag witch에 `>info`를 해서 Body 번호를 알려 준다. 그 번호를 바디 목록에 넣고 이름으로 찾는 부분은 지운다.
- Vampire Thrall 722도 같은 출처라서 확인되지 않았다.

#### 교전과 이동

- 적을 찍으면 10칸 안에서 Disco, Peace, 네크로 버스트, 오프너, 프록이 예전 순서로 나간다.
- 적이 없으면 버섯, RA, Reflect, Spell Siphon, 노래, Vampiric Embrace가 돈다.

#### Spell Siphon 순서

- RA와 Reflect가 빠진 채 이동하면 RA, Reflect가 먼저 서고, Siphon Magic Arrow는 그다음 패스에 나가야 한다.

#### 독과 힐

- 독에 걸린 채 다치면 큐어가 먼저 나가고, 힐 포션과 Greater Heal은 독이 풀린 뒤에 나간다. 예전보다 위험하게 느껴지면 기록한다.

#### 셀프 버프 끊기

- 잃은 HP 35 이상에서 RA와 Reflect 시전이 끊기는 것이 거슬리면 레시피에서 `buff_max_loss`를 올린다.

#### Journal

- `config__sysmsg`가 1이면 에이전트, 버프, 골드, 전투 대상 줄이 남는다. 너무 많으면 레시피에서 0으로 둔다.

#### 패스 속도

- 패스 끝에 0.1초 대기가, 그리고 10초마다 시약 읽기가 붙었다. 교전 반응이 눈에 띄게 늦으면 기록한다.

#### 버섯

- 교전 중에도 마나 55 이하이고 쿨다운이 끝났으면 먹는다. Create Food는 이동 중에만 나가야 한다.
