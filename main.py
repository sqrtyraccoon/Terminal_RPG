import os

os.system('clear')


#Boss Class
class Boss:
    def __init__(self, name, hp, ad):
        self.name = name
        self.hp = hp
        self.ad = ad

class Sauron(Boss):
    def __init__(self, name, hp, ad):
        super(Sauron, self).__init__(name, hp, ad)

class Chronos(Boss):
    def __init__(self, name, hp, ad):
        super(Chronos, self).__init__(name, hp, ad)

class Lilith(Boss):
    def __init__(self, name, hp, ad):
        super(Lilith, self).__init__(name, hp, ad)

Sauron = Sauron('Sauron', 100, 10)
Chronos = Chronos('Chronos', 100, 10)
Lilith = Lilith('Lilith', 100, 10)


# Hero Class
class Hero:
    def __init__(self, name, hp, ad, CombatPosture):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.CombatPosture = CombatPosture

class Warrior(Hero):
    def __init__(self, name, hp, ad, CombatPosture, rage):
        super(Warrior, self).__init__(name, hp, ad, CombatPosture)
        self.rage = rage

class Mage(Hero):
    def __init__(self, name, hp, ad, CombatPosture, mana):
        super(Mage, self).__init__(name, hp, ad, CombatPosture)
        self.mana = mana

class Archer(Hero):
    def __init__(self, name, hp, ad, CombatPosture, arrows):
        super(Archer, self).__init__(name, hp, ad, CombatPosture)
        self.arrows = arrows

Warrior = Warrior('', 0, 0, '', 0)
Mage = Mage('', 0, 0, '', 7)
Archer = Archer('', 0, 0, '', 6)










# Ask for username
print(f"Haii what's your username?")
username = input('> ')

# Command Strings
def cmd_help():
    print("""
NOTE: Type "help --CommandName" to get further explanation about a command.
      Type "--help_all" to get explanation for any command at once.
X_____Available Commands_____X
--help || --help_all || --clear || --exit
    """)
    
def help_all():
    print("""
--help:
    Downloads additional RAM on your PC.
--clear:
    Allows you to clear the terminal.
--exit:
    Allows you to quit the game.
    """)

while True:
    cmd = input(f'{username} >> ')
    if cmd == '--exit':
        print(f'Bye {username} :<')
        break
    if cmd == '--clear':
        os.system('clear')
    if cmd == '--help':
        cmd_help()
    if cmd == 'help --exit':
        print('Allows you to quit the game.')
    if cmd == 'help --clear':
        print('Allows you to clear the terminal.')
    if cmd == 'help --help':
        print('Are you serious? :|')
    if cmd == '--help_all':
        help_all()
