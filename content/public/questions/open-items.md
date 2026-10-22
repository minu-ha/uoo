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
| [13](#13) | recycle의 속도, 감정 실패, 루프 복귀 확인 |
| [14](#14) | bard-necro-enhanced 인게임 확인 |
| [15](#15) | loadout, regear, aspect 인게임 확인 |
| [16](#16) | bard-archer-enhanced 인게임 확인 |
| [17](#17) | 프로보 후보 입력과 인게임 확인 |
| [18](#18) | tamer-archer-enhanced 인게임 확인 |

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
| 대상 위 줄은 1288([Overheads](../scripting/overheads.md#01.C) 01.C절) | moongate의 `[ moongate, set ]`은 290으로 게이트 위, archive/backstab-mugging의 `[ range, out ]`은 254로 lasttarget 위 | 1288로 바꿀까, 예외로 적을까 |
| 한 대상에 한 낱말([Overheads](../scripting/overheads.md#04) 04절) | 프로필 `[ omen, target ]`과 스크립트 `[ evil omen ]`, train/herding의 `[ herding, done ]`과 글로서리 `herd`, 바 `cannons`와 `[ cannon, out ]`도 불일치 | 어느 쪽으로 맞출까 |
| 대상만 쓰는 줄 = 시전 알림([Overheads](../scripting/overheads.md#05) 05절) | 프로필의 `[ swing ]`(290)은 대상만인데 시전 알림 아님 | `[ swing, on ]`처럼 상태를 붙일까 |
| 글로서리 낱말 | `gheal` `invis` `tp`를 쓰는 줄 없음 | 예약어로 둘까, 지울까 |

## <a id="03"></a>03 캐릭터와 핫키

| 무엇 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot | 키 배치 밖. 이동은 화살표 키, 매크로는 ClassicUO 기본 세트(F1 Guards, F2 bank, 4 all stay, 6 Circle Trans). `chars.lst`에도 없음 | 예외 캐릭터인가 |
| `Shift`+휠 | 아군 순환이 Shift 층 정의("밖으로 던지는 것")와 어긋남([Hotkeys](../game/hotkeys.md#02.A) 02.A절) | 의도한 예외인가 |
| 가장 가까운 플레이어 타겟 | "서버가 막아 놨다"([Hotkeys](../game/hotkeys.md#04) 04절)에 출처 없음 | 맞다면 PvP 제약 → [Razor](../scripting/razor.md#07) 07절로 옮길까 |
| "C and a click" | 지금은 없는 bard-necro-pvp 주석의 말. 어느 바인딩과도 불일치(summoner의 `C`는 All Guard Me) → "Q or Shift+X/C"로 수정함 | 원래 뜻이 있었나 |
| 저장소 밖 파일 | Wine `user.reg` 키 이름(01절), Clumsy subcode 62(05절) 미대조. L 이름은 2026-10-21 설치된 `Razor_lang.enu`와 대조 완료([Hotkeys](../game/hotkeys.md#05) 05절) | 나머지도 게임이 깔린 기계에서 대조 가능한가 |

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
| 헤더는 설명 한 줄과 `Needs:`([Conventions](../scripting/conventions.md#02.C) 02.C절) | archive의 bard-throwing, bard-mace: 배너 뒤 "Naming convention" 블록. bard-necro-enhanced: 배너 없이 설명 한 줄, 설계 문서 안내, Needs, 긴 메모 | 긴 루프의 헤더 모양 |
| `cooldown` 명령은 기존 파일이 그 스타일일 때만([Conventions](../scripting/conventions.md#04) 04절) | archive의 bard-throwing이 `cooldown "ability"`로 게이트 | 규칙이 낡았나, 바 표시를 위한 의도인가 |
| 같은 성격 3개 이상이면 폴더([Conventions](../scripting/conventions.md#01.C) 01.C절) | `gather/` 2개, `restock/` 1개 | 규칙 수정, 또는 폴더 병합 |
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

- 근거: 공식 계산값과 실제 정수 처리의 구분 필요
- 확인할 것: Magery 80에서 Bless만 쓰고 STR, DEX, INT, 최댓값, 현재 마나 기록.
  Bless 비용 9, 공식값 +8.8의 정수 처리, 스크롤로 꺼내는 데 필요한 실제 마나 50 조건을 구분
- 기록: Magery 100의 Bless는 2026-10-09 `changed by 11`로 +11 확인(12절)
- 기록: 포션과 Bless는 안 겹침. 포션이 걸린 동안 Bless의 STR, DEX는 더해지지 않음. 2026-10-21 사용자 확인, [PvP](../game/pvp.md#09.D) 09.D절

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

- 왼손이 비면 들고 있던 도끼를 다시 듦. 아무것도 기억 못 하면 graphic 5187 검색. 손에 든 것은 라벨 없이 serial로 한 번 기억(`fight/rearm`, 2026-10-21 `fight/axe`에서 이름 변경. 오른손도 같은 규칙)
- item-list의 5187이 아닌 graphic의 도끼면 백팩 검색 실패 → `config__rearm_graphic` 변경
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
- `defensive_enter_diff` 초과면 `[ sword, defensive ]`, `defensive_leave_diff` 미만이면 `[ sword, warrior ]`
- 기본값은 [sword-codex 모듈](https://github.com/minu-ha/uoo/blob/master/module/fight/sword-codex.razor). 경계값과 두 선 사이에서는 기존 상태 유지
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
- 포션(+20)과 Bless(+11)는 안 쌓임(120). 2026-10-21 사용자 확인. 포션이 끝난 뒤 `Cunning`이 남은 동안 Bless의 힘과 민첩이 살아 있는지 확인.
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
- 2026-10-20 걷는 중 Greater Heal이 안 나감 → 긴급선 Greater Heal만 가드 없음. 달리며 피가 빠질 때 나가는지, 걸음에 끊기면 다음 패스에 다시 나가는지

## <a id="13"></a>13 recycle 인게임 확인

`loot/recycle`: 루팅 백의 장비만 단일 ID wand로 감정. 저품질은 분해, 보관품은 보급 파우치로 이동.
2026-10-21 검색 범위 축소, 보관 위치 통합, 고정 대기 제거. 처리 실패도 공통 정리 뒤 루프 복귀.
새 경로의 인게임 동작은 확인되지 않았다.

#### 컨테이너

- 검색: `global__my_loot_bag`. 보관: `global__my_supply_pouch`. 둘 다 백팩 안에 있어야 함
- 저장된 역할을 찾지 못하면 백팩의 bag `3702`, hue 0 pouch `3705`가 각각 정확히 하나일 때만 임시 사용. global 값은 덮어쓰지 않음
- 루팅 백 누락이나 중복은 `[ loot bag, out ]`, 보급 파우치 누락이나 중복은 `[ supplies, out ]`. 장비 처리와 자원 드롭 없이 루프로 복귀
- 두 역할이 같거나 서로 안에 들어 있으면 `[ loot bag, wrong ]`, 처리 없이 복귀
- 시작에 두 컨테이너를 한 번씩 열고 행동 큐가 비워질 때까지 대기. 기한 초과는 `[ loot bag, blocked ]`, 처리 없이 루프로 복귀
- 다른 가방, 백팩에 따로 둔 장비, 보급 파우치의 보관품은 검사 대상 아님
- 루팅 백의 미감정 일반품, 미감정 보관품, 이미 감정한 품목을 섞어 확인. 저장품은 보급 파우치의 오른쪽 아래 `130 200`으로
- `ignore`는 이번 실행의 재선택 방지용. 시작과 끝에 초기화. 보관품은 루팅 백 밖으로 옮기므로 다음 실행에서도 조회 생략

#### 도구와 분해 모드

- 단일 ID wand `20496`만 사용. Item Identification 스킬 경로와 `config__min_item_id_skill`, `wait__item_id` 제거
- 재활용 도구: tinker tool, sewing kit 또는 saw. 완드와 도구는 백팩에서 검색. 시작에 없으면 경고 뒤 루프로 복귀
- 분해 검프의 `Recycle Single Item` 문구를 확인한 뒤 개별 아이템만 타깃. 다른 모드는 `[ recycle, wrong ]`, 후속 아이템 처리 중단

> "Recycle single item" is the recommended option, as it is limited to recycling individual items.

출처: [공식 Recycling](https://wiki.uooutlands.com/Recycling), 2026-10-21 확인.
다른 분해 모드는 백팩의 유용한 장비까지 대상이 될 수 있음.
검프의 대소문자 `Recycle Single Item` 선례는 [Bapeths Slower Item Recycler](https://outlands.uorazorscripts.com/script/752d1745-90d4-4078-a8cb-8ce2cccef3e0).
현재 클라이언트 문구는 인게임 미확인. 단일 모드인데 `[ recycle, wrong ]`이면 검프 원문 기록.

#### 속도와 설정

| 항목 | 현재 동작 |
| --- | --- |
| 감정 직후 | 감정된 라벨을 받으면 같은 아이템 처리에서 바로 분류. 고정 대기 없음 |
| 아이템 라벨 조회 | 첫 조회로 감정 필요 여부 확인. 완드 사용 후 품질을 다시 조회. 조회 횟수와 완드 사용 횟수는 별개 |
| 보관 이동 | 파우치 소속을 `find`로 확인하면 즉시 다음 아이템. 고정 대기 없음 |
| 품목별 storage | 17개 제거. 보급 파우치 한 곳으로 통합 |
| 아이템별 Journal | `config__sysmsg 0` 기본값. `1`이면 검사와 저장 로그 |
| 완드와 분해 도구 | 선택한 serial 재사용, 완드 커서 실패나 분해 도구 유실 시 다시 검색 |

- 완드 감정은 성공 전제. 사용자 확인 2026-10-21. 이후 재조회는 갱신된 품질 라벨 수신용, 스킬 성공 여부 판정 아님
- `pushlist` 한 줄은 품목군 하나. 스태프, 쌍수, 투척, 검술, 메이싱, 펜싱, 활, 방패, 마법 장비, 레슬링, 악기, 방어구의 12종
- 숫자는 개별 물건의 serial이 아닌 graphic ID. 쌍수와 투척은 기존 이름 검색어와 ID를 함께 유지
  이름과 ID의 대응은 [Item list](../game/item-list.md#29) 29절, 방어구는 같은 문서 [02절](../game/item-list.md#02)
- 품질 판정은 무기, 메이싱, 악기, 방패, 방어구의 5종. 검색 대상 220개, 보관 설정 49개의 기본값과 재질 판정 유지
- 모든 그룹이 감정, 이동, 분해 코드를 공유. `config__skip_supply_pouch`와 품목별 storage, 백팩 보관 대체 경로 제거
- 컨테이너: `var__loot_bag`, `var__supply_pouch`. 도구: `var__id_wand`, `var__id_wand_out`, `var__tool`
- 처리 상태: `var__running`, `var__item_pending`, `var__id_sent`, `var__keep`, `var__kind`, `var__slayer`, `var__armor_type`
- `timer__recycle` 하나를 단계마다 초기화. 이전 `timer__recycle_identify` 제거

| 설정 | 값 | 용도 |
| --- | --- | --- |
| `wait__label` | 650ms | 완드 사용 후 갱신된 품질 라벨의 추가 조회 기한. 받으면 즉시 진행 |
| `wait__poll` | 50ms | 품질 라벨, 행동 큐, 보관 이동, 분해 결과의 재확인 간격 |
| `wait__target` | 500ms | 도구 커서 대기 상한 |
| `wait__timeout` | 5000ms | 행동 큐, 검프, 보관 이동, 분해 결과의 대기 상한 |
| `wait__drop` | 650ms | 자원 드롭 뒤 거절 문장을 읽기 전 대기 |

서버 쿨다운이나 실측 속도가 아닌 스크립트 설정. `getlabel` 자체 대기 시간은 별도([Razor](../scripting/razor.md#06) 06절).
정적 동일성 검사와 모의 실행은 통과. 실제 단축 시간, Outlands의 라벨 응답 시간과 행동 큐는 인게임 확인 필요.

#### 분류와 반복 실행

- 방어구는 graphic이 아닌 라벨의 재질로 판정. 돌려 놓은 체인 장갑은 링메일이 아닌 체인 설정으로 보관
- exceptional은 `config__save_exceptional 1`이면 보관, aspect는 항상 보관. 둘 다 파우치로 이동
- hue 0 주문서와 단검은 루팅 백에 유지, 감정과 분해 생략
- 같은 종류가 여러 개여도 개별 serial만 ignore. 같은 graphic ID의 남은 물건은 계속 검색, 각각 보관 또는 분해
- F3 재실행 시 저장품을 다시 조회하거나 옮기면 실패. 보관 설정을 바꿔 재분류할 때는 해당 장비를 루팅 백으로 옮겨 실행
- 품질 설정에 걸려 보관한 물건이 같은 처리에서 다시 분해되면 실패

#### 실패와 자원 정리

- `stop` 없음. 아래 실패는 `var__running 0`으로 이번 정리만 끝내고 공통 복귀 경로 실행
- 실패 뒤 남은 장비 처리와 자원 드롭 생략. 같은 실행에서 아이템마다 같은 타임아웃을 반복하지 않음
- 루팅 백에 남은 아이템은 다음 recycle 실행에서 재검사. 미확인 품목을 저품질로 간주하거나 분해하지 않음

| 실패 지점 | 경고 | 확인 방법 |
| --- | --- | --- |
| 컨테이너 열기 행동 큐 기한 초과 | `[ loot bag, blocked ]` | 장비와 자원은 건드리지 않고 루프 복귀 |
| 감정 전 행동 큐 기한 초과 | `[ recycle, blocked ]` | 완드 사용과 후속 아이템 처리 없이 루프 복귀 |
| 보관 이동 미확인 | `[ supplies, blocked ]` | 가득 찬 파우치로 시험. 보관품을 분해하지 않고 루프 복귀 |
| 분해 결과 미확인 | `[ recycle, blocked ]` | 타깃한 serial이 루팅 백에 남으면 후속 아이템 처리 없이 루프 복귀 |
| 분해 검프나 커서 누락 | `[ recycle, blocked ]` | 검프나 커서를 기다리는 횟수는 한 번, 자원 드롭 없이 루프 복귀 |
| 분해 모드 불일치 | `[ recycle, wrong ]` | `Recycle Single Item` 외 모드에서는 아이템을 찍지 않고 루프 복귀 |
| 자원 드롭 행동 큐 기한 초과 | `[ recycle, blocked ]` | 추가 대기 반복 없이 루프 복귀 |

- 첫 완드를 소진, 예비 완드는 유지. 커서를 못 연 완드는 그 실행에서 제외, 같은 아이템에 예비 완드 사용
- 모든 완드가 커서를 못 열면 `[ id wand, out ]` 한 번. 미감정품은 남기고 이미 감정된 품목은 계속 처리
- 품질 라벨을 못 받거나 갱신되지 않은 라벨만 받으면 `[ item, skip ]`. 그 물건만 건너뛰고 다음 아이템 처리
- 자원 드롭은 장비 처리를 마친 경우에만 기존대로 백팩 전체 검색. `config__drop_*`와 arcane essence 사용 설정 유지
- 자원 드롭의 거절 문장을 받으면 백팩 복구 요청. 거절 지역에서 실제 반환 확인 필요
- 백팩 `getlabel`을 대기용으로 사용하지 않음. 기준은 [Razor](../scripting/razor.md#06) 06절

#### 복귀 전 정리

- 정상 완료와 처리 실패 모두 `clearall`, 분해 검프 닫기, `clearignore` 뒤 복귀
- `clearall`: 현재 타깃과 타깃 큐 취소, 드래그 큐 정리, 들고 있는 아이템의 백팩 반환 요청
  근거: [CE clearall](https://www.razorce.com/guide/commands/#clearall),
  [CE ClearAll 구현](https://github.com/markdwags/Razor/blob/master/Razor/Scripts/Commands.cs),
  [CE DropCurrent 구현](https://github.com/markdwags/Razor/blob/master/Razor/Core/ActionQueue.cs). 2026-10-21 확인
- 이 명령을 모든 행동 큐나 서버에 이미 보낸 요청의 취소로 간주하지 않음. 정리 뒤 `queued`가 남아도 복귀 핫키 실행
- 백팩으로 반환된 보관품을 재분류할 때는 루팅 백에 다시 넣고 실행
- 모의 실행은 실패 분기의 복귀 경로 확인용. 실제 아이템 반환과 Outlands 클라이언트 큐 초기화는 인게임 확인 필요

#### 루프 복귀

- `list__resume_script`의 각 항목을 `hotkey`로 실행. 정상 완료, 컨테이너 선택 실패, 도구 부족, 위 처리 실패 모두 같은 경로
- bard-necro-enhanced, bard-archer-enhanced, tamer-mage-enhanced, dexxer-basic, skinning-enhanced, lumberjack-enhanced가 Play할 때 자기 핫키 이름 등록
  archive의 bard-mace와 bard-throwing은 archive 이름 등록. pvp는 등록하지 않음
- `hotkey 'Play Script: gather\skinning-enhanced'`의 실행과 복귀는 인게임 확인됨 2026-10-19
- skinning-enhanced를 Play한 뒤 F3 → 끝나고 그 루프의 loaded 문구. lumberjack이나 bard-archer를 Play한 뒤에는 그쪽으로 복귀
- 클라이언트를 켠 뒤 루프를 한 번도 Play하지 않았으면 recycle만 종료. pvp 중에는 마지막 사냥이나 채집 루프로 복귀
- 이름의 저장 형식은 [script/README.md](https://github.com/minu-ha/uoo/blob/master/script/README.md#returning-to-the-loop), 반영은 [Workflow](../working/workflow.md#04.A) 04.A절

## <a id="14"></a>14 bard-necro-enhanced 인게임 확인

2026-10-10 `combat/bard-necro-enhanced`를 레시피 조립으로 전환. 바드, 네크로, 공격 주문 블록의 코드는 그대로.
생존, 포션, 버프, 골드는 공용 모듈로, 하우스키핑과 교전 및 이동 분기는 레시피 그룹이 생성. 바뀐 동작은 [Modules](../scripting/modules.md#08.D) 08.D절.

#### 시작

- Play → 악기 검색(없으면 `[ inst, pick ]`), `[ bard necro, on ]`

#### 악기 복구

아처와 네크로 공통. 2026-10-21 추가, 인게임 동작은 확인되지 않았다.

- warmode를 켠 뒤 사용 중인 악기를 백팩 밖으로 이동, 예비 악기는 백팩에 유지. 다음 악기 점검에서 `[ inst, set ]`, warmode를 끄면 바딩 재개
- 예비 악기도 없으면 `[ inst, out ]`, 회복 블록은 계속. 악기를 다시 넣으면 스크립트 재시작 없이 다음 예비 검색에서 복구
- 타깃 커서나 시전이 있는 동안 예비 선택 대기. 커서와 시전이 끝나면 선택 재개

#### 소환수 이름

- 소환 뒤 5초 안에 `[ name, leech ]`처럼 이름이 뜨고 네임태그가 바뀌어야 함. 안 바뀌면 Journal 확인
- `Summon name: no known kind in its label: …`이 뜨면 그 라벨 기록. 아무것도 안 뜨는데 오버헤드만 뜨면 `rename` 거부
- 기록(2026-10-10): 종류를 읽은 판(`[ name, mummy ]`)은 서버가 `That name is unacceptable.`로 거절.
  종류 단어를 피한 철자로 바꾸자 `mumi`는 수락, `wytch`는 거절. 한 글자 차이도 막는 것으로 보고 모든 이름을 두 글자 이상 떨어뜨림(`leech`, `vampa`, `wicca` 등).
  새 이름의 수락 여부 확인
- 기록(2026-10-13): `wicca`도 거절 → `wichy`로 교체. `wichy`와 나머지 이름의 수락 여부 확인

#### 소환수 바디

- Rag Witch 740은 인게임 확인됨 2026-10-18. 기본 이름 `a rag witch` 재검색 삭제 → 새 rag witch가 5초 안에 `wichy`가 되는지 확인
- Vampire Thrall 722는 구식 캐시가 출처라 확인되지 않았다. 뽑으면 `>info`

#### 재소환과 교체

설계와 실패 증상은 [Bard Necro](../templates/bard-necro.md#04.I) 04.I절. 2026-10-18 추가.

- 소환수 하나를 손으로 release → 서 있으면 `[ vengeful spirit ]`, Water Elemental 주문어, 5초 안에 `[ name, wichy ]`
- `mumi`만 release → Earth Elemental이 나와야 함. Water Elemental이 나오면 바디 740 검색 실패
- 둘 다 없음 → VS 한 번에 Rag Witch, Mummy 순서
- 교전 중 소환수가 죽음 → 그 자리에서 VS와 소환. VS와 첫 시전이 한 패스에 붙어 나감. 소환 중 긴급 HP면 `[ summon, cut ]`과 힐
- 교체 시계가 넘었어도 소환수가 10\~18칸의 몹과 싸우는 동안은 안 놓음
- 워모드, 걷는 중에는 아무것도 안 나감
- 레시피에서 잠시 `summon_refresh`를 60000으로 → 이동 중 1분 뒤 `wichy release`, 다시 소환. 확인 뒤 600000으로
- Bloodmoss를 빼 둠 → VS 심볼을 쓰지 않음
- 손으로 Alt+1 → 루프는 그 버프가 꺼질 때까지 소환하지 않음
- 교전 중 마나 20\~64에서 소환수가 죽음 → 심볼 6까지 Blood Oath 등 정지 → `[ wither ]`, `[ vengeful spirit ]`, 소환이 한 패스에. Journal `Summon: cast kind 2, wither state 2.`
- 둘 다 죽고 마나가 낮음 → 첫째는 바로, 둘째는 약 30초 뒤 다음 Wither. 그동안 Blood Oath는 은행이 찰 때만
- 루프는 Wither와 VS를 0.4초 간격으로 누름. 둘 다 들어가는지. 손으로 확인한 것은 Wither → VS 순서뿐
- `[ wither, miss ]`가 30초마다 반복되면 Razor 핫키 이름 `Wither` 확인
- Razor의 `mana` 값에 Wither 마나가 들어가는지. 들어가면 로테이션이 공격 주문을 헛시전할 수 있음
- 소환 중 긴급 끊기 → 힐 → 재시도에서, 힐이 Wither 마나를 먹어 재시도가 실패하는지. 실패하면 마나 부족 문장도 기록
- 맨 엘리멘탈이 한 번이라도 나오면 기록. 시작 마감 23초가 길다는 뜻

#### 교전과 이동

- 적을 찍으면 10칸 안에서 Disco, Peace, 네크로 버스트, 오프너, 프록이 예전 순서로
- 적이 없으면 버섯, RA, Reflect, Spell Siphon, 노래, Vampiric Embrace

#### 노래(2026-10-20)

- Shadowspire Cathedral과 집에서도 노래가 들어가는지(`You are now under the effect of a Song`). 노래는 다시 백팩
- 노래가 막히거나 실패해도 곡을 건너뛰지 않고, `use another skill`이 매 바퀴 반복되지 않는지

#### 프로보와 마지막 대상(2026-10-21)

- 후보 입력, 짝 선택, 실제 라타의 한계와 확인 절차는 [17절](#17)

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

## <a id="15"></a>15 loadout, regear, aspect 인게임 확인

2026-10-19 추가. 같은 날 loadout과 regear(옛 dress)를 모듈과 일회성 레시피로 옮김([Modules](../scripting/modules.md#03.A) 03.A절).
옛 `hotkey/aspect`는 지움. 두 루틴 안의 `gear/aspect` 블록이 대신함.
regear는 먼저 힐(`recovery/heal-first`), 옷(`gear/dress`, `gear/cosmetic`), 정리(`pack/pouches`, `pack/sorting`), aspect(`gear/aspect`) 순서.
loadout과 regear는 같은 `gear/aspect` 블록을 씀. 동작 설명은 각 모듈 머리 주석.

- aspect 근거: [Aspect Mastery](https://wiki.uooutlands.com/Aspect_Mastery): 켤 때마다 Arcane Essence 5, 죽으면 장비의 aspect가 풀림
- 같은 날 `gear/aspect`를 `[aspect` gump의 Activate 버튼으로 바꿈. 기억 없이 매번 누름. 버튼 번호와 이유는 `module/gear/aspect.razor` 머리 주석

#### 새 스크립트

- Razor를 다시 켠 뒤 Scripts 탭에 `hotkey\regear`가 보여야 함. Alt+0이 regear로 바뀜(summoner, default 프로필)
- loadout이 Play 때 `[ script, blocked ]`는 구조적 PvP에서만. 시작 4줄(clearall 등)은 전과 같음
- loadout에서 귀환 스크롤이 떨어져도 aspect까지 돌아야 함. 전에는 `stop`으로 끝남
- `config__use_runebook_refill` 0이면 스크롤 상자를 묻지 않음
- 귀환 직후 loadout에서도 룬북 리필이 돌아야 함. 상자를 연 뒤 스크롤이 보일 때까지 최대 2초 기다림. 전에는 0.2초 만에 `[ recall scroll, out ]`이 뜰 수 있었음
- 가구와 보급 상자를 연 뒤 0.6초(`wait__long`) 기다림. 금고, 저장소, 수리대, 선반, 리사이클러를 다시 묻지 않아야 함. 다시 물으면 이 대기를 늘림

#### 다시 켜기

- 죽고 시체를 먹은 뒤 regear → 옷을 다 입고 정리한 뒤 `[aspect` gump가 열리고, 방어구와 손 순서로 Activate가 두 번씩 눌린 뒤 닫힘 → Journal에 `... aspect activated.` 둘, Essence 10 감소
- 방어구 몇 조각만 벗었다 낀 채 돌리면 모든 조각이 다시 켜지는지
- gump가 안 열렸으면 `[ aspect, miss ]`, Journal에 `Aspect: the [aspect gump did not open.`
- gump가 Show Only Unlocked 목록으로 열려도 버튼 102로 줄 화면에 돌아가 눌러야 함. 참고 스크립트의 처리, 이 저장소에서는 미확인

#### 먼저 힐

- 다친 채 regear → 붕대, 힐 포션, Greater Heal을 각자 쓸 수 있을 때마다 겹쳐 써서 HP 가득(`heal_first_until` 0)까지
- Magery가 없거나 마나가 모자라면 붕대와 포션만. 포션이 쿨다운 중이면 기다림
- 쓸 것이 하나도 없으면 바로 옷 입기로. 20초(`wait__heal_first`) 안에 못 채워도 옷 입기로, 감던 붕대는 계속
- 시약이 없으면 Greater Heal은 한 번만 시도. 끝나고 남은 Greater Heal 커서는 취소

#### 정리

- regear 뒤 백팩 아래쪽에 새첼, 보급 파우치, 루팅 백, 트랩 파우치가 loadout 때처럼 쌓이고, 보급품이 보급 파우치로 들어가야 함
- 시체에서 보급 파우치나 루팅 백을 못 가져왔으면 묻지 않고 `[ supplies, out ]`, `[ loot bag, out ]`(`pouches_ask` 0)
- 보급 파우치가 없으면 보급품은 백팩에 그대로, aspect까지 계속. 다음 loadout에서 새 파우치를 고름

## <a id="16"></a>16 bard-archer-enhanced 인게임 확인

2026-10-21 추가. 설계와 숫자는 [Bard Archer](../templates/bard-archer.md) 04절.
새 루프와 새 프로필 → 클라이언트 재시작, nomeehej의 Razor 프로필을 `bard`로([Workflow](../working/workflow.md#04.A) 04.A절).

#### 시작

- F1 → 악기 검색(없으면 `[ inst, pick ]`), `[ bard archer, on ]`
- Tab으로 warmode를 켜면 바딩, 노래, RA, Reflect, Protection이 멈추고 끄면 다시. 회복, 포션, 붕대는 계속
- 악기 복구: [14절](#14)의 공통 확인 항목

#### 회복

- 붕대가 있으면 붕대로 회복, 일반 Heal 시전 없음. 붕대를 감는 도중 마지막 붕대를 다 써도 끝날 때까지 일반 Heal 대기
- 붕대가 없고 감는 중도 아니면 손실이 `light_hits` 이상일 때만 `Agent: Smart Heal/Cure Self, light Heal.`. 마나나 시약이 없으면 시전 없음
- 붕대 중 힐 포션 기준에 닿으면 `heal pot` 바. 그 패스에는 Greater Heal을 건너뛰고, 다음 패스에도 긴급선 이상이면 `Agent: Greater Heal/Cure Self.`
- 힐 포션이 없거나 쿨 중이면 긴급선부터 Greater Heal. 마나나 시약이 없으면 시전 없음, 풀피가 되면 남은 회복 커서 취소
- 기준값과 회복 정책: [Bard Archer](../templates/bard-archer.md#04.A) 04.A절

#### 코덱스 라벨

- `debug/dump-label`로 codex of archery(11886) 라벨 기록. 지금 자세 하나와 지금 피니셔 하나만, 대소문자 그대로(`Arcane`, `Ricochet`) 보여야 함
- 다섯 자세나 두 피니셔를 모두 나열하면 `[ archery stance, off ]`나 `[ archery finisher, off ]`, 전환 정지. 그 라벨 문장으로 판정 방식 수정
- `[ArcheryAmmunition3`이 Incendiary를 켜는지, 켜진 자세를 다시 말하면 꺼지는지(`You deactivate your stance.`)
- `[ArcheryFinisher1`이 Ricochet을 고르고 Pincushion을 끄는지, 둘이 따로 켜지는지

#### 자세와 피니셔 전환

- 한 마리: Arcane, Pincushion. Journal에 `Archery stance switch`, `Archery finisher switch`
- `Z`나 `Q`로 두 마리 이상을 찍어 10칸 안에 두면 2초 안에 Incendiary와 `[ archery, ricochet ]`. 하나로 줄면 6초 뒤 Arcane, Pincushion
- [Bard Archer](../templates/bard-archer.md#02.B) 02.B절의 Fowling 기준: 진입선 초과에서 켜고 해제선 미만에서 원래 자세. 경계값과 두 선 사이에서는 기존 상태 유지
- 프로보 짝 둘 중 하나를 쏠 때 Incendiary가 짝에게 들어가는지
- 손으로 자세를 바꾸면 30초 안에 루프가 다시 맞추는지

#### Virtuoso

- 한 마리를 오래 잡을 때 Virtuoso 아이콘이 빠지면 Discordance가 다시 나가는지(약 15초마다). 실패하면 5초 뒤 다시
- 새 대상에서는 Discordance 뒤 Peacemaking. 프로보할 짝이 있으면 Provocation이 먼저 나가는지
- 끊긴 Peace와 Virtuoso 갱신이 겹치면 Discordance 먼저

#### 무기 능력

- 60초마다 `[ repeater ]`, Journal `Weapon ability request: codex 2, slot 3`. `[WeaponAbility3`이 Repeater인지
- 요청한 뒤 다음 요청(60초)까지 한 발도 못 맞히면 능력이 꺼지는지. 토글이면 요청을 `Weapon ability ready` 문장에 맞춰야 함
- Repeater 피해를 일반 사격 한 발과 비교. 무기 속도 보정 식이 위키에 없음

#### Protection

- `Buff: Protection.` 뒤 아이콘 `Protection`. 커서가 뜨는지, 뜨면 자기에게 들어가는지
- 2분 뒤 아이콘이 사라지면 다시. 마나 26 아래에서는 안 나감

#### 재장착

- 공용 `fight/rearm` 확인 항목. 2026-10-22 Play 때 회복보다 먼저 양손 기록, 백팩에서 고른 serial은 실제 장착을 관찰할 때까지 유지하도록 보강
- Play 때 석궁을 들고 있으면 Journal `Rearm: two-handed layer remembered`. 양손이 비고 기억한 무기도 없으면 graphic 31186으로 검색, `Rearm: graphic 31186 picked`
- 기억한 무기가 사라지면 graphic 검색으로 복귀. 검색 결과도 없으면 `[ weapon, out ]`, 공용 경고 타이머 3초 적용
- RA, Reflect, Protection, Greater Heal 뒤 석궁이 백팩으로 떨어지면 다음 가능한 2초 점검에서 재장착 요청. Journal `Rearm: equip requested on the two-handed layer`
- 같은 석궁을 하나 더 주워 둔 상태에서 Play 직후 회복 시전, 백팩에서 꺼낸 직후 버프 시전. 두 경우 모두 처음 든 것 또는 처음 고른 serial로 재장착하는지
- 장착 거절 뒤에도 같은 serial 재시도. 그 무기를 백팩 밖으로 옮기면 다른 같은 graphic 검색으로 전환하는지
- `rhandempty`와 `righthand`가 이 포크에 있는지. 없으면 오류 줄 기록
- graphic 검색은 1H 무기도 `drop self lefthand`로 보냄(`hotkey/weapon-katana`와 같은 경로). 서버가 제 레이어에 올리는지, 아니면 거절해 2초마다 다시 집는지
- 다시 든 뒤 사격이 이어지는지, `V`를 다시 눌러야 하는지
- 재장착이 바딩 커서나 자기 주문을 끊지 않는지. 끊기면 시전 중 가드가 샌 것
- 31186이 Pistol Crossbow와 같은 art인지. 같으면 백팩에 둘 다 있을 때 `findtype`이 어느 쪽을 집는지

| 상태 | 역할 |
| --- | --- |
| `var__rearm_left`, `var__rearm_right` | 실제로 관찰한 손별 serial, Play를 넘어 유지 |
| `var__rearm_pending` | 백팩에서 고른 뒤 장착 확인을 기다리는 serial, Play 때 초기화. 장착 성공 표시가 아님 |
| `var__rearm_sent` | 이번 점검에서 장착 요청을 보냈으면 1, 둘째 손은 다음 점검 |

소스 기반 모의 검사에서 최초 회복, 연속 시전, 장착 거절 때 다른 무기를 고르는 경우 재현 후 수정.
서버의 레이어 배치와 실제 장착 시점은 인게임 확인 필요.

#### 마나와 바딩

- 체인 한 벌, 음식 버프 없이 마나 10이 차는 시간. 50초면 Butler 식([PvP](../game/pvp.md#05.D) 05.D절)
- 송 메시지가 `8.5%`인지. `6.8%`면 Lyric Aspect 보너스 없음([Bard Archer](../templates/bard-archer.md#01.C) 01.C절)

## <a id="17"></a>17 프로보 후보 입력과 인게임 확인

2026-10-21 두 바드 루프에 구현. 새 입력 경로의 인게임 동작은 확인되지 않았다.
`bard/provo-picks`가 후보 입력, `bard/provo`가 짝 선택과 시전 담당.

#### 반영과 첫 확인

1. `Shift+Space` = `Set Last Target (Beneficial)`(L:2061). 2026-10-21 summoner와 bard 프로필에 추가, 게임에 들어오는지 확인 전([Hotkeys](../game/hotkeys.md#01.F) 01.F절)
2. 수정 파일 반영 뒤 루프 시작. 핫키 실행은 클라이언트 재시작, Scripts 탭 Play는 리로드([Workflow](../working/workflow.md#04) 04절)
3. Tab으로 warmode 수동 구간 진입, 이미 나간 시전과 커서가 끝난 뒤 후보 선택
4. 가장 가까운 몹 A 선택, 아처는 V로 공격. 선택 키는 프로필별 배치([Hotkeys](../game/hotkeys.md#01.E) 01.E절), A의 `[ provo, set ]` 확인 뒤 Shift+Space로 B부터 E까지 등록
5. 후보마다 `[ provo, set ]` 확인 뒤 다음 선택. Tab으로 자동 구간 복귀, A→B와 C→D 확인

- 최초 실행 전에 남은 슬롯은 등록하지 않으므로 루프 시작 뒤 선택 필요
- 시작 슬롯과 같은 몹을 다시 골라도 값 변경이 없음. 새 알림이 없으면 다른 후보를 등록한 뒤 해당 몹 재선택
- 알림 확인에는 `config__chatty` 1 필요. 중복 후보에는 새 등록 알림 없음
- 전투 중 자동 시전과 등록 커서의 중첩은 아직 미검증. 초기 사용은 위 수동 구간, Q로 바딩 대상을 순회해도 프로보 목록 유지
- 커서 색만으로 네이티브 등록 커서 식별 불가. 근거와 한계는 [Razor](../scripting/razor.md#03) 03절

#### 입력과 저장

| 역할 | 입력 | 저장과 알림 |
| --- | --- | --- |
| 현재 바딩 대상 T | Q의 `Set Last Target (Harmful)` 또는 가장 가까운 몹 선택 | `var__combat_target` 채택 뒤 `[ target, set ]` |
| 프로보 후보 | 가장 가까운 몹 선택 또는 `Shift+Space`의 `Set Last Target (Beneficial)` | `lastbeneficial`에서 serial 복사, `list__provo_candidates` 추가 뒤 `[ provo, set ]` |
| 이번 자동 시전 | 후보 목록에서 선택한 둘 | `var__provo_first`, `var__provo_second`에 고정 |

- `lastbeneficial`은 단일 입력 슬롯. 후보 목록의 저장소나 수동 프로보 성공 기록으로 사용하지 않음
- 입력 계약은 새로 관찰한 적대 `lastbeneficial` 값을 후보 등록으로 해석. 같은 슬롯을 갱신하는 다른 핫키와 병용 여부는 프로필에서 확인
- 가장 가까운 몹 선택도 후보 등록으로 수용. 슬롯 갱신 동작의 근거는 [Razor](../scripting/razor.md#03) 03절
- 후보 수집은 자동 바딩보다 먼저, 쿨다운과 무관하게 실행. 검색 가능한 살아 있는 적대 모빌만 등록, 라벨 조회 없이 저장
- serial을 먼저 복사하고 목록에 넣은 뒤 알림. 모든 선택의 무손실 수집 보장 없음, 입력 순서는 위 첫 확인 절 참고
- Q만으로 채택한 T는 후보에 자동 추가하지 않음. 가장 가까운 몹 선택 또는 Beneficial 키로 등록한 T는 다른 후보와 같은 규칙 적용
- Bard Archer의 아처리 마릿수 판정에는 현재 대상과 등록된 후보의 중복 없는 합집합 반영

CE의 `Set Last Target (Beneficial)`은 선택 커서로 `_lastBeneTarget`을 갱신.
근거: [CE Targeting 구현](https://github.com/markdwags/Razor/blob/master/Razor/Core/Targeting.cs), 2026-10-21 확인.
Outlands 포크의 해당 핫키와 커서 간섭은 아래 검증 필요.

#### 후보와 짝

- 자동 프로보는 등록된 후보끼리만. 사용 가능한 후보가 둘 미만이면 대기, 현재 대상 T로 자동 보충하지 않음
- 현재 바딩 대상 T와 무관하게 사용 가능한 후보 둘을 등록 순서대로 선택. 실패한 후보는 선택 순서 뒤로 이동
- 짝 탐색 때 거리, 생존, 라벨 확인. 라벨 미수신은 이번 선택에서 제외
- 각 커서 대기 뒤 두 후보의 거리와 생존 재확인. 첫 후보를 보내지 않았으면 둘째 전달 생략
- `provoked`는 유지, `barding break`는 대기. 어느 쪽에도 해당하지 않는 후보끼리 조합
- 죽은 후보는 제거. 사거리 밖 후보는 시전에서 제외, 목록 유지 여부는 기존 acquire_range 판정 사용
- 풀린 후보는 현재 라벨을 기준으로 다시 조합. 원래 성공했던 짝을 영구 저장하지 않음

| 현재 대상 | 등록한 후보 | 사용 가능한 상태에서의 선택 |
| --- | --- | --- |
| T | B만 | 프로보 대기, T의 Disco와 Peace 계속 |
| T | B, C | B→C, T의 바딩 대상 유지 |
| T | B, C, D, E | B→C, 다음 공유 쿨이 허용할 때 D→E |
| A | A, B | A→B. A가 provoked이면 Peace 생략 |
| A | A, B, C, D, E | A→B, 다음 공유 쿨이 허용할 때 C→D. E는 짝 대기 |

#### 다섯 마리 입력 시나리오

bard 프로필에서 루프 실행 중 Z로 A 선택, V로 A 공격, Shift+Space로 B부터 E까지 등록한 경우.
모두 생존, 사거리 안, 라벨 수신, 시전 성공 가정. 시전 시점은 공유 쿨다운에 따름.

- Z의 A부터 목록에 저장, B까지 등록되면 A→B. B가 이미 provoked이면 B→C 재시전 없음
- C와 D도 등록되면 C→D. E는 다른 사용 가능한 후보가 생길 때까지 대기
- 현재 바딩 대상이 A이면 A에 Disco, provoked 동안 Peace 생략. 짝 없는 E를 자동으로 Peace하는 순회는 없음
- Q로 B, C, D, E를 선택하면 바딩 대상만 이동, 후보 목록과 진행 중인 프로보 유지
- B, C, D는 provoked 동안 Disco만. E는 현재 대상이 된 뒤 Disco와 Peace 조건을 각각 검사
- `[ target, set ]`은 선택 확인. 쿨다운 중 빠른 Q 순회가 지나간 몹의 Disco 시전을 예약하지 않음
- 평타 대상은 V를 다시 누르지 않으면 A 유지. 프로보가 풀리면 Q의 현재 대상과 무관하게 가능한 후보 둘을 다시 조합

#### 수동 조작과 실패

- 수동 프로보는 기존 warmode 수동 구간 사용. 등록된 후보의 실제 라벨로 효과 반영, 성공 메시지만으로 짝이나 후보 추측 금지
- 수동 작업 뒤 Q로 바딩 대상 T를 다시 확인하고 자동 구간 복귀
- 프로보나 후보 등록 커서가 보이면 다른 자동 바딩 시작 보류
- 진행 중인 바딩도 warmode이면 커서 전달과 취소 보류. 전투 중 같은 종류의 등록 커서가 끼어드는 경우의 소유권 판별은 미검증
- Peace는 provoked 후보를 덮어쓰지 않음. 효과 규칙은 [Bard Necro](../templates/bard-necro.md#02.P) 02.P절
- 시전 요청만으로 성공 처리하지 않음. 서버 응답과 실제 라벨 확인, 대기와 재시도는 유한
- 실패한 후보의 재시도 간격 적용, 다음 가능한 짝 검사. `stop`으로 사냥 루프 종료 금지
- 등록과 짝 선택은 분리. 쿨다운 중에는 후보 저장만, 새 짝이 필요할 때 라벨 조회

#### 실제 라타의 한계

- 자동 프로보가 바꾼 `lastharmful`은 `var__target_hold`로 제외, 루프의 바딩 대상 T 유지
- 실제 `lastharmful`을 T로 즉시 복원하는 기능까지 포함한 설계가 아님. 다음 T 대상 바딩 전까지 마지막 프로보 대상이 남을 수 있음
- 그 사이 E와 V 등 기본 라타 핫키가 마지막 프로보 대상을 사용할 수 있음. 같은 serial을 Q로 다시 고르는 입력도 완전히 구별 불가
- 두 프로보 커서 대기 중 완료된 새 harmful 선택은 자동 타깃 전에 T에 반영. 같은 serial 재선택 한계와 실제 슬롯 복원은 별개
- 명시적 복원과 수동 라타 핫키 보존은 별도 검증 과제. 현재 금지한 `setlasttarget serial`에 의존하지 않음([Razor](../scripting/razor.md#03) 03절)
- 가장 가까운 몹 선택은 의도한 후보 입력에 포함. 그 밖의 Beneficial 타깃 지정도 `lastbeneficial`을 바꿀 수 있어 해당 슬롯만으로 입력 출처 보증 불가
- 동료 회복 등에 Beneficial 라타를 쓰는 프로필에서는 후보 등록과 충돌 가능. 공용 슬롯을 전용 슬롯으로 간주하지 않음

#### 추가된 상태와 검증 범위

| 이름 | 역할 |
| --- | --- |
| `var__provo_last_pick` | 마지막으로 관찰한 입력, Play를 넘어 유지 |
| `var__provo_pick` | 이번 패스의 입력 serial 사본 |
| `var__provo_added` | 새 후보 등록 신호, 그 패스에서 짝 탐색 대기 단축 |
| `var__provo_sent` | 이번 요청의 모빌 전달 단계. 0은 전달 전, 1은 첫 후보 전달, 2는 둘째 후보 전달 |
| `list__provo_candidates` | 등록 순서의 후보 목록, Play를 넘어 유지. 옛 harmful 입력 목록과 분리 |
| `timer__disco_target`, `timer__peace_target` | 기존 `wait__bard_target`으로 커서 전달 반복 제한 |

- `var__provo_skip` 제거. 실패한 첫 후보를 목록 뒤로 이동, 일반 실패는 서버 바의 공유 쿨다운 사용
- 2026-10-21 소스 본문을 읽는 모의 시나리오 25개 통과. 서버, 커서 시점, 스코프는 모형이므로 인게임 검증의 대체가 아님

#### 인게임 확인

| 검사 | 통과 기준 |
| --- | --- |
| `Shift+Space` | 커서가 뜨고 찍은 몹에 `[ provo, set ]`. 안 뜨면 macOS 입력 소스 전환부터([Hotkeys](../game/hotkeys.md#02.B) 02.B절) |
| T 선택 뒤 Beneficial로 B 선택 | `lastharmful`과 루프 대상은 T, 후보는 B로 분리 |
| B, C, D, E 등록 | 알림을 받은 serial 전부 목록에 존재, 후보 등록 중 T가 바뀌지 않음 |
| T가 후보에 없고 B 하나만 등록 | B→T 자동 시전 없음 |
| 가장 가까운 몹 A 선택 뒤 B 등록 | 후보에 A와 B 존재, 현재 바딩 대상이 A여도 A→B 선택 |
| 가장 가까운 몹 A 선택 뒤 B, C, D, E 등록 | 성공한 짝은 A→B와 C→D, E 대기. provoked 몹을 다른 짝에 중복 사용하지 않음 |
| Q로 B, C, D, E 순회 | 프로보 목록과 짝 선택 우선순위 유지. Disco 시전은 선택 알림과 별도로 확인 |
| 자동 B→C | 실제 harmful은 C로 바뀌어도 루프 대상 T와 후보 목록 유지 |
| 두 프로보 커서 대기 중 새 harmful 선택 | 자동 시전 후에도 새 바딩 대상 유지, 선택하지 않은 몹으로 초점 이동 없음 |
| 다른 커서와 등록 입력 중첩 | 자동 바딩이 후보 커서를 먹거나 잘못된 몹을 찍지 않음, 등록 취소도 정상 처리 |
| 수동 B→C 뒤 자동 복귀 | 등록된 B, C에 재프로보와 Peace 중복 없음 |
| 사망, 거리 이탈, 라벨 미수신 | 무한 반복과 스크립트 종료 없음, 유효한 다음 짝 처리 |
| 아처리 코덱스 | Q로 T만 선택해도 등록 후보를 마릿수 판정에 반영 |
| 다른 슬롯 갱신과 같은 값 재선택 | 초기 슬롯, 가장 가까운 몹 선택, 동료 회복, 중복 선택의 동작을 기록 |

두 바드 루프는 조립 완료, 위 인게임 확인은 아직 대기.
등록 커서를 자동 바딩과 구별하는 근거가 확보되기 전까지 기존 warmode 수동 구간에서 등록.
실제 라타 복원은 별도 과제. 반영 방법은 [Workflow](../working/workflow.md#04) 04절.

## <a id="18"></a>18 tamer-archer-enhanced 인게임 확인

2026-10-21 추가. 블록 순서와 설정의 정본은 [recipe/tamer-archer-enhanced-recipe.razor](https://github.com/minu-ha/uoo/blob/master/recipe/tamer-archer-enhanced-recipe.razor).
입력은 summoner 프로필 배치([Hotkeys](../game/hotkeys.md#01.E) 01.E절), 코덱스와 사격, 펫 명령은 수동.

#### 템플릿과 설계

- 템플릿: Animal Lore, Animal Taming 120. Veterinary, Resisting Spells, Magery, Archery, Tactics, Herding 80. 사용자 화면 2026-10-21.
  Healing 없음 → 붕대 블록 없음, 수의사 키트가 셀프 붕대([12절](#12)). 사용자 확인 2026-10-21
- 바드 블록 없음. 펫 명령과 대상 지정은 수동, 루프는 펫을 명령하지 않음
- `[CodexHotbar`를 시작 때 한 번 요청([Commands](https://wiki.uooutlands.com/Commands) "Launches the Codex Hotbar"). 코덱스 자세와 피니셔의 자동 전환 없음
- 뺀 것: `escape/tracking`, `recovery/bandage`, `bard/provo-picks`, `fight/archery-codex`, `buff/mushroom`, `magery/flamestrike`, Bless, Arch Protection. 사용자 요청 2026-10-21
- Full Draw: 활은 2.21초에 한 발([PvP](../game/pvp.md#09.B) 09.B절 표) → 15초에 6.8발 × 50% = 약 340%. Repeater 225%보다 큼. 정지 3초 조건이라 움직이며 쏘면 Repeater(`ability_main` 3)
- 사거리 10: 활([Bard Archer](../templates/bard-archer.md#02.A) 02.A절). `target_range`와 `ability_range` 모두 10
- 버프는 bard-archer와 같은 RA 24, Reflect 34, Protection 26. Greater Heal 11과 Teleport 9의 20을 남김
- 스탯 포션 기준선 STR 120, DEX 100은 기본값. 이 템플릿의 스탯은 미기록 → 다르면 레시피에서 변경
- `rearm_graphic` 5042로 활 검색. 공용 재장착 동작과 상태는 [16절](#16) 재장착 항목

#### 반영과 첫 확인

1. 사용할 캐릭터의 summoner 프로필 F1을 `Play Script: combat\tamer-archer-enhanced`로 연결. 현재 프로필에는 연결 없음, 설정 파일은 게임 종료 뒤 수정
2. 수정 파일 반영 뒤 실행. 핫키는 클라이언트 재시작, Scripts 탭은 리로드 뒤 Play([Workflow](../working/workflow.md#04) 04절)
3. `[ crook, out ]` 없이 `[ tamer archer, on ]`, 코덱스 핫바 표시 확인

#### 인게임 확인

- 코덱스 핫바가 이미 떠 있을 때 다시 Play하면 닫히는지
- 수의사 키트: [12절](#12)의 항목 그대로
- 시전 뒤 활 재장착: [16절](#16) 재장착 항목. Journal `Rearm: two-handed layer remembered`, 시전 뒤 `Rearm: equip requested on the two-handed layer`
- `[ full draw ]` 60초마다. 정지 3초 뒤 발사되는지, 움직이면 안 나가는지. 손해면 `ability_main` 3
- `Buff: Protection.` 뒤 아이콘, 2분 뒤 다시([16절](#16) Protection 항목)
