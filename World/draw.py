# Let's try it another way again and again and again
# Imports
import Collections.tools as tools
import globals
import random
import string
from sympy import *
from sympy import geometry
import tabulate
import math

# So, what I want to do now
# There are some world, and I mean the whole world inside local machine
# It has no any special properties, instead of list of territory, nations and gates
# This world contains several territories, for tribes

# There is one question, why I make world and their territory by separate objects?
# At first, world is about transportation and infrastructure, territory all about nation and rule, they has no cross
#   information
# At second, territory can be totally separate from world and go away, which is harder if it inherit some stuff

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


# Something about size of sectors
TINY = [1, 5]
SMALL = [5, 15]
NORMAL = [15, 45]
BIG = [45, 90]
LARGE = [90, 179]
TUNNEL = [180, 180]
HUGE = [181, 359]
COVER = [360, 360]


def decide_fi(size):
    return random.randint(size[0], size[1])


def create_sector(alpha, fi):
    point_a = Point(cos(math.radians(alpha)), sin(math.radians(alpha)))
    point_b = Point(cos(math.radians(alpha + fi)), sin(math.radians(alpha + fi)))
    if fi == 180:
        # Such line will be used as tunnel, portal, transport field or something like this
        sector = Line(point_a, point_b)
    else:
        sector = Triangle(Point(0, 0), point_a, point_b)
    # I do not need exact sector, just triangle is fine enough
    # The only reason to use circle at all - is make closed numerical line
    return sector


class World:
    def __init__(self, name=None):
        self.id = "localhost"
        # Each world can actively contain several territories on one local machine
        if name is None:
            name = tools.generate_new_name()
        self.name = name
        self.territories = []
        # Gates are connector to other worlds
        self.star_gates = []
        self.description = ""
        self.capital = self.create_capital

    def describe(self):
        print("This is the world " + self.name)
        if self.description == "":
            print("There is no any description")

    def create_new_territory(self, size=None, name=None):
        if size is None:
            size = decide_fi(NORMAL)
        else:
            size = decide_fi(size)
        if name is None:
            name = tools.generate_new_name()
        else:
            name = name
        territory = Territory(name, size)
        self.territories.append(territory)

    def create_capital(self):
        pass


# That territories is a country size, controlled by one nation group
class Territory:
    def __init__(self, name, size):
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

        self.size = random.randint(10, 16)
        for i in range(0, self.size):
            # generate lands here
            pass



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

# World generation
# We need a simple rules, an initial state, some limitations and after all, collision between different parts of the
# world
# So, There are some territory
# The main spot - it's not like a square with 1 km size or so, it's more like province, that can hold one big city
'''
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
'''

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




# Well, I need a capital land, with full control of player
# So he can kill and destroy everithing. change climate, and recultivate with any nations, guilds and ordens
capital = Territory("Capital")

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
        self.feature = random.choice(land_base_feature)

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
# radius = 1
capital = Point(0, 0)
# territory = Circle(capital, radius)

# First param is angle alfa
# for now without overlaps
#alfa = random.randint(0, 270)

# second param angle fi, the main angle of sector
#fi = random.randint(1, 90)

# Point A on this circle have coordinates
#point_A = Point(cos(math.radians(alfa)), sin(math.radians(alfa)))

#point_B = Point(cos(math.radians(alfa + fi)), sin(math.radians(alfa + fi)))
'''
print(capital)
print(territory)
print(alfa)
print(math.radians(alfa))
print(fi)
print(alfa + fi)
print(math.radians(alfa + fi))
print(point_A)
print(point_B)
'''
alfa_1 = 10
fi_1 = 10

point_A1 = Point(cos(math.radians(alfa_1)), sin(math.radians(alfa_1)))
point_B1 = Point(cos(math.radians(alfa_1 + fi_1)), sin(math.radians(alfa_1 + fi_1)))

#print(Triangle(Point(0,0), point_A1, point_A1))

# Well, I get the points
# Point itself lie on circle, but really, I do not need circle itself
# So, well, the each territory have only two coordinates - alfa and fi


# Now, I need a sector of this circle

# By game, it is enough only two value to keep - angle and the lenght of this sector (the less, the better)

# Well, sorry, I need some time to remember circular points calculation =)
# So, the only coordinate, any point on circle have is angle
# But we need a two point, to make some area on that circle
# Happily, I need only one coordinate for each point


# We just need interception of this two sectors
# They intercept if any of the point in one sector are in second sector
# And we can take the border value to check
def intercept_checker(a1, a2, b1, b2):
    if a1 < b1:
        if a2 < b1:
            return "no"
        elif a2 > b2:
            return "included"
        else:
            return "intercept"
    else:
        if a1 > b2:
            return "no"
        elif a2 < b2:
            return "included"
        else:
            return "intercept"


assert intercept_checker(1, 3, 5, 7) == "no"
assert intercept_checker(1, 5, 3, 7) == "intercept"
assert intercept_checker(1, 7, 3, 5) == "included"
assert intercept_checker(3, 7, 1, 5) == "intercept"
assert intercept_checker(3, 5, 1, 7) == "included"
assert intercept_checker(5, 7, 1, 3) == "no"

# Now, back to problem with the degree
# The angle show the point between [0, 360) on the circle
# And after 360 value, it should start over, so 369 degree = 9 degree
# Probably I need to use functions (like cosines or sinus), instead of raw angle value
#print(8*pi - 2*pi)

arcs_rads = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4,
        4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7]
arcs = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180,
        190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360,
        370, 380, 390, 400]
all_arcs = []
for arc in arcs:
    all_funcs = [arc, math.radians(arc), sin(math.radians(arc)), cos(math.radians(arc)),
                 tan(math.radians(arc)), cot(math.radians(arc)), atan(math.radians(arc)),
                 acot(math.radians(arc))]
    all_arcs.append(all_funcs)
# Well, I need to calculate and show all trigonometry functions, to decide wich one I need, for my purpose
# print(tabulate.tabulate(all_arcs, headers=["arc", "rads", "sin", "cos", "tan", "cot", "atan", "acot"]))
