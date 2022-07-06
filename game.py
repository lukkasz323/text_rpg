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
        
        self.table_xp = [0, 10, 20, 50, 100, 200, 500, float('inf')]
        self.table_str = [0, 1, 2, 1, 3, 2, 3, 5, float('inf')]
         
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
        return gain_hp, gain_str
    
    def get_dmg(self, target):
        return self.str + self.weapon.stat

    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}/{self.hp_max}, STR: {self.str}] - [LVL: {self.lvl}, XP: {self.xp}/{self.table_xp[self.lvl]}]'\
                f' - [GOLD: {self.gold}] - [DAY: {self.day}]\n[W: {self.weapon.name} ({self.weapon.stat}), A: {self.armor.name}'\
                f' ({self.armor.stat}), BED: {self.bed.name} ({self.bed.stat})]\n'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.hp_max = 1
        self.hp = self.hp_max
        self.str = 1
        self.reward_xp = 1
        self.reward_gold = 1
    
    def get_dmg(self, target):
        dmg = self.str - target.armor.stat
        if dmg > 0:
            return dmg
        else:
            return 0
    
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
        self.str = 3
        self.reward_xp = 16
        self.reward_gold = 14

class Cobra(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Cobra'
        self.hp_max = 14
        self.hp = self.hp_max
        self.str = 5
        self.reward_xp = 26
        self.reward_gold = 0
        
class Ghoul(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ghoul'
        self.hp_max = 22
        self.hp = self.hp_max
        self.str = 4
        self.reward_xp = 17
        self.reward_gold = 19
        
class Werewolf(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Werewolf'
        self.hp_max = 30
        self.hp = self.hp_max
        self.str = 6
        self.reward_xp = 32
        self.reward_gold = 0
        
class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Skeleton'
        self.hp_max = 40
        self.hp = self.hp_max
        self.str = 5
        self.reward_xp = 23
        self.reward_gold = 21
        
class Ogre(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ogre'
        self.hp_max = 60
        self.hp = self.hp_max
        self.str = 5
        self.reward_xp = 35
        self.reward_gold = 25
        
class Troll(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ogre'
        self.hp_max = 70
        self.hp = self.hp_max
        self.str = 5
        self.reward_xp = 40
        self.reward_gold = 20
        
class Wyvern(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Wyvern'
        self.hp_max = 80
        self.hp = self.hp_max
        self.str = 6
        self.reward_xp = 70
        self.reward_gold = 0

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Dragon Lord'
        self.hp_max = 100
        self.hp = self.hp_max
        self.str = 10
        self.reward_xp = 0
        self.reward_gold = 0

# [Items]
class Item():
    name = None
    value = 0
    stat = 0

# Weapons
class Weapon(Item): # value per dmg
    name = None
    value = 0
    stat = 0
        
class Club(Weapon): # 4.00
    name = 'Club'
    value = 8 
    stat = 2
    
class Dagger(Weapon): # 4.25
    name = 'Dagger'
    value = 17
    stat = 4
    
class Shortsword(Weapon): # 4.33
    name = 'Shortsword'
    value = 26
    stat = 6
    
class Spear(Weapon): # 4.375
    name = 'Spear'
    value = 35
    stat = 8
    
class Mace(Weapon): # 4.58
    name = 'Mace'
    value = 55
    stat = 12
    
class Saber(Weapon): # 5.00
    name = 'Saber'
    value = 80
    stat = 16
    
class Katana(Weapon): # 5.83
    name = 'Katana'
    value = 140
    stat = 24
    
class Claymore(Weapon): # 7.50
    name = 'Claymore'
    value = 300
    stat = 40
        
# Armors
class Armor(Item): # value per defense
    name = None
    value = 0
    stat = 0

class LeatherArmor(Armor): # 15.00
    name = 'Leather Armor'
    value = 15
    stat = 1
    
class Chainmail(Armor): # 16.66
    name = 'Chainmail'
    value = 50
    stat = 3
    
class PlateArmor(Armor): # 20.00
    name = 'Plate Armor'
    value = 100
    stat = 5
    
# Beds
class Bed(Item):
    name = None
    value = 0
    stat = 5
    
class SimpleBed(Bed):
    name = 'Simple Bed'
    value = 20
    stat = 10
    
class ComfortableBed(Bed):
    name = 'Comfortable Bed'
    value = 100
    stat = 20

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
               33: [Werewolf, Skeleton],
               34: [Werewolf, Skeleton],
               35: [Werewolf, Skeleton],
               36: [Skeleton],
               37: [Skeleton, Ogre],
               38: [Skeleton, Ogre],
               39: [Skeleton, Ogre],
               40: [Ogre],
               41: [Ogre, Troll],
               42: [Ogre, Troll],
               43: [Ogre, Troll],
               44: [Troll],
               45: [Troll, Wyvern],
               46: [Troll, Wyvern],
               47: [Troll, Wyvern],
               48: [Wyvern],
               49: [Wyvern]}
    
    try:        
        result = random.choice(enemies[plr.day])
    except KeyError:
        result = Boss
    
    return result()

def msg(string, duration=1.0):
    print(f'\n {string}')
    time.sleep(duration)

def shop(plr, item_list):
    for i, element in enumerate(item_list):
        item = element[0]
        is_owned = element[1]
        print(f' ({i + 1}) {item.name} / {item.stat} / {item.value} / [{is_owned}]')
    inp = input('> ')
    try:
        element = item_list[int(inp) - 1]
        item = element[0]
        if plr.gold >= item.value:
            if element[1] is False:
                plr.gold -= item.value
            if issubclass(item, Weapon):
                plr.weapon = item
            elif issubclass(item, Armor):
                plr.armor = item
            elif issubclass(item, Bed):
                plr.bed = item
            element[1] = True
            msg(f'Bought {item.name}!')
        else:
            msg('Not enough gold!')
    except (IndexError, ValueError):
        pass

def main():
    plr = Player()
    weapon_list = [[Weapon, True], [Club, False], [Dagger, False], [Shortsword, False], [Spear, False], [Mace, False], [Saber, False], [Katana, False], [Claymore, False]]
    armor_list = [[Armor, True], [LeatherArmor, False], [Chainmail, False], [PlateArmor, False]]
    bed_list = [[Bed, True], [SimpleBed, False], [ComfortableBed, False]]
    is_boss_defeated = False

    while True:
        os.system('cls')
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
                                gain = plr.lvl_up()
                                msg(f'LEVEL UP!\n  +{gain[0]} HP, +{gain[1]} STR')
                            if enemy.__class__ == Boss:
                                is_boss_defeated = True
                            break
                    else:
                        break
                if plr.hp <= 0:
                    msg("You've died.", 2)
                    break
                if is_boss_defeated:
                    msg('The final boss has been defeated!', 2)
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
                        total_regen = plr.hp_add(plr.bed.stat)
                        plr.day += 1
                        rested = True
                    else:
                        msg(f'Rested for {total_regen} HP.')
                        break
            case '3':
                print(plr.get_status())
                print(' [SHOP]\n (1) Weapons\n (2) Armors\n (3) Beds\n (ENTER) Back')
                inp = input('> ')
                os.system('cls')
                print(plr.get_status())
                match inp:
                    # Weapons
                    case '1':
                        print(' [SHOP] - [Weapons]\n\n Name / Damage / Price / Owned')
                        shop(plr, weapon_list)
                    # Armors
                    case '2':
                        print(' [SHOP] - [Armors]\n\n Name / Defense / Price / Owned')
                        shop(plr, armor_list)
                    # Beds
                    case '3':
                        print(' [SHOP] - [Beds]\n\n Name / Regen / Price / Owned')
                        shop(plr, bed_list)
            case _:
                exec(inp) # Debug, TO BE REMOVED!
    print(f"\n    {plr.name}'s adventure is over.\n\n             The End\n")

if __name__ == '__main__':
    main()
    
# TODO: Fix ending