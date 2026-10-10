---
name: Lumberjack PvP
label: 벌목과 PvP 핸드북
group: Templates
order: 20
---

Lumberjacking을 유지하며 도끼, 붕대, 마법으로 필드에서 반격하는 캐릭터. 스킬, 장비 선택과 교전 설계.
서버 규칙 정본은 [PvP](../game/pvp.md), 미확인 메커니즘과 실험 절차는 [Open items](../questions/open-items.md#08) 08절.

## <a id="00"></a>00 한눈에

**벌목 120을 지키는 근접 중심 하이브리드.** 순수 결투 캐릭터의 최적해로 단정하지 않음.
2026-10-01 대화에서 근접과 붕대 중심으로 변경. 수치는 공식 계산값, 전투 시나리오는 실전 미검증.

- 기본안: 스킬 720, **STR 100, DEX 80, INT 45**. 도끼 압박과 붕대 우선
- Great Axe로 한 방, Norse Axe로 붙어서 압박. Hatchet은 벌목과 중간 속도의 싸움
- 상대도 파우치, 붕대, 포션 자동 사용. Paralyze 동안 멈춰 기다리는 상대는 가정하지 않음
- TK는 자기 방어와 공격 부착 중 하나. **반사 TK를 공짜 자기 방어로 계산하지 않음**
- Explosion과 EB 자동 콤보는 제외. 마법은 짧은 견제, 회복, 이동용. TK 뒤 폭발 포션은 적용 확인 가능할 때만
- 채집은 `lumberjack-enhanced`(08절), PvP 자기관리는 공통 `pvp`(09절).
  두 루프는 핫키를 따로 두고 수동 전환. 두 파일 모두 전체 동작은 인게임 미확인

| 절 | 내용 |
| --- | --- |
| 01\~03 | 스킬, 스탯, 장비와 공유 스윙 |
| 04\~05 | 마나 예산과 이동 중심 교전 |
| 06\~07 | 자동화로 확인 불가한 것, 피해 계산 예시 |
| 08 | 채집 루프 lumberjack-enhanced. 구현 순서와 인게임 확인 |
| 09 | PvP 루프. 설정, 타이머, 인게임 확인 |

::part[캐릭터]

## <a id="01"></a>01 스킬 720

| 스킬 | 값 | 이 템플릿에서 맡는 일 |
| --- | --- | --- |
| Lumberjacking | 120 | 채집 목적 유지, 도끼의 PvP 보조 피해 |
| Swordsmanship | 100 | 도끼 명중, 무기를 든 동안의 근접 방어. Lumberjacking으로 대체 불가 |
| Tactics | 100 | 근접 기본 피해 페널티 제거 |
| Magery | 80 | 회복, 해독, 이동, 짧은 견제, TK. Explosion과 EB는 자동 루프에서 제외 |
| Tracking | 80 | 적 탐지, 보조 피해. Hamstring 자격의 한 자리 |
| Resisting Spells | 80 | 주문 피해 방어. PvP 시전 인터럽트 방어는 아님 |
| Anatomy | 80 | Hamstring 자격의 다른 자리. 근접 기본 피해와 붕대 보조 |
| Healing | 80 | 붕대 회복으로 공격 마나 절약 |
| 합계 | 720 | Eval, Meditation, Wrestling, Alchemy 없음 |

- Hamstring: Swordsmanship으로 공격, Anatomy와 Tracking으로 보조 조건. **Swordsmanship과 Tracking만으로는 부족.** 조건 원문은 [PvP](../game/pvp.md#03) 03절
- 도끼 근접 보조 상한: Lumberjacking 120의 +12%, Tracking 80의 +8%로 채움
- Tracking 주문 보조도 +8%, 단 Eval 대체 아님. Tactics와 Anatomy도 이 상한 밖([PvP](../game/pvp.md#09.A) 09.A절)
- 무기를 들면 Swordsmanship으로 싸움. 시전하려고 손을 비우면 Wrestling 없음이 약점
- 상대 무기 스킬 100 대 내 맨손 Wrestling 0 → 상대 기본 명중률 100% → 근거리 긴 시전 운영은 피함([PvP](../game/pvp.md#02.E) 02.E절)

### <a id="01.A"></a>01.A 마지막 20점의 선택

Lumberjacking 120, Swordsmanship 100, 나머지 여섯 스킬 80씩 = 700. 남은 20점 비교.

| 100으로 올릴 스킬 | 얻는 것 | 고르는 기준 |
| --- | --- | --- |
| Tactics, 기본안 | 기본 무기 피해의 -10% 보정 제거 | 도끼로 붙어서 마무리할 생각이면 먼저 |
| Healing | 슬립 전 붕대 평균 46.4 → 58 | 힐에 마나를 많이 쓰거나 오래 주고받을 때 밀리면 비교 |
| Resisting Spells | 주문 피해 방어 강화 | 메이지 폭딜에 회복 전에 무너지면 비교 |
| Tracking | 탐지 거리와 성공률 상승, 주문 보조 +8% → +10% | 조기 발견이 가장 중요할 때. 도끼 보조 피해는 이미 상한 |
| Anatomy | 근접 기본 피해 +16% → +20%, 붕대 평균 46.4 → 48 | 회복량만 보면 Healing보다 작음 |

계산 근거: [PvP](../game/pvp.md#09.A) 09.A절과 09.C절, 방어는 [08절](../game/pvp.md#08), 탐지는 [10절](../game/pvp.md#10).

### <a id="01.B"></a>01.B Magery 80, 그리고 Eval과 Meditation을 뺀 비용

- Magery 80: 유틸리티와 Greater Heal용으로 유지. 자동 Explosion과 EB를 뺐다고 60으로 낮추기로 한 것 아님
- Earth Elemental 스크롤의 성공률과 필요 마나는 별도 확인. **기본 최대 마나 45로는 50마나 소환 불가**
- 버프로 실제 마나 50 초과 확보 여부 확인 필요. 소환 직후는 교전 준비 안 된 상태([PvP](../game/pvp.md#05.B) 05.B절, [06절](../game/pvp.md#06))
- Magery 100은 7서클과 8서클만의 문제가 아님. 피해와 Greater Heal도 함께 강해짐
- Magery 80 GH 기본 회복 32\~40. 60으로 줄이려면 회복량과 시전 신뢰도 재비교
- Eval 없는 주문 ≠ 주력 메이지의 공격. Meditation 없는 마나로는 긴 주문 교환이 어려움
- 지금 안: 둘 중 하나를 80 넣는 안이 아니라 **Anatomy와 Healing을 함께 지키는 안**
- 예전 안: Wrestling 80 + Eval 80 또는 Meditation 80. 돌아가려면 Anatomy와 Healing을 빼는 재설계 필요.
  그 경우 Hamstring 조건은 Tracking과 Wrestling, 대신 붕대 상실. 주문전 위주로 바꿀 때 별도 비교

## <a id="02"></a>02 스탯 225와 회복

STR 100 고정, DEX와 INT 배분. 표는 Greater Agility +20만 반영.
Greater Strength 복용 시 최대 HP 120으로 계산. Bless의 정수 처리와 중첩은 제외([PvP](../game/pvp.md#09.D) 09.D절).

| STR, DEX, INT | 포션 뒤 DEX | 자기 붕대 | 판단 |
| --- | --- | --- | --- |
| 100, 25, 100 | 45 | 약 13.67초 | 마나는 넉넉, 목표 붕대 11\~12초보다 느림 |
| 100, 50, 75 | 70 | 12초 | 이전 안. 긴 공격 주문까지 쓸 때의 비교용 |
| 100, 60, 65 | 80 | 약 11.33초 | 근접과 회복을 조금 더 |
| 100, 65, 60 | 85 | 11초 | 붕대 목표는 확실히 당기지만 마나 여유 감소 |
| **100, 80, 45** | 100 | **10초** | 지금 기본안. 도끼와 붕대 중심, 마나는 유틸리티에 아낌 |

- [PvP](../game/pvp.md#09.C) 09.C절 공식의 이론값. 자동 붕대는 재사용 실수만 줄이고 완료 시간은 그대로
- 서버 계산 상한을 넘는 DEX는 붕대 속도와 PvP 공속에 추가 효과 없음
- 출발안으로 싸워 보고 부족한 것을 기록
  - 마나가 먼저 바닥 → 공격 주문 감소
  - 붕대 완료 전 압박에 밀림 → Healing 상향 비용 비교
  - 포션 만료, Curse, 독, 슬립이 섞인 결과는 따로 기록
- Bless: Magery 80에서 공식상 INT +8.8. **45 + 11 = 56으로 계산하지 않음**
- 정수 처리와 현재 마나 동반 상승은 미확인. 시전에 9마나 → 발견 즉시 Bless로 마나 여유가 바로 는다고 보지 않음
- 포션과 STR, DEX 중첩도 실측 전에는 더하지 않음([PvP](../game/pvp.md#09.D) 09.D절)

### <a id="02.A"></a>02.A 장비 출발안

- 기본 방어구 Leather. Meditation 0이어도 자연 재생 있음
- 가죽의 이유: 재생 보너스가 아니라 방어구 재생 페널티 없음
- Studded의 물리 방어는 무기를 섞는 메이지나 근접 상대에게 유효 → 언제나 무의미하다고 단정하지 않음
- 전투용 Great Axe와 Norse Axe, 벌목 겸 예비 Hatchet. 무기 품질, 마법 옵션, 방패 운용은 미정
- 장비를 바꿔 잰 값과 아래 일반 무기 계산은 섞지 않음. 재생 조건은 [PvP](../game/pvp.md#05.D) 05.D절

## <a id="03"></a>03 도끼와 스윙

목적에 맞는 도끼는 [Swordsmanship 무기표](https://wiki.uooutlands.com/Swordsmanship)에서 선택.
Katana나 Halberd는 같은 스킬이어도 Lumberjacking 보너스 없음([PvP](../game/pvp.md#09.A) 09.A절).

| 무기 | 역할 | Speed | 기본 피해 |
| --- | --- | --- | --- |
| Great Axe, 2H Burst | 붙는 순간의 한 방과 Hamstring 시도 | 25 | 21\~46 |
| Hatchet, 2H Medium | 벌목 도구 겸 중간 속도의 지속전 | 38 | 17\~32 |
| Norse Axe, 1H Light | 붙어 있는 동안 잦은 명중과 인터럽트 | 48 | 13\~23 |

무기표의 Speed, MinDmg, MaxDmg. 실제 피해에는 스킬과 방어구 계산이 추가.

| 현재 스태미나 | Great Axe | Hatchet | Norse Axe |
| --- | --- | --- | --- |
| 45 | 4.14초 | 2.72초 | 2.16초 |
| 70, 이전 안 | 3.53초 | 2.32초 | 1.84초 |
| 80 | 3.33초 | 2.19초 | 1.74초 |
| 100, 지금 안의 최대 스태미나 | 3초 | 1.97초 | 1.5625초 |

- [PvP](../game/pvp.md#09.B) 09.B절 공식. 피해로 스태미나가 떨어지면 포션 뒤 최대 DEX만으로 공속 예측 불가
- 예: 스태미나 100, Great Axe t=0, Norse Axe t=1.5625 → 다음 Great Axe는 t=4.5625부터. 원래 간격 t=3의 공짜 한 대 아님
- 큰 무기 쿨 중이라고 무조건 작은 무기를 들지 않음. 곧 올 큰 한 방의 기회와 지금 빠른 스윙으로 회복 시전을 견제하는 편을 비교. 명중 자체는 보장 없음

::part[교전]

## <a id="04"></a>04 마나 예산과 시작 조건

[PvP](../game/pvp.md#05.B) 05.B절 기본 마나의 합. 자연 회복, 실패, 추가 시전 제외.
INT 45 = 기본 최대 마나. 실제 판단은 현재 마나, 재생, 남겨 둔 회복 몫 기준.

| 행동 묶음 | 마나 | 판단 |
| --- | --- | --- |
| TK와 폭발 포션 | 9 | 공격 TK 적용 확인 가능할 때만 점화. 포션 자체는 마나 없음 |
| GH와 Teleport | 20 | 공격보다 먼저 남길 초기 몫. 생존 보장 아님 |
| TK, TP, GH, MA 두 번 | 37 | 30초 사용 시 이상적 자연 재생 15를 빼면 순소모 22 |
| TK, Explosion, EB | 49 | 기본 최대 마나 45 초과, 회복 여유 없음. 자동 루프에서 제외 |

- 최소 여유: GH와 Teleport 몫을 따로 남김. 생존 보장이 아니라 회복과 이동 한 번씩의 예산
- 해독, 견제, 실패에 마나가 더 들면 긴 콤보 포기. 자기 TK를 미리 걸었어도 다시 안 찬 마나는 이미 쓴 것
- Rope: 기본 추격 수단으로 자동 사용 안 함. 마나 부족처럼 정말 필요할 때 수동 선택으로 남김.
  단, 그 뒤 Teleport까지 공유 쿨에 묶이는 비용 표시 필요([PvP](../game/pvp.md#05.C) 05.C절)
- 가죽, Meditation 0의 자연 재생은 초당 0.5. 위 30초 예시에서 45로 시작하면 약 23 잔여.
  단, 최대 마나에서 버린 재생, 시전 시점, 추가 해독, 실패는 빠짐 → 실제 잔량 보장 아님
- TK 30초, TP 15초마다 계속 쓰면 둘만으로 초당 0.9마나 → 재생보다 빠름 → 쿨마다 자동 사용 안 함
- 붕대와 포션이 기본 회복이어도 위험할 때 GH를 끝까지 미루지 않음. 자연 재생 조건은 [PvP](../game/pvp.md#05.D) 05.D절

## <a id="05"></a>05 상대도 스크립트를 쓰는 전투

- 05.A\~05.C절: TK와 폭발 포션을 쓰는 Alchemy와 Inscription 메이지 가정
- 05.D절: 사용자가 고른 상대, Inscription 없는 순수 Alchemy 메이지와의 조건부 계산
- 교전 판단 = 상대의 이동, 회복, 반사와 내 실패에 대한 대응. 이벤트별 명령 제한은 별도 확인

### <a id="05.A"></a>05.A 기본안: 움직이며 다가가고, 붙으면 도끼

1. **발견.** Tracking으로 적 발견 → 무게, 퇴로, 마나, 포션 상태 확인. 짐이 무거운 채집 상태에서는 추격 시작 안 함.
   먼저 반격 주문을 쓰면 도주 제한도 생김([PvP](../game/pvp.md#01) 01절)
2. **TK 선택.** 전투 제어가 켜진 동안만 수동 Tab의 Warmode를 의도로 읽음. ON → 공격 TK, OFF → 자기 TK.
   스크립트는 Warmode를 바꾸지 않음. Warmode OFF인 평소에 자기 TK 반복 없음, 시전자 공용 쿨 우회 없음.
   공격 TK 뒤 포션 조건이 되면 05.B절 먼저, 그 뒤 견제로 복귀
3. **견제.** 사거리, LOS, 남긴 마나가 맞으면 MA 한 번. 낮은 반사 피해를 감수하는 선택일 뿐 상대 Reflect 소진 확인 수단 아님.
   Inscription이 있다고 두 발 강제 없음, 다음 행동으로 긴 공격 주문 예약 없음
4. **접근.** 기본은 이동. 짧은 주문은 시전에 필요한 동안만 멈췄다가 다시 추격.
   상대가 멈춰야만 견제 가능하다고 보지 않고, 이동 중 끊김 없는 시전도 가정하지 않음
5. **접촉.** 실제 근접 사거리와 공유 스윙 준비 확인 → Great Axe와 Hamstring 시도.
   붙어 있는 동안 Norse Axe로 압박. 근접 스윙 사이에 새 공격 주문 끼워 넣지 않음
6. **이탈.** 상대가 달아나면 추격, 거리와 마나가 맞을 때만 MA나 Harm 한 번.
   실패하거나 사거리를 벗어나도 즉시 연속 재시전 없음. 다시 붙으면 공유 스윙에 맞춰 도끼로 복귀
7. **회복.** 붕대와 포션이 기본. 위급하면 GH, 해독, 퇴로 확보가 공격보다 먼저.
   상대도 포션을 마시며 달릴 수 있음. 내 포션을 맞은 상대가 GH 시전을 위해 꼭 멈춘다고 가정하지 않음

- Warmode = 공격 의도일 뿐, 상대 Reflect 상태 정보 아님
- Explosion과 EB는 수동 마무리로 남길 수 있음. 단, 기본 루프와 마나 예산에는 넣지 않음
- 상대 시전 상태를 못 읽으면 견제일 뿐, 확정 인터럽트로 적지 않음

| 거리 분기 초안 | 행동 |
| --- | --- |
| 실제 근접 사거리 | 도끼 우선. 화면상 1\~2타일이라고 명중 가능으로 확정하지 않음 |
| 근접 밖 4타일까지 | MA나 Harm 한 번 → 다시 접근 |
| 5\~6타일 | MA 우선. Harm은 멀수록 피해 감소 → 2서클 견제가 꼭 필요할 때만 검토 |
| 6타일 밖 | 접근 우선. 실측 후 시작 임계값 수정 |

- 6타일 = 시험할 **시전 시작 임계값**, 서버 최대 사거리 아님. 주문과 포션의 대상 지정 거리와 LOS는 별도 검증
- MA 0.5초, Harm 0.75초 시전과 서클별 제한: [PvP](../game/pvp.md#05.A) 05.A절, 05.B절

### <a id="05.B"></a>05.B 조건부 공격안: 공격 TK 직후 포션

- 공격 TK를 적에게 실제로 건 경우에만 포션 부착 기대. 자기 TK 방어 동시 획득 가정 없음
- 포션 부착 안내는 자기 TK에도 뜸 → 누구에게 건 TK인지 모르면 성공으로 읽지 않음
- TK는 Reflect 제거용 아님([PvP](../game/pvp.md#04.C) 04.C절)

1. 공격 대상 A의 serial 저장, 공격 TK 시도 여부와 대상 변경 관리. Last Target 하나만 전투 대상 저장소로 쓰지 않음
2. 공격 TK가 A에게 걸렸다고 믿을 수 있고 투척 거리와 LOS가 맞으면 즉시 투척. TK와 포션 사이에 MA 없음
3. 지금 관찰 가능한 신호만으로는 그 믿음의 조건을 항상 채울 수 없음. 응답 대기 중 적 TK가 들어오면 미확인 처리, 점화 안 함
4. 이미 확인한 공격 TK 뒤 적 TK를 맞은 경우 ≠ 성공 판정 자체가 모호한 경우. `teleki, me`만 보고 앞의 경우를 무효로 만들지 않음
5. 포션 실제 부착 확인 → 접근, 도끼와 Hamstring. 투척 성공, 부착 성공, 명중 피해는 서로 다른 상태

- Hamstring은 침묵이나 기절 아님. 그동안에도 상대는 회복 주문, 공격 주문, 포션 사용 가능
- Paralyze도 자동 파우치 상대를 긴 콤보 동안 묶는 도구로 계산하지 않음
- 상대가 내게 포션을 붙였으면 던진 사람과 함께 폭발 범위에 들어가 Splashback 시도 가능.
  단, 더 큰 근접 피해나 주문 피해를 받는 상황인지 먼저 확인([PvP](../game/pvp.md#04.A) 04.A절)

**구현을 막는 조건.** 시도 뒤의 새 안내, 같은 대상, target 바만으로는 공격 TK 성공 증명 불가.
거짓 성공을 막으려면 별도 확인 수단 검증 전까지 자동 점화 보류([PvP](../game/pvp.md#04.D) 04.D절).
TK에서 포션까지의 완전 자동 처리가 안전하게 풀렸다는 뜻 아님.

### <a id="05.C"></a>05.C 길어진 교전과 철수

붙지 못한 채 주문만 주고받으면 Eval과 Meditation을 갖춘 메이지보다 자원 면에서 불리.
상대는 회복을 마쳤는데 내 마나와 스태미나만 줄었으면 같은 오프너 반복 안 함.

- 원거리 견제: MA와 Harm 기본, 고정 순서 없음. 거리, 마나, 서클별 제한으로 선택
- 붕대는 미리 돌림. 완료 전에 못 버티면 포션, GH, 시야 차단. 자동 사용은 판단 수고만 줄일 뿐 피해는 그대로
- 추격용 Teleport 직후에는 도주용으로 즉시 재사용 불가. 포션과 가방 자원은 출발 전 확인
- 철수는 이동과 시야 차단 우선. 공격 직후 즉시 Recall 가능하다고 가정하지 않음

### <a id="05.D"></a>05.D 순수 Alchemy 메이지와 30초, 60초 모형

2026-10-05 사용자가 고른 비교. **실제 필드 승률은 알 수 없음.**

- 값 = 정해진 행동만 반복하는 두 캐릭터가 제한 시간 안에 상대를 쓰러뜨리는 비율
- 둘 다 생존 → 미결판. 남은 HP가 많아도 승리로 세지 않음
- v4 회복 정책 고정 모형. v5의 긴급 커서 중단, 손실 35부터의 GH 정책은 미재현
- **던전에서 처음 마주쳐 10초 안에 죽는 상황의 생존 판단에는 사용 불가**
- 이 정책은 성공한 Explosion, EB, 폭발 포션을 한 시점에 모으는 콤보를 보장하지 않음
- HP 약 100, Reflect 없이 시작한 실제 보고와 첫 버스트 대응은 [05.E절](#05.E)

| 대상 | 고정한 조건 |
| --- | --- |
| 내 캐릭터 | 01절의 스킬 720, STR 100, DEX 80, INT 45. 일반 Great Axe와 Norse Axe |
| 상대 | STR 100, DEX 25, INT 100. Magery, Eval, Meditation, Wrestling, Resist, Tracking 각 100, Alchemy 120 |
| 준비 | 양쪽 Strength 포션으로 HP 120. 나는 Agility 포션 뒤 STA 100 유지. RA, Reflect, Protection, 시폰은 전투 전 준비, 마나를 채운 뒤 서로 공격 TK |
| 시작 자원 | TK에 9를 이미 써서 내 마나 36/45, 상대 91/100. 재생은 가죽의 수동 재생만. 보급품 넉넉 |
| 방어와 무기 | 상대 총 AR 50, Inscription과 Parry 0. 실제 마지막 스윙 공유, 명중률 50%. RA는 남은 방어량이 있는 동안만. 시작 Reflect 각자 1회 |
| 공격 시작 | 0초에 양쪽 TK 적용, 0.2초에 각자 폭발 포션 1개, 0.4초에 각자 MA 시도. 이후 상대는 Explosion과 EB 교대 시도. 끊긴 Explosion 재시전이나 콤보 완성은 보장 없음 |
| 내 수동 정책 | 붙으면 도끼. 떨어지면 MA 최소 8초 간격, 20마나 유지. 다음 TK도 20 유지, 시전자 쿨과 대상 쿨이 모두 끝났을 때만. 성공한 TK 하나에 포션 1개 |
| 내 자동 회복 | 피해 시 붕대, 손실 35에 힐 포션, 손실 45에 GH. 회복 주문 재시도 2.5초, 안전한 HP에서 RA 재시도 5초. 시전 중 아이템과 도끼 대기 |
| 상대 회복 정책 | 손실 35에 힐 포션, HP 85 이하에 GH, 다 쓴 RA 재시전. 공격 주문은 회복용 마나 11 유지, 부족하면 공격 대기. Meditation 능동 사용 없음 |

- 상대 스킬: [공식 Pure Alchemy Mage 720](https://wiki.uooutlands.com/TemplatesPvPMage) 구성
- 계산식 정본: [PvP](../game/pvp.md#05) 05절의 회복과 버프, [08절의 주문 보정](../game/pvp.md#08), [09절의 무기, 명중, AR](../game/pvp.md#09)
- Tracking은 Eval 항에 더하는 예시 해석. 서버의 결합 순서는 실측 미확정

#### 실험 결과

- 근접 여부: 평균 2초의 접촉 구간과 비접촉 구간을 교대로 두는 모형. 25%, 50%, 75%는 목표 유지율
- Hamstring 성공이나 이동 경로로 자동 계산한 추격 성능 아님. 조건마다 2,000회, seed 410
- 끊긴 시전의 마나 소모는 미확정 → 0%와 주문 비용 100%를 각각 계산
- 두 값의 차이 = 미확인 규칙에 대한 민감도. 통계적 신뢰구간도, 실제 승률의 하한이나 상한도 아님

| 목표 근접 유지율 | 끊긴 주문 마나 비용 | 30초: 승 / 패 / 미결판 | 60초: 승 / 패 / 미결판 |
| --- | --- | --- | --- |
| 25% | 0% | 0.0 / 0.2 / 99.8% | 0.0 / 0.2 / 99.8% |
| 50% | 0% | 0.0 / 0.1 / 99.9% | 0.0 / 0.1 / 99.9% |
| 75% | 0% | 0.0 / 0.1 / 100.0% | 0.1 / 0.1 / 99.9% |
| 25% | 100% | 0.0 / 0.0 / 100.0% | 0.3 / 0.0 / 99.7% |
| 50% | 100% | 0.1 / 0.0 / 99.9% | 3.5 / 0.0 / 96.5% |
| 75% | 100% | 0.5 / 0.0 / 99.5% | 11.8 / 0.0 / 88.2% |

- 반올림으로 합이 100%와 조금 다를 수 있음. 0.0% = 이 표본에서 처치 없음, 불가능의 뜻 아님
- 동시 사망 0건. 첫 사망에서 종료 → 그 뒤 예약된 폭발 피해로 생길 동시 사망은 미집계
- **이 정책에서는 30초 안에 대부분 결판 안 남. 60초 생존 ≠ 상대 처치**
- 모형의 회복 정책이 잘 돈 경우. 실제 첫 버스트를 붕대와 포션으로 버틸 수 있다는 증거 아님
- TK, 포션, MA만으로 회복하는 메이지를 빨리 잡는 결과는 없음

#### 상대 정책을 바꾸면 달라지는 결과

다른 조건은 그대로, 상대가 공격 뒤 GH 몫을 남기지 않게 바꾸면 처치 비율 증가.
범위 = 끊긴 주문 비용 0%와 100% 두 실험의 값. 실제 상대와의 실력 차이 측정값 아님.

| 목표 근접 유지율 | 60초 처치: 상대 예비 마나 11 | 60초 처치: 상대 예비 마나 0 |
| --- | --- | --- |
| 25% | 0.0\~0.3% | 1.1\~3.7% |
| 50% | 0.0\~3.5% | 11.9\~32.5% |
| 75% | 0.1\~11.8% | 24.6\~62.1% |

스킬과 스탯이 같아도 상대의 마나 관리 가정 하나로 숫자가 크게 변함 → 이 값을 “내 승률”로 부를 수 없음.

#### 미확인 가정과 재현

- 폭발 퓨즈 2초, 근접이면 양쪽에 Splashback 50/50: 모형의 가정. 실제 폭발 반경, 투척 지연, 회피 경로 미재현
- 피해와 회복은 공식 범위 안 균등 추출. AR과 Resist 분포, 시전 중 재생, 서버 반올림 미실측
- Poison, Curse, Paralyze, 이동 방해, 시야 차단, 지형, 후퇴, 핑 제외. 실제 메이지의 여러 압박을 생략 → 내 생존을 실제보다 좋게 볼 수 있음
- 무기 장착은 즉시 적용 모형. 실제 300ms 장비 조회, Dress 큐, 걷기 제한 미재현.
  아이템과 시전 회복에 200ms 적용, 같은 tick에서는 시전 완료를 피해보다 먼저 처리
- 필드 Hamstring의 이동 제한은 목표 근접 유지율에 포함한 가정. DEX 80의 조직 PvP 강화 피해는 필드에 미적용
- 버섯 마나 보충, 시폰의 PvM 효과 제외. 실제 Razor, 게임 서버, 전투 로그로 보정한 모형 아님

- 입력, 공식, 정책: [util/pvp-sim.mjs](https://github.com/minu-ha/uoo/blob/master/util/pvp-sim.mjs)
- 수치와 일정 검사: [util/pvp-sim.test.mjs](https://github.com/minu-ha/uoo/blob/master/util/pvp-sim.test.mjs). Node 표준 라이브러리만 사용
- 검사는 모형 계산 확인용, 인게임 동작 증명 아님

```
node --test util/pvp-sim.test.mjs
node util/pvp-sim.mjs --trials 2000 --output tmp/pvp-analysis/results.json
node util/pvp-sim.mjs --trials 2000 --mage-reserve 0 --output tmp/pvp-analysis/aggressive.json
```

### <a id="05.E"></a>05.E 던전에서 첫 버스트를 받는 경우

- 2026-10-05 사용자 보고: 적 메이지 한 명에게 약 10초 만에 사망. 순서는 TK, 폭발 포션, Explosion, EB
- 당시 Reflect 없음, 몹에게 한두 대 맞아 HP 약 100. 피해마다의 정확한 시각과 상대 스킬은 확인되지 않았다
- 최대 HP 120에서 네 단계 모두 피해로 계산하지 않음. TK는 포션 부착 준비 단계

#### HP 100이 사라질 수 있는 피해량

가정: 상대 Magery와 Eval 100, 주문 보조 상한 10%, Alchemy 120. 나는 Resist 80, 반사와 Splashback과 중간 회복 없음.
Tracking과 Eval 결합은 05.D절과 같은 예시 해석. 서버 반올림과 실측 분포 확정값 아님.

| 피해 | 이 조건의 계산 범위 |
| --- | --- |
| Greater Explosion 포션 | 24\~40 |
| Explosion 주문 | 24.01\~39.69 |
| Energy Bolt 주문 | 24.01\~39.69 |
| 세 피해 합계 | 72.02\~119.38 |

- HP 약 100 → 이 세 피해만으로 사망 가능. 보고를 설명할 수 있는 조건일 뿐, 실제 상대 스킬 판정 아님
- 범위별 중간값의 합 94.72. 실측 평균이나 사망 확률로 읽지 않음
- Inscription 120은 스크롤 시전 보조 상한을 채울 수 있음. 단, Tracking 같은 다른 보조와 합쳐도 상한은 그대로
  → Inscription 120 없이도 위 피해량 가능. 보정 정본은 [PvP](../game/pvp.md#08) 08절
- Explosion 0초 방출, 회복 0.2초 뒤 즉시 EB 시전 → EB 피해 2.45초, Explosion 피해 2.5초 가능
- 약 0.05초 차이에 포션 폭발까지 겹치면 HP가 한꺼번에 사라진 것처럼 보임.
  실제 포션 퓨즈, 투척 지연, 핑 반영값 아님. 주문 시각 정본은 [PvP](../game/pvp.md#05.B) 05.B절

#### 이 템플릿의 대응 순서

1. 적에게 드러나기 전에 Reflect와 HP 준비. HP 100, Reflect 없이 공격 콤보부터 시작하면 첫 버스트를 버틸 여유가 작음
2. 적 TK보다 먼저 자기 TK를 걸 수 있으면 방어용. 적 포션 부착만 막을 뿐 지면 폭발, Explosion, EB는 못 막음.
   적 TK가 이미 걸린 뒤에는 자기 TK로 제거 불가. 공격 TK와 묶이는 제한은 [PvP](../game/pvp.md#04.C) 04.C절
3. 발견 시 HP가 모자라면 모퉁이로 다음 주문의 시야를 끊고 즉시 회복할 틈 확보.
   이미 붙은 포션이나 방출된 Explosion이 사라졌다고 판단하지 않음. 붙은 포션은 가능하면 적에게 접근해 Splashback 시도.
   단, 먼 거리, 몹, 퇴로를 무시한 돌진은 안 함
4. 상대가 실제로 시전하는 순간 MA, Harm, 도끼 명중으로 다음 주문 끊기.
   상대 Reflect와 주문 방해 창이 있으니 MA 연타나 첫 한 방이 항상 시전을 끊는다고 기대하지 않음

#### 붕대를 먼저 시작하는 것과 지금 자동 회복의 한계

- Agility 뒤 DEX 100 → 기본 자기 붕대 10초. 첫 피해 뒤 시작한 붕대는 몇 초 안에 겹쳐 오는 첫 버스트에 늦음
- 미리 시작해 완료 시각을 앞당기는 생각은 맞음. 단, 붕대가 HP를 즉시 채우거나 피해를 막지는 않음. 공식 정본은 [PvP](../game/pvp.md#09.C) 09.C절
- 이번 보고처럼 HP 약 100이면 지금 스크립트의 붕대 시작 조건 충족 → 붕대 시작을 위한 자기 MA 불필요
- 진행 중인 붕대가 없고 커서나 시전 대기도 없을 때 붕대를 요청하는지는 인게임 확인 대상
- HP가 가득이면 지금 스크립트는 붕대를 요청하지 않음. 서버가 HP 가득 상태의 자기 붕대를 허용하는지는 확인되지 않았다
- 자기 MA는 한 번에 마나 4, 계속 맞으면 진행 중인 붕대가 미끄러질 수 있음 → 자동 반복 안 함
- 보고 당시 v4: 기본값 힐 포션 손실 35, GH 손실 45, 수동 입력 중 회복 보류.
  최대 HP 120 중 100 잔여는 두 회복 요청의 시작값에 못 미침
- v5: GH를 손실 35로 앞당김, 준비된 긴급 회복이 있으면 수동 주문을 끊음.
  단, 아직 피해가 없거나 중립 커서를 들고 있으면 다음 버스트를 예상한 자동 회복은 없음
- 공식 포션 동작과 지금 정책: [PvP](../game/pvp.md#05.B) 05.B절, [05.E절](../game/pvp.md#05.E)
- HP 기준을 높이는 것만으로 거의 동시에 들어오는 피해를 모두 막을 수는 없음

::part[구현과 확인]

## <a id="06"></a>06 자동화 요구사항

2026-10-05 공격은 수동, 자기관리는 공통 `script/combat/pvp.razor`로 변경. 실제 구현은 09절.
아래 TK, 공격 타겟, 스윙, 포션 복구 항목은 향후 자동화 검토 기준. 지금 루프의 동작 아님.

| 상태 | 요구사항 |
| --- | --- |
| TK | 자기 TK와 공격 TK의 의도, 저장한 대상 serial, 응답 대기, 실패와 만료 구분. 공통 문구와 같은 대상만으로 성공 확정 안 함 |
| Reflect | 확인 못 한 상태는 미확인 처리. 공격자에게 오지 않는 메시지를 조건으로 쓰지 않음 |
| 시전과 타겟 | 시전 중, 완료 뒤 보유, 방출, 취소 구분. 포션, 붕대, 무기 교체가 공격 타겟을 빼앗는지 확인 |
| 무기 | 실제 마지막 스윙 기준. 장착 완료나 공격 명령만으로 명중이나 Hamstring 성공 처리 안 함 |
| 우선순위 | 위험 HP, 해독, 탈출 판단이 공격 예약보다 먼저. 마나 부족이나 LOS 상실 시 콤보 중단 |
| Teleport와 Rope | 공유 쿨 표시. Rope 자동 추격 없음, 긴 이동 잠금은 알고 선택 |

- 서버가 허용하는 정보와 명령만 사용([Razor](../scripting/razor.md#07) 07절)
- TK 대상 판정, 상대 Reflect 메시지, 버프 중첩, 프리캐스트 충돌의 실험 목록: [Open items](../questions/open-items.md#08) 08절

### <a id="06.A"></a>06.A 점화한 포션의 실패 처리

포션 상태: 점화 전, 점화 후 내 포션 커서 보유, 투척 시도, 투척 뒤 결과.
투척 뒤 결과: 부착 확인, 투척 뒤 미확인, 지면 투척 시도, 상태 불명.

- 점화 뒤에는 새 공격 주문보다 포션 처리 우선. 긴급 생존 동작과는 커서 사용권 조정
- 대상이 사라져도 내 포션 커서가 남아 있으면 쓸 만한 땅에 던지는 복구 경로 마련
- 커서가 닫혔는데 부착 메시지가 없다는 이유만으로 땅 재지정 안 함. 다른 회복 커서를 쓰거나 두 번째 포션을 점화할 위험
- 땅 투척도 발밑, 이동 경로, 폭발 반경, LOS 고려 필요. 명령 전송 = 안전한 투척 아님
- 실패나 취소에도 퓨즈는 초기화되지 않는다고 보고 추가 점화 차단.
  커서 소유권, 남은 퓨즈, 지면 투척 결과가 불분명하면 경고하고 회피

`targetrelloc`의 존재 ≠ 안전한 투척 지점의 자동 선택.
실제 동작과 허용 범위는 [Razor](../scripting/razor.md#02.A) 02.A절과 [Open items](../questions/open-items.md#08.C) 08.C절의 확인 대상.

::part[기록]

## <a id="07"></a>07 Eval을 뺀 비용과 근접 한 대

실측 피해나 승률이 아닌 비교용 계산. 스킬, 상대 방어, 명중, 회복을 나눠서 봄.
Tracking 주문 보조의 결합 순서를 단정하지 않으려고 첫 표에서는 양쪽 모두 제외.

- 예시: Magery 80, 상대 Resist 100의 피해 감소 25%, 주문 기본 피해의 중간값
- `피해 예시 = 기본 피해 × 0.8 × (0.75 + 0.375 × Eval / 100) × 0.75`
- 25%는 비교용 가정, 모든 타격의 고정 저항률 아님([PvP](../game/pvp.md#08) 08절)

| 주문 | Eval 0 | Eval 100 | 차이 |
| --- | --- | --- | --- |
| MA, 기본 중간값 6 | 2.70 | 4.05 | 1.35 |
| Explosion 또는 EB, 기본 중간값 32 | 14.40 | 21.60 | 7.20 |
| Explosion + EB | 28.80 | 43.20 | 14.40 |

- 같은 Magery면 이 모델에서 Eval 100 = Eval 0의 1.5배. 차이 없음이 아님
- Magery 100, Eval 100 메이지와 비교하면 1.875배. 둘 다 다른 보정 제외

근접 예시: 일반 무기, Tactics 100, Anatomy 80, 도끼 보조 상한 20%, 상대 AR 50. Parry, Reactive Armor, 추가 장비 보정 없음.
`피해 = 무기 기본 피해 × (1 + 0.16 + 0.20) × (1 − 방어구 감소율)`. AR 감소식은 [PvP](../game/pvp.md#09.E) 09.E절.

| 무기 | 명중했을 때 계산 범위 | 기본 피해와 감소율 중간값의 예시 | 명중률 50%를 곱한 스윙당 예시 |
| --- | --- | --- | --- |
| Great Axe | 19.05\~52.14 | 34.18 | 17.09 |
| Norse Axe | 11.79\~26.07 | 18.37 | 9.18 |

- Alchemy 0의 Greater Explosion 포션 15\~25 포함 시, 포션과 Great Axe 한 대와 Norse Axe 한 대가 모두 맞은 합은 약 45.84\~103.22
- 상대 회복, 추가 방어, Splashback, 빗나감, 접근 실패 제외. 확정 콤보 피해나 DPS로 쓰지 않음
- 상대가 Inscription 100의 Reactive Armor를 유지하고 남은 방어량도 넉넉하면 위 근접 중간값에 0.75 추가 곱 → Great Axe 약 25.64, Norse Axe 약 13.77
- 방어량이 도중에 바닥나는 타격까지 이 감소율이 그대로라고 가정하지 않음([PvP](../game/pvp.md#05) 05절)
- 이 예시에서는 **더 맞힌** 근접 한 대가 Eval로 늘어나는 두 주문의 차이를 넘을 수 있음
- 단, 명중과 접근은 보장 없음. Eval 100을 얻으려면 다른 스킬 100점 제외 필요
- 두 빌드 모두 원래 때릴 한 대를 한쪽에만 더해 유리하다고 계산하지 않음

::part[채집]

## <a id="08"></a>08 lumberjack-enhanced

대상: `script/gather/lumberjack-enhanced.razor`. 옛 `lumberjack.razor`는 구버전 보존(2026-10-10부터 `script/archive/`).
채집 루프와 PvP 자기관리 루프는 핫키를 따로 두고 수동 전환. 자동 공격과 자동 PvP 전환 없음.

### <a id="08.A"></a>08.A 실행 흐름

1. 설정, 타이머, 상태 초기화. 레시피에 `escape/tracking`이 있고 Tracking 스킬이 있으면 시작 시 Tracking 준비.
   같은 클라이언트 세션에서 확인한 색으로 Hunting이 켜져 있으면 그대로 재사용.
   첫 실행은 지금 창의 색을 읽고, 바꿀 때만 Hunting을 끈 뒤 필터 전환. 리콜 설정과 무관, 기본 필터 red
2. 루프는 마비 해제, 해독, 붕대, 포션, 주문 회복 먼저.
   그 뒤 생존, 자동 리콜, 시약, Hatchet 확인과 Smart Harvest, 자기 버프, 음식, 목재 정리 순서.
   v18부터 음식과 목재 정리는 housekeeping 주기 없이 각자의 타이머를 패스마다 확인. 집 문과 Stockpile 기능 삭제.
   블록 이름과 순서의 정본은 `recipe/lumberjack-enhanced-recipe.razor`, 모듈 구성은 [Modules](../scripting/modules.md#02) 02절
3. 생존 바로 뒤 `RECALL`(`escape/recall`)이 리콜 관련 일을 한곳에서 처리. Tracking 감지, 책, 무게, 요청, 실패 응답.
   자동 리콜을 안 쓰려면 레시피에서 이 블록을 빼고 재조립 → 감지나 책 때문에 채집이나 자기 버프를 멈추지 않음
4. 리콜이 필요해지면 같은 패스부터 채집, 목재 정리, 준비 버프 보류, 회복은 계속. v18부터 음식은 리콜 결정과 무관하게 먹음.
   `RecallCharge Home`은 실제 Recall 주문 요청. Moongate 동작 없음.
   요청은 실행마다 한 번, 명령 전송 = 도착 아님. 싸우려면 사용자가 PvP 스크립트로 전환
5. 서버가 보내는 Tracking, 저장, 채집 결과와 채집 거절 안내는 프로필 오버헤드가 표시.
   리콜 전송 뒤의 실제 거절 문구는 같은 리콜 블록이 안내.
   시약 부족 메시지는 리콜 감지 뒤에 읽고, 같은 패스에서 시약 재확인
6. `util/check.sh script/gather/lumberjack-enhanced.razor`, `node util/check-docs.mjs`, `git diff --check` 실행,
   두 프로필의 XML과 오버헤드 변경 범위 확인. 아래 인게임 확인 항목은 이 정적 검증과 별개

### <a id="08.B"></a>08.B 채집 근거

> Lumberjacking always uses Smart Harvest

- [공식 Lumberjacking 문서](https://wiki.uooutlands.com/Lumberjacking): 장착한 Hatchet 더블클릭 → 주변 나무 채집
- [공식 Smart Harvest 문서](https://wiki.uooutlands.com/Smart_Harvest): 도구 사용 뒤 자신이나 상태바를 타깃하는 경로

#### 지금 동작

- 손의 Hatchet 확인 → `Use item in hand`, 커서 대기, `Target Self` 순서로 채집. 이미 수동으로 연 커서가 있으면 새 채집 시작 안 함
- 빈손: `lhandempty` 먼저 확인 → 저장한 `var__my_hatchet`을 백팩에서 찾아 `lift`, `drop self lefthand`로 장착.
  방식은 [bard-mace](https://github.com/minu-ha/uoo/blob/master/script/archive/bard-mace.razor)를 따름
- 장착 다음 시도에서는 `findlayer self lefthand`의 serial이 저장한 도끼와 같을 때만 사용.
  검색 성공이나 장착 요청만으로 실제 장착으로 보지 않음
- 다른 왼손 장비만 비움, 오른손 무기는 수동 장비 핫키 담당
- 주변 나무는 Smart Harvest가 선택 → 나무별 검색 없음
- 공식 문구만으로는 요청 한 번이 나무가 다할 때까지 계속 도는지 확정 불가. 기본 재시도는 커서 처리 뒤 4초
- 주변 채집 자원 없음 응답 → 다음 시도만 2초 뒤(v15). 그다음 요청부터 기본 간격 복귀.
  이 응답은 Tracking과 리콜 감지 뒤에 읽음. 대기 중에도 회복 루프, 수동 입력 차단, 리콜 차단 조건은 그대로

Hatchet은 [공식 무기 표](https://wiki.uooutlands.com/Template:SwordsWeaponClass)에서 2H.
[UO의 양손 장비 레이어는 0x02](https://github.com/ServUO/ServUO/blob/pub57/Server/Item.cs),
[Razor의 이름은 LeftHand](https://github.com/markdwags/Razor/blob/master/Razor/Core/Item.cs).

#### 확인 상태

- v8 기본 채집: 사용자가 정상 작동 보고. 인게임 확인됨 2026-10-05
- v13 END와 그 뒤 채집 응답: 사용자 Journal에서 확인. 인게임 확인됨 2026-10-05
- v10 빈손 장착과 serial 확인 경로: 아직 확인되지 않았다
- 목재 이동 전체 완료 여부, v14 파우치 제외: 아직 확인되지 않았다

#### 바뀐 경위

- v4: 도구 사용 뒤 커서만 남는 화면 보고. v5에서 옛 `lumberjack.razor`의 `Use item in hand`, 커서 대기, `Target Self` 순서 도입
- v7: 이 클라이언트에서 `dress serial` 실패 보고 → `lift`, `drop self lefthand`로 장착, 다음 시도에서 손 재확인
- v9: 빈손인데 백팩 Hatchet을 장착하지 않는다는 사용자 보고. 인게임 확인됨 2026-10-05.
  `findtype … self`의 실제 검색 범위나 실패한 가드까지는 미확인 → `lefthand` 문법 오류로 단정하지 않음
- v10: 지금의 `lhandempty` 확인과 serial 비교 경로 도입

> they will have a 60 second delay before they can attempt to Harvest again

- 같은 문서: Recall, Moongate, Hike 뒤 채집 제한 60초, Teleport와 Rope에도 적용. **60초는 확인된 서버 규칙**
- 단, 스크립트가 이동 성공 시각이나 서버 잔여 시간을 읽을 수 있는지는 별개
- 이동 거절 안내는 두 프로필이 `[ harvest, wait ]`로 표시, 스크립트의 별도 조회 없음
- 4초는 채집 명령 재시도 간격일 뿐, 서버 60초 제한을 줄이거나 대신하지 않음
- 거절 안내 시점부터 60초를 새로 세는 타이머 없음. 매핑은 [Overheads](../scripting/overheads.md#07) 07절

### <a id="08.C"></a>08.C 기본값과 상태

구조 요점:

- 도끼 상태는 `var__my_hatchet` 하나, 장착 여부의 equipped 플래그 없음.
  장착 판정 = 실제 왼손 슬롯 serial과 저장한 도끼 serial의 일치. 오른손 제어 없음
- 도구 사용, 커서 대기, 자기 타깃은 채집 블록 하나에서 완료. v8 경로와 pending 없는 구조 유지
- 목재 가공과 파우치 이동에도 별도 처리 단계나 pending 상태 없음
- Tracking 시작 설정과 자동 리콜 판정은 분리 유지
- 채집 허용 캐시나 숫자 단계 대신 실제 정지 조건과 리콜 상태의 뜻을 코드에 직접 기록
- 변수 이름은 공통 접두 `config__`, `var__`, `timer__`
- 클라이언트에 옛 session 변수나 persistent 변수 값이 남아 있어도 이 스크립트는 읽지 않음

#### 설정

- **`config__chatty`, `config__sysmsg`**: 각 1. chatty = 선택 가능한 스크립트 오버헤드, sysmsg = Journal 진단(시작 버전, 리콜 원인, 도끼 장착 요청, 목재 정리).
  따로 끌 수 있음. 부족과 차단 경고, 프로필이 표시하는 서버 사건은 둘 다 꺼도 남음
- **`escape/recall` 블록**(v17까지 `config__auto_recall`): 레시피의 `#@ use escape/recall`.
  빼고 조립하면 감지 메시지, Hunting 점검, 책, 여유 무게, 실패 응답 조회 전부 없음.
  `var__hold_gathering`을 세우는 블록도 없어서 책이나 Hunting 때문에 채집 보류 없음.
  시작 시 Tracking 설정과 프로필 화면 표시는 남음. 가까운 red 때문에 채집이나 자기 회복을 멈추지 않음
- **`config__recall_on_detection`, `tracking_color`, `show_tracking`**: 1, 1, 0. 시작 설정은 레시피의 `escape/tracking`(v17까지 `use_tracking`).
  Tracking 스킬 0이면 건너뜀. 색 값: 1 red, 2 grey, 3 orange, 4 세 그룹 전체. 설정은 시작 시 한 번.
  감지 리콜은 `recall_on_detection` 1이고 Hunting을 확인한 경우에만. 적 발견 → 다음 패스부터 채집과 준비 버프 보류, 리콜 요청
- **`config__recall_at_any_distance`**: 0. 기본은 기존처럼 1\~45 steps 분기에서 리콜 필요 여부 기록.
  1이면 준비된 필터의 발견 문구만으로 리콜 요청. 화면 알림은 프로필 담당
- **`config__recall_on_weight`, `weight_remaining`, `require_runebook`**: 1, 10, 1. 리콜 블록이 있으면 남은 무게 10 이하에서 리콜 필요 기록.
  책 보유 여부는 5초 주기 캐시. 마지막 설정 = 책이 없을 때 채집 보류 여부.
  0이어도 실제 리콜에는 책 필요. 책 검사는 충전량이나 Home 룬 유무까지 보지 않음
- **`config__heal_hits`, `emergency_hits`, `light_hits`, `use_light_heal`**: 잃은 HP 35, 45, 15와 0.
  평소 붕대, 35부터 힐 포션, 45부터 Greater Heal 보조. 붕대를 못 쓰면 15부터 Smart Heal/Cure 대체 시도.
  v16부터 `use_light_heal` 1이면 붕대와 병행. 독이면 Cure 포션과 해독 주문 먼저.
  v17부터 이 회복은 pvp와 같은 `recovery/` 모듈([Modules](../scripting/modules.md#02) 02절). 워모드의 회복 주문 정지 규칙은 `warmode_is_manual` 1로 유지
- **`config__use_reactive_armor`, `use_magic_reflect`**: 각 1. 리콜 불필요하고 안전할 때 마나 24, 34부터 각각 시전.
  시작 마나는 레시피의 `config__mana_reactive_armor`, `config__mana_magic_reflect`.
  준비 버프 뒤에도 GH와 Teleport 마나 예산 20을 남기려는 값. 근거는 [Item list](../game/item-list.md#19) 19절과 이 문서 04절
- **`config__use_potions`**: 1. 독, 피해, 스태미나에 Cure, Heal, Refresh 포션. 리콜 준비용 Strength와 Agility 포션과 그 옵션은 삭제
- **`pack/lumber` 블록**(v17까지 `config__pack_lumber`): 레시피의 `#@ use pack/lumber`. Logs 가공과 Boards 파우치 이동을 한 묶음으로.
  빼고 조립하면 정리 없음. `loadout`에서 고른 `global__my_looting_pouch` 재사용, 없거나 백팩에 없으면 시작 시 파우치 선택.
  Logs 7133, Boards 7127은 [Item list](../game/item-list.md#15) 15절 값, 색 구분 없음.
  가공은 [공식 Lumberjacking 문서](https://wiki.uooutlands.com/Lumberjacking)의 Logs 더블클릭 경로

- 짧게 적은 설정 이름도 실제 파일에서는 모두 `config__` 접두
- 나머지 설정: 스태미나 15 이하의 Refresh, 출력 빈도. Hatchet 하나로 채집, 예비 수량 검사 없음

#### 채집을 미루는 조건

- 빈손 장착은 남은 무게를 기다리지 않음. v18부터 `var__hold_gathering` 1이면 장착과 채집 함께 보류
- `var__hold_gathering` 1이 되는 경우: 리콜 결정, 책 필수인데 없음, 감지 리콜인데 Hunting 없음
- 회복과 수동 입력 가드도 장착과 채집에 함께 적용. 리콜 블록이 없어도 실제 남은 무게 0 이하면 채집 보류
- 채집 직전 `if / elseif / else` 사슬로 정지 사유를 차례로 확인. 손의 도끼, 남은 무게, 수동 입력 중 하나라도 준비 안 되면 보류
- 책과 Hunting 조건은 v18부터 이 사슬에서 제외. 리콜 블록이 패스마다 리콜 결정과 함께 `var__hold_gathering` 하나로 합치고, 채집 블록은 맨 앞 조건에서 그 값만 읽음
- 차단 조건을 모두 통과하면 도구 사용, 커서 대기, 자기 타깃을 같은 블록에서 처리
- `require_runebook` 0이면 책 조건, `recall_on_detection` 0이거나 Tracking 스킬 0이면 Hunting 조건 건너뜀. 리콜 블록을 빼면 둘 다 없음
- 건강, 남은 무게, 수동 입력 조건은 이와 별도로 통과 필요
- `and`만 이어진 조건은 합칠 수 있음. `or` 예외까지 한 줄에 섞지 않음. 이 포크에서 괄호를 쓴 확인된 선례 없음
- CE 원본은 섞인 논리 연산을 왼쪽부터 평가([CE Interpreter의 EvaluateLogicalExpression](https://github.com/markdwags/Razor/blob/master/Razor/Scripts/Engine/Interpreter.cs)).
  Outlands에서 연산자 우선순위를 새로 검증한 것은 아님. 채집 가능 여부를 저장하는 상태는 없음

#### Tracking 필터 색

- red = Tracking의 Murderer Players, grey = Criminal Players, orange = Enemy Players
- grey는 범죄자 필터 이름일 뿐, 회색 대상 전부를 따로 검색하는 기능 아님
- 전체 선택 = 서버의 All Hostile Players 필터. grey와 orange 확인 문장의 서버 일치 여부는 인게임 확인 대상
- 추적 화면 표시는 [Overheads](../scripting/overheads.md#07) 07절의 프로필 매핑

#### 상태와 타이머

- **`var__recall_needed`**: 0 = 채집 계속, 1 = 리콜 필요. 감지나 여유 무게 부족으로 1이 되면 재실행 전까지 유지.
  1이면 리콜 블록이 같은 패스에 `var__hold_casts`와 `var__hold_gathering`을 1로 두어 준비 버프, 채집, 목재 정리 정지
- **`var__recall_sent`**: 0 = 미전송, 1 = RecallCharge 전송. 회복 루프가 도는 동안 같은 요청과 리콜용 재검색 차단.
  실패해도 1 유지, 새 요청은 재실행 필요. 명령 전송 = 도착 아님
- **`var__recall_book_available`**: 리콜 책 보유 캐시. 초기값 0을 첫 패스의 채집 전 점검이 갱신, 이후 리콜 블록의 5초 점검 주기.
  책 필수인데 0이면 `var__hold_gathering`이 채집 정지. 요청 직전 책 재확인.
  그때 책이 없으면 캐시를 0으로 바꾸고 다음 점검까지 검색 보류
- **`var__tracking_filter_confirmed`, `tracking_hunting_active`, `tracking_button_answered`**: 설정 색의 서버 확인 여부, 최근 확인한 Hunting의 켜짐 여부, 지금 필터 버튼의 응답 여부.
  필터와 버튼 상태는 시작 설정용. 루프의 Hunting 점검은 감지 리콜이 켜져 있고 아직 리콜 미결정일 때만.
  감지 리콜인데 Hunting이 아니면 리콜 블록이 `var__hold_gathering`으로 채집 정지
- **`var__tracking_setup_color`**: 같은 클라이언트 세션에서 확인한 색 값. Hunting이 켜져 있고 config 색과 같으면 시작 설정 재사용.
  버프만으로는 색을 알 수 없음 → 첫 실행은 창이나 서버 응답으로 확인. 필터를 수동으로 바꿨으면 Hunting을 끈 상태로 재실행.
  클라이언트 종료 시 캐시 소멸
- **`wait__harvest_target`**: 3000ms. 손 도구 핫키 직후 `waitfortarget`으로 커서를 기다리는 한도.
  같은 채집 블록에서 중립 커서를 `target self`로 처리 → 대기 중 다른 자동 행동 끼어들기 없음.
  도구 큐가 남아도 자기 타깃 생략 안 함. 새 수동 시전, 숨기, warmode, 다른 종류의 커서는 처리 안 함.
  시간 초과로 커서가 없으면 자기 타깃 미전송, 다음 시도 간격은 이 블록 종료 뒤부터 계산
- **`var__recall_check_due`, `regs_*`, 시약별 보유 변수**: 이번 패스가 리콜 블록 5초 점검 차례인지, 주문별 시약 조합.
  v18에서 housekeeping 주기(`var__housekeeping_pass`) 삭제. 리콜의 책, Hunting, 무게 점검은 이 값으로 채집 전에, 음식과 목재 정리는 루프 끝에서 각자의 타이머로.
  시약은 `magery/reagents`가 10초마다, 부족 안내를 읽은 즉시 재확인. 그 블록은 자동 리콜 뒤 → Tracking 줄을 먼저 읽음
- **`interval__harvest_retry`, `interval__harvest_out_retry`, `var__harvest_retry`**: 기본 재시도 4000ms, 주변 자원 없음 응답 뒤 재시도 2000ms.
  `var__harvest_retry` = 다음 시도에 쓸 간격. 처음과 각 시도 직후는 기본값, 자원 없음 응답을 읽으면 짧은 값.
  응답을 읽은 시각에 기존 `timer__harvest`를 0으로 되돌리고 새 간격과 비교. 별도 타이머나 2초짜리 wait 없음.
  수확 성공, 실패, 여행 제한, 채집 불가 응답은 기본 간격 유지. 이 새 경로는 아직 인게임에서 확인되지 않았다
- **`var__my_hatchet`, `wait__equip`**: 고른 도끼 serial 하나, 장착 뒤 1000ms 대기. 초기값 0, Stop과 Play 사이에 재사용.
  왼손이 비었는데 캐시한 도끼가 백팩에 없으면 3907, 3908로 재검색. 이 graphic 검색은 도끼 찾기 전용.
  이미 든 도끼가 캐시와 다르면 라벨을 한 번 읽고 그 serial 저장. 다른 왼손 도구면 비우고 다음 시도에서 도끼 장착.
  새 타이머 없음, 기존 `timer__harvest`로 장착 재시도와 채집을 함께 조절.
  장착 뒤 손 슬롯 serial 재확인, 캐시나 요청만으로 성공 표시 안 함
- **`var__hold_casts`, `var__hold_gathering`**: `module/base.razor`가 0으로 선언하는 블록 사이 신호([Modules](../scripting/modules.md#06) 06절).
  리콜 결정 시 리콜 블록이 `var__hold_casts`를 1로 → 자기 버프 정지.
  `var__hold_gathering`은 리콜 결정, 책 없음, Hunting 없음에서 1 → 채집과 목재 정리 정지.
  v17에서 `var__bandage_available`, `heal_spell`, `buff_cast` 삭제. 회복 블록마다 지금 상태를 읽고 바로 시전
- **`timer__recall_check`, `interval__recall_check`**: 5000ms. v18에서 housekeeping 주기 대신 리콜 블록이 쓰는 점검 주기.
  리콜 책과 무게는 명령 전송 전까지 점검. Hunting 상태는 2026-10-10부터 `escape/tracking`이 자기 5초 시계(`interval__tracking_check`)로 읽고, 리콜 블록은 결과만 확인.
  Tracking 메시지는 준비 상태면 패스마다 확인, 무게 판정보다 먼저
- **`interval__pack_lumber`, `timer__pack_lumber`, `wait__lumber_item`**: 120000ms마다 정리. 180000ms로 바꾸면 3분.
  v18부터 housekeeping 대기 없이 패스마다 이 타이머 확인. 첫 정리도 이 주기가 지난 뒤.
  입력이 비고 회복이 필요 없을 때 시작, 묶음마다 사용이나 이동 뒤 500ms 대기.
  작업 중에는 같은 타이머로 단계별 시간 계산, 정리 완료 시 0으로 되돌려 다음 2분 계산.
  가공이나 이동에 실패한 묶음과 남은 묶음은 다음 주기에 재시도. 파우치가 없을 때도 이 주기로 제한
- **`wait__lumber_batch`, `var__lumber_graphic`, `global__my_looting_pouch`**: 요청 사이마다 확인하는 단계별 작업 예산 2500ms, 지금 검색하는 graphic, 로드아웃과 공유하는 영속 파우치
  - graphic 순서 7133 Logs, 7127 Boards, 색 필터 없음. `findtype graphic backpack`에서 hue를 빼므로 같은 graphic의 모든 목재 색이 대상
  - 검색은 시간, 입력, 대상 존재 조건으로 끝나는 `while`. `for 2`는 가공과 이동 두 단계를 같은 본문으로 처리.
    `for`가 `while`보다 빠르다는 뜻 아님. 임시 스택 목록과 `foreach`는 삭제
  - v14부터 파우치 소속 먼저 확인 → 이미 넣은 Boards는 요청 없이 건너뜀.
    판별하거나 요청한 serial은 ignore → 같은 단계에서 실패한 묶음 재선택 없음.
    단계 시작과 끝에 clearignore → 영구 제외 아님. 실패한 묶음은 다음 2분 주기에 재시도
  - Boards는 가공 뒤 지금 인벤토리에서 검색. 변환과 병합 전 serial 재사용 없음
  - 별도 pending, 처리 단계 플래그, 타이머 없음. 단계 시작과 요청마다 큐가 남아 있으면 예산 안에서 대기.
    큐 대기와 검색은 조건이 거짓이 되면 정상 종료
  - 목재 블록에 break, continue, 별도 125회 검색 반복 없음. 다음 요청 전 회복, 수동 입력, 큐, 파우치, 예산 확인
  - 남은 다른 색의 Logs는 색 구분이 아니라 작업 예산 때문에 다음 주기로 넘어갈 수 있음
  - `lift`와 `drop`은 붙여서 처리. 예산은 명령마다의 대기를 포함한 절대 실행 시간 상한 아님.
    [CE lift 문서](https://www.razorce.com/guide/commands/#lift)에는 별도 기본 대기 한도 기재
- **리콜 응답 안내**: 전송 뒤 실제 서버 거절 메시지만 확인. 5초 경과 안내와 그 반복을 막는 상태 없음.
  도착 여부와 남은 채집 제한 시간 추정 없음, 거절이나 응답 지연 뒤에도 채집 자동 재개 없음
- **채집 조건과 나머지 타이머**: 채집 블록은 `var__hold_gathering`, 실제 무게 한도, 건강, 수동 입력 조건을 읽음.
  리콜 필요 여부, 책, Hunting은 리콜 블록이 그 값으로 통합. 회복, 버프, 채집 재시도, 시약과 음식 주기는 각자 유지.
  서버 저장 상태는 별도 관리 없음

- 짧게 적은 상태 이름도 실제로는 `var__` 접두
- 주기는 클라이언트의 재시도 값, 서버 잔여 시간 측정값 아님

#### 메시지를 읽는 순서

- 회복과 버프 대기는 기존 `casting`과 횟수를 정한 반복으로 처리, 끊김 메시지 별도 소비 없음
- 메인 루프는 Tracking 감지보다 앞에서 메시지를 소비하지 않음
- 시작 설정에서 Hunting을 멈추고 필터를 확인한 뒤 `clearsysmsg`로 앞선 필터와 중간 필터 메시지 비움
- 리콜 감지는 채집 전에 읽음 → 경보 발견 시 같은 패스의 채집과 정리 보류
- 채집의 3초 커서 대기나 목재 정리 중 새 경보는 다음 패스에서 읽음. 그 동작 중 계속 감지하는 것 아님
- 시약 부족은 리콜 감지 뒤에 읽고, 같은 패스에서 시약 재확인
- 목재는 가공과 이동 요청 사이마다 회복, 수동 입력, 큐 상태 재확인
- 단계별 시간 예산 종료 시 남은 목재는 다음 정리 주기로, 생존과 채집 점검으로 복귀

#### 목재 정리 뒤 채집이 멈춘 보고

- 2026-10-05 사용자 보고: 목재 가공과 파우치 이동 성공 뒤 다른 Logs가 남고 채집 정지
- 화면에 가공 성공 문구 있음, `Script Error`와 줄 번호는 확인되지 않았다
- Play 상태라는 보고만으로 오류 위치 확정 안 함
- 옛 코드: 스택을 모두 처리할 때까지 메인 루프로 복귀 안 함, `queued`가 남으면 다음 스택부터 처리 중단 조건 존재

v15부터 sysmsg 기록 순서: `Lumber pack BEGIN`, 가공과 `Lumber skip`과 `Lumber move request`, `Lumber pack END`.

- `skip: … already in pouch`: 기존 Boards를 들어 올리지 않았다는 판별 기록
- `move request`: lift와 drop 직전의 요청 기록. 서버의 이동이나 병합 보증 아님
- 같은 hue의 새 Boards가 기존 묶음에 합쳐지면 원래 파우치 묶음 serial이 남을 수 있음 → 요청한 serial 소멸 = 실패로 단정하지 않음
- 기존 파우치 묶음 자체를 다시 옮겨 합치는 로직 없음. 실제 병합 결과, 용량, 서버 응답은 인벤토리에서 확인

END 뒤에도 채집이 보류되면 큐와 커서 안내, 리콜과 책과 Hunting 조건을 함께 확인. 남은 확인은 [Open items](../questions/open-items.md#09) 09절.

#### 버전 기록

- **v10(2026-10-05)**: 장착 판정을 실제 왼손 슬롯과 저장한 도끼 serial의 일치로 변경.
  목재 가공과 파우치 이동을 housekeeping에 묶음. 책, Hunting, 무게 점검은 housekeeping 주기 사용,
  리콜 결과를 확인하지 않는 5초 안내 타이머와 그 상태는 삭제
- **v11**: 집 문과 Stockpile의 설정, 선택, 동작, 타이머 삭제, housekeeping을 루프 끝으로 이동
- **v12**: 채집 직전 네 겹 허용 조건 → 차단 조건 사슬 하나.
  채집과 목재 정리의 주기 조건을 이웃한 다른 `and` 조건과 합쳐 허용 경로의 명령문 수 감소.
  Journal 진단은 새 `config__sysmsg`로 분리, 목재 큐가 비어 있으면 대기 반복 진입 없음.
  새 상태나 타이머 없음. 명령문 비용 근거는 [Razor](../scripting/razor.md#06) 06절
- **v13**: v12 실행 화면에서 `BEGIN` 뒤 `convert`만 이어지고 다음 단계로 안 간다는 보고. 인게임 보고 2026-10-05.
  CE 원본의 명령 단위 제어 흐름 재현 결과, `if` 안의 `break`는 현재 범위를 한 단계만 제거.
  안쪽 반복문 범위가 남아 바깥 `for 2`가 첫 진입으로 판정하고 index를 0으로 되돌리는 경로 존재.
  그래서 Logs 단계와 작업 타이머가 거듭 초기화되어 Boards 단계와 END에 도달 못 함.
  v13은 목재 검색과 큐 대기를 종료 조건이 있는 `while`로 바꿔 이 블록의 `break`와 `continue` 제거.
  앞서의 Python 모의 검사는 재귀 반복이라 범위 정리 차이를 놓침.
  CE 흐름 재현 시 옛 본문은 반복, 새 본문은 END와 범위 정리까지 완료. Outlands 내부 구현이 CE와 같다는 확인은 아님.
  이후 사용자 Journal에서 v13의 가공, 이동 요청, END와 채집 응답 확인. 인게임 확인됨 2026-10-05.
  단, 두 번의 정리에서 같은 Boards serial이 이동 대상으로 거듭 기록, 사용자가 일부 미이동 보고
- **v14**: 파우치 소속 검사 전에 ignore하던 순서 수정. 공식 문서상 ignore는 검색 제외 → 판별은 ignore 전에.
  직접 serial 검색에 대한 적용은 [Razor](../scripting/razor.md#03) 03절에서 별도 확인.
  지금 포크에서 이 순서가 같은 묶음 반복 이동의 실제 원인인지는 아직 확인되지 않았다.
  근거와 재확인 범위는 [Razor](../scripting/razor.md#03) 03절과 [Open items](../questions/open-items.md#09) 09절
- **v18(2026-10-10)**: 모듈을 관심사별 폴더로 재분할하며 housekeeping 주기 삭제([Modules](../scripting/modules.md#08) 08절).
  리콜 블록이 자기 5초 주기로 책, Hunting, 무게 점검, 음식(`buff/food`)과 목재 정리(`pack/lumber`)는 각자의 타이머를 패스마다 확인.
  리콜 결정, 책 없음, Hunting 없음은 리콜 블록이 패스마다 `var__hold_gathering` 하나로 통합, 채집과 목재 정리는 그 값만 읽음.
  `config__auto_recall`, `use_tracking`, `pack_lumber` 삭제. 블록을 끄려면 레시피에서 그 블록 제외.
  음식은 skinning-enhanced와 같은 블록 → 다쳤거나 독이거나 리콜 결정 중에도 먹음. 워모드에서는 `warmode_is_manual` 1이라 안 먹음

### <a id="08.D"></a>08.D 실행 준비와 인게임 확인

1. Tracking 감지 리콜을 쓰면 Tracking 창의 Hunt Frequency를 **Always Get Closest**로.
   스크립트는 대상 필터만 맞추고 추적 빈도 모드는 그대로. 모드별 차이는 [Tracking 문서](https://wiki.uooutlands.com/Tracking)의 Hunting 항목
2. 레시피가 `escape/recall`을 쓰면 충전한 책에 `Home` 룬 준비.
   룬 이름이 다르면 `module/escape/recall.razor`의 `say "[RecallCharge Home"` 한 줄 수정 → `pnpm build`.
   명령의 뜻은 [공식 Commands 문서](https://wiki.uooutlands.com/Commands)의 RecallCharge 항목
3. Hatchet, 붕대, 시약, 포션 준비, 이 캐릭터에서 다음 핫키 동작 확인.
   `Use item in hand`, `Bandage Self`, 각 Drink 핫키, `> Smart Heal/Cure Self`, `> Greater Heal/Cure Self`, `> Interrupt`, `Cancel Current Target`
4. 백팩 안에 파우치 준비. 파우치 미지정이거나 백팩에 없으면 시작 시 `[ loot pouch, pick ]`, 한 번 선택.
   이미 `loadout`으로 정했으면 그 값 사용. 실행 중 파우치가 없으면 `[ loot pouch, out ]` 후 정리 건너뜀
5. 이 캐릭터의 `heal pot`, `walk`, `reflect` 바 확인.
   없는 바는 0으로 보임 → 이동 차단과 Reflect 재시전 제한 미준수. 설정 변경은 별도 작업

상황별 기대 동작과 실패 판정:

#### 안전한 나무 옆에서 시작, 기존 필터가 몬스터나 우호 플레이어

- sysmsg 켜짐 → `Lumberjack enhanced v18 loaded`, chatty 켜짐 → `[ lumberjack, on ]`, 이어서 기본 red 필터 확인과 Hunting 유지
- 재실행 시 확인한 색으로 Hunting이 켜져 있으면 창이나 버튼 조작 없음
- 레시피에 리콜 블록이 없어도 `escape/tracking`이 있으면 설정
- 기존 Hunting을 꺼 버리면 실패
- 감지 리콜인데 필터 확인 실패 → `[ track, miss ]`나 `[ track, check ]`, 채집 보류

#### Tracking 설정 뒤 오래 채집, Hunting 해제, 시작할 때 수동 시전

- 채집 중 Tracking 창이나 필터 버튼을 다시 건드리면 실패
- 다른 색으로 바꾸기 전에 Hunting 먼저 해제. 설정 중 곰 같은 중간 필터의 추적 문구로 리콜하지 않음
- Hunting 해제는 감지 리콜이 켜져 있을 때 다음 채집 전 상태 점검에서 채집 보류로 반영
- 리콜 블록 없음, `recall_on_detection` 0, Tracking 스킬 0 중 하나면 Hunting 때문에 채집 보류 없음
- 처음 설정을 못 마쳐도 회복은 계속. 안전해지면 재실행으로 필터와 Hunting 재확인

#### grey, orange, 전체 필터

- 2, 3, 4로 각각 재실행해 범죄자, 적대 길드, 전체 필터의 확인 문장 기록
- 고른 필터와 다르면 감지 리콜이 켜져 있을 때 채집 보류
- 감지 화면 표시는 프로필의 `[ track, … ]`

#### Hatchet 없음, 교체, 손에 다른 무기, 나무 고갈

- 손과 백팩 모두 도끼 없음 → `[ hatchet, out ]`. 하나만 있어도 수량 경고 없이 채집
- 빈손이면 무게가 가득 차도 캐시한 백팩 도끼 장착. v18부터 책 필수인데 없음, 감지 리콜인데 Hunting 없음이면 장착도 대기
- sysmsg 켜짐 → `Hatchet equip requested: stored serial=…`, 1000ms 뒤 루프 복귀
- 다음 시도에서 왼손 serial이 `var__my_hatchet`과 같을 때만 `Use item in hand`.
  장착 거절이나 캐시가 백팩에만 남았는데 채집으로 넘어가면 실패
- 다른 왼손 장비만 비움, 오른손은 수동 처리
- 같은 블록에서 3000ms 한도로 커서 대기 → 중립 커서를 `target self`로 처리. 도구 큐가 남아도 자기 타깃 전송.
  커서가 없으면 미전송, 다음 시도까지 4초
- 커서를 다음 패스에서 처리, 스크립트 전체 종료, 다음 도구 요청이 기존 커서를 덮음 → 실패

#### 자원 없음 뒤 짧은 채집 재시도

- `[ harvest, out ]`의 원문 응답을 읽고 약 2초 뒤 다음 도구 요청
- 새 장소에서 채집을 시작하면 그 뒤 요청은 기본 4초 간격 복귀. 자원 없음이 반복되면 응답마다 2초 재계산
- 여행 대기와 수확 실패는 짧은 재시도 조건 아님
- 그 2초 동안 회복 루프 정지, 또는 시전, 기존 커서, walk 바, 리콜 결정을 무시한 채집 → 실패
- 두 간격과 재시도 뒤 복귀는 모의 검사 완료. 실제 서버 응답 시각과의 간격은 아직 확인되지 않았다

#### 오버헤드와 Journal 설정 나누기

- chatty와 sysmsg의 0과 1 조합 네 가지 시험
- chatty는 lumberjack과 recall의 시작 오버헤드만, sysmsg는 진단 줄만 변경
- 둘 다 꺼도 도끼, 파우치, 시약 부족 경고와 프로필의 채집 결과는 유지

#### 일반 목재와 특수 목재의 가공, 파우치 이동

- 실행 2분 뒤 일반 Logs와 특수 Logs가 Boards로 바뀌고 고른 파우치로 이동
- 기존 Boards와 합쳐진 묶음도 이동. 이미 파우치에 있던 Boards를 다시 들면 실패
- 가공 실패나 파우치 용량 부족은 묶음마다 한 번만 요청, 다음 주기까지 대기
- 주기 미도래, 기존 커서, 시전, 피해, `var__hold_gathering`(리콜 결정, 책 없음, Hunting 없음) → 정리 안 함
- 도중에 수동 입력이나 회복 조건이 생기면 다음 묶음 전 정지, 기존 커서는 그대로
- sysmsg 켜짐 → Lumber pack BEGIN, convert와 skip과 move request, END 출력 후 채집 재개 확인
- 파우치 안 Boards는 skip만 기록하고 이동 안 함. 다음 주기에도 새로 생긴 백팩 Boards만 이동 요청
- 같은 hue는 합쳐지고 다른 hue는 따로 남는지, 실패한 이동을 다음 주기에 재시도하는지 인벤토리와 함께 확인
- 시간 예산 때문에 남은 묶음은 다음 정리 주기에 처리
- BEGIN 한 번 뒤 convert, move, END 순서. 목재가 없는 단계는 그 요청 없이 END까지
- END가 없으면 마지막 serial, Script Error, Line 번호 기록

#### 채집 성공, 실패, 추가 수확, 스킬 안내

- 로그 획득 시 두 프로필이 `[ lumber, logs ]`나 `[ lumber, dullwood ]`처럼 목재 종류 표시. `You chop some` 한 항목이 문장의 네 번째 단어를 받음
- 수확 실패 `[ lumber, miss ]`, 두 배 수확 `[ harvest, double ]`
- 스킬 확률과 실제 상승은 서로 다른 안내
- 스크립트가 같은 결과를 또 띄우면 실패
- 검색어, hue, 숫자 자리의 정본은 [Overheads](../scripting/overheads.md#07) 07절

#### 독, 보통 피해, 큰 피해, 포션과 붕대와 시약 부족

- 채집보다 해독과 회복 우선
- 부족 시 `[ cure pot, out ]`, `[ bandage, out ]`, `[ heal pot, out ]`
- 시약은 첫 패스, 그 뒤 10초마다, 부족 안내를 읽은 즉시 재확인
- 포션 재사용 불가 동안 반복 복용, 또는 붕대 진행 중 새 붕대 연속 사용 → 실패

#### 수동 프리캐스트, 폭발 포션 커서, warmode, 이동

- 기존 커서를 채집이 자기에게 보내지 않음
- warmode에서는 채집과 자동 주문 보류
- 자체 회복이나 채집 커서 대기 중 수동 입력이 겹치는 경우는 별도 시험
- 요청 전 기존 커서는 피하지만, 대기 중 입력이 겹쳤을 때 커서 소유권을 증명하는 장치는 없음

#### red 46 steps와 45 steps, 거리가 든 발견 문구, 채집 거절 안내가 함께 도착

- 기본 설정: 46 steps에서는 리콜 안 함, 45 steps에서 리콜 필요 기록
- 화면의 추적 안내는 프로필 담당
- 채집 전 감지한 같은 패스부터 채집 보류
- 시약 부족이나 시전 끊김 안내가 함께 와도 감지를 놓치지 않는지 확인

#### 리콜 블록 없음, 책 없음, 남은 무게 1\~10, 가까운 red

- 레시피에서 `escape/recall`을 빼고 조립했는데 책이나 여유 무게 때문에 채집 보류나 RecallCharge 요청 → 실패
- Tracking 시작 설정은 `escape/tracking`이 있으면 실행
- 루프에서 리콜용 버프나 감지 메시지 조회, 또는 가까운 red 때문에 채집이나 자기 버프 정지 → 실패. 화면 안내는 유지

#### 리콜 허용, Heat of Battle, 마나 부족, 룬 없음, 늦은 응답

- 요청 시 `[ recall, on ]`, 읽은 서버 거절은 `[ recall, blocked ]`, 마나 부족은 `[ mana, low ]`
- sysmsg 켜짐 → `Recall trigger: Tracking report`나 `Recall trigger: spare weight`로 요청 사유 기록
- 집 접근 거절 문구도 실제 서버 거절로 안내. Home 룬의 위치와 접근 권한은 사용자 확인
- Heat of Battle 버프만 보고 명령 전송 전에 차단 → 실패. 실제 서버의 허용과 거절을 따로 기록
- 시간 경과만으로 결과 안내 없음
- 전송 뒤에도 회복은 계속, 채집은 재실행까지 보류. 실제 도착은 화면으로 확인
- 같은 실행에서 Recall 재요청, 또는 준비용 Strength, Agility 포션 복용 → 실패
- 요청 직전 책을 빼면 다음 5초 점검까지 재검색 보류하는지도 확인

#### 무게 리콜 켬과 끔, 실제 무게 한도, 여행 직후

- 무게 리콜 켬(기본) → 다음 채집 전 5초 점검에서 `[ weight, low ]` 뒤 채집 정지와 리콜 요청. 끄면 여유 조건으로는 정지 없음
- 실제 남은 무게 0 이하면 채집 보류
- 여행 거절은 두 프로필이 `[ harvest, wait ]`로 표시. 서버는 실제 이동 뒤 60초 동안 채집 차단.
  스크립트의 4초 재시도로 이 제한이 풀리지 않음. 거절 안내 시점부터 60초를 새로 세는 동작 없음
- 주변 자원 없음 `[ harvest, out ]`, 나무 소진 문장 `[ wood, out ]` → 다음 장소로 이동
- 채집 불가도 프로필이 한 번 표시. 스크립트가 같은 알림을 또 띄우면 실패

#### 음식(v18)

- Food Satisfaction이 없으면 60초마다 백팩의 tray를 한 번 먹음
- v18부터 다쳤거나 독이거나 리콜 결정 중에도 먹음, 워모드에서는 안 먹음
- 버프가 있는데 먹거나, 먹는 동작이 기존 커서, 시전, 큐를 덮으면 실패

#### 서버 저장 안내

- 저장 시작과 완료 알림은 기존 프로필 담당. 스크립트에는 저장 상태나 저장 문구에 따른 정지와 재개 분기 없음

#### 확인 상태와 반영

- Heat of Battle 이동 제한 정본은 [PvP](../game/pvp.md#01) 01절
- 2026-10-05 확인한 공식 문서는 Recall도 차단한다고 설명. 이번 변경은 버프를 보고 미리 막던 스크립트 동작의 삭제일 뿐, 서버의 Recall 허용 판정 아님
- 정적 검사로는 게임 응답과 커서 소유권 증명 불가. 위 동작은 아직 인게임에서 확인되지 않았다
- 후속 확인은 [Open items](../questions/open-items.md#09) 09절
- 반영은 [Workflow](../working/workflow.md#04.A) 04.A절. Scripts 탭 Reload all scripts 뒤 Play로 반복 확인, 외부 파일 수정 뒤 핫키 실행이면 클라이언트 재시작
- 게임 종료 뒤 `git status --short`로 Razor가 덮어쓴 파일 확인

::part[필드 PvP]

## <a id="09"></a>09 공통 pvp의 마법, 무기, 붕대 설정

[combat/pvp.razor](https://github.com/minu-ha/uoo/blob/master/script/combat/pvp.razor)의 독립 옵션으로 공통 [PvP 자기관리 루프](../game/pvp.md#05.E) 사용.
채집 루프를 멈추고 `Play Script: combat\pvp`에 연결한 별도 핫키로 전환.
템플릿별 PvP 파일과 프리셋 분기는 삭제. 설정은 레시피 `recipe/pvp-recipe.razor` 하나에서.

### <a id="09.A"></a>09.A 수동 공격, 자동 회복과 장착

- 수동: Q 대상 선택, Tab, 근접 공격 요청, Hamstring, MA와 Harm, TK, 폭발 포션, Teleport, Rope
- 없음: 상대 noto 필터, 거리 검색, 사망 조회, 공격 재요청. 서버에 이미 남은 자동공격과 반격은 사용자 제어
- 자동: 자기 파우치, 큐어, 힐, Refresh, Strength와 Agility 포션, Healing이 있으면 붕대, 큰 피해의 GH, 해독과 붕대 부족 때의 Heal
- 무기 옵션 켬 → 시전과 커서가 없을 때 스윙 바를 읽고 Great Axe나 Norse 자동 장착
- 준비된 무기와 빈손 재장착 순서는 공통 문서 [PvP](../game/pvp.md#05.E) 05.E절. 무기를 들어도 새 공격 요청 없음
- Warmode나 상대 선택과 무관하게 자기 상태만 확인
- 평소엔 수동 시전과 커서를 기다림, 준비된 긴급 회복은 수동 주문을 끊고 먼저 사용
- HP 가득일 때 다음 붕대 준비용 자기 MA는 수동으로 남김. 기준과 입력 경합의 한계는 공통 문서 05.E절

### <a id="09.B"></a>09.B 독립 설정

- 마법과 붕대: `config__use_magery`, `config__use_bandages` 기본 1. 무기 교체: 레시피의 `fight/weapon-swap` 블록
- 지금 pvp에는 셋 모두 포함. Magery 없는 템플릿은 Magery만 0
- 회복 마나와 자원 절약 → RA, Reflect, Resist 포션 중 불필요한 옵션을 각각 0
- 시폰용 자기 MA와 버섯 자동화는 안 씀. pvp 레시피에 `buff/mushroom` 없음, `buff/spells`의 `use_spell_siphon`은 기본 0 그대로
- 한 기능을 바꿔도 다른 기능의 설정은 그대로
- 이 도끼 조합: `swing 4`에 Great Axe, `swing 1`에 Norse Axe
- 바 시간은 지금 STA로 낸 [03절 계산](#03)과 비교해 쓰는 클라이언트에서 조정
- 빠른 스윙 때문에 큰 한 방의 시점이 밀릴 수 있음. 그 시점을 수동으로 고르려면 무기 옵션 끔
- 슬롯 ID, 충돌 장비 해제, 회복 임계값, 상태, 타이머의 정본은 공통 문서 05.E절

### <a id="09.C"></a>09.C 인게임 반영과 확인

- `recipe/pvp-recipe.razor`의 설정 수정 → `pnpm build`로 루프 재생성. 생성된 루프의 CONFIG 직접 수정 금지
- Stop, Reload all scripts, `pvp` Play 순서로 `PvP sustain v9 loaded` 확인
- Q로 alt를 골라도 자동 공격이나 자동 TK 없음. 피해와 독에는 자기 회복 동작
- 지금 본문(v9)은 아직 인게임에서 확인되지 않았다
- 수동 프리캐스트, 회복, 무기 교체, 옵션, 정지 조건별 예상 알림과 실패 판정: [Open items](../questions/open-items.md#10) 10절
- 외부 수정 뒤 기존 핫키로 실행하면 [Workflow](../working/workflow.md#04.A) 04.A절대로 재시작해 옛 캐시 정리
- 게임 종료 뒤 `git status --short`로 덮어쓰기 확인
