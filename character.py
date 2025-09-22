from item import Item, Inventory

class Character:
    def __init__(self, name, health, attack_power, mp):
        self.name = name
        self.health = health
        self.max_health = health 
        self.attack_power = attack_power
        self.mp = mp
        self.max_mp = mp

class Player(Character):
    from skill import AttackSkill, HealSkill
    def __init__(self, name, health, attack_power, mp, shield, skills = None):
        super().__init__(name, health, attack_power, mp)
        self.shield = shield
        self.max_shield = shield
        self.skills = skills
        self.gold = 0
        self.inventory = Inventory([])

    def take_damage(self, damage: int):
        if self.shield > 0 and damage >= self.shield:
            leftover = damage - self.shield
            self.shield = 0
            self.health -= leftover
        elif self.shield > 0 and damage <= self.shield:
            self.shield -= damage
        else:
            self.health -= damage

        self.health = max(self.health, 0)
        print(f"{self.name} 의 [체력: {self.health} / 쉴드: {self.shield}]")

    def attack(self, target):
        print(f"{self.name} 이(가) {target.name} 을 공격! [데미지: {self.attack_power}]")
        target.take_damage(self.attack_power)
        

    def use_mp(self, cost: int):
        if self.mp >= cost:
            self.mp -= cost
            return True
        else:
            print(f"{self.name} 의 마나가 부족합니다. [MP: {self.mp}]")
            return False
        
    def use_skill(self, skill, target):
        if self.use_mp(skill.mp_cost):
            skill.activate(self, target)

    def add_gold(self, amount: int):
        self.gold += amount
        print(f"{self.name} 이(가) Gold({amount}) 획득했습니다! [현재 골드:{self.gold}]")

    def add_item(self, item):
        self.inventory.add_item(item)
        print(f"{self.name} 이(가) {item.name} 을(를) 획득했습니다! [티어: {item.value}]")
class Monster(Character):
    def __init__(self, name, health, attack_power, mp, shield, skills = None):
        super().__init__(name, health, attack_power, mp)
        self.shield = shield
        self.max_shield = shield
        self.skills = skills

    def take_damage(self, damage: int):
        if self.shield > 0 and damage >= self.shield:
            leftover = damage - self.shield
            self.shield = 0
            self.health -= leftover
        elif self.shield > 0 and damage <= self.shield:
            self.shield -= damage
        else:
            self.health -= damage

        self.health = max(self.health, 0)
        print(f"{self.name} 의 [체력: {self.health} / 쉴드: {self.shield}]")

    def attack(self, target):
        print(f"{self.name} 이(가) {target.name} 을 공격! [데미지: {self.attack_power}]")
        target.take_damage(self.attack_power)

    def use_mp(self, cost: int):
        if self.mp >= cost:
            self.mp -= cost
            return True
        else:
            print(f"{self.name} 의 마나가 부족합니다. [MP: {self.mp}]")
            return False
        
    def use_skill(self, skill, target):
        if self.use_mp(skill.mp_cost):
            skill.activate(self, target)

    def drop_gold(self):
        return Item.drop_gold(self)
    
    def drop_item(self):
        return Item.drop_item(self)
    
