from character import Player, Monster
from skill import AttackSkill, HealSkill

class Battle():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def reset_battle(self):
        self.player.health = self.player.max_health
        self.player.shield = self.player.max_shield
        self.monster.health = self.monster.max_health
        self.monster.shield = self.monster.max_shield
        

    def fight_turn(self, player_action = 'attack', player_skill = None, monster_skill = None):
        if player_action == 'attack':
            self.player.attack(self.monster)
        elif player_action == 'skill' and player_skill is not None:
            self.player.use_skill(player_skill, self.monster)

        if self.monster.health <= 0:
            print(f"{self.monster.name} 의 남은체력이 없으므로 패배!")
            amount = self.monster.drop_gold()
            self.player.add_gold(amount)
            drop = self.monster.drop_item()
            if drop.type == 'gold-item':
                self.player.add_gold(drop.value)
            else:
                self.player.add_item(drop)
            return
        
        if player_action == 'attack':
            self.monster.attack(self.player)
        elif player_action == 'skill' and monster_skill is not None:
            self.monster.use_skill(monster_skill, self.player)

        if self.player.health <= 0:
            print(f"{self.player.name} 의 남은체력이 없으므로 패배!")






        
pl1 = Player("용사", 50, 10, 50, 10)
pl1.skills = [AttackSkill("파이어볼", 15, 10)]
pl1.skills.append(HealSkill("큐어", 10, 5))

ms1 = Monster("몬스터", 40, 6, 30, 10)
ms1.skills = [AttackSkill("할퀴기", 10, 5)]
ms1.skills.append(HealSkill("힐", 10, 5))


bt1 = Battle(pl1, ms1)

bt1.fight_turn()
bt1.fight_turn(player_action='skill', player_skill=pl1.skills[0], monster_skill=ms1.skills[0])
bt1.fight_turn(player_action='skill', player_skill=pl1.skills[1], monster_skill=ms1.skills[1])
bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()

bt1.reset_battle()

bt1.fight_turn()
bt1.fight_turn(player_action='skill', player_skill=pl1.skills[0], monster_skill=ms1.skills[0])
bt1.fight_turn(player_action='skill', player_skill=pl1.skills[1], monster_skill=ms1.skills[1])
bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()
bt1.fight_turn()

print(pl1.gold)
pl1.inventory.show_inventory()



print(__file__)