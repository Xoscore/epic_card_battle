# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string
from sympy import *
from sympy import geometry


list_of_possible_gender = ["male", "female", "undefine"]

yet_another_message = "New turn has start, command me your majesty! "
list_of_pc_objects = []
list_of_locations = []
# Define the main process here
class character:
    def __init__(self, id, main=False, name=None, gender=None, title=None, home=None):
        self.id = id
        self.main = main
        if name is None:
            name = tools.generate_new_name()
        self.name = name.capitalize()
        if gender is None:
            gender = "undefine"
        self.gender = gender
        if title is None:
            title = "nobody"
        self.title = title
        if home is None:
            home = tools.generate_new_name()
        self.home = home.capitalize()

    def describe(self):
        if self.main:
            gender = ""
            if self.gender == "male":
                gender = " - the man "
            elif self.gender == "female":
                gender = " - the woman "
            print("Your name is " + self.name + " you are the " + self.title + gender + " from " + self.home)
        else:
            gender = " one's "
            if self.gender == "male":
                gender = " man's "
            elif self.gender == "female":
                gender = " woman's "
            print("This" + gender + "name is " + self.name + " The " + self.title + "from " + self.home)


class location:
    def __init__(self, id, name=None, description=None):
        self.id = id
        if name is None:
            name = tools.generate_new_name()
        self.name = name.capitalize()
        if description is None:
            description = "but nobody knows about it"
        self.description = description

    def describe(self):
        print("There is a place, called " + self.name + ", " + self.description)


class main_process():
    def __init__(self):
        self.flag_is_playing = True

    def start_game(self):
        print("The game has started")

        char_name = tools.entry_point("What is your name?")
        if char_name == "":
            char_name = tools.generate_new_name()
            print("I will call you " + char_name.capitalize() + " this time")

        start_town_name = tools.entry_point("What the name of your hometown? ", str_max=10)
        if start_town_name == "":
            start_town_name = tools.generate_new_name()
            print("I'm sure, that you from this place " + start_town_name.capitalize())
        start_town = location("start_town", name=start_town_name)
        list_of_locations.append(start_town)

        gender = tools.entry_point("What is your gender?", list_of_possible_gender)

        main_PC = character("main_PC", main=True, name=char_name, gender=gender, home=start_town_name)
        list_of_pc_objects.append(main_PC)

        main_PC.describe()
        start_town.describe()

    def running(self):
        self.start_game()
        while self.flag_is_playing:
            command = tools.entry_point(yet_another_message)
            if command == "name":
                print(tools.generate_new_name().capitalize())
            elif command == "exit":
                self.flag_is_playing = False
            else:
                print("nothing happens")

    def on_exit(self):
        self.flag_is_playing = False


#new_game = main_process()
#new_game.running()


# World generation
# We need a simple rules, an initial state, some limitations and after all, collision between different parts of the
# world
# So, There are some territory
# The main spot - it's not like a square with 1 km size or so, it's more like province, that can hold one big city
class Territory:
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


# So, what I want to do now
# There are some world, and I mean the whole world inside local machine
# It has no any special properties, instead of list of territory, nations and gates
# This world contains several territories, for tribes

# There is one question, why I make world and their territory by separate objects?
# At first, world is about transportation and infrastructure, territory all about nation and rule, they has no cross
#   information
# At second, territory can be totally separate from world and go away, which is harder if it inherit some stuff

class World:
    def __init__(self, name=None):
        self.id = "localhost"
        # Each world can actively contain several territories on one local machine
        if name is None:
            name = tools.generate_new_name()
        self.territories = []
        # Gates are connector to other worlds
        self.gates = []

    # TO FEATURE:
    # Copy of all worlds with online status must be collected in some hub under new id with link to local one
    # Worlds must exchange the list and status between each other from time to time
    # Worlds cannot be destroyed or deleted
    # If user decline the world, clean the machine or stop being online, this world make new copy, marked as "forbidden"
    # (Also need to think, what if user create "forbidden" name of the world, as easter egg)
    # This new copies will be offered as new created world (as it happens), to more experienced people
    # It will contain some special features, like ruins of previous player, with some hidden story of what happens
    #   with the old link to first player, so his world can be connected special way to new one
    # I think it would be funny to boost both pvp and mentoring for such cases, that makes legend of "The lost curse of
    #   forgotten worlds" are technically true
    # Of cause this can be happened several times, so it is possible to create world with a lot of layers from previous
    #   games
    # Also because of this, more and more copies of the same world will appear, so central hubs must decide if merge
    #   such versions into one (with some event happens) or finally de-link them
    # To generate


# One of territory option - is climate
# It is just example
climates = ["dry", "wet", "cold", "hot"]
# This is the type of continent, that affect earth and caves type
platform_types = [
    "motherland", # One big continent - a stable platform
    "one_big_lot_small", # Also one big, but with lot of small ones around - that means vulcano activities, islands and
    # so on
    "lot_small", # A lot of small continents, collide each other, earthquakes and vulkano ahead
    "amorph", # The platform is too soft (sand, clay) to make it solid, no quake and caves
    "bubbles" # A lot of big rocky bubbles with gas, liquid and other materials inside, a lot of caves
]


# That territories is a country size, controlled by one nation group
class Territory:
    def __init__(self, name):
        # Not sure, if I need to have id, but want to make sure, it have unique one for now
        self.id = "terr_1"
        if name is None:
            name = tools.generate_new_name()
        self.name = name
        self.climate = random.choice(climates)
        self.platform = random.choice(platform_types)
        # It just name for now
        self.nation = tools.generate_new_name()

        # Now the main feature, I want to add today
        # Because all lands are for one nation, and so far for one government, there is only one capital in such
        #   territory
        # So, make capital land as a center of abstract circle, where all lands are equally far (but +- by roads and
        #   obstacles)
        # All generated lands then - are circular sectors around, randomly placed on the circle
        # The number of lands are not limited - it can be added new portals, pocket universe, hell, heaven, chaos gates
        #   and so on and so on
        # But interception between sectors, means how far this one from another

        self.size = random.randint(10,16)
        for i in range(0, self.size):
            # generate lands here
            pass


land_base_feature = ["wood", "desert", "grassland", "mauntine"]
land_additional_feature = ["river", "cave_entry", "hills"]


# So the land is a one big notable feature, like mountian, grassfield or forest
# In land is usually several families, guilds or other groups inside
class Land:
    def __init__(self):
        self.id = "land_1"
        self.name = tools.generate_new_name()
        self.size = random.randint(10,16)
        # It can  e several features inside one territory, although it should not conflict each other, so leave it now
        self.feature = random.choice(land_feature)

# And in the end, there are location inside that land
# Locations is not that strict - it can be many in big city or just few in the desert
# It should be generated by will and keeped until something happens
# Example: two armies met in some land, so location for their fight generate anew (eith territory and land features)
# After they battle, this location kept with bodies and equip on that
# So, locals use it to loot, necros can raise the bodies, holyes can make the rest and so on
# But after some time, this field depleted, and disappear
# But before that, it can be choosen and used for another battle (because tactics, that corpses, forts and so on)

class Location:
    def __init__(self):
        pass


# At first we need some algebra magic here
# I need a circle
capital = Point(0, 0)
territory = Circle(capital, 1)
# Now, I need a sector of this circle