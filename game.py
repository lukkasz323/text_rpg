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
        target.hp -= dmg
        return dmg
        
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Player'
        self.hp = 10
        self.str = 1
        
        self.lvl = 1
        self.xp = 0
        self.gold = 0
        
    def get_status(self):
        return f'[{self.name}] - [HP: {self.hp}, STR: {self.str}, LVL: {self.lvl}, XP: {self.xp}]\n'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.hp = 1
        self.str = 1
        
    def get_status(self):
        return f'[FIGHT] - [{self.name}, HP: {self.hp}]\n'
        
class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Rat'
        self.hp = 4
        self.str = 1
        
class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Slime'
        self.hp = 6
        self.str = 1
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.hp = 8
        self.str = 2

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
                enemy = random_enemy(2)
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
                                        msg(f'{plr.name} attacks.')
                                        plr.attack(enemy)
                                    case '2':
                                        msg('Fleeing!', 1)
                                        break
                                    case _:
                                        msg('You do nothing.')
                                is_player_turn = False
                            else:
                                msg(f'{enemy.name} attacks.')
                                enemy.attack(plr)
                                is_player_turn = True
                        else:
                            msg('Enemy defeated!', 1)
                            # TODO: Reward (Gold, XP)
                            break
                    else:
                        break
                if plr.hp <= 0:
                    break
            case '2':
                print('[SHOP]\n')
                inp = input('> ')
        os.system('cls')
    os.system('cls')
    print(f"\n    {plr.name}'s adventure is over.\n\n           The End\n")

if __name__ == '__main__':
    main()