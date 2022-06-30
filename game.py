import os
import time
import random

class Entity:
    def __init__(self):
        self.name = 'Entity'
        self.hp_max = 1
        self.hp = self.hp_max
        self.str = 1
        
    def attack(self, target):
        dmg = self.str
        target.hp_sub(dmg)
        return dmg
    
    def hp_add(self, n):
        result = self.hp + n
        if result > self.hp_max:
            total = n - (result - self.hp_max)
            
            self.hp += total
            return total
        else:
            self.hp += n
            return n
        
    def hp_sub(self, n):
        self.hp -= n
        
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Player'
        self.hp_max = 10
        self.hp = self.hp_max
        self.str = 1
        self.lvl = 1
        self.xp = 0
        self.gold = 0
        self.weapon = None
        self.armor = None
        self.bed = None
        self.day = 1
        
        self.table_xp = {1: 10, 2: 20, 3: 50, 4: 100, 5: 200}
        self.table_str = {1: 1, 2: 1, 2: 2, 4: 2, 5: 3}
        self.rest = 5
        
    def lvl_up(self):
        gain_hp = self.lvl
        gain_str = self.table_str[self.lvl]
        
        self.xp -= self.table_xp[self.lvl]
        self.hp_max += gain_hp
        self.hp += gain_hp
        self.str += gain_str
        self.lvl += 1
        return gain_str
        
    def is_lvl_up_available(self):
        if self.xp >= self.table_xp[self.lvl]:
            return True
        else:
            return False
        
    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}/{self.hp_max}, STR: {self.str}] - [LVL: {self.lvl}, XP: {self.xp}] - [GOLD: {self.gold}] - [DAY: {self.day}] - [W: {self.weapon} A: {self.armor} BED: {self.bed}]\n'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.hp_max = 1
        self.hp = self.hp_max
        self.str = 1
        self.reward_xp = 1
        self.reward_gold = 1
        
    def get_status(self):
        return f' [{self.name}] - [HP: {self.hp}]\n'
        
class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Rat'
        self.hp_max = 3
        self.hp = self.hp_max
        self.str = 2
        self.reward_xp = 7
        self.reward_gold = 0
        
class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Slime'
        self.hp_max = 5
        self.hp = self.hp_max
        self.str = 1
        self.reward_xp = 6
        self.reward_gold = 1
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.hp_max = 8
        self.hp = self.hp_max
        self.str = 2
        self.reward_xp = 9
        self.reward_gold = 6
        
class Wolf(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Wolf'
        self.hp_max = 10
        self.hp = self.hp_max
        self.str = 3
        self.reward_xp = 15
        self.reward_gold = 0
        
class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Zombie'
        self.hp_max = 20
        self.hp = self.hp_max
        self.str = 2
        self.reward_xp = 5
        self.reward_gold = 8
        
class Bandit(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Bandit'
        self.hp_max = 20
        self.hp = self.hp_max
        self.str = 4
        self.reward_xp = 10
        self.reward_gold = 14

def random_enemy(obj, tier=None):
    enemies = [Rat, Slime, Goblin]
    
    enemies = {1: [Rat], 
               2: [Rat, Slime],
               3: [Rat, Slime], 
               3: [Rat, Slime],
               4: [Slime],
               5: [Slime, Goblin],
               6: [Slime, Goblin],
               6: [Slime, Goblin],
               7: [Goblin], 
               8: [Goblin, Wolf],
               9: [Goblin, Wolf],
               9: [Goblin, Wolf],
               10: [Wolf], 
               11: [Wolf, Zombie],
               12: [Wolf, Zombie],
               12: [Wolf, Zombie],
               13: [Zombie],
               14: [Zombie, Bandit],
               16: [Zombie, Bandit], 
               16: [Zombie, Bandit], 
               17: [Bandit]}
            
    result = random.choice(enemies[obj.day])
    return result()

def msg(string, duration=1.0):
    print(f'\n {string}')
    time.sleep(duration)

def main():
    plr = Player()

    while True:
        print(plr.get_status())
        print(' [HUB]\n (1) Fight\n (2) Rest\n (3) Shop')
        inp = input('> ')
        os.system('cls')
        match inp:
            case '1':
                enemy = random_enemy(plr)
                is_player_turn = True
                while True:
                    os.system('cls')
                    print(plr.get_status())
                    print(enemy.get_status())
                    if plr.hp > 0:
                        if enemy.hp > 0:
                            if is_player_turn == True:
                                print(' Choose action: (1) Attack | (2) Flee')
                                inp = input('> ')
                                match inp:
                                    case '1':
                                        dmg = plr.attack(enemy)
                                        msg(f'{plr.name} attacks for {dmg}.', 0.5)
                                    case '2':
                                        msg('Fleeing!')
                                        break
                                    case _:
                                        msg('You do nothing.', 0.5)
                                is_player_turn = False
                            else:
                                dmg = enemy.attack(plr)
                                msg(f'{enemy.name} attacks for {dmg}.')
                                is_player_turn = True
                        else:
                            msg(f'Enemy defeated!\nReward: {enemy.reward_xp} XP | {enemy.reward_gold} Gold')
                            plr.xp += enemy.reward_xp
                            plr.gold += enemy.reward_gold
                            try:
                                if plr.is_lvl_up_available():
                                    gain_str = plr.lvl_up()
                                    msg(f'LEVEL UP!\n  +{gain_str} STR')
                            except KeyError:
                                break
                            break
                    else:
                        break
                if plr.hp <= 0:
                    msg("You've died.")
                    break
                plr.day += 1
            case '2':
                rested = False
                regen = 0
                
                while True:
                    os.system('cls')
                    print(plr.get_status())
                    print(' [REST]\n')
                    if not rested:
                        msg('Resting...', 2)
                        regen = plr.hp_add(plr.rest)
                        plr.day += 1
                        rested = True
                    else:
                        msg(f'Rested for {regen} HP.')
                        break
            case '3':
                print(plr.get_status())
                print(' [SHOP]\n')
                inp = input('> ')
        os.system('cls')
    os.system('cls')
    print(f"\n    {plr.name}'s adventure is over.\n\n             The End\n")

if __name__ == '__main__':
    main()