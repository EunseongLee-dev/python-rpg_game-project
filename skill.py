class Skill():
    def __init__(self, name, power, mp_cost):
        self.name = name
        self.power = power
        self.mp_cost = mp_cost


    def activate(self, user, target):
        raise NotImplementedError
        
class AttackSkill(Skill):
    def __init__(self, name, power, mp_cost):
        super().__init__(name, power, mp_cost)

    def activate(self, user=None, target=None):
        print(f"{user.name} 의 공격 스킬 {self.name}! [데미지: {self.power}]")
        target.take_damage(self.power)

class HealSkill(Skill):
    def __init__(self, name, power, mp_cost):
        super().__init__(name, power, mp_cost)

    def activate(self, user, target=None):
        if user is None:
            return
        before = user.health
        user.health = min(user.health + self.power, user.max_health)
        actual_heal = user.health - before
        print(f"{user.name} 의 회복 스킬 {self.name}! [회복량: {actual_heal}]")
        print(f"{user.name} 의 [체력: {user.health} / 쉴드: {user.shield}]")

        