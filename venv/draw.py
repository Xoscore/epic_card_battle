# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string



yet_another_message = "New turn has start, command me your majesty! "
# Define the main process here
class main_process():
    def __init__(self):
        self.flag_is_playing = True

    # I need the only one entry point to check, format and parse user's commands
    def entry_point(self, message=None, asked_type=None, int_min=None, int_max=None, strict_yes=False, str_max=None):
        if message is None:
            message = "What now? "
        if asked_type is None:
            asked_type = str
        if asked_type is int:
            # I need to control max and min later on, but need some system default limitations
            if int_min is None:
                int_min = globals.RANGE_INT_SIZE["min"]
            if int_max is None:
                int_max = globals.RANGE_INT_SIZE["max"]
            ask_for_type = " Input number, from " + str(int_min) + " to " + \
                           str(int_max) + ", please: "
            #TODO This part try to repeat input until desired typr has inputted
            # Need to improve this part to make it on the same line of screen
            # when the UI will be ready, to do not let user forget what he should input
            while True:
                user_command = input(message + ask_for_type)
                if len(user_command) == 0:
                    message = "Do not input empty value!"
                # reverse check if it a digit
                elif not(user_command[0] == '-' and user_command[1:].isdigit() or user_command.isdigit()):
                    message = "Wrong input type!"
                elif int(user_command) < int_min:
                    message = "Please, input more, then " + str(int_min) + "!"
                elif int(user_command) > int_max:
                    message = "Please, not more, then " + str(int_max) + "!"
                else:
                    break
        elif asked_type is bool:
            ask_for_type = " Do you accept this? "
            while True:
                user_command = input(message + ask_for_type)
                if user_command.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
                    print("You accept this")
                    user_command = True
                    break
                elif user_command.upper() in globals.LIST_OF_DECLINE_CHARACTERS:
                    print("You decline it")
                    user_command = False
                    break
                elif strict_yes:
                    message = "Please, exact 'Yes' or 'No'"
                else:
                    print("We translate it as 'No'")
                    user_command = False
                    break

        else:
            ask_for_type = " "
            if str_max is None:
                str_max = globals.MAX_STRING_SIZE
            user_command = input(message + ask_for_type)
            if len(user_command) > globals.MAX_STRING_SIZE:
                print("It is more, then I want, I will cut it")
                user_command = user_command[:globals.MAX_STRING_SIZE]
        return user_command



    def running(self):
        char_name = self.entry_point("What is your name?")
        char_age = self.entry_point("What is your age?", int)
        char_live = self.entry_point("Are you alive?", bool, strict_yes=False)
        print("you are " + char_name)
        print("your age is " + str(char_age))
        if char_live:
            print("you live")
        else:
            print("you are dead")
        while self.flag_is_playing:
            if random.randint(1,10) < 5:
                self.entry_point(yet_another_message)
            else:
                self.entry_point()

    def on_exit(self):
        self.flag_is_playing = False

new_game = main_process()
new_game.running()
#eval_string = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or \
#                     len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x
a = "false"
if a:
 print("da")

if len(a) > 0:
    if a.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
        print("it is yes")
    elif a.upper() in globals.LIST_OF_DECLINE_CHARACTERS:
        print("it is no")
    elif a[0] == '-' and a[1:].isdigit():
        print("it is negative")
        print(int(a))
    elif a.isdigit():
        print("it is positive")
        print(int(a))
    else:
        print("not digit")
else:
    print("empty string")


# World generation
# We need a simple rules, an initial state, some limitations and after all, collision between different parts of the
# world
# So, There are some territory
# The main spot - it's not like a square with 1 km size or so, it's more like province, that can hold one big city
class territory:
    def __init__(self, name):
        # That territory has some name
        self.name = name
        # Some main theme mmm... I think the first is type of terrain, like flat or mountians or sea, that's it
        #self.terrain
        # Temperature as well, but it somethink like choose from nine, between wet and dry, hot and cold, maybe
        # something else, let's think about it later
        #self.climat
        # There are some natural process over here, like a forest or bush like vegs and related animals
        #self.vegetaion
        # It should have kind of coordinates to link it to some place in world
        #self.address
        # Whit the address, it should keep an info about it's borderlines, to simplify description
        #self.borders
        # And, of cause, some rare resource, that can be gotten here
        #self.resource
        # And some gays, who tell, that it's "Their land and they will die for it"
        #self.locals
        # Of cause, there are some infrustructer level for the whole province
        #self.infrastructure
        # And manufacturing as well
        #self.manufacture
        # And if user want, he can made a comment, to shorten the
        self.comment = None
        # Give a flag of full description
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

class character():
    def __init__(self, name):
        self.name = name
        self.title = "Peasant"
        self.description = "You are hero and blah blah, who save everything and get drunk!"

    def describe(self):
        print("You are " + self.name + " The " + self.title)
        print(self.description)

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
    print("The game has started")
    player_name = input("What is the name of your character? ")
    if len(player_name) == 0:
        print("Smartass, ya?")
        player_name = random.choice(globals.LIST_STUPID_NAMES)
        print("I will call you " + player_name + " for that")
    player_character = character(name=player_name)
    print(player_character.description)
    print("For now, you cannot move in some places, only just move to somewhere")
    start_location = territory(name="Old farm")
    start_location.description()
    direction = input("Do you want to go adventure? ")
    if direction.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
        print("So you drink a cup of wine, sing the song and go in nowhere!")
    else:
        print("You want to stay in your dirty old farm forever")
    print("Anyway, we start to emulate life right now!")



