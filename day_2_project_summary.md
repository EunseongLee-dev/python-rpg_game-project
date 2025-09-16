# 오늘 진행한 프로젝트 작업 정리 (GitHub용)

## 1. Character 모듈 수정
### Player 클래스
- Character 클래스를 상속받아 Player 클래스 생성
- `shield` 속성 추가 (플레이어 보호막)
- `skills` 속성 추가 (플레이어가 사용할 스킬 리스트)
- 메서드
  - `take_damage(damage)`
    - 쉴드 우선으로 피해 계산
    - 체력 감소 후 상태 출력
  - `use_mp(cost)`
    - MP 체크 후 소모
    - 부족하면 메시지 출력 및 False 반환, 충분하면 True 반환
  - `attack(target)`
    - target.take_damage 호출
    - 공격 메시지 출력
  - `use_skill(skill, target)`
    - use_mp 체크 후 skill.activate 호출

```python
class Player(Character):
    def __init__(self, name, health, attack_power, mp, max_mp, shield, skills=None):
        super().__init__(name, health, attack_power, mp, max_mp)
        self.shield = shield
        self.skills = skills

    def take_damage(self, damage: int):
        if self.shield > 0:
            if damage >= self.shield:
                leftover = damage - self.shield
                self.shield = 0
                self.health -= leftover
            else:
                self.shield -= damage
        else:
            self.health -= damage

        print(f"{self.name} 의 [체력: {self.health} / 쉴드: {self.shield}]")

    def use_mp(self, cost: int):
        if self.mp >= cost:
            self.mp -= cost
            return True
        else:
            print(f"{self.name} 의 마나가 부족합니다. [MP: {self.mp}]")
            return False

    def attack(self, target):
        target.take_damage(self.attack_power)
        print(f"{self.name} 이(가) {target.name} 을 공격! [데미지: {self.attack_power}]")

    def use_skill(self, skill, target):
        if self.use_mp(skill.mp_cost):
            skill.activate(self, target)
```

## 2. Skill 모듈 생성
### Skill 클래스
- 스킬 이름, 효과 타입, 위력, MP 소모량 정의
- 메서드
  - `activate(user, target)`
    - effect_type에 따라 공격, 회복 처리
    - 결과 메시지 출력

```python
class Skill():
    def __init__(self, name, power, mp_cost, effect_type):
        self.name = name
        self.power = power
        self.mp_cost = mp_cost
        self.effect_type = effect_type

    def activate(self, user, target):
        if self.effect_type == 'attack':
            target.take_damage(self.power)
            print(f"공격 스킬 {self.name}! [데미지: {self.power}]")
        elif self.effect_type == 'heal':
            user.health += self.power
            print(f"회복 스킬 {self.name}! [회복량: {self.power}]")
```

## 3. Battle 모듈 수정
- fight_turn 메서드 개선
  - player_action에 따라 기본 공격 또는 스킬 사용 분기
  - 스킬 사용 시 Player 클래스의 use_skill 메서드 호출

```python
from character import Player, Monster
from skill import Skill

class Battle():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def fight_turn(self, player_action='attack', skill=None):
        if player_action == 'attack':
            self.player.attack(self.monster)
        elif player_action == 'skill' and skill is not None:
            self.player.use_skill(skill, self.monster)

        if self.monster.health <= 0:
            print(f"{self.monster.name} 의 남은체력이 없으므로 패배!")
            return

        # 몬스터 기본 공격
        self.monster.take_damage(self.player.attack_power)  # 추후 몬스터 attack 메서드로 교체 가능
        print(f"{self.monster.name} 이(가) {self.player.name} 을 공격! [데미지: {self.player.attack_power}]")

        if self.player.health <= 0:
            print(f"{self.player.name} 의 남은체력이 없으므로 패배!")
            return
```

---

### 오늘 정리 포인트
1. Player 클래스: 쉴드, 스킬, MP 소모, 공격 메서드 재조정
2. Skill 클래스: 공격/회복 스킬 정의 및 activate 메서드 구현
3. Battle 클래스: fight_turn에서 공격/스킬 분기 처리 및 출력 순서 조정

> 오늘 목표는 플레이어 중심으로 스킬과 기본 공격 로직을 통합하고, 출력 순서를 정리하여 테스트 가능한 상태로 만드는 것

