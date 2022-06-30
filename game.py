import os
import time
import random

class Entity:
    def __init__(self):
        self.name = 'Entity'
        self.hp = 1
        self.str = 1
        
    def attack(self, target):
        dmg = self.str
        target.hp_sub(dmg)
        return dmg
    
    def hp_add(self, amount):
        self.hp += amount
        
    def hp_sub(self, amount):
        self.hp -= amount
        
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Player'
        self.hp = 10
        self.str = 1
        self.lvl = 1
        self.xp = 0
        self.gold = 0
        self.xp_table = {1: 10, 2: 25, 3: 50, 4: 100, 5: 250}
        
    def lvl_up(self):
        self.xp -= self.xp_table[self.lvl]
        self.lvl += 1
        
    def is_lvl_up_available(self):
        if self.xp >= self.xp_table[self.lvl]:
            return True
        else:
            return False
        
    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}, STR: {self.str}] - [LVL: {self.lvl}, XP: {self.xp}] - [GOLD: {self.gold}]\n'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.hp = 1
        self.str = 1
        self.reward_xp = 1
        self.reward_gold = 1
        
    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}]\n'
        
class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Rat'
        self.hp = 4
        self.str = 1
        self.reward_xp = 2
        self.reward_gold = 0
        
class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Slime'
        self.hp = 6
        self.str = 1
        self.reward_xp = 3
        self.reward_gold = 1
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.hp = 8
        self.str = 2
        self.reward_xp = 5
        self.reward_gold = 3

def random_enemy(tier=None):
    enemies = [Rat, Slime, Goblin]
    
    match tier:
        case 1:
            enemies = [Rat, Slime]
        case 2:
            enemies = [Goblin]
            
    result = random.choice(enemies)
    return result()

def msg(string, duration=0.5):
    print(f'\n{string}')
    time.sleep(duration)

def main():
    plr = Player()

    while True:
        print(plr.get_status())
        print('[HUB]\n(1) Fight\n(2) Shop')
        inp = input('> ')
        os.system('cls')
        match inp:
            case '1':
                enemy = random_enemy()
                is_player_turn = True
                while True:
                    os.system('cls')
                    print(plr.get_status())
                    print(enemy.get_status())
                    if plr.hp > 0:
                        if enemy.hp > 0:
                            if is_player_turn == True:
                                print('Choose action: (1) Attack | (2) Flee')
                                inp = input('> ')
                                match inp:
                                    case '1':
                                        dmg = plr.attack(enemy)
                                        msg(f'{plr.name} attacks for {dmg}.')
                                    case '2':
                                        msg('Fleeing!', 1)
                                        break
                                    case _:
                                        msg('You do nothing.')
                                is_player_turn = False
                            else:
                                dmg = enemy.attack(plr)
                                msg(f'{enemy.name} attacks for {dmg}.')
                                is_player_turn = True
                        else:
                            msg(f'Enemy defeated!\nReward: {enemy.reward_xp} XP | {enemy.reward_gold} Gold', 1)
                            plr.xp += enemy.reward_xp
                            plr.gold += enemy.reward_gold
                            try:
                                if plr.is_lvl_up_available():
                                    plr.lvl_up()
                                    msg('LEVEL UP!')
                            except KeyError:
                                break
                            break
                    else:
                        break
                if plr.hp <= 0:
                    msg("You've died.", 1)
                    break
            case '2':
                print('[REST]\n')
                msg('Resting...', 3)
                plr.hp_add(5)
            case '3':
                print('[SHOP]\n')
                inp = input('> ')
        os.system('cls')
    os.system('cls')
    print(f"\n    {plr.name}'s adventure is over.\n\n             The End\n")

if __name__ == '__main__':
    main()