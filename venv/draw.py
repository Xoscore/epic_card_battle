# Let's try it another way again and again and again
# Imports
import tools
import globals
import random



#new_game = event_handler()
#while True:
#    new_game.before_start()
#    new_game.turn_process()
#    new_game.after_turn()


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
if direction in globals.LIST_OF_ACCEPT_CHARACTERS:
    print("So you drink a cup of wine, sing the song and go in nowhere!")
else:
    print("You want to stay in your dirty old farm forever")
print("Anyway, we start to emulate life right now!")