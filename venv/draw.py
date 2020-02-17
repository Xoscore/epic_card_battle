# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string


def rus_to_eng(rus_word):
    eng_word = ''
    for L in rus_word.lower():
        if L == ' ':
            eng_word += ' '
        elif L == 'а':
            eng_word += 'a'
        elif L == 'б':
            eng_word += 'b'
        elif L == 'в':
            eng_word += 'v'
        elif L == 'г':
            eng_word += 'g'
        elif L == 'д':
            eng_word += 'd'
        elif L == 'е':
            eng_word += 'e'
        elif L == 'ё':
            eng_word += 'jo'
        elif L == 'ж':
            eng_word += 'zh'
        elif L == 'з':
            eng_word += 'z'
        elif L == 'и':
            eng_word += 'i'
        elif L == 'й':
            eng_word += 'jj'
        elif L == 'к':
            eng_word += 'k'
        elif L == 'л':
            eng_word += 'l'
        elif L == 'м':
            eng_word += 'm'
        elif L == 'н':
            eng_word += 'n'
        elif L == 'о':
            eng_word += 'o'
        elif L == 'п':
            eng_word += 'p'
        elif L == 'р':
            eng_word += 'r'
        elif L == 'с':
            eng_word += 's'
        elif L == 'т':
            eng_word += 't'
        elif L == 'у':
            eng_word += 'u'
        elif L == 'ф':
            eng_word += 'f'
        elif L == 'х':
            eng_word += 'kh'
        elif L == 'ц':
            eng_word += 'c'
        elif L == 'ч':
            eng_word += 'ch'
        elif L == 'ш':
            eng_word += 'sh'
        elif L == 'щ':
            eng_word += 'shh'
        elif L == 'ь':
            eng_word += '``'
        elif L == 'ы':
            eng_word += 'y'
        elif L == 'ъ':
            eng_word += '`'
        elif L == 'э':
            eng_word += 'eh'
        elif L == 'ю':
            eng_word += 'ju'
        elif L == 'я':
            eng_word += 'ja'
    return eng_word

yet_another_message = "New turn has start, command me your majesty! "
list_of_pc_objects = []
list_of_locations = []
# Define the main process here
class character:
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = tools.generate_new_name()
        self.name = rus_to_eng(name).capitalize()

    def describe(self):
        print("Your name is " + self.name)

class location:
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = tools.generate_new_name()
        self.name = rus_to_eng(name).capitalize()

    def describe(self):
        print("This is the place, called " + self.name)

class main_process():
    def __init__(self):
        self.flag_is_playing = True

    def start_game(self):
        print("The game has started")
        char_name = tools.entry_point("What is your name?")
        if char_name == "":
            print("Smartass, ya?")
            char_name = tools.generate_new_name()
            print("I will call you " + char_name.capitalize() + " for that")
        main_PC = character("main_PC", name=char_name)
        list_of_pc_objects.append(main_PC)
        main_PC.describe()
        start_town_name = tools.entry_point("What the name of your hometown? ", str_max=10)
        if start_town_name == "":
            print("I do not like you already")
            start_town_name = tools.generate_new_name()
            print("I'm sure, that you from this place " + start_town_name.capitalize())
        start_town = location("start_town", name=start_town_name)
        list_of_locations.append(start_town)
        start_town.describe()

    def running(self):
        self.start_game()
        while self.flag_is_playing:
            command = tools.entry_point(yet_another_message)
            if command == "name":
                tools.generate_new_name()
            elif command == "exit":
                self.flag_is_playing = False
            else:
                print("nothing happens")

    def on_exit(self):
        self.flag_is_playing = False

new_game = main_process()
new_game.running()


# World generation
# We need a simple rules, an initial state, some limitations and after all, collision between different parts of the
# world
# So, There are some territory
# The main spot - it's not like a square with 1 km size or so, it's more like province, that can hold one big city
class territory:
    def __init__(self, name):
        self.name = name
        self.comment = None
        self.full_description = True

    # We have two kind of description, short and long
    def description(self):
        print("This is the land " + str(self.name))
        if self.comment is None:
            print("Nothing specific here")
        else:
            print("As the %player_name% say:" + str(self.comment))
        if self.full_description:
            #print("It lies on the " + str(self.terrain) + " in the place of " + str(self.address))
            #print("This land have " + str(self.climat) + " , with a " + str(self.vegetaion))
            #print("This land is bordered by %border_list%")
            self.full_description = False

class event_handler():
    def __init__(self):
        self.turn_number = 1
        self.doing = ""
        self.start_event_list = []
        self.past_event_list = []
        self.event_list = {
            "rain": {
                "start": ["It's a rainy day today"],
                "end": ["You become wet", "Your hairs wet"],
            }
        }

    def before_start(self):
        print("The turn " + str(self.turn_number) + " has started")
        if len(self.start_event_list) != 0:
            print(self.start_event_list.pop())
        else:
            print("Nothing happens yet")

    def turn_process(self):
        self.doing = input("What do you want to do? ")
        self.check_doing(self.doing)

    def after_turn(self):
        print("In this turn you " + self.doing)
        if len(self.past_event_list) != 0:
            print(self.past_event_list.pop())
        print("The turn " + str(self.turn_number) + " has ended")
        self.turn_number += 1

    def check_doing(self, todoing):
        if todoing in self.event_list:
            self.start_event_list += self.event_list[todoing]["start"]
            self.past_event_list += self.event_list[todoing]["end"]

def initialle():
    direction = input("Do you want to go adventure? ")
    if direction.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
        print("So you drink a cup of wine, sing the song and go in nowhere!")
    else:
        print("You want to stay in your dirty old farm forever")
    print("Anyway, we start to emulate life right now!")
