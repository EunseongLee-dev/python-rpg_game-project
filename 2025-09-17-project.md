# 파이널 프로젝트 - 3일차 작업 정리

## 오늘 작업 내용 요약

### 1. 스킬 모듈 구조 개편
- 기존 Skill 클래스 하나로 공격, 회복 스킬을 처리하던 구조를
  `AttackSkill`, `HealSkill` 클래스로 분리
- Skill 클래스는 부모 클래스로 유지, 공통 속성(name, power, mp_cost)만 관리
- 각각의 activate 메서드를 오버라이딩하여 공격/회복 로직 구분

```python
class Skill():
    def __init__(self, name, power, mp_cost):
        self.name = name
        self.power = power
        self.mp_cost = mp_cost

    def activate(self, user, target):
        raise NotImplementedError

class AttackSkill(Skill):
    def activate(self, user=None, target=None):
        target.health -= self.power
        print(f"공격 스킬 {self.name}! [데미지: {self.power}]")
        print(f"{target.name} 의 [체력: {target.health} / 쉴드: {target.shield}]")

class HealSkill(Skill):
    def activate(self, user, target=None):
        before = min(user.health + self.power, user.max_health)
        actual_heal = before - user.health
        user.health = before
        print(f"회복 스킬 {self.name}! [회복량: {actual_heal}]")
        print(f"{user.name} 의 [체력: {user.health} / 쉴드: {user.shield}]")
```

- `user`와 `target`은 필요에 따라 `None` 처리
- 힐은 user만, 공격은 target만 사용하는 구조로 통일

---

### 2. Player 클래스 use_skill 메서드 수정
- 기존 Skill 사용 시 Skill 클래스 그대로 사용하던 부분을
  AttackSkill/HealSkill로 변경
- 기본적으로 스킬 리스트에서 선택하여 activate 호출

```python
pl1.skills = [AttackSkill("파이어볼", 15, 5)]
pl1.skills.append(HealSkill("힐", 10, 5))

# 스킬 사용
self.player.use_skill(skill, self.monster)
```

---

### 3. Battle 클래스 수정
- fight_turn 메서드 구조 변경
- 공격/스킬 사용 여부를 player_action과 skill 파라미터로 구분
- 체력 음수 방지 처리 추가 (`max` 사용)
- 출력 순서 조정하여 턴별 상태 출력 명확화

```python
if self.monster.health <= 0:
    print(f"{self.monster.name} 의 남은체력이 없으므로 패배!")
    return

if self.player.health <= 0:
    print(f"{self.player.name} 의 남은체력이 없으므로 패배!")
```

- 몬스터 스킬은 아직 구현하지 않았으므로 공격만 수행
- 추후 몬스터 스킬 추가 시 구조 확장 가능

---

### 4. 체력 및 쉴드 처리 개선
- take_damage 메서드 수정
- 체력/쉴드 차감 후 음수 방지
- max/min 활용하여 한 줄로 처리 가능

```python
self.health = max(self.health, 0)
self.shield = max(self.shield, 0)
```

---

### 5. 출력 개선
- 스킬 사용 시 단순 메시지 대신 대상과 본인의 체력/쉴드 상태 출력
- Battle에서 순서대로 공격 및 스킬 출력 정리
- print 위치를 skill 모듈 내 activate에서 처리하지 않고, Character/Battle에서 상태 확인 후 출력

---

### 6. 기타
- 기존 skills 리스트에 `append` 방식으로 스킬 추가
- 기존 Skill 클래스 기반의 초기화 코드 수정 필요 (AttackSkill/HealSkill로 교체)
- 현재 프로젝트는 테스트 단계이므로 몬스터 스킬은 최소 1개만 추가 예정
- 오늘 작업은 구조 분리, 출력 개선, 음수 처리, 스킬 리스트 정리 등 부수적 개선 중심

