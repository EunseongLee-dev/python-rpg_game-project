# RPG 게임 프로젝트 - 오늘 구현 요약 (2025-09-15)

## 오늘 구현 내용

### 1. Character 클래스
- **Character**: 기본 캐릭터 속성
```python
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
```

### 2. Player & Monster 클래스
- **Player**: 체력, 공격력, 마나, 쉴드 속성 포함
- **Monster**: 체력, 공격력, 쉴드 포함
- **take_shield 메서드**: 공격 데미지에 따라 쉴드 먼저 소모, 남은 데미지는 체력에서 차감

```python
class Player(Character):
    def __init__(self, name, health, attack_power, mana, shield):
        super().__init__(name, health, attack_power)
        self.mana = mana
        self.shield = shield

    def take_shield(self, damage: int):
        if self.shield > 0:
            if damage >= self.shield:
                leftover = damage - self.shield
                self.shield = 0
                self.health -= leftover
            else:
                self.shield -= damage
        else:
            self.health -= damage
        print(f"{self.name} 의 [체력: {self.health} / 쉴드: {self.shield}]" )

class Monster(Character):
    def __init__(self, name, health, attack_power, shield):
        super().__init__(name, health, attack_power)
        self.shield = shield

    def take_shield(self, damage: int):
        if self.shield > 0:
            if damage >= self.shield:
                leftover = damage - self.shield
                self.shield = 0
                self.health -= leftover
            else:
                self.shield -= damage
        else:
            self.health -= damage
        print(f"{self.name} 의 [체력: {self.health} / 쉴드: {self.shield}]" )
```

### 3. Battle 클래스
- **Battle**: 플레이어와 몬스터의 전투 관리
- **player_attack / monster_attack**: take_shield 호출
- **fight_turn**: 한 턴 전투 진행 및 체력 체크

```python
class Battle():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def player_attack(self):
        self.monster.take_shield(self.player.attack_power)
        print(f"{self.player.name} 이(가) {self.monster.name} 을 공격! [데미지: {self.player.attack_power}]" )

    def monster_attack(self):
        self.player.take_shield(self.monster.attack_power)
        print(f"{self.monster.name} 이(가) {self.player.name} 을 공격! [데미지: {self.monster.attack_power}]" )

    def fight_turn(self):
        self.player_attack()
        if self.monster.health <= 0:
            print(f"{self.monster.name} 의 남은체력이 없으므로 패배!")
            return

        self.monster_attack()
        if self.player.health <= 0:
            print(f"{self.player.name} 의 남은체력이 없으므로 패배!")
            return
```

### 4. 테스트 예시
```python
pl1 = Player("용사", 50, 10, 10, 10)
ms1 = Monster("몬스터", 40, 6, 0)

bt1 = Battle(pl1, ms1)

bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()
```

### 5. 오늘 학습 핵심
- take_shield 메서드 구현으로 쉴드 우선 소모 후 체력 감소 처리
- Battle 클래스에서 전투 흐름(fight_turn) 구성
- 클래스와 메서드 구조를 분리하여 **재사용 가능하고 확장성 있는 설계** 경험
- 오늘 뼈대 구현 완료, 내일 스킬 기능 확장 가능

