import os

class Player:
    def __init__(self):
        self.name = 'Unknown'
        self.lvl = 1
        self.xp = 0

def main():
    plr = Player()
    
    while True:
        print(f'[TEXT RPG] - [{plr.name}, LVL: {plr.lvl}, XP: {plr.xp}]\n')
        print('[HUB]\n(1) Fight\n(2) Shop')
        inp = input('> ')
        os.system('cls')
        match inp:
            case '1':
                print('[FIGHT]\n')
                inp = input('> ')
            case '2':
                print('[SHOP]\n')
                inp = input('> ')
        os.system('cls')
    
    print('The End')
    

if __name__ == '__main__':
    main()