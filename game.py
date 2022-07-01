import os
import time
import random

# [Entities]
class Entity:
    def __init__(self):
        self.name = 'Entity'
        self.hp_max = 1
        self.hp = self.hp_max
        self.str = 1
        
    def attack(self, target):
        dmg = self.get_dmg(target)
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
        
    def get_dmg(self, target):
        return self.str
        
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
        self.day = 1
        self.weapon = Weapon
        self.armor = Armor
        self.bed = Bed
        self.dmg = self.str + self.weapon.dmg
        
        self.table_xp = [0, 10, 20, 50, 100, 200, 500, float('inf')]
        self.table_str = [0, 1, 1, 2, 2, 3, 3, float('inf')]
         
    def buy(self, item, type=None):
        match type:
            case 'weapon':
                self.weapon = item
            case 'armor':
                self.armor = item
    
    def lvl_up(self):
        gain_hp = self.lvl
        gain_str = self.table_str[self.lvl]
        
        self.xp -= self.table_xp[self.lvl]
        self.hp_max += gain_hp
        self.hp += gain_hp
        self.str += gain_str
        self.lvl += 1
        return gain_str
    
    def get_dmg(self):
        return self.str + self.weapon.dmg
    
    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}/{self.hp_max}, STR: {self.str}] - [LVL: {self.lvl}, XP: {self.xp}/{self.table_xp[self.lvl]}]'\
                f' - [GOLD: {self.gold}] - [DAY: {self.day}]\n[W: {self.weapon.name} A: {self.armor.name} BED: {self.bed.name}]\n'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.hp_max = 1
        self.hp = self.hp_max
        self.str = 1
        self.reward_xp = 1
        self.reward_gold = 1
        self.dmg = self.str
    
    def get_dmg(self, target):
        return self.str - target.armor.defense
    
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
        self.reward_xp = 14
        self.reward_gold = 0
        
class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Zombie'
        self.hp_max = 18
        self.hp = self.hp_max
        self.str = 2
        self.reward_xp = 12
        self.reward_gold = 8
        
class Bandit(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Bandit'
        self.hp_max = 20
        self.hp = self.hp_max
        self.str = 4
        self.reward_xp = 16
        self.reward_gold = 14

class Cobra(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Cobra'
        self.hp_max = 14
        self.hp = self.hp_max
        self.str = 6
        self.reward_xp = 23
        self.reward_gold = 0
        
class Ghoul(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ghoul'
        self.hp_max = 22
        self.hp = self.hp_max
        self.str = 5
        self.reward_xp = 17
        self.reward_gold = 19
        
class Werewolf(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Werewolf'
        self.hp_max = 30
        self.hp = self.hp_max
        self.str = 7
        self.reward_xp = 32
        self.reward_gold = 0
        
class Ogre(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ogre'
        self.hp_max = 40
        self.hp = self.hp_max
        self.str = 6
        self.reward_xp = 23
        self.reward_gold = 21

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Boss'
        self.hp_max = 100
        self.hp = self.hp_max
        self.str = 15
        self.reward_xp = 0
        self.reward_gold = 0

# [Items]
class Item():
    name = None
    value = 0

# Weapons
class Weapon(Item):
    name = None
    value = 0
    dmg = 0
        
class Club(Weapon):
    name = 'Club'
    value = 8
    dmg = 2
        
# Armors
class Armor(Item):
    name = None
    value = 0
    defense = 0
    
# Beds
class Bed(Item):
    name = None
    value = 0
    regen = 5
    
class SimpleBed(Bed):
    name = 'Simple Bed'
    value = 20
    regen = 10
    
class ComfortableBed(Bed):
    name = 'Comfortable Bed'
    value = 100
    regen = 20

# [Functions]
def random_enemy(plr):
    enemies = {1: [Rat], 
               2: [Rat, Slime],
               3: [Rat, Slime], 
               3: [Rat, Slime],
               4: [Slime],
               5: [Slime, Goblin],
               6: [Slime, Goblin],
               7: [Slime, Goblin],
               8: [Goblin], 
               9: [Goblin, Wolf],
               10: [Goblin, Wolf],
               11: [Goblin, Wolf],
               12: [Wolf], 
               13: [Wolf, Zombie],
               14: [Wolf, Zombie],
               15: [Wolf, Zombie],
               16: [Zombie],
               17: [Zombie, Bandit],
               18: [Zombie, Bandit], 
               19: [Zombie, Bandit], 
               20: [Bandit],
               21: [Bandit, Cobra],
               22: [Bandit, Cobra],
               23: [Bandit, Cobra],
               24: [Cobra],
               25: [Cobra, Ghoul],
               26: [Cobra, Ghoul],
               27: [Cobra, Ghoul],
               28: [Ghoul],
               29: [Ghoul, Werewolf],
               30: [Ghoul, Werewolf],
               31: [Ghoul, Werewolf],
               32: [Werewolf],
               33: [Werewolf, Ogre],
               34: [Werewolf, Ogre],
               35: [Werewolf, Ogre],
               36: [Ogre]}
    
    try:        
        result = random.choice(enemies[plr.day])
    except KeyError:
        result = Boss
    
    return result()

def msg(string, duration=1.0):
    print(f'\n {string}')
    time.sleep(duration)

def main():
    plr = Player()
    weapon_list = [Weapon, Club]
    armor_list = [Armor]
    bed_list = [Bed, SimpleBed, ComfortableBed]

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
                            msg(f'Enemy defeated!\n  Reward: {enemy.reward_xp} XP | {enemy.reward_gold} Gold')
                            plr.xp += enemy.reward_xp
                            plr.gold += enemy.reward_gold
                            while plr.xp >= plr.table_xp[plr.lvl]:
                                gain_str = plr.lvl_up()
                                msg(f'LEVEL UP!\n  +{gain_str} STR')
                            break
                    else:
                        break
                if plr.hp <= 0:
                    msg("You've died.")
                    break
                plr.day += 1
            case '2':
                rested = False
                total_regen = 0
                
                while True:
                    os.system('cls')
                    print(plr.get_status())
                    print(' [REST]\n')
                    if not rested:
                        msg('Resting...', 2)
                        total_regen = plr.hp_add(plr.bed.regen)
                        plr.day += 1
                        rested = True
                    else:
                        msg(f'Rested for {total_regen} HP.')
                        break
            case '3':
                print(plr.get_status())
                print(' [SHOP]\n (1) Weapons\n (2) Armors\n\n (ENTER) Back')
                inp = input('> ')
                os.system('cls')
                match inp:
                    # Weapons
                    case '1':
                        print(plr.get_status())
                        print(' [SHOP] - [Weapons]\n\n Name / Damage / Price')
                        for i, weapon in enumerate(weapon_list):
                            print(f' ({i + 1}) {weapon.name} | {weapon.dmg} | {weapon.value}')
                        inp = input('> ')
                        try:
                            weapon = weapon_list[int(inp) - 1]
                            if plr.gold >= weapon.value:
                                plr.gold -= weapon.value
                                plr.weapon = weapon
                            else:
                                msg('Not enough gold!')
                        except (IndexError, ValueError):
                            pass
                    # Armors
                    case '2':
                        print(plr.get_status())
                        print(' [SHOP] - [Armors]\n\n Name / Defense / Price')
                        for i, armor in enumerate(armor_list):
                            print(f' ({i + 1}) {armor.name} | {armor.defense} | {armor.value}')
                        inp = input('> ')
                        try:
                            armor = armor_list[int(inp) - 1]
                            if plr.gold >= armor.value:
                                plr.gold -= armor.value
                                plr.armor = armor
                            else:
                                msg('Not enough gold!')
                        except (IndexError, ValueError):
                            pass
                    # Beds
                    case '3':
                        print(plr.get_status())
                        print(' [SHOP] - [Beds]\n\n Name / Regen / Price')
                        for i, bed in enumerate(bed_list):
                            print(f' ({i + 1}) {bed.name} | {bed.regen} | {bed.value}')
                        inp = input('> ')
                        try:
                            bed = bed_list[int(inp) - 1]
                            if plr.gold >= bed.value:
                                plr.gold -= bed.value
                                plr.bed = bed
                            else:
                                msg('Not enough gold!')
                        except (IndexError, ValueError):
                            pass
            case _:
                exec(inp) # Debug, TO BE REMOVED!

        os.system('cls')
    os.system('cls')
    print(f"\n    {plr.name}'s adventure is over.\n\n             The End\n")

if __name__ == '__main__':
    main()
    
# TODO: Encapsulate shops
# TODO: Add "bought?" after "Price" in shop.