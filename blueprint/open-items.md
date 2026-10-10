---
name: Questions
label: 확인할 것
group: Records
order: 10
---

작업하면서 사용자에게 물을 것으로 남긴 것을 한곳에 모았다. 스크립트나 설정을 바꿔야 하는 것, 출처가 없는 숫자, 해석이 갈리는 규칙이다.
답이 정해지면 그대로 반영하고 이 문서에서 지운다.

## <a id="00"></a>00 한눈에

표마다 마지막 열이 물을 것이다. 답은 "01 drain: 지운다"처럼 절 번호와 항목 이름으로 알려 주면 된다.
새로 물을 것이 생기면 여기에 더한다 ([workflow.md](workflow.md#03) 03절).

먼저 답이 필요한 것은 다음과 같다.

1. **다섯 캐릭터의 옛 `cooldowns.xml`** (01절). 그 캐릭터로 스크립트를 돌리면 바를 하나도 못 읽는다.
2. **뜨지 않는 바 14개** (01절). 지우든 트리거를 달든 정해야 바 목록이 실제와 같아진다.
3. **자기·수신 TK에도 켜지는 target 바** (08.B절). 내 공격 TK 성공을 잘못 판단해 포션을 점화할 수 있다.

::part[스크립트 · 설정]

## <a id="01"></a>01 쿨다운 바

| 바 | 지금 | 정할 것 |
| --- | --- | --- |
| nomeehej 말고 다섯 캐릭터의 `cooldowns.xml` | 옛 22항목 형식이다 (`mushroom`, `CorpseSkin` 같은 이름). 지금 이름을 읽는 스크립트는 그 캐릭터에서 바를 찾지 못한다 | nomeehej 파일로 맞출까 |
| `pain spike` `necrosis` `noble sacrifice` `holy light` `poison strike` `curse` `mass curse` `spyglass` `divine fury` `consecrate weapon` `spam` `crew heal` `quest` | 트리거도 없고 세우는 스크립트도 없어서 뜨지 않는다 ([overheads.md](overheads.md#06.C) 06.C절) | 지울까, 트리거 문장을 달까 |
| `drain` | 트리거가 머리 위 메시지 "MV ON" 하나인데 이 메시지를 띄우는 곳이 없다 | 지울까, 다른 트리거를 달까 |

## <a id="02"></a>02 머리 위 메시지

규칙은 [overheads.md](overheads.md)에 있다. 아래는 그 규칙과 어긋난 채 남은 줄이다.

| 규칙 | 지금 | 정할 것 |
| --- | --- | --- |
| 22자 상한 ([overheads.md](overheads.md#02) 02절) | `[ magic arrow, target ]` 23자 (프로필), `[ trapped pouch, moved ]` 24자와 `[ alch satchel, moved ]` 23자 (loadout) | 줄일까. `magic arrow`는 줄이지 않는다는 규칙과 부딪힌다 |
| 대상 위에 띄우는 줄은 1288 ([overheads.md](overheads.md#01.C) 01.C절) | moongate의 `[ moongate, set ]` 290은 게이트 위에, archive/backstab-mugging의 `[ range, out ]` 254는 lasttarget 위에 뜬다 | 1288로 바꿀까, 예외로 적을까 |
| 한 대상에 한 낱말 ([overheads.md](overheads.md#04) 04절) | loadout의 `[ pouch, moved ]`는 looting pouch 줄인데 글로서리는 `pouch`를 트랩 파우치에 쓴다 (`loot pouch`가 맞다). `[ omen, target ]` (프로필)과 `[ evil omen ]` (스크립트), `[ herding, done ]`과 글로서리의 `herd`, 바 `cannons`와 `[ cannon, out ]`도 갈린다 | 어느 쪽으로 맞출까 |
| 대상만 쓰는 줄은 시전 ([overheads.md](overheads.md#05) 05절) | 프로필의 `[ swing ]` 90은 대상만 쓰는데 시전이 아니다 | `[ swing, on ]`처럼 상태를 붙일까 |
| 고르라는 줄은 `pick` 55 | refill-runebook의 `[ chest, set ]`과 loadout의 `[ loot pouch, set ]`은 대상을 고르게 하는 줄인데 `set` 90이다 | `pick` 55로 바꿀까 |
| 글로서리 낱말 | `gheal` `invis` `tp`를 쓰는 줄이 없다 | 예약어로 둘까, 지울까 |

## <a id="03"></a>03 캐릭터와 핫키

| 무엇 | 지금 | 정할 것 |
| --- | --- | --- |
| indian angus bot | 배치를 따르지 않는다. 이동이 화살표 키이고 매크로는 ClassicUO 기본 세트다 (F1 Guards, F2 bank, 4 all stay, 6 Circle Trans). `chars.lst`에도 없다 | 예외로 두는 캐릭터인가 |
| `Shift`+휠 | 아군 순환이 Shift 층의 정의 ("밖으로 던지는 것", [hotkeys.md](hotkeys.md#02.A) 02.A절)와 어긋난다 | 일부러 둔 예외인가 |
| 가장 가까운 플레이어 타겟 | "서버가 막아 놨다" ([hotkeys.md](hotkeys.md#04) 04절)에 출처가 없다 | 맞다면 PvP 제약이니 [razor.md](razor.md#07) 07절로 옮길까 |
| "C and a click" | bard-necro-pvp 주석에 있던 말이다. 어느 바인딩과도 맞지 않아 (summoner의 `C`는 All Guard Me) "Q or Shift+X/C"로 고쳤다 | 원래 뜻이 있었나 |
| 저장소 밖 파일 | L 이름과 `Razor_lang.enu` (hotkeys 05절), Wine `user.reg` 키 이름 (01절), Clumsy subcode 62 (05절)는 대조하지 못했다 | 게임이 깔린 기계에서 대조할 수 있나 |

::part[근거]

## <a id="04"></a>04 출처 없는 숫자와 사실

숫자는 인용한다는 규칙 ([workflow.md](workflow.md#01.C) 01.C절)에 비춰 근거가 없는 것이다. 문서에는 그대로 두었거나 "확인되지 않았다"로 표시했다.

| 무엇 | 어디 | 물을 것 |
| --- | --- | --- |
| 캐릭터 기본 STR·DEX (스탯 포션 기준선) | bard-necro-enhanced·tamer-mage-enhanced의 기준선 120·45, pvp·skinning-enhanced의 120·100 (archive의 bard-mace·bard-throwing·hally-mage는 120·120) | 버프 없는 STR·DEX가 얼마인가. 기준선은 그 값 + 20이다 ([pvp.md](pvp.md#09.D) 09.D절). bard-necro의 DEX 25는 사용자가 확인했다 (2026-10-10, 포션을 마셔도 45). 그 전의 120은 예전 임계값 100에서 짐작한 값이었다. STR 100은 아직 짐작이다. pvp는 벌목·skinning 템플릿의 100·80을 따랐다. pvp는 summoner 프로필에서도 쓰니 그 캐릭터의 기본값이 다르면 실행 전에 바꾼다. 선이 높으면 포션이 도는 동안 5초마다 거절될 마시기가 나가고, 낮으면 포션을 아예 마시지 않는다 |
| Lyric 방어구 무시 42.5% | handbook 03.F | 출처가 어디인가. Peace 가동률 62%가 이 숫자에서 나왔다 |
| Barding Break 동안 Virtuoso | handbook 03.F, bard-necro-enhanced PEACE | 정말 꺼지나. "Barded Creatures"에 디스코만 걸린 몹도 드는지 모른다 |
| PK의 Alchemy | handbook 06.C | 80인가 100인가. 지금 숫자는 80 기준이다 |
| song, peace/provo 성공 쿨 | `cooldowns.xml`은 11초, 위키는 10초 (handbook 02.C) | 1초를 일부러 더했나 |
| Vengeful Spirit의 마나 | handbook 04.A, 04.I | "마나 101"을 심볼 1 + 마나 100으로 고쳤다. 마나가 따로 들지 않나 |
| `cooldown "…"`의 반환값 | razor.md | 1인가, 남은 초인가 |
| `and`의 단락 평가 | handbook 05.H | 버섯 `findtype`과 `counttype`을 서 있을 때만 읽는다는 설명이 이것에 기댄다. razor.md에 없다 |
| `in`의 대소문자 구분 | conventions 05절 | 근거가 `dump-label.razor:11` 주석뿐이다. 인게임에서 봤다면 razor.md 03절 함정 표에 넣는다 |
| Vampiric Embrace 확인 날짜 | razor 04절 | 2026-09-25는 커밋 날짜에서 가져왔다. 실제로 본 날짜인가 |
| `auto-mage.razor:1160` 인용 | razor 04절 | 저장소와 이력 어디에도 없는 파일이다. 어디 있나 |
| overheads의 숫자 | overheads 07절, 09절 | 광역 바딩 8타일 · 5초 · 2초, Resist 흡수 `25% x Resist/100` · -75% (pvp의 Parrying 공식과 섞이지 않았나), siphon 5분마다 · 60분, reactive 25, drain 레지 -10 / -20 · 2분, Paralyze PvP 10초, Teleport 15초 |
| pvp의 주장 | pvp 02절, 03절, 05절 | "Swordsmanship도 같은 형태다", 크리처 주문 패링 25%, Hamstring이 PvM 목록에는 있다 |

::part[규칙]

## <a id="05"></a>05 규칙과 파일이 다른 곳

| 규칙 | 파일은 | 정할 것 |
| --- | --- | --- |
| 헤더는 설명 한 줄 + `Needs:` ([conventions.md](conventions.md#02.C) 02.C절) | archive의 bard-throwing과 bard-mace는 배너 뒤에 "Naming convention" 블록이, bard-necro-enhanced는 배너 · 설명 · Needs 순으로 온다. loadout은 헤더 없이 `clearall`로 시작한다 | 긴 루프의 헤더는 어떤 모양인가 |
| `cooldown` 명령은 기존 파일이 그 스타일일 때만 ([conventions.md](conventions.md#04) 04절) | archive의 bard-throwing이 `cooldown "ability"`로 게이트를 세운다 | 규칙이 낡았나, 바가 보여야 해서 일부러 쓴 것인가 |
| 같은 성격이 3개 이상이면 폴더 ([conventions.md](conventions.md#01.C) 01.C절) | `gather/`와 `restock/`은 2개씩이다 | 규칙을 고칠까, 폴더를 합칠까 |
| 시작 4줄 ([conventions.md](conventions.md#02.D) 02.D절) | loadout · claim-loot · share-loot는 `clearall` → `clearsysmsg` → `cleardragdrop` → `clearignore`, archive의 bard-throwing · bard-mace는 `clearsysmsg` → `clearall` → `clearignore` → `cleardragdrop` | 순서가 중요한가 |
| `AutoSaveScript`를 끈다 ([workflow.md](workflow.md#04.B) 04.B절) | 프로필에는 `AutoSaveScriptPlay`도 있다. `summoner.xml`은 둘 다 False, `default.xml`은 둘 다 True다 | 둘 다 끌까. default 프로필 캐릭터는 외부 편집기를 쓰지 않나 |
| 세션 값과 영속 값 ([conventions.md](conventions.md#03.B) 03.B절) | stock-vendor의 `setvar var__…` (영속 `var__`), loadout의 `setvar! global__my_recall_scroll` (세션 `global__`), loadout의 `as item` (`alias__` 없음) | 스크립트를 규칙에 맞출까 |

## <a id="06"></a>06 문서 정리

옮길 곳을 정해야 하는 중복과 제자리가 아닌 내용이다. 한 사실은 한 곳에 둔다 ([writing.md](writing.md)).

| 무엇 | 제안 |
| --- | --- |
| handbook 04.H가 되풀이하는 문법 사실 | razor.md 03절 링크로 바꾼다 |
| "바드 쿨을 자기 타이머로 복사하지 않는다" | 세 문서에 있다. 한 곳을 정본으로 두고 나머지는 링크로 바꾼다 |
| Defensive Barding과 서버 스킬 게이트 (handbook 06.A) | 모든 바드 템플릿에 해당하니 pvp.md로 옮긴다 |
| overheads 11절 링크 메모의 Hamstring (3초 / 30초 / 30\~53초)과 TK (30초) 숫자 | pvp.md 03절, 04절이 정본이다. 숫자를 빼고 링크만 남긴다 |
| handbook 07절의 "loadout 배치" 행 | 이 템플릿 이야기가 아니다. conventions나 hotkeys로 옮길까 |
| 2026-09-29에 바꾼 루프 (교전과 이동 분기, 하우스키핑 시계, peace 대기, 한 줄로 접은 게이트) | handbook 07절에 "확인 대기" 행이 없다. 더할까 |

::part[보류]

## <a id="07"></a>07 미뤄 둔 것

사용자가 그대로 두라고 한 것이다 (2026-09-29). 답이 아니라 순서를 기다린다.

| 무엇 | 남은 일 |
| --- | --- |
| archive/hally-mage | `[ cure pot, on ]` 90을 아직 띄워 프로필 줄과 겹친다. `[ pvp, on ]`이 33이다 (공통 pvp는 90). 읽는 무기 바 `Halberd` `Battle Axe` `Viking Sword` `Katana`가 어느 `cooldowns.xml`에도 없다 |
| indian angus nom, kit, pay | [hotkeys.md](hotkeys.md#03) 03절에 summoner 캐릭터가 nomeehej 하나뿐이다. gumps 파일의 serial로 보면 이 셋도 summoner다 (추정). 그렇다면 Bard Necro 칸 (1 2 3 Disco / Peace / Provo, F1 bard-necro-enhanced)을 받는다 |

::part[필드 PvP]

## <a id="08"></a>08 벌목 · PvP 실험과 구현 전 확인

2026-10-01 후속 관찰과 근접 중심 설계를 반영했다. 확인된 자기 TK 공용 쿨과 두 클라이언트 관찰은
[pvp.md](pvp.md#04) 04절에 반영했다. 아래는 그 결과로도 아직 확정할 수 없거나 수정이 필요한 부분이다.

### <a id="08.A"></a>08.A TK와 Reflect의 추가 확인 범위

이번 실험에서 TK로 Reflect가 사라지지 않았다는 결과는 다시 미확인으로 돌리지 않는다.
다만 "모든 조건에서 반사 판정 자체를 완전히 우회한다"는 서버 내부 결론이나 포션 부착 소유권까지 화면만으로 확장하지 않는다.

1. A가 공격자, B가 대상인 통제 테스트에서 B의 Inscription 값과 Reflect 상태를 기록한다. 처음에는 A의 Reflect를 끄고 양측 TK 제한이 끝난 상태로 시작한다.
2. A → B TK 직후 양측 Journal과 B의 Reflect를 함께 기록한다. A에게 TK 수신 안내가 오는지, B에게 누가 걸었다고 뜨는지 확인한다.
3. 별도 시행에서 A가 B에게 포션을 던지고 B가 이동해 실제 부착을 확인한다. 반대 방향 시험은 새 시행으로 분리하고 모든 TK·포션 제한이 끝난 뒤 한다.
4. 비교군으로 Reflect 없는 B, A의 자기 TK를 각각 시험한다. 포션 부착 때 대상 제한이 갱신되므로 마지막 적용·부착부터 시간을 센다.
5. Inscription 0과 높은 경우를 구분한다. "첫 반사 후 유지"를 "전혀 반사되지 않음"과 혼동하지 않도록 양쪽 화면으로 확인한다.
6. 화면 주인을 매번 적고, 자기 TK만 / 내가 상대에게만 / 상대가 나에게만 / 양방향 동시 시도를 독립 시행한다.
   양측 Journal·실제 대상 serial·시도와 응답 시점을 함께 기록한다. 캐릭터 이름이 화면 주인의 이름인지 시전자의 이름인지 구분한다.
7. 취소·실패·대상 변경·응답 지연·남아 있는 과거 메시지·수동 TK 핫키 개입을 각각 넣어 허위 성공 여부를 확인한다.

이 실험을 완료하기 전에도 운영 결론은 같다. TK를 Reflect 제거나 공짜 자기 TK 획득 수단으로 삼지 않는다.

### <a id="08.B"></a>08.B 자동화 전에 남은 것

| 항목 | 현재 근거 | 다음 확인 또는 수정 범위 |
| --- | --- | --- |
| 플레이어 조회 진단과 이전 Q 전투 버전 | 직접 serial의 alt TK·Explosion→EB 적용, 플레이어 find 실패, 변수 비교 방향 문제와 조회별 제한은 인게임 확인됨 2026-10-04. 결과는 [razor.md](razor.md#03.A) 03.A절이 정본이다 | 2026-10-05 공격을 수동으로 바꾸고 상대 조회와 자동 공격을 현재 루프에서 제거했다. 새 자기관리 루프의 확인은 10절이다. 이전 자동 공격의 캐시·후속 주문 테스트는 현재 동작의 요구사항이 아니다. 사용자는 실행 중 `Range check Last Target` ON·12타일이라고 확인했다. 현재 Outlands에서 거리 밖 → 안 전환 때 수동 Last Target의 커서 보유·방출은 확인되지 않았다. 검색이 플레이어를 누락하는 내부 원인도 미확인이다. 진단 핫키는 유지한다. 남은 진단은 바디 ID를 넣은 findtype 비교, 실제 거리를 기록한 반복 검사, NPC getlabel에 label이 오지 않은 이유다 |
| 자기·수신 TK로 target 바가 켜짐 | 사용자 후속 보고상 적 TK 수신도 공통 안내와 me·target 바를 만들 수 있음 | 응답 대기 + 새 안내 + 같은 대상만으로 성공 처리 금지. 수신만 있는 시행에서 절대로 점화하지 않는지 검증. 독립 성공 신호를 확보하지 못하면 자동 점화 보류. 2026-10-04 bard-necro-pvp에서는 공통 바를 근거로 한 자동 점화 블록을 제거했다. 실제 포션은 수동으로 던진다 |
| 나에게 걸린 TK의 소유자 | me 바는 `applied telekinesis to you`만 읽음 | 화면 주인별 고정 문구 검사와 name 표현식을 테스트. 동적 문자열 조합은 미확인. 확인된 공격 TK를 me 바만으로 취소하지 않되, 동시 시도로 귀속이 모호하면 점화하지 않는지 검증 |
| 상대 Reflect 최종 소진 | Harm 반사 피해와 Spell Siphon 표시는 소진 전용 신호가 아님 | 첫 반사로 소진 / 첫 반사 후 유지 / 두 번째로 소진을 나눠 공격자 Journal을 수집. 전용 문구가 없으면 스크립트에서 확정 상태로 만들지 않음 |
| Bless와 스탯 포션 | 공식 계산과 실제 정수·중첩 처리는 구분해야 함 | Magery 80에서 포션만 / Bless만 / 둘 다 순서를 바꿔 STR·DEX·INT·최댓값과 현재 마나 기록. Bless 비용 9, 공식 +8.8의 정수 처리, 스크롤 소환에 실제 마나 50이 필요한 조건을 구분. Magery 100의 Bless는 2026-10-09 `changed by 11`로 +11이 확인됐다 (12절) |
| 프리캐스트와 자동 회복 | 공식은 완료한 프리캐스트 보유 중 포션 음용이 주문을 취소한다고 설명 | v5는 일반 수동 입력을 기다리며 준비된 긴급 회복이 있으면 수동 주문을 중단한다 (pvp.md 05.E절). 자체 자기 시전 도중 새 수동 입력이 겹치는 경우는 10절에서 확인 |
| 출발 스탯과 무기 교체 | 핸드북 표는 공식 대입 계산 | 현재안 100/80/45, 포션 후 DEX 100에서 붕대 10초와 STA 100의 GA 3초·Norse 1.5625초 확인. 공유 마지막 스윙, 피격 후 스태미나 감소, 가죽·Meditation 0의 30초 재생량도 기록 |
| 이동 중 짧은 견제 | 시전 시작 6타일은 설계 초안, 최대 사거리 아님 | 이동 차단 옵션·LOS·시전 완료 때의 거리·상대 이동 속도·실패 재시도를 확인. Harm 5타일 이상 피해 감소와 접근 지연을 비교 |
| 피해 계산 | 핸드북 07절은 Tracking 주문 보조를 제외한 비교 모델 | 동일 상대·장비로 Eval 0/100, Tracking 유무, RA 유무를 분리 측정. 계산 중간값을 실측 평균으로 표시하지 않음 |
| Reflect 재시전 제한 | 2026 공식 패치는 PvP 플래그 중 60초로 명시 | 시전·첫 반사·최종 소진 중 제한이 언제 시작하는지, 플래그 전환과 남은 시간 안내를 양측에서 기록 |

### <a id="08.C"></a>08.C 포션 부착과 실패 복구

1. 30초 안내가 뜨는 플레이어 대상에서 실제 부착 메시지·이동 추적·피해를 확인한다.
   60초 안내 화면에서 관찰한 `Your explosion potion sticks to your target.`를 PvP에서도 받는지 검증한다.
2. 점화·커서 생성·투척·부착·폭발 시각을 별도로 잰다. 화면의 5·4·3·2만으로 정확한 퓨즈나 네트워크 여유 시간을 확정하지 않는다.
3. 점화 뒤 대상 이탈·LOS 차단·사망·대상 변경을 만든다. 자기 포션 커서가 남은 경우에만 지면 투척 복구를 시험한다.
4. 지면 투척은 유효/무효 위치·높이·벽·발밑·이동 경로를 나눠 확인한다. 투척 완료 신호와 실제 폭발 위치·반경을 함께 기록한다.
5. 커서 취소·자동 회복 개입·부착 메시지 누락을 넣는다. 다른 커서를 소비하거나 같은 실패에서 포션을 또 점화하지 않아야 한다.
6. Splashback의 현재 피해 분담과 반경을 확인한다. 회수·재타겟이 가능하더라도 퓨즈가 초기화된다고 가정하지 않는다.

위 실험 전에는 완전 자동 공격 TK 확인이나 안전한 자동 폭탄 폐기가 구현됐다고 표시하지 않는다.
수신 TK만으로 점화되는 경우는 기능 실패이고, 이미 확인된 공격 TK를 단순 me 바 때문에 취소하는 것도 별도의 판정 오류다.

::part[채집]

## <a id="09"></a>09 lumberjack-enhanced 인게임 확인

2026-10-05 v8의 기본 채집은 사용자가 정상 작동을 보고했다. 인게임 확인됨 2026-10-05.
v9에서는 손이 비었는데 백팩 도끼를 장착하지 않는다는 보고를 받았다. 인게임 확인됨 2026-10-05.
실제 검색 범위·실패한 가드는 미확인이므로 레이어 문법 오류로 단정하지 않는다.
v10은 lhandempty → 저장한 var__my_hatchet 장착 → 실제 왼손 serial 일치 확인으로 바꾼다.
목재 가공·파우치 정리는 유지하며 도끼 장착에 책·Hunting·무게 준비 조건을 요구하지 않는다.
도구 사용·커서 대기·자기 타깃은 같은 채집 블록에서 처리하고 별도 pending 상태는 두지 않는다.
리콜용 책·Hunting·무게 점검은 기존 housekeeping 주기를 재사용하며, 시간 경과만 알리는 응답 타이머와 안내 상태는 제거했다.
Tracking 시작 설정과 자동 리콜 판정의 분리는 유지한다.
목재 가공·파우치 이동 후 채집 중단과 남은 Logs를 보고받았다. 인게임 보고 2026-10-05.
화면의 오류 문구·줄 번호는 확인되지 않았다. v11은 목록·foreach를 제거하고 작업 예산과 횟수를 제한한다.
생존 → 자동 리콜 → 채집 → 자기 버프 → housekeeping 순서로 정리하며 집 문·Stockpile 코드는 제거했다.
v12 화면에서도 BEGIN 뒤 convert만 계속 나오는 현상을 보고받았다. 인게임 보고 2026-10-05.
CE 원본의 제어 흐름 재현에서 if 안 break가 반복문 범위를 남겨 바깥 for 2를 Logs 단계로 되돌리는 경로를 확인했다.
v13은 목재 검색·큐 대기를 조건 종료 while로 바꾸고 break·continue를 제거한다. 새 상태나 타이머는 없다.
기존 모의 검사가 엔진 범위 처리를 놓친 점을 기록한다. 실제 Outlands 내부의 동일 동작은 확인되지 않았다.
이후 사용자 Journal에서 v13의 END와 채집 응답을 확인했다. 인게임 확인됨 2026-10-05.
두 정리에서 같은 Boards serial이 이동 대상으로 반복되고 일부가 안 옮겨진다는 보고는 남았다.
v14는 파우치 소속을 ignore 전에 판별하고 이미 보관한 Boards는 skip, 나머지는 move request로 기록한다.
검색이 ignore를 적용하거나 적용하지 않는 경우 모두와 병합·다음 주기 재시도는 모의 검사했다.
현재 포크의 직접 serial 검색에서 ignore가 적용되는지와 v14의 실제 이동 성공은 아직 확인되지 않았다.
v12는 네 겹의 채집 조건을 차단 사슬로 정리하고, 큐가 남아 있을 때만 대기하며 진단 출력을 sysmsg로 분리한다.
2026-10-10 v18은 housekeeping 주기를 없앴다. 리콜 블록이 자기 5초 주기로 책·Hunting·무게를 점검하고, 음식·목재 정리는 각자의 타이머를 매 패스 본다.
책·Hunting 조건은 리콜 결정과 함께 `var__hold_gathering` 하나로 채집과 목재 정리를 세운다 ([modules.md](modules.md#08) 08절).
설정·상태·타이머와 반영 절차의 정본은
[lumberjack-pvp-handbook.md](lumberjack-pvp-handbook.md#08) 08절이다.

| 남은 항목 | 확인할 것 |
| --- | --- |
| 실제 Smart Harvest 경로 | Hatchet 한 개만 준비해 손 슬롯 확인 → Use item in hand → target self 채집을 확인한다. 빈손에서는 var__my_hatchet으로 백팩 도끼를 장착하고 다음 시도에서 왼손 serial과 일치하는지 확인한다. sysmsg ON의 Hatchet equip requested 줄은 요청 기록이며 성공 증거가 아니다. 무게 한도에서도 빈손 장착이 실행되는지 확인한다. v18부터 책 필수인데 책이 없거나 감지 리콜인데 Hunting이 없으면 장착도 기다려야 한다. 장착 거절·도끼 파손·교체·이미 장착한 상태로 재실행도 시험한다. 백팩에만 도끼가 있을 때 장착된 것으로 판정하면 실패다. 다른 왼손 장비만 비우고 오른손 장비는 수동으로 처리한다. 1초 이후 도착한 중립 커서도 3초 타임아웃 안에 같은 블록에서 처리하고, 도구 큐가 남아 있어도 자기 타깃을 보내야 한다. 3초 무응답이면 자기 타깃을 보내지 않고 다음 요청을 4초 더 보류하는지 확인한다. 기존 커서가 있으면 새 채집 요청은 보류하고 루프는 유지해야 한다. 대기 중 수동 입력과 중립 커서 겹침도 시험한다 |
| v17 공용 회복 모듈 | 2026-10-10 v17은 모듈로 조립하면서 회복·버프·시약을 pvp와 같은 모듈로 바꿨다 ([modules.md](modules.md#08) 08절). 재시도 타이머 없이도 같은 행동이 패스마다 되풀이되지 않아야 한다. 워모드를 켜면 회복 주문과 버프가 서고 포션은 계속 나가야 한다. 리콜이 정해지면 버프가 서야 한다. 버프는 손실 15부터 시작하지 않고 시전 중이면 끊긴다. 시약은 자동 리콜 뒤에 읽어 Tracking 줄을 먼저 본다. `[ refresh, out ]`은 이제 뜨지 않는다 |
| v18 블록별 타이머와 채집 보류 | 2026-10-10 v18에서 housekeeping 주기를 없앴다. `Lumberjack enhanced v18 loaded`를 먼저 확인한다. 음식은 60초마다, 목재 정리는 2분마다, 리콜의 책·Hunting·무게 점검은 5초마다 각자의 타이머로 돌아야 한다. 음식은 다쳤거나 독·리콜 결정 중에도 먹지만 워모드에서는 쉰다. 책 필수인데 책이 없거나 감지 리콜인데 Hunting이 없으면 빈손 장착·채집·목재 정리가 모두 기다리고, 책을 넣거나 Hunting을 켜면 다음 5초 점검 뒤 다시 시작해야 한다. 리콜 결정 뒤에는 재실행 전까지 다시 시작하지 않는다 |
| 자원 없음 뒤 2초 재시도 | v15에서 주변 자원 없음 원문과 `[ harvest, out ]` 뒤 약 2초 후 도구 요청을 확인한다. 새 장소에서 요청하면 다음 간격은 기본 4초로 돌아가야 한다. 자원 없음이 반복될 때는 각 응답 뒤 2초를 센다. 대기 중 회복을 계속하고 기존 커서·시전·이동 바·리콜 결정을 무시하지 않아야 한다. 여행 제한·수확 실패·채집 불가를 자원 없음으로 처리하면 실패다. 실제 간격과 응답 소비는 아직 인게임에서 확인되지 않았다 |
| 출력 설정 분리 | config__chatty·config__sysmsg의 네 조합에서 선택 오버헤드와 Journal 진단이 서로 독립적인지 확인한다. 둘을 꺼도 도끼·파우치 부족 경고와 프로필 채집 결과는 남아야 한다 |
| 주기적 목재 가공·파우치 정리 | pack/lumber를 넣고 뺀 조립, 2분·3분 주기, 파우치 최초 선택·제거·용량 부족을 시험한다. 일반·특수 Logs가 Boards로 바뀌고, 기존 Boards와 합쳐져도 새 묶음을 옮겨야 한다. 이미 파우치 안 Boards는 제외한다. 가공·이동 실패가 반복 루프를 만들지 않고 다음 주기까지 남기는지 확인한다. 수동 커서·시전·피해와 `var__hold_gathering` (리콜 결정·책 없음·Hunting 없음)은 정리를 보류하며, 처리 중 상태가 바뀌면 다음 묶음 전에 양보해야 한다. 2.5초씩의 가공·이동 예산이 끝나면 남은 목재는 다음 주기로 넘기고 채집을 재개하는지 확인한다. v18 loaded를 확인한 뒤 sysmsg의 Lumber pack BEGIN → convert/skip/move request → END와 큐·커서 안내를 남긴다. 기존 파우치 Boards는 skip만 기록되어야 한다. move request는 완료 증거가 아니므로 백팩·파우치의 실제 묶음 수량을 확인한다. 같은 hue 병합 뒤 다음 주기에 새 Boards만 들어 올리고, 거절된 이동은 다음 주기에 다시 시도하는지 확인한다. 한 정리에서 BEGIN은 한 번이며 다른 색상·큐 지연·목재 없음·이미 보관한 Boards에서도 END에 도달해야 한다. 실행이 Play로 돌아가면 Script Error·Line 번호·Script finished 문구도 함께 기록한다. 실제 서버의 인벤토리 갱신에 500ms 대기가 충분한지도 기록한다 |
| 리콜·Tracking 블록을 뺀 조립 | `escape/tracking`이 있으면 확인한 Hunting을 재사용하고 필요한 경우에만 시작 설정을 한다. 빼면 시작 설정도 없다. `escape/recall`은 Tracking 블록의 상태를 읽으므로 Tracking만 빼면 조립기가 멈춘다. `escape/recall`을 빼면 루프의 리콜용 감지·책·여유 무게 조회가 없어야 한다. 가까운 red가 있어도 자기 회복·버프·채집은 계속한다 |
| 감지 리콜과 채집의 설정 조합 | recall_on_detection이 1이고 캐릭터에 Tracking이 있을 때만 Hunting 준비를 채집 조건으로 요구한다. 0이면 Hunting 때문에 채집을 보류하지 않는다. `[ track, check ]`는 2026-10-10부터 `escape/tracking`이 띄우므로 recall_on_detection과 상관없이 Hunting이 꺼지면 뜨고, Tracking이 0이면 뜨지 않아야 한다. 이때도 무게 리콜과 책 필수 조건은 유지된다 |
| Tracking 초기 필터·상태 | 기본 red, 현재 창의 필터 확인과 세션 색상 캐시 재사용. 변경이 필요하면 Hunting을 먼저 끄고 최대 10개 필터를 순환하며, 설정 중 곰 같은 추적 문구를 비운 뒤 Hunting을 켠다. 다른 필터의 활성 Hunting·반복 Play·수동 필터 변경 뒤 Hunting OFF·클라이언트 재시작을 각각 시험한다. 초기 응답 누락·피해·수동 시전이면 안전해진 뒤 재실행해 준비 상태로 복구. 감지 리콜 ON이고 리콜 결정 전일 때만 리콜 블록의 5초 점검 주기로 상태를 점검하며 Hunting 미확인 시 채집을 보류한다. grey·orange 확인 문장의 서버 일치도 기록한다 |
| Tracking 거리 오버헤드 | 사용자 요청으로 현재 매핑을 유지한다. spaces to target가 포함된 전체 서버 문장을 받은 뒤 거리 숫자의 단어 위치를 확인한다. 이름의 단어 수가 달라질 때 고정된 {n}이 같은 숫자를 가리키는지도 확인한다 |
| 채집 전 리콜 판정과 메시지 순서 | 45·46 steps, 거리 무관 옵션, 같은 패스의 무게 부족, 시약 부족·시전 끊김 안내의 동시 도착을 시험한다. 감지는 무게보다 먼저 읽으며 같은 패스부터 채집을 보류한다. 자기 시전·최대 3초 도구 커서 대기·목재 정리 중 판정 지연과 입력 충돌도 기록한다. sysmsg ON의 Recall trigger 로그로 Tracking 또는 여유 무게 중 실제 요청 원인을 구분한다 |
| 회복 에이전트·시약과 수동 입력 | 독·붕대·회복 포션·시약 부족·프리캐스트 조합과 자동 회복 직후 커서 충돌. 첫 패스와 이후 10초 시약 갱신, 부족 안내를 읽은 패스의 즉시 재검색을 확인한다 |
| Home 리콜·책 캐시 | 책 충전량·룬 이름·지연·실패와 실행당 한 번의 요청. 사용자 화면의 집 접근 거절은 도착 성공이 아니다. Home 룬의 목적지·집 권한을 확인하고 실제 거절 안내가 뜨는지 기록한다. 책 없음·제거·새로 넣기와 책 필수 OFF를 나눠 확인한다. 정기 책·무게 점검은 리콜 블록의 5초 점검 패스에서 채집 전에 한다. 요청 직전 책이 사라졌으면 캐시를 0으로 바꾸고 다음 점검까지 재검색을 보류해야 한다. 준비용 Strength·Agility 포션은 사용하지 않는다 |
| 리콜 결정·전송과 응답 지연 | 마나 부족·기존 수동 커서·이동 때문에 요청을 보류해도 채집은 중단하고 회복은 계속한다. 전송 후에는 늦은 거절을 안내하되 같은 실행에서 재전송하거나 채집을 재개하지 않아야 한다. 5초 경과만으로 결과 안내나 도착 상태를 만들지 않는다. 새 요청은 재실행으로 시작한다 |
| Heat of Battle와 실제 서버 응답 | 버프만으로 명령 전송을 막지 않아야 한다. 공식 문서에는 Recall도 제한된다고 적혀 있으므로 실제 허용·거절과 서버 문구를 확인한다. 규칙 정본은 [pvp.md](pvp.md#01) 01절이다 |
| 채집 결과·스킬·거절 프로필 안내 | default·summoner 각각에서 일반 logs와 특수 목재 종류 표시·수확 실패·두 배 수확·스킬 확률·스킬 상승 안내를 확인한다. 재질은 You chop some으로 검색하고 전체 문장의 {4}를 표시한다. 고갈 안내를 보고 다음 장소로 이동한다. 확률 숫자를 실제 스킬 상승으로 해석하지 않는다. 이동 제한·주변 자원 없음·채집 불가 안내도 한 번 표시돼야 한다. 실제 이동 후 서버의 60초 제한과 스크립트의 4초 명령 재시도 간격을 구분한다. 거절 메시지를 받은 시점부터 새 60초를 세지 않는다. 매핑 정본은 [overheads.md](overheads.md#07) 07절이다 |
| 현재 캐릭터의 쿨다운 바 | heal pot·walk·reflect의 실제 트리거. 없거나 다르면 해당 캐릭터만 후속 수정한다 |

::part[필드 PvP]

## <a id="10"></a>10 공통 pvp 자기관리·무기 장착 인게임 확인

2026-10-05 `combat/pvp.razor`로 자기관리를 통합하고 기존 두 PvP 파일은 삭제했다.
2026-10-06 v5는 회복 선택·긴급 수동 주문 중단·자기관리 실행·무기 장착 순서다.
GH와 긴급 중단 기준을 손실 35로 맞추고, 시폰·버섯 자동화와 양손·슬롯 상태를 제거했다.
2026-10-08 v6은 각 블록이 지금 상태를 읽고 바로 행동하는 구조로 다시 썼다. 회복 주문은 에이전트, 버프는 빠지면 바로,
스탯 포션은 켜 둔 동안 유지한다. 수동 입력 중단·주문의 이동 가드·6초 시전 대기와 `[ cast, check ]` 정지·재시도 타이머를 없앴고,
시약은 10초마다 또는 시약 거절 직후 읽는다.
2026-10-09 v7은 Strength·Agility 포션을 버프 대신 STR·DEX 값으로 판정한다. 아군 Bless가 같은 아이콘을 띄워 포션을 막았기 때문이다 ([pvp.md](pvp.md#09.D) 09.D절).
2026-10-10 v8은 가벼운 Heal을 `config__use_light_heal`로 붕대 옆에서도 쓸지 정한다 (기본 0). 붕대를 쓸 수 없으면 옵션과 상관없이 대타로 나간다.
같은 날 v9는 모듈로 조립한다. 동작은 v8과 같다 ([modules.md](modules.md#08) 08절).
현재 본문은 아직 인게임에서 확인되지 않았다. 설정·변수·타이머와 커서 처리의 정본은 [pvp.md](pvp.md#05.E) 05.E절이다.

Scripts 탭에서 Stop → Reload all scripts → Play로 먼저 확인한다.
외부 편집 뒤 기존 핫키로 실행할 때는 클라이언트를 재시작한다 ([workflow.md](workflow.md#04.A) 04.A절).
게임 종료 후 `git status --short`로 옛 본문 덮어쓰기를 확인한다.

| 상황 | 예상 알림·동작과 실패 판정 |
| --- | --- |
| 마법·무기 각각 0/1, 붕대 0/1, 핫키 재연결 | CONFIG를 바꿔 재실행한다. `[ pvp, on ]`·`PvP sustain v9 loaded`가 떠야 한다. F4와 별도 PvP 키는 `combat\pvp`로 재연결한다. 이전 프리셋이 설정을 덮어쓰거나 OFF 기능을 요청하면 실패 |
| Q alt·NPC 선택, Q 변경, Tab ON/OFF | 스크립트는 자동 TK·공격 주문·소환수 공격·근접 공격 요청·Hamstring 토글을 보내지 않는다. 무기 옵션은 상대 선택 없이 동작한다. 상대 find·dead·getlabel 제한 경고가 뜨면 실패. 서버의 기존 자동공격과 수동 요청은 구분한다 |
| 피해·독·마비·낮은 STA, 포션·붕대·시약 부족 | 파우치 → Cure 포션 → 힐 포션 → GH 에이전트 → 붕대 → 가벼운 Heal 순서다. 기본 손실 35부터 포션, 포션이 나갈 수 없으면 GH를 쓴다. `use_light_heal` 0에서 붕대가 도는 동안 가벼운 Heal이 나가면 실패, 1이면 붕대와 함께 나가야 한다. Cure 포션이 하나라도 있으면 Cure 에이전트를 쓰지 않아야 한다. Healing이 없거나 붕대가 없으면 Heal 경로를 확인한다. 부족하면 `[ pouch, out ]`·`[ cure pot, out ]`·`[ heal pot, out ]`·`[ bandage, out ]`. 진행 중 붕대를 반복 시작하면 실패 |
| Magery OFF·붕대 OFF, 버프·스탯 포션 옵션 | OFF 기능의 자동 요청이 없어야 한다. RA·Reflect는 자기 버프다. 시폰·버섯·자기 MA 자동 반복은 없어야 한다. Resist 포션은 버프가 빠진 다음 패스에, Strength·Agility 포션은 STR·DEX가 기준선 아래로 내려간 다음 패스에, RA·Reflect는 빠지면 빈 창에서 바로 다시 나가야 한다. 한 스탯 포션이 떨어져도 나머지는 계속 마셔야 한다. `config__str_potion`·`config__dex_potion`을 실행하는 캐릭터의 기본 + 20으로 맞추고, 아군 Bless가 걸린 채 교전해도 힘·민첩 포션이 한 번씩 나가는지 본다. 마신 뒤 5초마다 다시 눌리면 선이 높다. 포션이 도는 동안 Curse·Weaken·Clumsy를 맞으면 거절 메시지가 5초에 한 번만 나와야 한다. 걷는 중에도 버프를 건다. 긴급 손실에서는 버프를 시작하지 않고, 시전 중 그 선에 닿으면 끊는다. Resist 포션은 몹·펫용이며 적 플레이어 주문 피해 감소로 해석하지 않는다 |
| 시작 전에 수동 시전·프리캐스트·포션·소환수 커서 보유 | 기존 커서를 보존한다. 시전 중 (커서 전)에는 포션이 나가고, 커서를 든 동안에는 마비 파우치 외 모든 행동이 기다린다. 커서 종료를 공격 성공으로 해석하면 실패 |
| 긴급 HP의 수동 입력 | 손실 35 이상에서 수동 시전 중이면 포션은 나가고 GH는 시전이 끝난 다음 패스에 나가야 한다. 완료한 공격 커서를 든 동안에는 포션·GH 모두 기다리고, 커서를 놓은 다음 패스에 나가야 한다. 스크립트가 수동 시전·커서를 끊으면 실패. 시전 중 포션 음용이 실제로 주문을 끊지 않는지, 커서를 든 채 마시면 주문이 취소되는지도 기록한다 |
| 자동 자기 시전 중 끊김·응답 지연·새 수동 입력 | 에이전트·RA·Reflect는 `for 60` 폴링에서 시전이 끝나거나 끊김 줄이 보이면 다음으로 넘어간다. 스크립트는 커서에 답하지 않는다. 에이전트가 만피에서 남긴 beneficial 커서만 취소한다. 수동으로 연 harmful·neutral 커서를 취소하거나 자기 타깃으로 쓰면 실패. RA·Reflect 시전 중 긴급 HP면 `> Interrupt` 후 다음 패스에 회복한다. 에이전트가 Q 선택·수동 Last Target에 미치는 영향도 확인한다 |
| 긴급 아이템 회복·시약 소진·보충·빈 스탯 포션 시도 | 처음 실행과 보급품 보충 직후에도 필요한 마비 파우치·Cure 포션·힐 포션을 먼저 시도해야 한다. Magery OFF·해당 주문이 불필요·최소 마나 미달이면 시약 조회가 없어야 한다. 시약이 없는 상태에서 추가한 뒤 다음 회복·버프 점검에 반영되는지 확인한다. 시약이 떨어지면 `More reagents are needed` 직후 플래그가 바뀌어 같은 주문을 반복하지 않아야 하고, 보충은 10초 안에 반영되어야 한다. 붕대 제거·보충 직후에는 진행 중 붕대를 유지하면서 다음 점검의 Heal 대체 조건이 실제 재고를 따라야 한다. STR·DEX가 기준선 이상이고 Resist가 있거나 포션이 없으면 스탯 포션 블록에서 행동 대기 없이 무기 단계로 진행해야 한다 |
| 자기 주문 선택·마나 임계값 | 기존 기본값에서 Cure → 큰 피해 GH → 붕대 대체 Heal 순서를 유지한다. 회복이 끝난 패스에서 스탯 포션 → RA → Reflect가 차례로 나가야 한다. 각 `config__mana_*` 값의 바로 아래·같은 값에서 시작 조건을 비교한다. 예비 마나 20을 반영한 GH 최소값 31에서는 마나 30에 요청하지 않고 31부터 가능해야 한다. 기본값은 예비 마나를 보장하지 않는다. GH의 시약만 모자랄 때 붕대 대체 조건을 충족한 Heal, RA의 시약만 모자랄 때 가능한 Reflect도 확인한다. 폴링 종료를 주문 성공으로 해석하면 실패 |
| 무기 ON/OFF, 네 슬롯 ID, 가용 무기 없음 | OFF면 장착 명령 없음. ON에서 각 슬롯을 하나씩 켜 바 이름과 ID 연결을 확인한다. ID 0은 건너뛴다. v6부터 준비된 슬롯의 무기가 백팩에 없으면 다음 슬롯으로 넘어가지 않고, 양손이 비면 `[ weapon, out ]`만 뜬다. 어느 경우에도 장착 없이 회복 루프가 계속되어야 한다. `dress serial`이 이 클라이언트에서 실제로 장착되는지 ([razor.md](razor.md#03) 03절의 dress 실패 기록)도 확인한다 |
| 여러 스윙 바가 0, 모두 진행 중, 빈손 | 준비된 가용 슬롯 중 4 → 3 → 2 → 1 우선순위. Great 4가 진행 중이고 Norse 1만 0이면 Norse로 교체한다. 모두 진행 중이면 현재 장비 유지, 양손 공백이면 1 → 2 → 3 → 4로 재장착만 한다. 모두 0인 동안 두 도끼를 반복 교체하거나 장착을 명중으로 처리하면 실패 |
| 이미 든 무기·책·방패, 같은 graphic의 여분 | Arm/Dress의 충돌 장비 자동 해제를 켜고 1H ↔ 2H 교체를 확인한다. 선택한 serial이 손에 있으면 장착 요청을 반복하지 않는다. 검색 도중 새 수동 커서·시전·큐·은신이 생기면 장착 요청 직전 가드가 보류해야 한다. 마지막 선택 물건이 손에 있는데 여분으로 반복 교체하면 실패. `PvP weapon: equip requested`는 요청 표시이므로 실제 손 장비와 함께 확인한다 |
| 스윙 바 타입·시간, 현재 STA 변화와 실제 스윙 | 활성 캐릭터의 사용 슬롯에 `WeaponSwing` 바가 있는지 UI에서 확인한다. 바의 0만으로 설치·정확한 스윙 시간을 판정하지 않는다. STA를 바꾸고 계산식·바·실제 스윙을 비교한다. 스크립트가 스윙 바를 시작·초기화하거나 장착·Q 변경으로 실제 스윙을 확정하면 실패 |
| Stop 재실행, 은신·이동·구조화 PvP·필드 Heat of Battle | 행동 재시도 타이머를 유지하며 보급품 캐시·주기적 초기 조회는 없다. 시약 부족 점검 직후 Stop → Play를 반복해도 회복·버프 재조회 간격이 유지되어야 한다. 은신은 대기한다. v6부터 걷는 중에도 자동 주문을 시작하므로, 이동 중 시전이 서버에서 거절되거나 끊기는지 기록한다. 명령 제한은 `[ script, blocked ]` 후 정지. 필드 HoB만으로 같은 차단이 발생하면 구분 실패 |
| 조건부 전투 모형의 실측 입력 | [벌목 핸드북 05.D절](lumberjack-pvp-handbook.md#05.D)은 실제 승률이 아니다. 시전 시작·완료·방해 직전후 마나를 기록하여 중단 비용과 시전 중 재생을 확인한다. 근접 유지 시간·양쪽 회복·도끼 명중·포션 시각을 함께 기록하고 모형 입력과 비교한다. 퓨즈·Splashback 반경은 [08.C절](#08.C) 실험과 함께 확인한다 |
| 던전 첫 버스트와 회복 대기 | 2026-10-05 사용자는 메이지 한 명, Reflect 없음, 몹 피격 뒤 HP 약 100에서 약 10초 내 사망을 보고했다. [벌목 핸드북 05.E절](lumberjack-pvp-handbook.md#05.E)의 피해 범위는 설명 가능한 조건이며 실제 상대 스킬은 미확인이다. TK 적용·포션 부착·Explosion 방출·EB 시전·각 피해·회복 시각과 붕대 남은 시간을 기록한다. 시전 중 포션 음용과 완료한 프리캐스트 보유 중 음용을 구분하고, 현재 수동 입력 대기가 회복 요청을 보류했는지 확인한다. 30초·60초 모형의 낮은 사망 비율로 첫 버스트의 생존 가능성을 판단하지 않는다 |
| 만피에서 붕대 선행 | 서버가 만피 Bandage Self 요청을 받아 실제 붕대를 진행하는지 확인한다. 현재 루프는 피해·독이 있어야 요청한다. 이미 피해가 있으면 자기 MA 없이 시작되는지, 수동 커서·시전·진행 중 붕대가 요청을 막았는지 구분한다. 자기 MA 자동 반복으로 마나를 쓰거나 진행 중 붕대를 다시 시작하는 정책은 추가하지 않는다 |

::part[채집]

## <a id="11"></a>11 skinning-enhanced 인게임 확인

2026-10-06 `gather/skinning-enhanced.razor`를 만들었다. v8은 Two-Handed Axe를 쓰는 Magery 80 덱서용 던전 근접 루프다.
Forensic Evaluation 120, Swordsmanship·Tactics 100, Magery·Resisting Spells·Parrying·Anatomy·Healing 80, STR 100·DEX 80·INT 45 템플릿이다.
bard-mace에서 바드를 빼고, lumberjack-enhanced의 자기 회복 주문·RA·Reflect와 시체 칼질을 넣었다.
워모드는 사용자가 Tab으로 직접 켠다. Z → V는 워모드를 바꾸지 않는다. 싸우는 동안 워모드를 켜 두므로 회복·버프·칼질 어느 것도 워모드를 보지 않는다.
칼질은 위키 [Forensic Evaluation](https://wiki.uooutlands.com/Forensic_Evaluation)을 따른다.

> Players can target themselves or nearby ground to activate "Smart Harvest" which carves all grey notoriety corpses "within 2 tiles"

그래서 회색 시체만 깔 때는 `target self`, 회색·파란 시체를 모두 깔 때는 시체 serial을 하나씩 직접 찍는다 (`config__skin_unowned`).
스크립트는 시체 이름 색을 읽지 못하므로 회색 판정은 서버에 맡긴다.
사용자는 파란 시체에서 `[ loot, crim ]`이 뜨지만 아이템을 가져가야만 grey가 되고, 2칸 거리의 시체는 검색에 잡히며,
ignore한 시체는 clearignore 전까지 findtype에서 빠진다고 보고했다. 인게임 확인됨 2026-10-06.
lasttarget이 바뀌어도 지금 치고 있는 대상은 바뀌지 않는다는 bard-mace 경험도 함께 보고했다. 칼질이 문제가 되는 것은 다음 V 한 번이다.
2026-10-07 v3 Journal에서 직접 타겟 칼질의 `You carve materials from the corpse.`를 확인했다.
Sanctuary Dungeon의 파란 시체는 `Criminal actions are not permitted in the Sanctuary Dungeon.`으로 거절됐다.
사용자는 일반 던전에서는 아이템을 가져가야만 grey가 된다고 보고했다. 인게임 확인됨 2026-10-07.
다만 플레이어 시체는 다르다. v6이 파란 플레이어 시체 `the remains of Leap Day William`을 직접 찍자
`You have committed a criminal act! (corpse carving onLeap Day William).`로 범죄 판정을 받았다. 인게임 확인됨 2026-10-07.
몬스터 시체 이름은 `aged earth corpse`처럼 "…corpse"였다.
v7은 직접 찍기 전에 라벨을 읽어 "corpse"가 있고 "remains"가 없는 시체만 찍고, 그래도 범죄 판정이 나오면 그 Play 동안 직접 찍기를 끈다.
공개 스크립트 [forensics](https://outlands.uorazorscripts.com/skills/forensics/c8e4e8eb-743d-4a7f-9043-4c17d2cabb6a)도
`"the remains"`를 플레이어 시체로 보고 건너뛴다.
v8은 직접 찍은 뒤의 응답을 읽는다. `That corpse has already been carved.`는 끝난 시체로,
`That is too far away.`와 `You must wait to perform another action.`은 한 번 더 시도할 시체로 본다. 인게임 확인됨 2026-10-07.
`config__sysmsg`는 전투 대상 변화·칼질 요청과 결과·codex 전환·회복과 버프 시전·도끼 장착·골드·가죽 정리를 Journal에 남긴다.
v3의 `setlasttarget` 복원은 Set Last Target 커서를 띄워 스크립트를 멈췄다. 인게임 확인됨 2026-10-07
([razor.md](razor.md#03) 03절).
v5부터 복원을 빼고 기억한 적이 없을 때만 칼질하며, 거절이 보이면 5분 동안 회색 시체만 깎는다.
Parry Codex는 랭크가 오를 때까지 Bulwark를 쓰고, 근접 밖에서 독·출혈·질병이 걸리면 Warding으로 바꾼다.
v6은 sword codex 이름에 `sword_` 접두를 붙이고, 칼질 결과와 범죄 행위 거절을 프로필 오버헤드로 넘겼다.
같은 날 overhead 팔레트의 채도를 낮췄다 ([overheads.md](overheads.md#05) 05절).
스탠스·피니셔·어빌리티는 Arms Lore가 없어 무기 특수 확률이 기본 10%인 점을 반영해 고른다. 근거는 스크립트 CODEX STANCE와 WEAPON ABILITY 주석에 있다.
2026-10-09 v9는 힘·민첩 포션을 버프 대신 STR·DEX 값으로 판정하고 ([pvp.md](pvp.md#09.D) 09.D절), 세 스탯 포션을 따로 판정한다.
v8은 `elseif` 사슬이라 힘 포션이 떨어지면 민첩·저항 포션까지 막혔다.
2026-10-10 v10은 가벼운 Heal을 `config__use_light_heal`로 붕대 옆에서도 쓸지 정한다 (기본 0). 붕대를 쓸 수 없을 때의 대타는 그대로다.
같은 날 v11은 모듈로 조립하면서 회복·포션·버프·시약을 pvp와 같은 core 블록으로 바꿨다. 바뀐 동작은 [modules.md](modules.md#08) 08절에 있다.
현재 본문은 아직 인게임에서 확인되지 않았다.

Scripts 탭에서 Reload all scripts → Play로 먼저 확인한다. 핫키에 묶었다면 클라이언트를 재시작한다
([workflow.md](workflow.md#04.A) 04.A절). `Skinning enhanced v11 loaded`가 Journal에 떠야 한다.

| 남은 항목 | 확인할 것 |
| --- | --- |
| 전투 중 칼질 중단 | Z로 몹을 고른 뒤 V를 늦게 눌러도 그 사이 `Carve request`가 없어야 하고 V가 그 몹을 쳐야 한다. 몹이 죽고 약 1.2초 뒤부터 주변 시체를 깎는다. 칼 커서가 떠 있을 때 Z를 누르면 커서가 취소되고 시체는 전투가 끝난 뒤 다시 요청된다. `Target a new 'Last Target'` 커서가 뜨거나 V가 시체·나를 치면 실패 |
| 범죄 행위 거절 지역 | Sanctuary Dungeon에서 파란 시체를 한 번 요청한 뒤 프로필의 `[ crim, blocked ]`와 Journal의 `Carve mode: grey corpses only`가 뜨고 5분 동안 Smart Harvest만 써야 한다. 같은 파란 시체를 다시 요청하면 실패. 일반 던전에서는 거절 없이 파란 시체도 깎여야 한다 |
| 칼질 결과 오버헤드 | 깎으면 `[ carve, done ]`, 이미 깎은 시체면 `[ corpse, carved ]`, Smart Harvest가 깎을 시체를 못 찾으면 `[ corpse, out ]`, 범죄 판정이면 `[ crim, on ]`이 프로필에서 떠야 한다. 게임을 끈 상태에서 두 프로필에 넣는다. 스크립트가 같은 문장을 다시 띄우면 실패 |
| 칼 커서 종류와 도착 | 스크립트는 칼을 쓴 뒤 2초 안에 온 중립 커서에만 답한다. 칼 커서가 중립이 아니거나 2초 뒤에 오면 커서가 남아 회복·칼질이 모두 선다. 그 경우 실패이고, 남은 커서는 직접 닫는다 |
| 시체 직접 타겟 (skin_unowned 1) | 시체마다 `Carve request: corpse=...` 한 줄과 서버 응답을 기록한다. 회색·파란 몬스터 시체는 깎이고, 플레이어 시체는 `Carve skip: ... label=the remains of ...` 뒤 요청 없이 건너뛰어야 한다. 플레이어 시체를 찍거나 `You have committed a criminal act`가 다시 뜨면 실패. 인간 NPC 시체의 라벨과 건너뛴 몬스터 시체 라벨도 기록한다. 라벨을 늦게 받아 비어 있으면 몬스터 시체도 건너뛴다. `Carve done`·`Carve miss`·`Carve refused`·`Carve no reply` 중 하나가 요청마다 남아야 한다. 너무 멀거나 바쁜 시체는 한 번 더 요청하고 (`One more try`), 두 번째도 실패하면 `Skipped`. 같은 시체를 세 번 이상 찍으면 실패 |
| Smart Harvest (skin_unowned 0) | 회색 시체가 깎인 뒤 `worth carving`이 든 응답이 오면 2칸 안 시체를 모두 건너뛰어야 한다. 파란 시체만 있으면 self 한 번 뒤 건너뛴다. 위키는 한 번에 가장 가까운 시체라고도, 2칸 안 회색 시체 전부라고도 적었으니 실제 동작을 기록한다. 응답 문구가 달라 시체가 있는 동안 2초마다 self가 반복되면 실패 |
| Two-Handed Axe 재장착 | 왼손을 비우면 저장한 도끼 (없으면 graphic 5187)를 다시 든다. 손에 든 도끼는 라벨의 `two-handed axe`로 한 번 저장한다. item-list의 5187이 아닌 다른 graphic의 도끼면 백팩 검색이 실패하니 `config__axe_graphic`을 바꾼다. 시전 중에는 장착하지 않아야 한다. 무장 해제 뒤 장착이 거절되면 2초마다 다시 시도하고, 장착 때문에 자기 주문이 끊기면 실패 |
| Magery 자기 회복·버프 | 워모드를 켜고 싸우는 중에도 손실 45부터 Greater Heal이 나가야 한다. 붕대가 있으면 가벼운 Heal은 쓰지 않는다 (`config__use_light_heal` 1이면 붕대 옆에서도 쓴다). 독이면 Cure 포션이 먼저다. 포션이 없을 때만 Smart Heal/Cure로 푼다. 포션과 주문이 같은 독에 함께 나가면 실패. RA와 Reflect는 상시 유지한다. 마나가 RA 24, Reflect 34 이상이면 건다. 손실 35 이상이거나 독이면 시작하지 않고, 시전 중 그렇게 되면 Interrupt로 끊는다. 버프 시전 동안 근접 타격이 멈추는 시간도 기록한다. 시약이 없으면 30초 안에 다시 확인해야 한다 |
| v11 core 회복 (모듈 조립) | 재시도 타이머 없이도 같은 행동이 패스마다 되풀이되지 않아야 한다. 큐어 포션 → 힐 포션 (35) → Greater Heal (45, 그 패스에 포션이 안 나갔을 때) → 붕대 → Refresh (60 이하) 순이다. 붕대가 우리 시전 중에도 시작되는지, 그때 시전이 끊기지 않는지 본다. 버프는 빠지면 바로, 독·손실 35 이상이면 시작하지 않고 끊는다. 힐 포션 쿨 라벨·`[ refresh, out ]`·`[ str, out ]` 경고는 이제 뜨지 않는다. Journal은 `Agent: …`·`Buff: …` |
| 스탯 포션 | 기억한 적이 있을 때 STR 120·DEX 100 아래면 힘·민첩 포션을 5초에 한 번, 저항 버프가 빠지면 마신다. 아군 Bless가 걸려 있어도 마셔야 하고, 힘 포션이 떨어져도 민첩·저항은 계속 나가야 한다 |
| 골드 버리기 | 최대 무게를 넘으면 한 패스에 2000골드를 발밑에 버리고 `[ gold, dropped ]`가 뜬다. 버리는 사이에도 회복이 돌아야 한다. 골드가 없으면 `[ weight, over ]`만 뜬다. 무게를 넘지 않았는데 버리면 실패 |
| 가죽 정리 | 칼질로 나온 가죽이 item-list의 `cut up leather` 4225인지 확인한다. 다른 graphic (hides 등)이면 검색에 더한다. 기억한 적이 없을 때만 2분마다 돈다. 파우치 안 묶음만 ignore하고 목록을 비우지 않으므로, 정리 뒤 깎은 시체에 다시 요청하면 실패. 이미 파우치에 든 가죽을 다시 옮겨도 실패다. 거절된 이동은 2.5초 예산 안에서 다시 시도한다 |
| 시체가 Last Target일 때 | 기억한 적이 없을 때 시체를 깎으면 Last Target이 바닥의 시체가 된다. 캐시는 `0x40000000 > serial`로 모빌만 `dead`·`noto`에 넘긴다. Mobile not found나 Script Error로 멈추면 실패 |
| Sword Codex 라벨 | `debug/dump-label`로 sword codex 라벨에 스탠스 이름과 `Execute`·`Bleed Out`이 보이는지 확인한다. 피를 60 넘게 잃으면 `[ sword, defensive ]`, 48 아래로 차면 `[ sword, warrior ]`가 되어야 한다. Bleed Out이 선택돼 있으면 `[SwordsFinisher2`로 Execute로 바뀌는지, 피니셔가 꺼져 있으면 명령 없이 `[ execute, off ]`만 뜨는지 본다. 라벨에 스탠스 이름이 없으면 `[ sword stance, off ]` |
| Parry Codex | `debug/dump-label`로 shield codex 라벨에 스탠스 이름과 `Last Stand`·`Barrier`가 보이는지 확인한다. 기본은 Bulwark다. Testudo 랭크가 오르면 `config__parry_stance_main`을 `config__parry_stance_testudo`로 바꾼다. 기억한 적이 2칸 밖에 있거나 없을 때 독·출혈·질병이 걸리면 `[ parry, warding ]`, 풀리면 `[ parry, bulwark ]`가 떠야 한다. 2칸 안에서 싸우는 중에는 주 스탠스를 유지한다. 출혈·질병 중에 Warding으로 바뀌지 않으면 `findbuff "Bleed"`·`"Disease"`의 버프 이름을 확인한다. 스탠스 이름이 없으면 명령 없이 `[ parry stance, off ]`만 뜨고 이번 Play 동안 멈춘다. 같은 스탠스 명령이 3초마다 반복되면 실패 |
| Chop 간격 | 기억한 적이 2칸 안에 있으면 `[ chop ]` 뒤 다음 타격에 나가는지 확인한다. Arms Lore가 없으니 60초 간격이 맞는지도 본다 |

::part[사냥]

## <a id="12"></a>12 tamer-mage-enhanced 인게임 확인

2026-10-10 사용자가 지금 쓰지 않는다고 해서 `script/archive/`로 옮겼다가, 같은 날 레시피로 조립하면서 `script/combat/`으로 되돌렸다 (v6).
바뀐 동작은 [modules.md](modules.md#08.E) 08.E절에 있다.

2026-10-09 `combat/tamer-mage-enhanced.razor` v1을 만들었다. Animal Lore·Animal Taming·Veterinary 120, Magery·Tracking 100,
Resisting Spells·Meditation 80 템플릿용이다. bard-necro-enhanced의 생존·전투 대상·타겟 주문 모양과 lumberjack-enhanced의 Tracking 설정을 가져왔다.
펫 명령과 대상 지정은 수동이고, 워모드를 켜면 Flamestrike·Bless·Arch Protection·Create Food가 선다.

설계 근거는 위키다. 수의사 키트 (Veterinary Supplies)는 붕대와 같은 5초 뒤 2칸 안 내 펫 전부를 치료하고, 해독·부활은 50% (펫 하나면 75%)이며,
쓰면 진행 중 붕대가 취소된다 ([Veterinary](https://wiki.uooutlands.com/Veterinary)). 사용자는 힐링 코덱스로 사거리를 3 늘려 5칸으로 쓴다.
Bless는 9마나·2분, Arch Protection은 11마나·2분으로 나와 6칸 안 아군 전부의 AR을 올리고, Flamestrike는 40마나다
([Magery](https://wiki.uooutlands.com/Magery)). Razor `diffhits`는 내 체력만 읽어 펫 체력에 따른 자동 GH는 넣지 않았다.
주문 이름은 클라이언트 `spells.def`의 `Flamestrike`·`Bless`·`Arch Protection`·`Create Food`다.

같은 날 사용자가 버프 바를 확인했다. Bless는 `Strength`·`Agility`·`Cunning` 세 아이콘으로 뜨고
(시스템 메시지는 `Your strength/dexterity/intelligence has changed by 11`), Arch Protection은 `Protection`으로 뜬다.
Strength·Agility는 스탯 포션과 겹치므로 v2는 Bless를 `Cunning`으로, Arch Protection을 `Protection`으로 판정하고 시전 시각 타이머를 없앴다.
힘·민첩 포션도 버프 이름에 Potion이 없어 (사용자 확인) 버프로는 Bless와 구분되지 않는다. 위키 BuffIcons의 `Strength Potion Usage Cooldown`은 표의 라벨일 뿐이다.
그래서 포션은 스탯 값으로 판정한다. 포션을 마신 값 (기본 + 20)을 `config__str_potion`·`config__dex_potion`에 두고 그보다 낮으면 마신다.
Bless만 걸린 상태 (기본 + 11)는 그보다 낮다. 거절된 마시기가 회복 포션과 같은 아이템 큐를 패스마다 차지하지 않도록 5초 재시도 간격을 둔다.
사용자는 수의사 키트가 나와 주변 팔로워를 함께 치료하고, 아무도 치료가 필요 없거나 팔로워가 멀면
`You or your nearby followers do not require healing.`만 남기고 적용되지 않는다고 확인했다.
그래서 v3은 펫 지정·거리 확인을 없애고 키트를 셀프 붕대로 쓴다.
v4는 프로필 오버헤드에 등록된 `You begin using veterinary supplies`·`You finish using veterinary supplies`로 키트가 도는 동안을 잡는다.
도는 동안은 다시 쓰지 않고 (다시 쓰면 진행 중 치료가 취소된다), 피가 1이라도 빠지면 바로, 풀피면 끝난 직후와 거절 2초 뒤에 펫용으로 쓴다.
v5는 가벼운 Heal 에이전트를 `config__use_light_heal`로 켜고 끄며 기본은 끈다. 사용자가 너무 자주 나간다고 해서,
회복은 키트·힐 포션·GH만 쓴다. 독일 때 큐어 포션이 없으면 쓰는 Smart Heal/Cure는 그대로다.
나머지 본문은 아직 인게임에서 확인되지 않았다.

새 파일이므로 Scripts 탭에서 Reload all scripts → Play로 먼저 확인한다. 핫키에 묶었다면 클라이언트를 재시작한다
([workflow.md](workflow.md#04.A) 04.A절). `Tamer mage enhanced v6 loaded`가 Journal에 떠야 한다. 핫키는 `Play Script: combat\tamer-mage-enhanced`다.

| 남은 항목 | 확인할 것 |
| --- | --- |
| 수의사 키트 | 내 피가 1이라도 빠지면 키트가 돌고 있지 않은 한 바로 `[ vet, on ]`이 떠야 한다. `[ vet, on ]`부터 `[ vet, done ]`까지는 다시 쓰지 않아야 하고, 끝나면 바로 다음 시도가 나간다. 아무도 다치지 않았으면 `You or your nearby followers do not require healing.`이 약 2초마다 한 번 남아야 한다. 더 잦거나 더 뜸하면 기록한다. 치료 중 키트가 끊기면 실패. 거절 때 키트가 줄지 않는지, 키트 시간이 실제로 5초인지, 죽은 펫 부활 시도도 기록한다. 없으면 `[ vet kit, out ]` |
| Bless·Arch Protection | 교전 중이 아니고 (전투 대상이 10칸 밖이거나 없음) 워모드가 꺼져 있을 때 `Cunning`·`Protection` 아이콘이 없으면 커서 (Bless는 beneficial, Arch Protection은 neutral)에 자기 자신을 찍고 `Buff: Bless`·`Buff: Arch Protection`이 남아야 한다. 아이콘이 뜬 뒤 다음 패스에서 같은 주문을 다시 시전하지 않아야 한다. 2분 뒤 아이콘이 사라지면 다시 시전하는지, 펫도 Arch Protection을 받는지 펫 상태에서 확인한다 |
| Bless와 스탯 포션 | `config__str_potion`·`config__dex_potion`을 내 기본 힘·민첩 + 20으로 맞춘다 (기본값 120·45는 이 템플릿의 STR 100·DEX 25·INT 100 기준). Bless가 걸린 채 전투에 들어가도 힘·민첩 포션이 한 번씩 나가고, 마신 뒤 5초마다 다시 눌리지 않아야 한다. 다시 눌리면 값이 높거나 포션이 +20이 아니다. 포션 (+20)이 Bless (+11)를 덮어쓰는지 (120) 쌓이는지 (131), 포션이 끝난 뒤 `Cunning`이 남은 동안 Bless의 힘·민첩이 살아 있는지도 본다. 사라진다면 그동안은 Bless를 다시 걸지 않는다. 저항 포션은 아직 `findbuff "Magic Resist Potion"`으로 판정하므로 버프 바에 그 이름이 뜨는지 확인한다 |
| Flamestrike | 전투 대상이 10칸 안이고 마나 51 이상이며 워모드가 꺼져 있을 때만 시전한다. 시전 중 다른 몹을 V로 고르면 커서가 취소되고 다음 패스에 새 대상으로 나가야 한다. 대상이 죽으면 취소. 손실 35 이상이면 시작하지 않고 시전 중이면 끊는다. aspect 발동 여부도 기록한다 |
| 버섯 | 마나 55 이하이고 쿨다운이 끝났으면 먹는다. 교전 중이 아니고 마나 70 이상이며 버섯이 2개 미만이면 Create Food를 시전한다. Create Food가 실제로 버섯을 만드는지 (Grimoire 단계) 확인한다 |
| Tracking | 설정한 색 필터로 Hunting이 켜지고, 감지는 프로필의 `[ track, … ]` 오버헤드로만 경고한다. Hunting이 꺼지면 5초마다 `[ track, check ]`. 귀환은 하지 않는다 |
| 이동 가드 | bard-necro-enhanced처럼 시전 블록은 `walk` 바가 돌 때 기다린다. 걷는 동안 회복 에이전트가 늦으면 기록한다. 포션은 걷는 중에도 나간다 |

::part[도구]

## <a id="13"></a>13 recycle 복귀 인게임 확인

2026-10-10 `loot/recycle`이 끝나면 마지막으로 Play한 사냥·채집 루프를 다시 켜게 했다. 전에는 마지막 줄의 `script "…"`를 루프를 바꿀 때마다 손으로 고쳤다.
recycle에는 원작자가 넣어 둔 같은 장치가 있었다. 아이템 ID를 못 해 일찍 끝날 때 이전 스크립트 리스트의 항목을 `hotkey`로 실행한다.
원작자 저장소에는 이 리스트를 읽는 스크립트만 있고 채우는 스크립트는 없어, 쓰는 사람이 채운다.
그 리스트 이름을 저장소 규칙대로 `list__resume_script`로 바꾸고, recycle 마지막 줄도 같은 모양으로 바꿨다.
bard-necro-enhanced·skinning-enhanced·lumberjack-enhanced가 Play할 때 자기 핫키 이름을 이 리스트에 넣는다.
tamer-mage-enhanced와 dexxer-basic도 넣는다. archive로 옮긴 bard-mace·bard-throwing은 `Play Script: archive\…` 이름으로 넣는다.
pvp는 싸울 때만 켜므로 등록하지 않는다.

핫키 이름은 프로필 xml이 F1을 저장한 모양 `Play Script: gather\skinning-enhanced`를 따랐다. `hotkey`가 이 이름으로 스크립트를 켜는지,
따옴표 안의 `\`가 그대로 넘어가는지는 아직 확인되지 않았다. 변수는 단어를 `4294967295`로 읽으므로 ([razor.md](razor.md#03) 03절) 리스트에 넣는다.

| 남은 항목 | 확인할 것 |
| --- | --- |
| 복귀 | skinning-enhanced를 Play한 뒤 F3 recycle을 돌리면 끝나고 `Skinning enhanced v11 loaded`가 다시 떠야 한다. lumberjack-enhanced를 Play한 뒤에는 그쪽으로 돌아와야 한다. 아무것도 안 돌면 핫키 이름 모양이 다른 것이니 Razor Hotkeys 탭의 스크립트 이름을 기록한다 |
| ID 불가로 일찍 끝날 때 | ID 스킬·완드가 없어 `Jase says: Not able to ID items..`가 뜰 때도 같은 루프로 돌아와야 한다 |
| 등록 전 | 클라이언트를 켠 뒤 루프를 한 번도 Play하지 않고 recycle을 돌리면 아무 스크립트도 돌지 않아야 한다 |
| pvp 중 | pvp 중 recycle을 돌리면 마지막 사냥·채집 루프로 돌아간다. pvp로 돌아오길 바라면 기록한다 |
| 다시 쓴 recycle | 2026-10-10 저장소 규칙으로 다시 썼다 (변수 이름·오버헤드·대기 값·시작 4줄). 분류는 그대로여야 한다. Journal에 `Recycle check: …`가 아이템마다, 저장할 때 `[ item, saving ]`과 `Recycle save: …`가 남고, 나머지는 분해된다. 링메일 fortification·hardening·guarding·defense 스위치가 이제 먹고, studded 방어구는 studded 보관함으로 간다 (지금은 둘 다 루트 파우치). 재질을 못 읽은 방어구는 루트 파우치로 간다. 재활용 도구가 없을 때도 루프로 돌아와야 한다 |

::part[사냥]

## <a id="14"></a>14 bard-necro-enhanced 인게임 확인

2026-10-10 `combat/bard-necro-enhanced`를 레시피로 조립하게 바꿨다. 바드·네크로·공격 주문 블록의 코드는 그대로지만,
생존·포션·버프·골드는 공용 모듈로 바뀌었고 하우스키핑과 교전·이동 분기는 레시피 그룹이 만든다. 바뀐 동작은 [modules.md](modules.md#08.D) 08.D절에 있다.

| 남은 항목 | 확인할 것 |
| --- | --- |
| 시작 | Play하면 악기를 찾고 (없으면 `[ inst, pick ]`), `[ bard necro, on ]`이 뜬다 |
| 소환수 이름 | 소환 후 5초 안에 `[ name, leech ]`처럼 이름이 뜨고 네임태그가 바뀌어야 한다. 안 바뀌면 Journal을 본다. `Summon name: no known kind in its label: …`이 뜨면 그 라벨을 기록하고, 아무것도 안 뜨는데 오버헤드만 뜨면 `rename`이 거부된 것이다. 2026-10-10 고친 판은 종류를 읽었지만 (`[ name, mummy ]`) 서버가 `That name is unacceptable.`로 거절했다. 종류 단어를 피한 철자로 바꾼 뒤 `mumi`는 받아졌지만 `wytch`는 거절됐다. 한 글자 차이도 막는 것으로 보고 모든 이름을 두 글자 이상 떨어뜨렸으니 (`leech`, `vampa`, `wicca` 등), 새 이름이 받아지는지 본다 |
| Rag Witch 바디 | `mumi`는 바뀌었지만 rag witch는 안 바뀌었다 (2026-10-10). 바디 번호 740이 틀린 것으로 보고 기본 이름 `a rag witch`로도 찾게 했고, 그다음 판은 rag witch를 찾아 이름을 붙이려 했다 (`wytch`는 거절). Journal에 `a rag witch found by its name, not its body`가 뜨면 그 rag witch에 `>info`를 해서 Body 번호를 알려 준다. 그 번호를 바디 목록에 넣고 이름 찾기는 지운다. Vampire Thrall 722도 같은 출처라 확인되지 않았다 |
| 교전과 이동 | 적을 찍으면 10칸 안에서 Disco·Peace·네크로 버스트·오프너·프록이 예전 순서로 나가고, 적이 없으면 버섯·RA·Reflect·Spell Siphon·노래·Vampiric Embrace가 돈다 |
| Spell Siphon 순서 | RA와 Reflect가 빠진 채 이동하면 RA, Reflect가 먼저 서고 Siphon Magic Arrow는 그다음 패스에 나가야 한다 |
| 독과 힐 | 독에 걸린 채 다치면 큐어가 먼저 나가고 힐 포션·Greater Heal은 독이 풀린 뒤에 나간다. 예전보다 위험하게 느껴지면 기록한다 |
| 셀프 버프 끊기 | 잃은 HP 35 이상에서 RA·Reflect 시전이 끊기는 것이 거슬리면 레시피에서 `buff_max_loss`를 올린다 |
| Journal | `config__sysmsg` 1로 에이전트·버프·골드·전투 대상 줄이 남는다. 너무 많으면 레시피에서 0으로 둔다 |
| 패스 속도 | 패스 끝 0.1초 대기와 시약 10초 읽기가 붙었다. 교전 반응이 눈에 띄게 늦으면 기록한다 |
| 버섯 | 교전 중에도 마나 55 이하이고 쿨다운이 끝났으면 먹는다. Create Food는 이동 중에만 나가야 한다 |
