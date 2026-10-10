---
name: Open items
label: 확인할 것
group: Open questions
order: 10
---

사용자에게 물을 것 모음. 스크립트나 설정 변경 건, 출처 없는 숫자, 해석이 갈리는 규칙, 스크립트별 인게임 확인.
답이 정해지면 반영하고 이 문서에서 삭제.

## <a id="00"></a>00 한눈에

표마다 마지막 열 = 물을 것. 답은 "01 drain: 지운다"처럼 절 번호와 항목 이름으로.
새로 물을 것은 여기에 추가([Workflow](../working/workflow.md#03) 03절).

먼저 답이 필요한 셋:

1. **네 캐릭터의 옛 `cooldowns.xml`**(01절). 그 캐릭터로 돌리면 바를 하나도 못 읽음
2. **뜨지 않는 바 14개**(01절). 삭제나 트리거 추가를 정해야 바 목록이 실제와 일치
3. **내가 나에게 건 TK, 받은 TK에도 켜지는 target 바**(08.B절). 내 공격 TK 성공으로 오판해 포션을 점화할 위험.
   지금 루프는 자동 점화 없음 → 자동 점화를 다시 넣기 전에 해결

| 절 | 물을 것 |
| --- | --- |
| [01](#01) | 뜨지 않거나 옛 형식인 쿨다운 바 처리 |
| [02](#02) | 머리 위 알림 규칙과 어긋난 줄의 기준 |
| [03](#03) | 키 배치와 맞지 않는 캐릭터와 바인딩이 예외인지 |
| [04](#04) | 출처 없는 숫자와 사실의 근거 |
| [05](#05) | 규칙과 다른 파일: 파일 수정인지 규칙 수정인지 |
| [06](#06) | 겹치거나 제자리가 아닌 문서 내용의 이동처 |
| [07](#07) | 순서를 기다리는 일 |
| [08](#08) | 벌목과 PvP 자동화 전 실험 |
| [09](#09) | lumberjack-enhanced 인게임 확인 |
| [10](#10) | 공통 pvp 인게임 확인 |
| [11](#11) | skinning-enhanced 인게임 확인 |
| [12](#12) | tamer-mage-enhanced 인게임 확인 |
| [13](#13) | recycle의 루프 복귀 확인 |
| [14](#14) | bard-necro-enhanced 인게임 확인 |

::part[설정과 알림]

## <a id="01"></a>01 쿨다운 바

| 바 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot, kit, nom, pay 네 캐릭터의 `cooldowns.xml` | 옛 22항목 형식(`mushroom`, `CorpseSkin` 등). 지금 이름을 읽는 스크립트는 그 캐릭터에서 바를 못 찾음. nomeehui는 nomeehej와 같은 105항목 | nomeehej 파일로 맞출까 |
| `pain spike` `necrosis` `noble sacrifice` `holy light` `poison strike` `curse` `mass curse` `spyglass` `divine fury` `consecrate weapon` `spam` `crew heal` `quest` | 트리거 없음, 세우는 스크립트 없음 → 안 뜸([Overheads](../scripting/overheads.md#06.C) 06.C절) | 삭제, 또는 트리거 문장 추가 |
| `drain` | 트리거는 머리 위 메시지 "MV ON" 하나, 띄우는 곳 없음 | 삭제, 또는 다른 트리거 |

## <a id="02"></a>02 머리 위 메시지

규칙은 [Overheads](../scripting/overheads.md). 아래는 규칙과 어긋난 채 남은 줄.

| 규칙 | 지금 | 정할 것 |
| --- | --- | --- |
| 22자 상한([Overheads](../scripting/overheads.md#02) 02절) | 프로필의 `[ magic arrow, target ]` 23자. loadout의 `[ trapped pouch, moved ]` 24자, `[ alch satchel, moved ]` 23자 | 줄일까. `magic arrow`를 줄이지 않는 규칙과 충돌 |
| 대상 위 줄은 1288([Overheads](../scripting/overheads.md#01.C) 01.C절) | moongate의 `[ moongate, set ]`은 290으로 게이트 위, archive/backstab-mugging의 `[ range, out ]`은 254로 lasttarget 위 | 1288로 바꿀까, 예외로 적을까 |
| 한 대상에 한 낱말([Overheads](../scripting/overheads.md#04) 04절) | loadout의 `[ pouch, moved ]`는 looting pouch 줄인데 글로서리의 `pouch`는 트랩 파우치(`loot pouch`가 맞음). 프로필 `[ omen, target ]`과 스크립트 `[ evil omen ]`, train/herding의 `[ herding, done ]`과 글로서리 `herd`, 바 `cannons`와 `[ cannon, out ]`도 불일치 | 어느 쪽으로 맞출까 |
| 대상만 쓰는 줄 = 시전 알림([Overheads](../scripting/overheads.md#05) 05절) | 프로필의 `[ swing ]`(290)은 대상만인데 시전 알림 아님 | `[ swing, on ]`처럼 상태를 붙일까 |
| 고르라는 줄은 `pick` 255 | refill-runebook의 `[ chest, set ]`, loadout의 `[ loot pouch, set ]`은 고르게 하는 줄인데 `set` 290 | `pick` 255로 바꿀까 |
| 글로서리 낱말 | `gheal` `invis` `tp`를 쓰는 줄 없음 | 예약어로 둘까, 지울까 |

## <a id="03"></a>03 캐릭터와 핫키

| 무엇 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot | 키 배치 밖. 이동은 화살표 키, 매크로는 ClassicUO 기본 세트(F1 Guards, F2 bank, 4 all stay, 6 Circle Trans). `chars.lst`에도 없음 | 예외 캐릭터인가 |
| `Shift`+휠 | 아군 순환이 Shift 층 정의("밖으로 던지는 것")와 어긋남([Hotkeys](../game/hotkeys.md#02.A) 02.A절) | 의도한 예외인가 |
| 가장 가까운 플레이어 타겟 | "서버가 막아 놨다"([Hotkeys](../game/hotkeys.md#04) 04절)에 출처 없음 | 맞다면 PvP 제약 → [Razor](../scripting/razor.md#07) 07절로 옮길까 |
| "C and a click" | 지금은 없는 bard-necro-pvp 주석의 말. 어느 바인딩과도 불일치(summoner의 `C`는 All Guard Me) → "Q or Shift+X/C"로 수정함 | 원래 뜻이 있었나 |
| 저장소 밖 파일 | L 이름과 `Razor_lang.enu`([Hotkeys](../game/hotkeys.md#05) 05절), Wine `user.reg` 키 이름(01절), Clumsy subcode 62(05절) 미대조 | 게임이 깔린 기계에서 대조 가능한가 |

::part[근거]

## <a id="04"></a>04 출처 없는 숫자와 사실

숫자 인용 규칙([Workflow](../working/workflow.md#01.C) 01.C절) 기준으로 근거 없는 것. 문서에는 그대로 두거나 "확인되지 않았다"로 표시.

| 무엇 | 어디 | 물을 것 |
| --- | --- | --- |
| 캐릭터의 기본 STR과 DEX(스탯 포션 기준선) | 기준선: bard-necro-enhanced와 tamer-mage-enhanced 120과 45, pvp와 skinning-enhanced 120과 100, archive의 bard-mace, bard-throwing, hally-mage 120과 120 | 버프 없는 STR과 DEX. 기준선 = 그 값 + 20([PvP](../game/pvp.md#09.D) 09.D절). bard-necro의 DEX 25는 사용자 확인(2026-10-10, 포션을 마셔도 45), 그 전 120은 옛 임계값 100에서 짐작. STR 100은 아직 짐작. pvp는 벌목과 skinning 템플릿의 100과 80 기준, summoner 프로필에서도 쓰므로 그 캐릭터의 기본값이 다르면 실행 전 변경. 선이 높으면 포션 도는 동안 5초마다 거절될 마시기, 낮으면 아예 안 마심 |
| Lyric 방어구 무시 42.5% | [Bard Necro](../templates/bard-necro.md#03.F) 03.F절 | 출처. Peace 가동률 62%의 근거 |
| Barding Break 동안 Virtuoso | [Bard Necro](../templates/bard-necro.md#03.F) 03.F절, `bard/peace` 모듈 | 정말 꺼지나. "Barded Creatures"에 디스코만 걸린 몹도 드는지 모름 |
| PK의 Alchemy | [Bard Necro](../templates/bard-necro.md#06.C) 06.C절 | 80인가 100인가. 지금 숫자는 80 기준 |
| `song`과 `peace/provo` 바의 성공 쿨 | `cooldowns.xml` 11초, 위키 10초([Bard Necro](../templates/bard-necro.md#02.C) 02.C절) | 1초는 의도한 추가인가 |
| Vengeful Spirit의 마나 | [Bard Necro](../templates/bard-necro.md#04.A) 04.A절, 04.I절 | "마나 101"을 심볼 1과 마나 100으로 수정함. 마나가 따로 드나 |
| `cooldown "…"`의 반환값 | [Razor](../scripting/razor.md) | 1인가, 남은 초인가 |
| `and`의 단락 평가 | [Bard Necro](../templates/bard-necro.md#05.H) 05.H절 | 버섯 `findtype`, `counttype`을 서 있을 때만 읽는다는 설명의 전제. Razor 문서에 없음 |
| `in`의 대소문자 구분 | [Conventions](../scripting/conventions.md#05) 05절 | 근거는 `dump-label.razor:11` 주석뿐. 인게임에서 봤다면 [Razor](../scripting/razor.md#03) 03절 함정 표로 |
| Vampiric Embrace 확인 날짜 | [Razor](../scripting/razor.md#04) 04절 | 2026-09-25는 커밋 날짜. 실제로 본 날짜인가 |
| `auto-mage.razor:1160` 인용 | [Razor](../scripting/razor.md#04) 04절 | 저장소와 이력 어디에도 없는 파일. 위치 |
| Overheads의 숫자 | [Overheads](../scripting/overheads.md#07) 07절, 09절 | 광역 바딩의 8타일과 5초, 2초. Resist 흡수 `25% x Resist/100`과 -75%(PvP의 Parrying 공식과 혼동 여부). siphon의 5분마다와 60분. reactive 25. drain의 레지 -10과 -20, 2분. Paralyze PvP 10초 |
| PvP의 주장 | [PvP](../game/pvp.md#02) 02절, 03절, 05절 | "Swordsmanship도 같은 형태다", 크리처 주문 패링 25%, Hamstring이 PvM 목록에 있다는 말의 출처 |

::part[규칙과 문서]

## <a id="05"></a>05 규칙과 파일이 다른 곳

| 규칙 | 파일 | 정할 것 |
| --- | --- | --- |
| 헤더는 설명 한 줄과 `Needs:`([Conventions](../scripting/conventions.md#02.C) 02.C절) | archive의 bard-throwing, bard-mace: 배너 뒤 "Naming convention" 블록. bard-necro-enhanced: 배너 없이 설명 한 줄, 설계 문서 안내, Needs, 긴 메모. loadout: 헤더 없이 `clearall`로 시작 | 긴 루프의 헤더 모양 |
| `cooldown` 명령은 기존 파일이 그 스타일일 때만([Conventions](../scripting/conventions.md#04) 04절) | archive의 bard-throwing이 `cooldown "ability"`로 게이트 | 규칙이 낡았나, 바 표시를 위한 의도인가 |
| 같은 성격 3개 이상이면 폴더([Conventions](../scripting/conventions.md#01.C) 01.C절) | `gather/`, `restock/`은 2개씩 | 규칙 수정, 또는 폴더 병합 |
| 시작 4줄([Conventions](../scripting/conventions.md#02.D) 02.D절) | loadout, claim-loot, share-loot: `clearall`, `clearsysmsg`, `cleardragdrop`, `clearignore` 순. archive의 bard-throwing, bard-mace: `clearsysmsg`, `clearall`, `clearignore`, `cleardragdrop` 순 | 순서가 중요한가 |
| 세션 값과 영속 값([Conventions](../scripting/conventions.md#03.B) 03.B절) | stock-vendor가 `setvar var__…`. 영속 값 `setvar`인데 접두가 `var__`. loadout은 지금 `setvar global__…`로 규칙 준수 | stock-vendor를 규칙에 맞출까 |

## <a id="06"></a>06 문서 정리

이동처를 정할 중복과 제자리가 아닌 내용. 한 사실은 한 곳에([Writing](../working/writing.md#08) 08절).

| 무엇 | 제안 |
| --- | --- |
| [Bard Necro](../templates/bard-necro.md#04.H) 04.H절이 되풀이하는 문법 사실 | [Razor](../scripting/razor.md#03) 03절 링크로 교체 |
| "바드 쿨을 자기 타이머로 복사하지 않는다" | 세 문서에 있음. 한 곳을 정본으로, 나머지는 링크 |
| Defensive Barding과 서버 스킬 게이트([Bard Necro](../templates/bard-necro.md#06.A) 06.A절) | 모든 바드 템플릿 공통 → [PvP](../game/pvp.md)로 이동 |
| [Bard Necro](../templates/bard-necro.md#07) 07절의 "loadout 배치" 행 | 이 템플릿 이야기 아님. Conventions나 Hotkeys로 옮길까 |
| 2026-09-29에 바꾼 루프(교전과 이동 분기, 하우스키핑 시계, peace 대기, 한 줄로 접은 게이트) | 2026-10-10 모듈 조립 뒤 인게임 확인 목록은 14절. 교전과 이동은 있음, 하우스키핑 시계와 peace 대기와 한 줄로 접은 게이트는 없음. 14절에 추가할까 |

::part[보류]

## <a id="07"></a>07 미뤄 둔 것

사용자가 그대로 두라고 한 것(2026-09-29). 답이 아닌 순서 대기.

| 무엇 | 남은 일 |
| --- | --- |
| archive/hally-mage | `[ cure pot, on ]`(290)을 아직 띄움 → 프로필 줄과 중복. `[ pvp, on ]`이 234(공통 pvp는 290). 읽는 무기 바 `Halberd` `Battle Axe` `Viking Sword` `Katana`가 어느 `cooldowns.xml`에도 없음. 2026-10-10 archive로 이동, 다시 쓸 때 수정 |
| indian angus nom, kit, pay | [Hotkeys](../game/hotkeys.md#03) 03절의 summoner 캐릭터는 nomeehej 하나뿐. gumps 파일 serial로 보면 이 셋도 summoner(추정). 그렇다면 Bard Necro 칸: 1 2 3은 Disco, Peace, Provo, F1은 bard-necro-enhanced |

::part[벌목과 PvP 실험]

## <a id="08"></a>08 벌목과 PvP, 자동화 전에 확인할 것

2026-10-01 후속 관찰과 근접 중심 설계 반영. 확인된 자기 TK 공용 쿨과 두 클라이언트 관찰은 [PvP](../game/pvp.md#04) 04절에 반영.
아래는 그 결과로도 아직 못 정하거나 고쳐야 할 부분.

### <a id="08.A"></a>08.A TK와 Reflect 추가 확인 범위

- 이번 실험의 "TK로 Reflect가 사라지지 않음" 결과는 미확인으로 되돌리지 않음
- 화면 관찰을 서버 내부로 넓히지 않음. "어떤 조건에서도 반사 판정을 완전히 건너뜀"이나 포션 부착의 소유권은 화면만으로 결정 불가

1. A 공격자, B 대상의 통제 시험. B의 Inscription 값과 Reflect 상태 기록. 처음엔 A의 Reflect 끔, 양쪽 TK 제한이 끝난 상태에서 시작
2. A가 B에게 TK를 건 직후 양쪽 Journal과 B의 Reflect 기록. A에게 TK를 받았다는 안내가 오는지, B에게 건 사람이 뜨는지
3. 별도 시행: A가 B에게 포션을 던지고 B가 움직여 실제 부착 여부 확인. 반대 방향은 새 시행, 모든 TK와 포션 제한이 끝난 뒤
4. 비교군: Reflect 없는 B, A의 자기 TK를 각각 시험. 포션이 붙으면 대상 제한이 새로 시작 → 마지막으로 걸거나 붙인 때부터 계측
5. Inscription 0과 높은 경우를 나눔. "첫 반사 뒤에도 남음"과 "전혀 반사되지 않음"을 양쪽 화면으로 구분
6. 매번 화면 주인 기록, 네 경우를 따로 시행: 자기 TK만, 내가 상대에게만, 상대가 나에게만, 양쪽 동시.
   양쪽 Journal, 실제 대상 serial, 시도와 응답 시점 함께 기록. 캐릭터 이름이 화면 주인인지 시전자인지 구분
7. 취소, 실패, 대상 변경, 응답 지연, 남은 옛 메시지, 수동 TK 핫키 개입을 하나씩 넣어 거짓 성공 여부 확인

실험 전에도 운영 결론은 같음: TK를 Reflect 제거나 공짜 자기 TK 수단으로 쓰지 않음.

### <a id="08.B"></a>08.B 자동화 전에 남은 것

#### 플레이어 조회 진단과 예전 Q 전투 버전

- 근거: 직접 serial을 쓴 alt TK와 Explosion에서 EB로 잇는 적용, 플레이어 find 실패, 변수 비교 방향 문제, 조회마다의 제한은 인게임 확인됨 2026-10-04.
  결과의 정본은 [Razor](../scripting/razor.md#03.A) 03.A절
- 지금: 2026-10-05 공격을 수동으로 전환, 상대 조회와 자동 공격을 루프에서 삭제. 새 자기관리 루프 확인은 10절.
  예전 자동 공격의 캐시와 후속 주문 시험은 지금 동작에 불필요
- 확인할 것: 실행 중 `Range check Last Target` ON, 12타일(사용자 확인).
  거리 밖에서 안으로 들어올 때 수동 Last Target이 커서를 쥐었다 놓는지는 확인되지 않았다.
  검색이 플레이어를 빠뜨리는 내부 원인도 모름. 진단 핫키 유지.
  남은 진단 셋: 바디 ID를 넣은 findtype 비교, 실제 거리를 기록하며 되풀이하는 검사, NPC getlabel에 label이 안 온 이유

#### 내가 나에게 건 TK, 받은 TK로 target 바가 켜짐

- 근거: 사용자 후속 보고. 적의 TK를 받아도 공통 안내, me 바, target 바가 생길 수 있음
- 확인할 것: 응답 대기 뒤 새 안내와 같은 대상만으로 성공 처리 금지. 받기만 한 시행에서 절대 점화하지 않는지 검증.
  독립된 성공 신호가 없으면 자동 점화 보류
- 기록: 2026-10-04 당시 bard-necro-pvp에서 공통 바 기반 자동 점화 블록 삭제. 실제 포션은 손으로 투척

#### 나에게 걸린 TK를 건 사람

- 근거: me 바는 `applied telekinesis to you`만 읽음
- 확인할 것: 화면 주인별 고정 문구 검사와 name 표현식 시험. 문자열 동적 조합 가능 여부는 모름.
  확인된 공격 TK를 me 바만 보고 취소하지 않음. 동시에 걸어 모호하면 점화하지 않는지 검증

#### 상대 Reflect의 마지막 소진 여부

- 근거: Harm 반사 피해와 Spell Siphon 표시는 소진 전용 신호가 아님
- 확인할 것: 첫 반사로 소진, 첫 반사 뒤에도 남음, 두 번째에 소진으로 나눠 공격자 Journal 수집.
  소진 전용 문구가 없으면 스크립트에서 확정 상태로 만들지 않음

#### Bless와 스탯 포션

- 근거: 공식 계산값과 실제 정수 처리, 중첩 처리의 구분 필요
- 확인할 것: Magery 80에서 포션만, Bless만, 둘 다를 순서를 바꿔 가며 쓰고 STR, DEX, INT, 최댓값, 현재 마나 기록.
  Bless 비용 9, 공식값 +8.8의 정수 처리, 스크롤로 꺼내는 데 필요한 실제 마나 50 조건을 구분
- 기록: Magery 100의 Bless는 2026-10-09 `changed by 11`로 +11 확인(12절)

#### 프리캐스트와 자동 회복

- 근거: 공식 설명상, 완료한 프리캐스트를 쥔 채 포션을 마시면 주문 취소
- 기록: v5는 보통의 수동 입력을 기다리고, 긴급 회복이 준비되면 수동 주문을 끊었음([PvP](../game/pvp.md#05.E) 05.E절). v6에서 수동 입력 중단 삭제(10절)
- 확인할 것: 자체 자기 시전 중 새 수동 입력이 겹치는 경우는 10절

#### 출발 스탯과 무기 교체

- 근거: 벌목 핸드북의 표는 공식에 값을 넣은 계산
- 확인할 것: 지금 안은 100, 80, 45. 포션 뒤 DEX 100에서 붕대 10초, STA 100에서 GA 3초와 Norse 1.5625초 확인.
  공유하는 마지막 스윙, 피격 뒤 스태미나 감소량, 가죽과 Meditation 0에서 30초 동안의 재생량도 기록

#### 이동 중 짧은 견제

- 근거: 시전 시작 거리 6타일은 설계 초안, 최대 사거리 아님
- 확인할 것: 이동 차단 옵션, LOS, 시전 종료 시 거리, 상대 이동 속도, 실패 뒤 재시도. Harm의 5타일 이상 피해 감소와 접근 지연 비교

#### 피해 계산

- 근거: [Lumberjack PvP](../templates/lumberjack-pvp.md#07) 07절은 Tracking의 주문 보조를 뺀 비교 모델
- 확인할 것: 같은 상대와 장비로 Eval 0과 100, Tracking 유무, RA 유무를 나눠 계측. 계산 중간값을 실측 평균처럼 적지 않음

#### Reflect 재시전 제한

- 근거: 2026 공식 패치는 PvP 플래그 중 60초
- 확인할 것: 시전, 첫 반사, 마지막 소진 중 제한 시작 시점, 플래그 전환과 남은 시간 안내를 양쪽에서 기록

### <a id="08.C"></a>08.C 포션 부착과 실패 복구

1. 30초 안내가 뜨는 플레이어 대상에서 실제 부착 메시지, 이동 추적, 피해 확인.
   60초 안내 화면의 `Your explosion potion sticks to your target.`을 PvP에서도 받는지 검증
2. 점화, 커서 생성, 투척, 부착, 폭발 시각을 따로 계측. 화면의 5, 4, 3, 2만으로 정확한 퓨즈나 네트워크 여유 시간을 정하지 않음
3. 점화 뒤 대상 이탈, LOS 차단, 대상 사망이나 변경 상황 연출. 내 포션 커서가 남은 경우에만 땅에 던져 버리는 복구 시험
4. 땅에 던지기: 유효와 무효 위치, 높이, 벽, 발밑, 이동 경로별 확인. 투척 완료 신호, 실제 폭발 위치와 반경 함께 기록
5. 커서 취소, 자동 회복 개입, 부착 메시지 누락 투입. 다른 커서를 써 버리거나 같은 실패에서 포션을 또 점화하면 안 됨
6. Splashback의 지금 피해 분담과 반경 확인. 회수나 재타겟이 되더라도 퓨즈가 처음으로 돌아간다고 가정하지 않음

실험 전에는 완전 자동 공격 TK 확인, 안전한 자동 폭탄 폐기를 구현됐다고 적지 않음.
받은 TK만으로 점화 = 기능 실패. 확인된 공격 TK를 me 바 하나 때문에 취소하는 것도 별개의 판정 오류.

::part[인게임 확인]

## <a id="09"></a>09 lumberjack-enhanced 인게임 확인

지금 v18. 설정, 상태, 타이머, 반영 절차의 정본은 [Lumberjack PvP](../templates/lumberjack-pvp.md#08) 08절.

- v18(2026-10-10): housekeeping 주기 삭제. 리콜 블록이 자기 5초 주기로 책, Hunting, 무게 점검, 음식과 목재 정리는 각자의 타이머를 패스마다 확인
- 책과 Hunting 조건은 리콜 결정과 함께 `var__hold_gathering` 하나로 채집과 목재 정리를 세움([Modules](../scripting/modules.md#08) 08절)

#### 기록

- **v8**: 기본 채집 정상 동작(사용자 보고, 2026-10-05). 인게임 확인됨 2026-10-05
- **v9**: 손이 비었는데 백팩 도끼를 장착하지 않음(보고). 인게임 확인됨 2026-10-05.
  실제 검색 범위와 실패한 가드는 모름 → 레이어 문법 오류로 단정하지 않음
- **v10**: 빈손이면 저장한 `var__my_hatchet` 장착, 실제 왼손 serial 일치 확인
  - 목재 가공과 파우치 정리는 그대로. 도끼 장착에는 책, Hunting, 무게 준비 불필요
  - 도구 사용, 커서 대기, 자기 타깃은 같은 채집 블록에서 처리. 별도 pending 상태 없음
  - 리콜용 책, Hunting, 무게 점검은 기존 housekeeping 주기 재사용. 경과만 알리던 응답 타이머와 안내 상태 삭제
  - Tracking 시작 설정과 자동 리콜 판정은 계속 분리
- **v11**: 목재 가공과 파우치 이동 뒤 채집이 멈추고 Logs가 남음(인게임 보고 2026-10-05). 화면의 오류 문구와 줄 번호는 확인되지 않았다.
  목록과 foreach 삭제, 작업 예산과 횟수 제한. 순서: 생존, 자동 리콜, 채집, 자기 버프, housekeeping. 집 문과 Stockpile 코드 삭제
- **v12**: 네 겹의 채집 조건을 차단 사슬로 정리, 큐가 남았을 때만 대기, 진단 출력은 sysmsg로 분리.
  v12에서도 BEGIN 뒤 convert만 반복(인게임 보고 2026-10-05).
  CE 원본의 제어 흐름 재현 결과, if 안의 break가 반복문 범위를 남겨 바깥 for 2를 Logs 단계로 되돌리는 경로 발견
- **v13**: 목재 검색과 큐 대기를 조건으로 끝나는 while로 교체, break와 continue 삭제. 새 상태나 타이머 없음.
  기존 모의 검사가 엔진의 범위 처리를 놓친 점 기록. 실제 Outlands 내부 동작이 같은지는 확인되지 않았다.
  그 뒤 사용자 Journal에서 v13의 END와 채집 응답 확인. 인게임 확인됨 2026-10-05
- **v14**: 두 번 정리할 때 같은 Boards serial이 이동 대상으로 반복, 일부 미이동(보고).
  파우치에 든 것인지를 ignore 전에 가림, 이미 보관한 Boards는 skip, 나머지는 move request로 기록.
  검색의 ignore 적용과 미적용 두 경우 모두 병합과 다음 주기 재시도까지 모의 검사.
  지금 포크의 직접 serial 검색에 ignore가 적용되는지, v14의 실제 이동 성공은 아직 확인되지 않았다

#### 실제 Smart Harvest 경로

- Hatchet 하나만 준비, 손 슬롯 확인 → Use item in hand → target self 순서로 채집되는지
- 빈손에서 `var__my_hatchet`으로 백팩 도끼 장착, 다음 시도에서 왼손 serial 일치 여부.
  sysmsg ON의 Hatchet equip requested 줄은 요청 기록일 뿐, 성공 증거 아님
- 무게 한도에서도 빈손 장착이 되는지. v18부터 책 필수인데 책이 없거나, 감지 리콜인데 Hunting이 없으면 장착도 대기
- 장착 거절, 도끼 파손, 교체, 장착 상태에서 재실행도 시험. 백팩에만 도끼가 있는데 장착으로 판정하면 실패
- 다른 왼손 장비만 비움, 오른손 장비는 수동 처리
- 1초 뒤 도착한 중립 커서도 3초 타임아웃 안에 같은 블록에서 처리. 도구 큐가 남아도 자기 타깃 전송.
  3초 동안 응답이 없으면 자기 타깃을 보내지 않고 다음 요청을 4초 더 미루는지
- 기존 커서가 있으면 새 채집 요청은 미루고 루프는 계속. 대기 중 수동 입력과 중립 커서가 겹치는 경우도 시험

#### v17 공용 회복 모듈

- 2026-10-10 v17: 모듈 조립으로 회복, 버프, 시약을 pvp와 같은 모듈로 교체([Modules](../scripting/modules.md#08) 08절)
- 재시도 타이머 없이도 같은 행동이 패스마다 반복되지 않아야 함
- 워모드 ON → 회복 주문과 버프 정지, 포션은 계속. 리콜 결정 → 버프 정지
- 버프는 손실 15부터 시작하지 않고, 시전 중이면 끊김
- 시약은 자동 리콜 뒤에 읽어 Tracking 줄을 먼저 확인
- `[ refresh, out ]`은 이제 안 뜸

#### v18 블록별 타이머와 채집 보류

- 2026-10-10 v18: housekeeping 주기 삭제. 먼저 `Lumberjack enhanced v18 loaded` 확인
- 음식 60초마다, 목재 정리 2분마다, 리콜의 책, Hunting, 무게 점검 5초마다, 각자의 타이머
- 음식은 다쳤거나, 독이거나, 리콜 결정 중에도 먹음. 워모드에서는 쉼
- 책 필수인데 책이 없거나, 감지 리콜인데 Hunting이 없으면 빈손 장착, 채집, 목재 정리 모두 대기.
  책을 넣거나 Hunting을 켜면 다음 5초 점검 뒤 재개
- 리콜 결정 뒤에는 재실행 전까지 재개 없음

#### 자원 없음 뒤 2초 재시도

- v15: 주변 자원 없음 원문과 `[ harvest, out ]` 뒤 약 2초 지나 도구 요청이 나가는지. 새 장소에서 요청하면 다음 간격은 기본 4초로 복귀
- 자원 없음이 반복되면 응답마다 2초
- 대기 중에도 회복은 계속, 기존 커서, 시전, 이동 바, 리콜 결정은 존중
- 여행 제한, 수확 실패, 채집 불가를 자원 없음으로 처리하면 실패
- 실제 간격과 응답 소비는 아직 인게임에서 확인되지 않았다

#### 출력 설정 분리

- `config__chatty`와 `config__sysmsg`의 네 조합에서 골라 켜는 오버헤드와 Journal 진단이 독립적으로 움직이는지
- 둘 다 꺼도 도끼와 파우치 부족 경고, 프로필의 채집 결과는 남아야 함

#### 주기적 목재 가공과 파우치 정리

- `pack/lumber`를 넣은 조립과 뺀 조립, 2분과 3분 주기, 파우치를 처음 고를 때, 뺄 때, 용량 부족 시험
- 일반 Logs와 특수 Logs → Boards, 기존 Boards와 합쳐져도 새 묶음 이동. 이미 파우치 안의 Boards는 제외하고 계수
- 가공이나 이동 실패에도 반복 루프 없이 다음 주기로 넘기는지
- 수동 커서, 시전, 피해, `var__hold_gathering`(리콜 결정, 책 없음, Hunting 없음) → 정리 연기. 처리 중 상태가 바뀌면 다음 묶음 전에 양보
- 가공과 이동 각 2.5초 예산이 끝나면 남은 목재는 다음 주기로, 채집 재개 여부
- v18 loaded 확인 뒤 sysmsg의 Lumber pack BEGIN, convert와 skip과 move request, END, 큐와 커서 안내 기록. 기존 파우치의 Boards는 skip만 기록돼야 함
- move request는 완료 증거 아님 → 백팩과 파우치의 실제 묶음 수량 확인.
  같은 hue로 합쳐진 뒤 다음 주기에 새 Boards만 들어 올리는지, 거절된 이동은 다음 주기에 재시도하는지
- 한 번 정리에 BEGIN 한 번. 다른 색, 큐 지연, 목재 없음, 이미 보관한 Boards에서도 END까지 도달
- Play로 돌리면 Script Error, Line 번호, Script finished 문구도 기록. 실제 서버 인벤토리 갱신에 500ms 대기가 충분한지도 기록

#### 리콜과 Tracking 블록을 뺀 조립

- `escape/tracking` 있음 → 확인한 Hunting 재사용, 필요할 때만 시작 설정. 없음 → 시작 설정도 없음
- `escape/recall`은 Tracking 블록의 상태를 읽음 → Tracking만 빼면 조립기 정지
- `escape/recall`을 빼면 리콜용 감지, 책, 여유 무게 조회가 없어야 함
- 가까이 red가 있어도 자기 회복, 버프, 채집은 계속

#### 감지 리콜과 채집의 설정 조합

- recall_on_detection 1이고 캐릭터에 Tracking이 있을 때만 Hunting 준비를 채집 조건으로 요구. 0이면 Hunting 때문에 채집을 미루지 않음
- `[ track, check ]`는 2026-10-10부터 `escape/tracking`이 띄움 → recall_on_detection과 무관하게 Hunting이 꺼지면 뜨고, Tracking 0이면 안 떠야 함
- 이때도 무게 리콜과 책 필수 조건은 그대로

#### Tracking 초기 필터와 상태

- 기본 red. 지금 창의 필터 확인, 세션의 색 캐시 재사용
- 바꿔야 하면 Hunting 먼저 끄고 최대 10개 필터를 돌며 맞춤. 설정 중 곰 같은 추적 문구를 비운 뒤 Hunting 켬
- 다른 필터로 Hunting이 켜진 경우, Play 반복, 필터를 손으로 바꾼 뒤 Hunting을 끈 경우, 클라이언트 재시작을 각각 시험
- 첫 응답 누락, 피해, 수동 시전 → 안전해진 뒤 재실행으로 준비 상태 복귀
- 감지 리콜 ON이고 리콜 결정 전일 때만 리콜 블록의 5초 점검 주기로 상태 확인, Hunting 미확인이면 채집 연기
- grey와 orange 확인 문장이 서버 문장과 일치하는지도 기록

#### Tracking 거리 오버헤드

- 사용자 요청으로 지금 매핑 유지. spaces to target가 든 서버 문장 전체를 받아 거리 숫자의 낱말 위치 확인
- 이름의 낱말 수가 달라질 때 고정된 {n}이 같은 숫자를 가리키는지

#### 채집 전 리콜 판정과 메시지 순서

- 45 steps와 46 steps, 거리 무관 옵션, 같은 패스의 무게 부족, 시약 부족과 시전 끊김 안내가 함께 오는 경우 시험
- 감지는 무게보다 먼저 읽고, 같은 패스부터 채집 연기
- 자기 시전, 최대 3초의 도구 커서 대기, 목재 정리 중의 판정 지연과 입력 충돌도 기록
- sysmsg ON의 Recall trigger 로그로 실제 요청 원인(Tracking 또는 여유 무게) 구분

#### 회복 에이전트, 시약, 수동 입력

- 독, 붕대, 회복 포션, 시약 부족, 프리캐스트를 조합, 자동 회복 직후의 커서 충돌 확인
- 첫 패스와 그 뒤 10초마다의 시약 갱신, 부족 안내를 읽은 패스의 즉시 재검색 확인

#### Home 리콜과 책 캐시

- 책 충전량, 룬 이름, 지연, 실패, 실행당 한 번의 요청 확인
- 사용자 화면의 집 접근 거절은 도착 성공 아님. Home 룬의 목적지와 집 권한 확인, 실제 거절 안내 기록
- 책 없음, 뺌, 새로 넣음, 책 필수 OFF를 나눠 확인
- 정기 책과 무게 점검은 리콜 블록의 5초 점검 패스에서 채집 전에. 요청 직전 책이 사라졌으면 캐시를 0으로, 다음 점검까지 재검색 없음
- 준비용 Strength 포션, Agility 포션은 안 씀

#### 리콜 결정, 전송, 응답 지연

- 마나 부족, 기존 수동 커서, 이동 때문에 요청을 미뤄도 채집은 정지, 회복은 계속
- 전송 뒤 늦은 거절은 알리되, 같은 실행에서 재전송이나 채집 재개 없음
- 5초 경과만으로 결과 안내나 도착 상태를 만들지 않음. 새 요청은 재실행으로 시작

#### Heat of Battle과 실제 서버 응답

- 버프만으로 명령 전송을 막지 않아야 함. 공식 문서상 Recall도 제한 → 실제 허용 여부와 서버 문구 확인
- 규칙의 정본은 [PvP](../game/pvp.md#01) 01절

#### 채집 결과, 스킬, 거절 프로필 안내

- default와 summoner 프로필에서 각각 일반 logs와 특수 목재의 종류 표시, 수확 실패, 두 배 수확 확인.
  스킬 확률과 스킬 상승, 주변 자원 없음 줄은 summoner에만([Overheads](../scripting/overheads.md#07) 07절)
- 재질은 You chop some으로 찾고 서버 문장 전체의 {4} 표시. 고갈 안내 → 다음 장소로 이동. 확률 숫자를 실제 스킬 상승으로 읽지 않음
- 이동 제한, 주변 자원 없음, 채집 불가 안내도 한 번씩 떠야 함
- 실제 이동 뒤 서버의 60초 제한과 스크립트의 4초 명령 재시도 간격 구분. 거절 메시지를 받은 때부터 60초를 새로 세지 않음
- 매핑의 정본은 [Overheads](../scripting/overheads.md#07) 07절

#### 지금 캐릭터의 쿨다운 바

- heal pot, walk, reflect의 실제 트리거 확인. 없거나 다르면 그 캐릭터만 나중에 수정

## <a id="10"></a>10 공통 pvp의 자기관리와 무기 장착 인게임 확인

`combat/pvp` 지금 v9, 본문은 아직 인게임에서 확인되지 않았다. 설정, 변수, 타이머, 커서 처리의 정본은 [PvP](../game/pvp.md#05.E) 05.E절.

#### 기록

- 2026-10-05: `combat/pvp.razor`로 자기관리 통합, 예전 PvP 파일 둘 삭제
- 2026-10-06 **v5**: 회복 선택, 긴급 수동 주문 중단, 자기관리 실행, 무기 장착 순서. GH와 긴급 중단 기준을 손실 35로 통일, 시폰과 버섯 자동화, 양손과 슬롯 상태 삭제
- 2026-10-08 **v6**: 각 블록이 지금 상태를 읽고 바로 행동하는 구조로 재작성. 회복 주문은 에이전트, 버프는 빠지면 바로 시전, 스탯 포션은 켜 둔 동안 유지.
  수동 입력 중단, 주문의 이동 가드, 6초 시전 대기와 `[ cast, check ]` 정지, 재시도 타이머 삭제. 시약은 10초마다, 또는 시약 거절 직후 읽음
- 2026-10-09 **v7**: Strength 포션, Agility 포션을 버프 대신 STR과 DEX 값으로 판정. 아군 Bless가 같은 아이콘을 띄워 포션을 막았음([PvP](../game/pvp.md#09.D) 09.D절)
- 2026-10-10 **v8**: 가벼운 Heal을 붕대 옆에서도 쓸지 `config__use_light_heal`로 결정(기본 0). 붕대를 못 쓰면 옵션과 무관하게 대신 나감
- 같은 날 **v9**: 모듈 조립. 동작은 v8과 같음([Modules](../scripting/modules.md#08) 08절)

#### 반영하는 법

- Scripts 탭에서 Stop → Reload all scripts → Play 순서로 먼저 확인
- 외부에서 고친 뒤 기존 핫키로 돌리면 클라이언트 재시작([Workflow](../working/workflow.md#04.A) 04.A절)
- 게임 종료 뒤 `git status --short`로 옛 본문의 덮어쓰기 여부 확인

#### 마법과 무기 옵션, 붕대 옵션, 핫키 재연결

- 마법과 무기를 각각 0과 1로, 붕대를 0과 1로 CONFIG에서 바꿔 재실행. `[ pvp, on ]`과 `PvP sustain v9 loaded`가 떠야 함
- F4와 별도 PvP 키는 `combat\pvp`로 재연결
- 예전 프리셋이 설정을 덮어쓰거나, 꺼 둔 기능을 요청하면 실패

#### Q로 alt나 NPC 고르기, Q 바꾸기, Tab ON과 OFF

- 스크립트는 자동 TK, 공격 주문, 소환수 공격, 근접 공격 요청, Hamstring 토글을 보내지 않음. 무기 옵션은 상대를 고르지 않아도 동작
- 상대 find, dead, getlabel 제한 경고가 뜨면 실패. 서버의 기존 자동공격과 수동 요청은 구분

#### 피해, 독, 마비, 낮은 STA, 포션과 붕대와 시약 부족

- 순서: 파우치, Cure 포션, 힐 포션, GH 에이전트, 붕대, 가벼운 Heal. 기본 손실 35부터 포션, 포션이 못 나가면 GH
- `use_light_heal` 0인데 붕대 중 가벼운 Heal이 나가면 실패. 1이면 붕대와 함께 나가야 함
- Cure 포션이 하나라도 있으면 Cure 에이전트를 쓰지 않아야 함
- Healing이나 붕대가 없으면 Heal 경로 확인
- 부족하면 `[ pouch, out ]`, `[ cure pot, out ]`, `[ heal pot, out ]`, `[ bandage, out ]`. 진행 중인 붕대를 반복해 시작하면 실패

#### Magery OFF, 붕대 OFF, 버프와 스탯 포션 옵션

- 꺼 둔 기능의 자동 요청 없음. RA와 Reflect는 자기 버프. 시폰, 버섯, 자기 MA의 자동 반복 없음
- Resist 포션은 버프가 빠진 다음 패스에, Strength 포션과 Agility 포션은 STR과 DEX가 기준선 아래로 내려간 다음 패스에.
  RA와 Reflect는 빠지면 빈 창에서 바로 다시
- 스탯 포션 하나가 떨어져도 나머지는 계속
- `config__str_potion`과 `config__dex_potion`은 실행 캐릭터의 기본값 + 20.
  아군 Bless가 걸린 채 교전해도 힘 포션과 민첩 포션이 한 번씩 나가는지. 마신 뒤 5초마다 다시 눌리면 선이 높음
- 포션 도는 동안 Curse, Weaken, Clumsy에 맞으면 거절 메시지는 5초에 한 번만
- 걷는 중에도 버프. 긴급 손실에서는 버프를 시작하지 않고, 시전 중 그 선에 닿으면 끊음
- Resist 포션은 몹과 펫용. 적 플레이어의 주문 피해 감소로 해석하지 않음

#### 시작 전에 수동 시전, 프리캐스트, 포션, 소환수 커서를 쥔 경우

- 기존 커서 보호. 시전 중이고 커서가 뜨기 전이면 포션은 나감, 커서를 쥔 동안에는 마비 파우치 외 모두 대기
- 커서 종료를 공격 성공으로 해석하면 실패

#### 긴급 HP에서의 수동 입력

- 손실 35 이상에서 수동 시전 중이면 포션은 나가고, GH는 시전이 끝난 다음 패스에
- 완료한 공격 커서를 쥔 동안에는 포션과 GH 모두 대기, 커서를 놓은 다음 패스에
- 스크립트가 수동 시전이나 커서를 끊으면 실패
- 시전 중 포션을 마셔도 주문이 실제로 안 끊기는지, 커서를 쥔 채 마시면 주문이 취소되는지도 기록

#### 자동 자기 시전 중의 끊김, 응답 지연, 새 수동 입력

- 에이전트, RA, Reflect는 `for 60` 폴링에서 시전이 끝나거나 끊김 줄이 보이면 다음으로
- 스크립트는 커서에 응답하지 않음. 에이전트가 만피에서 남긴 beneficial 커서만 취소. 손으로 연 harmful이나 neutral 커서를 취소하거나 자기 타깃으로 쓰면 실패
- RA나 Reflect 시전 중 긴급 HP → `> Interrupt` 뒤 다음 패스에 회복
- 에이전트가 Q 선택과 수동 Last Target에 주는 영향도 확인

#### 긴급 아이템 회복, 시약 소진과 보충, 빈 스탯 포션 시도

- 첫 실행과 보급품 보충 직후에도 필요한 마비 파우치, Cure 포션, 힐 포션을 먼저 시도
- Magery OFF, 그 주문이 불필요, 최소 마나 미달이면 시약 조회 없음
- 시약 없는 상태에서 넣은 뒤 다음 회복이나 버프 점검에 반영되는지.
  시약이 떨어지면 `More reagents are needed` 직후 플래그가 바뀌어 같은 주문 반복 없음, 보충은 10초 안에 반영
- 붕대를 빼거나 채운 직후 진행 중인 붕대는 유지, 다음 점검의 Heal 대체 조건은 실제 재고를 따라야 함
- STR과 DEX가 기준선 이상이고 Resist가 있거나 포션이 없으면, 스탯 포션 블록에서 대기 없이 무기 단계로

#### 자기 주문 선택과 마나 임계값

- 기본값에서 Cure, 큰 피해의 GH, 붕대 대체 Heal 순서 유지. 회복이 끝난 패스에서 스탯 포션, RA, Reflect 차례
- 각 `config__mana_*` 값의 바로 아래와 같은 값에서 시작 조건 비교
- 예비 마나 20을 반영한 GH 최소값 31: 마나 30에서는 요청 없음, 31부터 가능. 기본값은 예비 마나를 보장하지 않음
- GH 시약만 모자랄 때 붕대 대체 조건을 채운 Heal, RA 시약만 모자랄 때 가능한 Reflect 확인
- 폴링 종료를 주문 성공으로 해석하면 실패

#### 무기 ON과 OFF, 네 슬롯 ID, 쓸 수 있는 무기가 없을 때

- OFF면 장착 명령 없음. ON에서 슬롯을 하나씩 켜 바 이름과 ID 연결 확인. ID 0은 건너뜀
- v6부터 준비된 슬롯의 무기가 백팩에 없으면 다음 슬롯으로 넘어가지 않음, 양손이 비면 `[ weapon, out ]`만. 어느 경우에도 장착 없이 회복 루프 계속
- `dress serial`이 이 클라이언트에서 실제로 장착되는지([Razor](../scripting/razor.md#03) 03절의 dress 실패 기록)

#### 여러 스윙 바가 0일 때, 모두 진행 중일 때, 빈손일 때

- 준비된 슬롯 중 4, 3, 2, 1 순서. Great 4가 진행 중이고 Norse 1만 0이면 Norse로 교체
- 모두 진행 중이면 지금 장비 유지, 양손이 비면 1, 2, 3, 4 순서로 다시 들기만
- 모두 0인 동안 두 도끼를 반복 교체하거나 장착을 명중으로 처리하면 실패

#### 이미 든 무기, 책, 방패와 같은 graphic의 여분

- Arm/Dress의 충돌 장비 자동 해제를 켜고 1H와 2H 사이 교체 확인
- 고른 serial이 손에 있으면 장착 요청 반복 없음
- 찾는 도중 새 수동 커서, 시전, 큐, 은신 → 장착 요청 직전 가드가 연기
- 마지막으로 고른 물건이 손에 있는데 여분으로 반복 교체하면 실패
- `PvP weapon: equip requested`는 요청 표시일 뿐, 실제 손 장비와 함께 확인

#### 스윙 바의 타입과 시간, 지금 STA 변화와 실제 스윙

- 활성 캐릭터의 사용 슬롯에 `WeaponSwing` 바가 있는지 UI에서 확인
- 바의 0만으로 설치 여부나 정확한 스윙 시간을 판정하지 않음. STA를 바꿔 가며 계산식, 바, 실제 스윙 비교
- 스크립트가 스윙 바를 시작하거나 초기화하면, 또는 장착이나 Q 변경으로 실제 스윙을 확정하면 실패

#### Stop 뒤 재실행, 은신, 이동, 구조화 PvP, 필드 Heat of Battle

- 행동 재시도 타이머 유지, 보급품 캐시와 주기적 초기 조회 없음.
  시약 부족 점검 직후 Stop과 Play를 반복해도 회복과 버프의 재조회 간격 유지
- 은신 중 대기. v6부터 걷는 중에도 자동 주문을 시작 → 이동 중 시전의 서버 거절이나 끊김 기록
- 명령 제한 → `[ script, blocked ]` 뒤 정지. 필드 HoB만으로 같은 차단이 나면 구분 실패

#### 조건부 전투 모형의 실측 입력

- [Lumberjack PvP](../templates/lumberjack-pvp.md#05.D) 05.D절의 결과는 실제 승률 아님
- 시전 시작, 종료, 방해 직전과 직후의 마나 기록 → 중단 비용과 시전 중 재생 확인
- 근접 유지 시간, 양쪽 회복, 도끼 명중, 포션 시각을 함께 기록해 모형 입력과 비교
- 퓨즈와 Splashback 반경은 [08.C절](#08.C) 실험과 함께 확인

#### 던전 첫 버스트와 회복 대기

- 2026-10-05 사용자 보고: 메이지 한 명, Reflect 없음, 몹에게 맞은 뒤 HP 약 100에서 약 10초 안에 사망
- [Lumberjack PvP](../templates/lumberjack-pvp.md#05.E) 05.E절의 피해 범위는 설명 가능한 조건일 뿐. 실제 상대 스킬은 확인되지 않았다
- TK 적용, 포션 부착, Explosion 방출, EB 시전, 각 피해, 회복 시각, 붕대 남은 시간 기록
- 시전 중 포션과 완료한 프리캐스트를 쥔 채 마신 경우를 나누고, 지금의 수동 입력 대기가 회복 요청을 미뤘는지 확인
- 30초와 60초 모형의 낮은 사망 비율로 첫 버스트 생존 여부를 판단하지 않음

#### 만피에서 먼저 붕대 감기

- 서버가 만피 Bandage Self 요청을 받아 실제로 붕대를 감는지. 지금 루프는 피해나 독이 있어야 요청
- 이미 피해가 있으면 자기 MA 없이 시작되는지, 수동 커서, 시전, 진행 중인 붕대가 요청을 막았는지 구분
- 자기 MA 자동 반복으로 마나를 쓰거나 진행 중인 붕대를 재시작하는 정책은 넣지 않음

## <a id="11"></a>11 skinning-enhanced 인게임 확인

`gather/skinning-enhanced` 지금 v11, 본문은 아직 인게임에서 확인되지 않았다.
2026-10-06 `gather/skinning-enhanced.razor` 생성. Two-Handed Axe를 쓰는 Magery 80 덱서용 던전 근접 루프.

- 템플릿: Forensic Evaluation 120, Swordsmanship과 Tactics 100, Magery, Resisting Spells, Parrying, Anatomy, Healing 80, STR 100, DEX 80, INT 45
- bard-mace에서 바드를 빼고, lumberjack-enhanced의 자기 회복 주문, RA, Reflect와 시체 칼질 추가
- 워모드는 사용자가 Tab으로 직접. Z, V를 눌러도 워모드 불변.
  싸우는 동안 워모드를 켜 두므로 회복, 버프, 칼질 모두 워모드를 보지 않음

#### 칼질 규칙

위키 [Forensic Evaluation](https://wiki.uooutlands.com/Forensic_Evaluation) 기준.

> Players can target themselves or nearby ground to activate "Smart Harvest" which carves all grey notoriety corpses "within 2 tiles"

- 회색 시체만: `target self`. 회색과 파란 시체 모두: 시체 serial을 하나씩 직접 지정(`config__skin_unowned`)
- 스크립트는 시체 이름 색을 못 읽음 → 회색 판정은 서버에 맡김

#### 인게임에서 확인한 것

- 사용자 보고: 파란 시체에서 `[ loot, crim ]`이 뜨지만 아이템을 가져가야만 grey. 2칸 거리의 시체는 검색됨.
  ignore한 시체는 clearignore 전까지 findtype에서 빠짐. 인게임 확인됨 2026-10-06
- lasttarget이 바뀌어도 지금 치는 대상은 불변(bard-mace 경험, 함께 보고). 칼질이 문제가 되는 것은 다음 V 한 번
- 2026-10-07 v3 Journal에서 직접 타겟 칼질의 `You carve materials from the corpse.` 확인
- Sanctuary Dungeon의 파란 시체: `Criminal actions are not permitted in the Sanctuary Dungeon.`으로 거절.
  일반 던전에서는 아이템을 가져가야만 grey(사용자 보고). 인게임 확인됨 2026-10-07
- 플레이어 시체는 다름. v6이 파란 플레이어 시체 `the remains of Leap Day William`을 직접 지정 →
  `You have committed a criminal act! (corpse carving onLeap Day William).`로 범죄 판정. 인게임 확인됨 2026-10-07.
  몬스터 시체 이름은 `aged earth corpse`처럼 "…corpse"
- v8은 직접 지정 뒤 응답을 읽음. `That corpse has already been carved.` → 끝난 시체,
  `That is too far away.`와 `You must wait to perform another action.` → 한 번 더 시도할 시체. 인게임 확인됨 2026-10-07
- v3의 `setlasttarget` 복원은 Set Last Target 커서를 띄워 스크립트 정지. 인게임 확인됨 2026-10-07([Razor](../scripting/razor.md#03) 03절)

#### 기록

- **v5**: 복원 삭제, 기억한 적이 없을 때만 칼질. 거절이 보이면 5분 동안 회색 시체만
- **v6**: sword codex 이름에 `sword_` 접두, 칼질 결과와 범죄 행위 거절을 프로필 오버헤드로 이관.
  같은 날 오버헤드 팔레트 채도 하향([Overheads](../scripting/overheads.md#05) 05절)
- **v7**: 직접 지정 전 라벨을 읽어 "corpse"가 있고 "remains"가 없는 시체만. 그래도 범죄 판정이면 그 Play 동안 직접 지정 끔.
  공개 스크립트 [forensics](https://outlands.uorazorscripts.com/skills/forensics/c8e4e8eb-743d-4a7f-9043-4c17d2cabb6a)도 `"the remains"`를 플레이어 시체로 보고 건너뜀
- 2026-10-09 **v9**: 힘 포션과 민첩 포션을 버프 대신 STR과 DEX 값으로 판정([PvP](../game/pvp.md#09.D) 09.D절), 세 스탯 포션을 따로 판정.
  v8은 `elseif` 사슬이라 힘 포션이 떨어지면 민첩과 저항 포션까지 막힘
- 2026-10-10 **v10**: 가벼운 Heal을 붕대 옆에서도 쓸지 `config__use_light_heal`로 결정(기본 0). 붕대를 못 쓸 때 대신 나가는 것은 그대로
- 같은 날 **v11**: 모듈 조립. 회복, 포션, 버프, 시약을 pvp와 같은 core 블록으로. 바뀐 동작은 [Modules](../scripting/modules.md#08) 08절
- Parry Codex: 랭크가 오를 때까지 Bulwark, 근접 밖에서 독, 출혈, 질병이면 Warding
- 스탠스, 피니셔, 어빌리티는 Arms Lore가 없어 무기 특수 확률 기본 10%인 점을 반영해 선택.
  근거는 `fight/sword-codex`, `fight/weapon-ability` 모듈 주석
- `config__sysmsg`: 전투 대상 변화, 칼질 요청과 결과, codex 전환, 회복과 버프 시전, 도끼 장착, 골드와 가죽 정리를 Journal에 기록

#### 반영하는 법

- Scripts 탭에서 Reload all scripts → Play로 먼저 확인. 핫키에 묶었다면 클라이언트 재시작([Workflow](../working/workflow.md#04.A) 04.A절)
- Journal에 `Skinning enhanced v11 loaded`

#### 전투 중 칼질 멈춤

- Z로 몹을 고른 뒤 V를 늦게 눌러도 그 사이 `Carve request` 없음, V가 그 몹을 쳐야 함
- 몹이 죽고 약 1.2초 뒤부터 주변 시체 칼질
- 칼 커서가 떠 있을 때 Z → 커서 취소, 시체는 전투 뒤 다시 요청
- `Target a new 'Last Target'` 커서가 뜨거나 V가 시체나 나를 치면 실패

#### 범죄 행위가 거절되는 지역

- Sanctuary Dungeon에서 파란 시체를 한 번 요청한 뒤 프로필의 `[ crim, blocked ]`와 Journal의 `Carve mode: grey corpses only`, 5분 동안 Smart Harvest만
- 같은 파란 시체를 다시 요청하면 실패. 일반 던전에서는 거절 없이 파란 시체도 칼질

#### 칼질 결과 오버헤드

- 칼질 `[ carve, done ]`, 이미 깎은 시체 `[ corpse, carved ]`, Smart Harvest가 깎을 시체를 못 찾음 `[ corpse, out ]`,
  범죄 판정 `[ crim, on ]`. 모두 프로필에서
- 게임 종료 상태에서 두 프로필에 추가. 스크립트가 같은 문장을 다시 띄우면 실패

#### 칼 커서의 종류와 도착

- 스크립트는 칼을 쓴 뒤 2초 안에 온 중립 커서에만 응답
- 칼 커서가 중립이 아니거나 2초 뒤에 오면 커서가 남아 회복과 칼질 모두 정지 → 실패, 남은 커서는 직접 닫음

#### 시체 직접 타겟(skin_unowned 1)

- 시체마다 `Carve request: corpse=...` 한 줄과 서버 응답 기록
- 회색과 파란 몬스터 시체는 칼질, 플레이어 시체는 `Carve skip: ... label=the remains of ...` 뒤 요청 없이 건너뜀.
  플레이어 시체를 지정하거나 `You have committed a criminal act`가 다시 뜨면 실패
- 인간 NPC 시체와 건너뛴 몬스터 시체의 라벨도 기록. 라벨이 늦게 와 비어 있으면 몬스터 시체도 건너뜀
- 요청마다 `Carve done`, `Carve miss`, `Carve refused`, `Carve no reply` 중 하나가 남아야 함
- 너무 멀거나 바쁜 시체는 한 번 더 요청(`One more try`), 두 번째도 실패면 `Skipped`. 같은 시체 세 번 이상 지정은 실패

#### Smart Harvest(skin_unowned 0)

- 회색 시체 칼질 뒤 `worth carving`이 든 응답이 오면 2칸 안의 시체를 모두 건너뜀. 파란 시체만 있으면 self 한 번 뒤 건너뜀
- 위키는 한 번에 가장 가까운 시체라고도, 2칸 안의 회색 시체 전부라고도 적음. 실제 동작 기록
- 응답 문구가 달라 시체가 있는 동안 2초마다 self가 반복되면 실패

#### Two-Handed Axe 다시 들기

- 왼손이 비면 저장한 도끼를 다시 듦. 저장한 것이 없으면 graphic 5187 검색. 손에 든 도끼는 라벨의 `two-handed axe`로 한 번 저장
- item-list의 5187이 아닌 graphic의 도끼면 백팩 검색 실패 → `config__axe_graphic` 변경
- 시전 중에는 장착 없음. 무장 해제 뒤 장착이 거절되면 2초마다 재시도, 장착 때문에 자기 주문이 끊기면 실패

#### Magery 자기 회복과 버프

- 워모드로 싸우는 중에도 손실 45부터 Greater Heal
- 붕대가 있으면 가벼운 Heal은 안 씀. `config__use_light_heal` 1이면 붕대 옆에서도
- 독이면 Cure 포션 먼저, 포션이 없을 때만 Smart Heal/Cure. 포션과 주문이 같은 독에 함께 나가면 실패
- RA와 Reflect는 상시 유지. 마나가 RA 24, Reflect 34 이상이면 시전. 손실 35 이상이나 독이면 시작하지 않고, 시전 중 그렇게 되면 Interrupt
- 버프 시전 중 근접 타격이 멈추는 시간도 기록. 시약이 없으면 10초(`interval__reagents`) 안에 재확인

#### v11 core 회복(모듈 조립)

- 재시도 타이머 없이도 같은 행동이 패스마다 반복되지 않아야 함
- 순서: 큐어 포션, 힐 포션(35), Greater Heal(45, 그 패스에 포션이 안 나갔을 때), 붕대, Refresh(60 이하)
- 붕대가 우리 시전 중에도 시작되는지, 그때 시전이 안 끊기는지
- 버프는 빠지면 바로 시전, 독이나 손실 35 이상이면 시작하지 않고 끊음
- 힐 포션 쿨 라벨, `[ refresh, out ]`, `[ str, out ]` 경고는 이제 안 뜸. Journal에는 `Agent: …`와 `Buff: …`

#### 스탯 포션

- 기억한 적이 있을 때 STR 120, DEX 100 아래면 힘 포션과 민첩 포션을 5초에 한 번. 저항 버프가 빠지면 저항 포션
- 아군 Bless가 걸려도 마셔야 하고, 힘 포션이 떨어져도 민첩과 저항은 계속

#### 골드 버리기

- 최대 무게 초과 시 한 패스에 2000골드를 발밑에 버리고 `[ gold, dropped ]`. 버리는 사이에도 회복은 계속
- 골드가 없으면 `[ weight, over ]`만. 무게 초과가 아닌데 버리면 실패

#### 가죽 정리

- 칼질로 나온 가죽이 item-list의 `cut up leather` 4225인지. 다른 graphic(hides 등)이면 검색에 추가
- 기억한 적이 없을 때만 2분마다
- 파우치 안의 묶음만 ignore, 목록은 비우지 않음 → 정리 뒤 깎은 시체에 다시 요청하면 실패. 파우치 안 가죽을 다시 옮겨도 실패
- 거절된 이동은 2.5초 예산 안에서 재시도

#### 시체가 Last Target일 때

- 기억한 적이 없을 때 시체를 깎으면 Last Target이 바닥의 시체. 캐시는 `0x40000000 > serial`로 모빌만 `dead`와 `noto`에 전달
- Mobile not found나 Script Error로 멈추면 실패

#### Sword Codex 라벨

- `debug/dump-label`로 sword codex 라벨에 스탠스 이름과 `Execute`, `Bleed Out`이 보이는지
- 피를 60 넘게 잃으면 `[ sword, defensive ]`, 48 아래로 회복하면 `[ sword, warrior ]`
- Bleed Out이 골라져 있으면 `[SwordsFinisher2`로 Execute로 바뀌는지, 피니셔가 꺼져 있으면 명령 없이 `[ execute, off ]`만 뜨는지
- 라벨에 스탠스 이름이 없으면 `[ sword stance, off ]`

#### Parry Codex

- `debug/dump-label`로 shield codex 라벨에 스탠스 이름과 `Last Stand`, `Barrier`가 보이는지
- 기본 Bulwark. Testudo 랭크가 오르면 `config__parry_stance_main`을 `config__parry_stance_testudo`로
- 기억한 적이 2칸 밖이거나 없을 때 독, 출혈, 질병 → `[ parry, warding ]`, 풀리면 `[ parry, bulwark ]`. 2칸 안에서 싸우는 중에는 주 스탠스 유지
- 출혈이나 질병 중 Warding으로 안 바뀌면 `findbuff "Bleed"`와 `"Disease"`의 버프 이름 확인
- 스탠스 이름이 없으면 명령 없이 `[ parry stance, off ]`만, 이번 Play 동안 정지. 같은 스탠스 명령이 3초마다 반복되면 실패

#### Chop 간격

- 기억한 적이 2칸 안이면 `[ chop ]` 뒤 다음 타격에 나가는지. Arms Lore가 없으니 60초 간격이 맞는지도

## <a id="12"></a>12 tamer-mage-enhanced 인게임 확인

`combat/tamer-mage-enhanced` 지금 v6. 2026-10-10 사용자가 지금 안 쓴다고 해서 `script/archive/`로 옮겼다가, 같은 날 레시피 조립과 함께 `script/combat/`으로 복귀.
바뀐 동작은 [Modules](../scripting/modules.md#08.E) 08.E절.

#### 템플릿과 설계

- 2026-10-09 `combat/tamer-mage-enhanced.razor` v1 생성. Animal Lore, Animal Taming, Veterinary 120, Magery와 Tracking 100, Resisting Spells와 Meditation 80 템플릿용
- bard-necro-enhanced의 생존, 전투 대상, 타겟 주문 모양과 lumberjack-enhanced의 Tracking 설정 차용
- 펫 명령과 대상 지정은 수동. 워모드 ON → Flamestrike, Bless, Arch Protection, Create Food 정지
- 설계 근거는 위키. 수의사 키트(Veterinary Supplies)는 붕대처럼 5초 뒤 2칸 안의 내 펫 모두 치료.
  해독과 부활은 50%(펫이 하나면 75%), 쓰면 진행 중인 붕대 취소([Veterinary](https://wiki.uooutlands.com/Veterinary)). 사용자는 힐링 코덱스로 사거리 3을 늘려 5칸으로 사용
- Bless 9마나 2분, Arch Protection 11마나 2분. Arch Protection은 6칸 안 아군 모두의 AR 상승. Flamestrike 40마나([Magery](https://wiki.uooutlands.com/Magery))
- Razor `diffhits`는 내 체력만 읽음 → 펫 체력 기반 자동 GH 없음
- 주문 이름은 클라이언트 `spells.def`의 `Flamestrike`, `Bless`, `Arch Protection`, `Create Food`

#### 사용자가 확인한 것과 그에 따른 변경

- 같은 날 버프 바 확인: Bless는 `Strength`, `Agility`, `Cunning` 세 아이콘, 시스템 메시지는 `Your strength/dexterity/intelligence has changed by 11`.
  Arch Protection은 `Protection`
- `Strength`와 `Agility`는 스탯 포션과 겹침 → v2는 Bless를 `Cunning`으로, Arch Protection을 `Protection`으로 판정, 시전 시각 타이머 삭제
- 힘 포션과 민첩 포션도 버프 이름에 Potion이 없음(사용자 확인) → 버프로는 Bless와 구분 불가. 위키 BuffIcons의 `Strength Potion Usage Cooldown`은 표의 라벨일 뿐
- 그래서 포션은 스탯 값으로 판정. 포션을 마신 값(기본 + 20)을 `config__str_potion`과 `config__dex_potion`에, 그보다 낮으면 마심. Bless만 걸린 상태(기본 + 11)는 그보다 낮음
- 거절된 마시기가 회복 포션과 같은 아이템 큐를 패스마다 차지하지 않도록 5초 재시도 간격
- 수의사 키트가 나와 주변 팔로워를 함께 치료함(사용자 확인). 치료할 대상이 없거나 팔로워가 멀면
  `You or your nearby followers do not require healing.`만 남고 미적용 → v3에서 펫 지정과 거리 확인 삭제, 키트를 셀프 붕대로
- v4: 프로필 오버헤드의 `You begin using veterinary supplies`, `You finish using veterinary supplies`로 키트 진행 구간 파악.
  진행 중에는 재사용 없음(재사용 시 진행 중 치료 취소). 피가 1이라도 빠지면 바로, 풀피면 끝난 직후와 거절 2초 뒤에 펫용으로
- v5: 가벼운 Heal 에이전트를 `config__use_light_heal`로 켜고 끔, 기본 끔. 너무 잦다는 사용자 의견 → 회복은 키트, 힐 포션, GH만.
  독일 때 큐어 포션이 없으면 쓰는 Smart Heal/Cure는 그대로
- 나머지 본문은 아직 인게임에서 확인되지 않았다

#### 반영하는 법

- 새 파일이므로 Scripts 탭에서 Reload all scripts → Play로 먼저 확인. 핫키에 묶었다면 클라이언트 재시작([Workflow](../working/workflow.md#04.A) 04.A절)
- Journal에 `Tamer mage enhanced v6 loaded`. 핫키는 `Play Script: combat\tamer-mage-enhanced`

#### 수의사 키트

- 내 피가 1이라도 빠지면, 키트 진행 중이 아닌 한 바로 `[ vet, on ]`
- `[ vet, on ]`부터 `[ vet, done ]`까지 재사용 없음, 끝나면 바로 다음 시도
- 아무도 안 다쳤으면 `You or your nearby followers do not require healing.`이 약 2초마다 한 번. 더 잦거나 뜸하면 기록
- 치료 중 키트가 끊기면 실패. 거절 시 키트 소모 여부, 키트 시간이 실제 5초인지, 죽은 펫 부활 시도도 기록
- 키트가 없으면 `[ vet kit, out ]`

#### Bless와 Arch Protection

- 교전 중이 아니고(전투 대상이 10칸 밖이거나 없음) 워모드가 꺼져 있을 때 `Cunning`과 `Protection` 아이콘이 없으면, 커서에 자기 자신을 지정하고 `Buff: Bless`와 `Buff: Arch Protection` 기록.
  커서는 Bless가 beneficial, Arch Protection이 neutral
- 아이콘이 뜬 다음 패스에 같은 주문 재시전 없음. 2분 뒤 아이콘이 사라지면 재시전하는지, 펫도 Arch Protection을 받는지 펫 상태에서 확인

#### Bless와 스탯 포션

- `config__str_potion`과 `config__dex_potion`은 내 기본 힘과 민첩 + 20. 이 루프의 120과 45는 이 템플릿의 STR 100, DEX 25, INT 100 기준
- Bless가 걸린 채 전투에 들어가도 힘 포션과 민첩 포션이 한 번씩 나가고, 마신 뒤 5초마다 다시 눌리지 않아야 함. 다시 눌리면 값이 높거나 포션이 +20이 아님
- 포션(+20)이 Bless(+11)를 덮어쓰는지(120) 쌓이는지(131), 포션이 끝난 뒤 `Cunning`이 남은 동안 Bless의 힘과 민첩이 살아 있는지도 확인.
  사라진다면 그동안은 Bless 재시전 없음
- 저항 포션은 아직 `findbuff "Magic Resist Potion"`으로 판정 → 버프 바에 그 이름이 뜨는지 확인

#### Flamestrike

- 전투 대상이 10칸 안, 마나 51 이상, 워모드 꺼짐일 때만 시전
- 시전 중 다른 몹을 V로 고르면 커서 취소, 다음 패스에 새 대상으로. 대상이 죽으면 취소
- 손실 35 이상이면 시작하지 않고, 시전 중이면 끊음. aspect 발동 여부도 기록

#### 버섯

- 마나 55 이하이고 쿨다운이 끝났으면 먹음
- 교전 중이 아니고 마나 70 이상, 버섯 2개 미만이면 Create Food 시전. Create Food가 실제로 버섯을 만드는지(Grimoire 단계) 확인

#### Tracking

- 설정한 색 필터로 Hunting 켬, 감지는 프로필의 `[ track, … ]` 오버헤드로만 알림
- Hunting이 꺼지면 5초마다 `[ track, check ]`. 귀환 없음

#### 이동 가드

- bard-necro-enhanced처럼 시전 블록은 `walk` 바가 도는 동안 대기. 걷는 동안 회복 에이전트가 늦으면 기록. 포션은 걷는 중에도 나감

## <a id="13"></a>13 recycle 복귀 인게임 확인

2026-10-10부터 `loot/recycle`이 끝나면 마지막으로 Play한 사냥이나 채집 루프를 다시 켬. 전에는 루프를 바꿀 때마다 마지막 줄의 `script "…"`를 수동 수정.

- recycle에 원작자의 같은 장치가 있었음. 아이템 ID를 못 해 일찍 끝날 때 이전 스크립트 리스트의 항목을 `hotkey`로 실행.
  원작자 저장소에는 이 리스트를 읽는 스크립트만 있고 채우는 스크립트는 없음 → 사용자가 채움
- 그 리스트 이름을 저장소 규칙대로 `list__resume_script`로, recycle 마지막 줄도 같은 모양으로 변경
- bard-necro-enhanced, skinning-enhanced, lumberjack-enhanced, tamer-mage-enhanced, dexxer-basic이 Play할 때 자기 핫키 이름을 이 리스트에 추가.
  archive로 옮긴 bard-mace와 bard-throwing은 `Play Script: archive\…` 이름으로 추가. pvp는 싸울 때만 켜므로 제외
- 핫키 이름은 프로필 xml이 F1을 저장한 모양 `Play Script: gather\skinning-enhanced`를 따름.
  `hotkey`가 이 이름으로 스크립트를 켜는지, 따옴표 안의 `\`가 그대로 넘어가는지는 아직 확인되지 않았다
- 변수는 단어를 `4294967295`로 읽음([Razor](../scripting/razor.md#03) 03절) → 리스트 사용

#### 복귀

- skinning-enhanced를 Play한 뒤 F3 recycle → 끝나고 `Skinning enhanced v11 loaded`가 다시 떠야 함. lumberjack-enhanced를 Play한 뒤에는 그쪽으로 복귀
- 아무것도 안 돌면 핫키 이름의 모양이 다름. Razor Hotkeys 탭의 스크립트 이름 기록

#### ID를 못 해서 일찍 끝날 때

- ID 스킬이나 완드가 없어 `Jase says: Not able to ID items..`가 뜰 때도 같은 루프로 복귀

#### 등록 전

- 클라이언트를 켠 뒤 루프를 한 번도 Play하지 않고 recycle을 돌리면 아무 스크립트도 안 돌아야 함

#### pvp 중

- pvp 중 recycle → 마지막 사냥이나 채집 루프로 복귀. pvp 복귀를 원하면 기록

#### 다시 쓴 recycle

- 2026-10-10 저장소 규칙으로 재작성. 변수 이름, 오버헤드, 대기 값, 시작 4줄 변경, 분류는 그대로여야 함
- Journal에 아이템마다 `Recycle check: …`. 저장 시 `[ item, saving ]`과 `Recycle save: …`, 나머지는 분해
- 링메일의 fortification, hardening, guarding, defense 스위치가 이제 동작, studded 방어구는 studded 보관함으로(지금은 둘 다 루트 파우치)
- 재질을 못 읽은 방어구는 루트 파우치로. 재활용 도구가 없을 때도 루프로 복귀

## <a id="14"></a>14 bard-necro-enhanced 인게임 확인

2026-10-10 `combat/bard-necro-enhanced`를 레시피 조립으로 전환. 바드, 네크로, 공격 주문 블록의 코드는 그대로.
생존, 포션, 버프, 골드는 공용 모듈로, 하우스키핑과 교전 및 이동 분기는 레시피 그룹이 생성. 바뀐 동작은 [Modules](../scripting/modules.md#08.D) 08.D절.

#### 시작

- Play → 악기 검색(없으면 `[ inst, pick ]`), `[ bard necro, on ]`

#### 소환수 이름

- 소환 뒤 5초 안에 `[ name, leech ]`처럼 이름이 뜨고 네임태그가 바뀌어야 함. 안 바뀌면 Journal 확인
- `Summon name: no known kind in its label: …`이 뜨면 그 라벨 기록. 아무것도 안 뜨는데 오버헤드만 뜨면 `rename` 거부
- 기록(2026-10-10): 종류를 읽은 판(`[ name, mummy ]`)은 서버가 `That name is unacceptable.`로 거절.
  종류 단어를 피한 철자로 바꾸자 `mumi`는 수락, `wytch`는 거절. 한 글자 차이도 막는 것으로 보고 모든 이름을 두 글자 이상 떨어뜨림(`leech`, `vampa`, `wicca` 등).
  새 이름의 수락 여부 확인

#### Rag Witch 바디

- `mumi`는 바뀌었지만 rag witch는 안 바뀜(2026-10-10). 바디 번호 740이 틀린 것으로 보고 기본 이름 `a rag witch`로도 검색.
  다음 판은 rag witch를 찾아 이름을 붙이려 함(`wytch`는 거절)
- Journal에 `a rag witch found by its name, not its body`가 뜨면 그 rag witch에 `>info`로 Body 번호 확인 후 전달. 그 번호를 바디 목록에 넣고 이름 검색 삭제
- Vampire Thrall 722도 같은 출처라 확인되지 않았다

#### 교전과 이동

- 적을 찍으면 10칸 안에서 Disco, Peace, 네크로 버스트, 오프너, 프록이 예전 순서로
- 적이 없으면 버섯, RA, Reflect, Spell Siphon, 노래, Vampiric Embrace

#### Spell Siphon 순서

- RA와 Reflect가 빠진 채 이동하면 RA, Reflect 먼저, Siphon Magic Arrow는 그다음 패스

#### 독과 힐

- 독에 걸린 채 다치면 큐어 먼저, 힐 포션과 Greater Heal은 독이 풀린 뒤. 예전보다 위험하게 느껴지면 기록

#### 셀프 버프 끊기

- 잃은 HP 35 이상에서 RA와 Reflect 시전이 끊기는 것이 거슬리면 레시피의 `buff_max_loss` 상향

#### Journal

- `config__sysmsg` 1이면 에이전트, 버프, 골드, 전투 대상 줄 기록. 너무 많으면 레시피에서 0

#### 패스 속도

- 패스 끝 0.1초 대기, 10초마다 시약 읽기 추가. 교전 반응이 눈에 띄게 늦으면 기록

#### 버섯

- 교전 중에도 마나 55 이하이고 쿨다운이 끝났으면 먹음. Create Food는 이동 중에만
