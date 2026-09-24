# Bard Necro 전투 루프 설계

`script/combat/bard-necro-eval.razor` 를 다시 짤 때의 기준 문서. 코드가 아니라 **무엇이 무엇을 막는지**를 적어둔다.

## 왜 이 문서가 필요한가

소환수가 딜의 60% 이상을 내는데 **죽으면 바드 송 버프가 전부 날아간다.** 재소환하면 버프 없이 싸우고,
전투 중에는 3곡을 다시 부를 틈이 없다. 이걸 자동화하려면 루프 안에서 자원 경쟁을 정리해야 한다.

## 자원 세 가지

| 자원 | 쓰는 곳 | 성격 |
|---|---|---|
| `cooldown "Music"` | 노래 3곡, 디스코, 피스, 프로보 | **단일 병목.** 여기서 전부 경쟁한다 |
| Unholy Symbol | Blood Oath(4), Vampiric Embrace(3), Evil Omen | 5초당 1개, 최대 (유효 네크로/10) |
| 마나 | 본체 주문 사이클 | Eldritch 마나샘 + 버섯으로 보충 |

서로 독립이라 병렬로 돌 수 있다. 같은 자원을 쓰는 것들만 우선순위가 필요하다.

## 루프 구조

```
SETUP
  악기 확보 · 핫바 확인 · 타이머 생성
  list 'sung_followers'          버프를 받은 소환수 serial 명부
  list 'magic_cursed_targets'    커스가 걸린 대상 (기존)

while not dead

  1  SYSTEM MESSAGE      집중 방해 → replay
                         악기 분실 → 재선택

  2  생존                무게 · 힐 · 큐어 · 포션 · 버섯
                         최우선. 아래 전부를 가로막는다

  3  타겟 캐시           lasttarget → noto 검사 → 캐시
                         타겟이 바뀌면 var_magic_stage = 0 (커스 초기화)
                         디스코 재적용 필요
                         sung_followers 는 건드리지 않는다

  4  소환수 점검         findtype <4종 그래픽> ground 12 훑기
                         noto 필터로 적 라이치 제외
                         not inlist 'sung_followers' 면 var_resing = 1

  5  바드                cooldown "Music" 하나를 두고 경쟁
                         1순위  var_resing = 1  → 3곡 + 명부 재작성
                         2순위  노래 버프 없음   → 3곡 (15분 만료 경로)
                         3순위  디스코 미적용    → 디스코
                         4순위  피스 / 프로보

  6  네크로              symbols >= 4 → Blood Oath (followers > 0 필요)
                         symbols >= 3 → Vampiric Embrace (시체 필요)
                         Evil Omen   → 본체 주문 스팸 직전에

  7  본체 주문           커스 안 걸림 → Curse (var_magic_stage 0 → 1)
                         커스 걸림   → Grimoire proc 로테이션
                            magic_arrow_proc_timer >= 15초 → Magic Arrow
                            harm_proc_timer        >= 15초 → Harm
                            fireball_proc_timer    >= 15초 → Fireball
                            lightning_proc_timer   >= 15초 → Lightning
                            전부 쿨이면 → 일반 주문

endwhile
```

## 설계 결정

**재소환 감지를 바드 블록과 분리한다.** 4가 플래그만 세우고 5가 소비한다. 감지는 매 패스 돌아도
서버 왕복이 없고(`findtype` + `inlist`), 재시전은 플래그가 섰을 때만 Music 쿨을 쓴다.

**재소환 재시전이 디스코보다 우선이다.** 소환수가 딜의 60% 이상인데 버프 없이 싸우는 시간이 가장 비싸다.

**타입이 아니라 serial 로 추적한다.** 같은 종류를 두 마리 데리고 다닐 수 있기 때문에
(라이치 2마리 등) 타입별 슬롯으로는 한 마리만 잡힌다. `list` + `inlist` 면 마리 수와 종류에 제한이 없다.

**명부는 재시전 직후에 새로 쓴다.** 그 시점에 나와 있는 전원이 버프를 받았으므로
`removelist` → `createlist` → 현재 소환수를 다시 `pushlist`. 명부가 무한히 자라지 않는다.

**noto 필터가 필수다.** 적 라이치와 내 라이치가 같은 그래픽이다. `bard-necro.razor:433` 의 필터를 그대로 쓴다.

**타겟 스위칭은 명부를 건드리지 않는다.** 몹이 바뀌어도 소환수는 그대로다. 반대로 `var_magic_stage` 는
타겟 종속이라 3에서 리셋해야 한다.

## 쓸 수 있는 구문 (전부 저장소에 선례 있음)

| 구문 | 선례 |
|---|---|
| `not inlist '이름' alias` | `bard-necro.razor:787` |
| `createlist` / `removelist` / `pushlist` | 여러 파일 |
| `while findtype ... ground -1 -1 12 as` + `@ignore` | `bard-necro.razor:432` |
| `not dead X and noto X != "hostile" ...` | `bard-necro.razor:433` |
| `var__x != alias__y` | `bard-throwing.razor:412` |

## 쓰면 안 되는 구문 (선례 없음, 실제로 깨졌던 것들)

- 산술 `@setvar! var__n var__n + 1`
- `while <스크립트 변수> <` (내장 표현식은 가능, 스크립트 변수는 선례 없음)
- `menu <serial> <변수>` — 인덱스는 반드시 리터럴
- 조건 안의 괄호
- 미선언 변수 (`check.sh` 가 못 잡는다)
