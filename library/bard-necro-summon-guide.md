# Bard-Necro 소환 조합 · Tome 투자 가이드

소환수 조합과 `Summoner's Tome` 포인트 배분. 전투 루프 설계는 `bard-necro-combat-design.md` 를 본다.

## 캐릭터 전제

| 스킬 | 값 |
|---|---|
| Discordance / Peacemaking / Provocation | 80 / 80 / 80 |
| Musicianship | **0 (Bard Codex `Self Taught` T2 로 대체)** |
| Spirit Speak | 120 |
| Herding | 80 |
| Necromancy | 100 |
| Magery | 100 |
| Eval Int | 80 |

- **바딩 3종을 전부 찍었다.** `Self Taught` 가 "lowest printed skill amongst Discordance,
  Peacemaking, Provocation" 80 점을 Musicianship 대체로 쓰게 해준다. Musicianship 슬롯이
  통째로 비므로 Provocation 을 넣을 수 있다.
- **Meditation / Inscription 없음.** 본체 주문 사이클이 마나에 묶여 있다.
- 테이머 듀오와 함께 다니는 경우가 많다. **본체는 후열이다.**
- 주 사냥터 난이도 **300~500**. 전투 사이클은 한 마리 잡고 10~20초 이동해서 다음 한 마리다.
- 바드 숫자와 공식은 전부 `bard-mechanics.md` 에 있다. **여기서 다시 추론하지 않는다.**

## 측정 결과

인게임 데미지 트래커 기준.

| 구성 | 소환수 딜 비중 |
|---|---|
| 바딩 120 x3 / SS 80 / Eval 80 | 47.6% |
| 바딩 80 x3 / SS 120 / Eval 80 | **63.4%** |

**소환수가 딜의 3분의 2다.** 바딩을 120으로 올려 얻는 것보다 SS 를 120으로 올려
소환수 계수를 키우는 쪽이 훨씬 크다. 바딩 3개를 80으로 통일한 근거가 이것이다.

- 바딩 최소 성공률은 `33% x (유효/100)` 이라 80 에서도 실용 구간이 나온다.
- 바딩 지속시간은 난이도 300~500 구간에서 바닥값 `15초 x (Musicianship/100)` 이 지배한다.
  Musicianship 을 120으로 올려도 이 구간에서는 체감이 작다.
- Herding 80 이 팔로워 데미지 `22% x (유효 Herding/100)` 과 저항 `11%` 를 얹는다.
  크룩을 활성화해두면 패시브로 붙는다.

## 한 줄 결론

| 상황 | 조합 |
|---|---|
| **테이머 듀오 (기본)** | **Lich 2마리.** 테이머 펫이 전선을 잡으니 후열 딜에 전부 투자한다 |
| 테이머 듀오 + 장기 교전 | `Vampire 2마리`. Fury 가 3분이면 캡이라 실전성이 있다 |
| 솔플 | `Mummy + Lich`. 탱커 없이 후열만 세울 수 없다 |
| 고 Magic Resist 맵 | `Mummy + Air`. **물리 딜이 필요한 유일한 경우다** |

**Lich 와 Vampire 는 둘 다 주문 딜러다.** Vampire 위키에 `Spell Damage: 26 - 32` 로 명시돼 있다.
따라서 본체의 `Mana Drain` (`-20 Magic Resist`) 과 Fire Tome 의 `Hex` 가 **두 조합 모두에 걸린다.**
물리 딜러는 `Mummy` 와 `Air` 뿐이다.

**소환수 스탯은 반드시 SS 120 기준 스케일 표로 본다.** 위키의 기본 스탯은 낮은 SS 기준이라
실제 수치와 다르다. Herding 80 의 `+22% 팔로워 데미지` 도 그 위에 얹힌다.

## 왜 Lich 2마리인가 (테이머 듀오 기준)

- 테이머 펫이 어그로를 잡아주므로 **탱커 소환수가 필요 없다.** Mummy 슬롯을 딜로 바꿀 수 있다.
- Lich 는 `Epic Barrage` 로 거리를 유지하면서 딜을 넣는다. 후열 포지션과 맞는다.
- Fire Tome 의 `Scorched Earth` 가 거는 **Hex 는 대상의 마법 저항을 깎는다.**
  Lich 딜도 내 주문딜도 같이 올라간다. 본체가 마법 스팸 빌드라 시너지가 직접적이다.
- 내 `Mana Drain` 이 거는 `-20 Magic Resist` 도 같은 방향이다.
  Lich 는 주문 딜러라 이 감소를 그대로 받는다.

`Epic Barrage` 쿨타임이 30초고 관련 감소폭이 2.5초라 그 항목 자체는 결정적이지 않다.
Lich 를 고르는 이유는 어디까지나 **후열 딜 + Hex 시너지**다.

## Lich 2마리 vs Vampire 2마리

둘 다 주문 딜러라 `Mana Drain` 과 `Hex` 를 똑같이 받는다. 갈리는 지점은 **포지션과 Fury** 다.

> **Fury (Innate)**: "Damage Dealt increased by 5% for every 30 seconds alive (max +30%)"

**분당 5%가 아니라 30초당 5%다. 3분이면 캡에 도달하고 거기서 멈춘다.**
"1시간 사냥이니까 천천히 쌓여도 된다" 는 계산은 틀렸다. 반대로 **3분만 살면 되므로 문턱이 낮다.**

| | Lich 2마리 | Vampire 2마리 |
|---|---|---|
| 포지션 | 원거리. `Epic Barrage` | 근접 유지형 주문 딜러. 맞는다 |
| 딜 성장 | 없음 (즉시 최대) | 3분에 **+30%** 도달, 이후 고정 |
| 죽으면 | 뒤에 있어 잘 안 죽는다 | **Fury 0 으로 초기화.** 다시 3분 |
| Tome 시너지 | `Scorched Earth` 의 Hex 가 **파티 전체 주문딜**을 올린다 | `Bloodfuel` / `Battlecaster` / `Vengeance` 는 자기 딜만 |
| `Mana Drain -20 MR` | 적용 | 적용 |

**기본값은 여전히 `Lich 2마리` 다.** 이유는 Fury 가 아니라 **Hex 다.**
Fire Tome 의 `Scorched Earth` 가 거는 마법저항 감소는 Lich 자신, 내 주문, 그리고
테이머가 주문 딜을 넣는다면 그쪽까지 올린다. Vampire 의 Tome 업그레이드는 전부 자기 딜에만 붙는다.

`Vampire 2마리`는 **한 마리를 3분 이상 붙잡고 싸우는 장기 교전**에서 값을 한다.
지금 전투 사이클(한 마리 잡고 10~20초 이동)에서는 뱀파이어가 몹 사이를 살아서 넘어가야
Fury 가 유지된다. 테이머가 전선을 잡아주면 실현 가능하다.

> **미확인**: 몹을 바꿀 때 Fury 가 유지되는지, 전투가 끝나고 이동하는 동안에도
> "alive" 카운터가 계속 도는지 확인하지 않았다. 이동 중에도 돈다면 `Vampire 2마리`의
> 평가가 올라간다.

## 솔플

솔플이면 **`Mummy + Lich`** 다. 테이머 펫이 없으면 전선을 잡아줄 것이 필요하고,
소환수 둘이 동시에 맞으면 둘 다 녹는다. 소환수가 죽으면 3곡을 다시 불러야 해서
(`cooldown "Music"` 글로벌 5초 + 곡당 10초) **전투 중에 회복이 안 되는 손실**이다.

## Summoner's Tome 배분

**소환 주문 하나당 20 포인트.** 티어 비용은 누적으로 `T1=1 / T2=3 / T3=5`.
즉 20점은 **T3 네 개**가 정확히 맞아떨어진다.

### Fire Tome / Lich -- 최우선

주력 조합의 핵심이다.

```
Fanning The Flames   T3   5    Epic Barrage 를 직접 강화. 체감이 가장 크다
Scorched Earth       T3   5    Hex. 대상 마법저항 감소 -> Lich 딜 + 내 주문딜 동시 상승
Spirit Pact          T3   5    전투 성능 전반. 무난한 기본값
Wildfire             T3   5    멀티타겟 구간 효율
                        ---
                         20
```

`Glass Cannon` 은 뺐다. 딜은 좋지만 어그로를 끌어서, Lich 를 후열에 두는 목적과 충돌한다.
테이머 펫이 어그로를 확실히 잡아주는 것이 검증되면 `Wildfire` 와 바꿔볼 수 있다.

### Earth Tome / Ancient Mummy -- 솔플용, 두 번째

솔플 전선용. 테이머와만 다닌다면 우선순위가 내려간다.

```
Shatter        T3   5    Pierce 25. 물리 조합의 핵심
Spirit Pact    T3   5
Bedrock        T3   5    탱커 성격과 맞는다
Slam           T3   5    밀리몹 상대 체감이 좋다
                   ---
                    20
```

`Earthpull` 은 위 넷이 다 찍힌 뒤에 고려한다.

### Air Tome / Skeletal Fiend -- 고 MR 맵용, 세 번째

`Hex` 와 `Mana Drain` 으로도 저항이 안 깎이는 맵에서 물리 딜로 우회하는 카드다.

```
Tempest        T3   5    가장 중요하다
Spirit Pact    T3   5
Gale           T3   5
Microburst     T3   5
                   ---
                    20
```

`Whirlwind`, `Windshear`, `Cyclone` 은 상황형이라 후순위다.

### Daemon Tome / Vampire Thrall -- 마지막

`Vampire 2마리`를 실제로 주력으로 굴리기로 확정한 뒤에만 투자한다.

```
Bloodfuel      T3   5
Battlecaster   T3   5
Vengeance      T3   5
Spirit Pact    T3   5
                   ---
                    20
```

`Growing Fury` 는 오래 살 때만 값을 하는데, 난이도 300~500 에서 뱀파이어가 오래 사는지가
아직 확인되지 않았다. 위 넷을 먼저 채운다.

### 투자 순서

```
테이머 듀오 위주 (지금)    Fire -> Earth -> Air -> Daemon
솔플 비중이 늘면           Earth -> Fire -> Air -> Daemon
고 MR 맵을 자주 돌면       Fire -> Air -> Earth -> Daemon
```

## 스크립트 메모

- **Provocation 을 찍었으므로 provo anchor 경로가 살아 있다.** 구식 `bard-necro.razor` 의
  `var_provo_follower_kind` 는 `vampire / mummy / rag / lich` 만 인식했다.
  새 스크립트에서는 serial 추적으로 바꾼다 (`bard-necro-combat-design.md` 참조).
- `Revolution Song` (프로보한 몹이 `40/120/200%` 추가 피해) 은 Provocation 을 찍었으므로
  선택지에 들어온다. 다만 코덱스 20점 안에서 다른 것과 경쟁한다.
- `Air` 를 쓰려면 소환수 감지 `findtype` 목록에 그래픽을 추가해야 한다.
- 소환수 추적은 타입이 아니라 **serial** 로 한다. Lich 2마리처럼 같은 종류를 둘 데리고 다니면
  타입 슬롯으로는 한 마리만 잡힌다. `bard-necro-combat-design.md` 의 `sung_followers` 참조.
- **적 Lich 와 내 Lich 가 같은 그래픽이다.** `noto` 필터가 필수다 (`bard-necro.razor:433`).

## 참고 링크

- [Spirit Speak](https://wiki.uooutlands.com/Spirit_Speak)
- [Summoner's Tome](https://wiki.uooutlands.com/Summoner%27s_Tome)
- [Status Effects](https://wiki.uooutlands.com/Status_Effects) -- Hex 등
- [Ancient Mummy](https://wiki.uooutlands.com/Ancient_Mummy)
- [Skeletal Fiend](https://wiki.uooutlands.com/Skeletal_Fiend)
- [Lich](https://wiki.uooutlands.com/Lich)
- [Vampire Thrall](https://wiki.uooutlands.com/Vampire_Thrall)
- [Earth Elemental Tome Upgrades](https://wiki.uooutlands.com/Template%3ASummonersTomeEarthElemental)
- [Air Elemental Tome Upgrades](https://wiki.uooutlands.com/Template%3ASummonersTomeAirElemental)
- [Fire Elemental Tome Upgrades](https://wiki.uooutlands.com/Template%3ASummonersTomeFireElemental)
- [Daemon Tome Upgrades](https://wiki.uooutlands.com/Template%3ASummonersTomeDaemon)
