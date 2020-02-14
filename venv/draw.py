# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string


yet_another_message = "New turn has start, command me your majesty! "
list_of_pc_objects = []
list_of_locations = []
# Define the main process here
class character:
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = tools.generate_new_name()
        self.name = name.capitalize()

    def describe(self):
        print("Your name is " + self.name)

class location:
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = tools.generate_new_name()
        self.name = name.capitalize()

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
