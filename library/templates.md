# 템플릿 ↔ 파일 매핑

캐릭터(템플릿) 하나를 굴릴 때 필요한 파일이 어디 있는지 한 표로. 빈 칸은 집에서 채운다.

| 템플릿 | 전투 루프 `script/combat/` | 핫키 `script/hotkey/` | Shelf `script/home/` | Razor 프로필 `config/<이름>/razor/profiles/` | CUO 캐릭 `config/<이름>/classicuo/` |
|---|---|---|---|---|---|
| Bard Necro | `bard-necro` | `bard-buff` | | | |
| Bard Necro (Eval) | `bard-necro-eval` | `bard-buff` | | | |
| Bard Mace (Dexxer) | `bard-mace` | `bard-buff`, `weapon-*` | `shelf-bard-dexxer` | | |
| Bard Mage | `bard-mage`, `bard-mage-summon` | `bard-buff` | | | |
| Bard Archer | `bard-archer`, `bard-archer-no-potion` | `bard-buff` | | | |
| Hally Mage | `hally-mage` | `weapon-halberd`, `weapon-katana`, `weapon-viking-sword` | `shelf-hally-mage` | | |
| Dexxer | `dexxer-basic` | `weapon-*` | | | |
| Thief / Backstab | `backstab-mugging` | | | | |
| Sailing | `sea-cleaner` | | `shelf-sailing` | | |

공용: `cancel-target`, `dress`, `field/*`, `home/*` (shelf 제외)
