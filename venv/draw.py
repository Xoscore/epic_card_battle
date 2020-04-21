# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string

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


# Yet another try to make new language generator
# But this time, I make something completely different
# Instead of put rules one by one
# I make infrustructure first
# The goal is to make some container and transporter
# Both, they need to ask what was before and then tell what become next

'''
ёё|ёщ|ыё|ёу|йэ|гъ|кщ|щф|щз|эщ|щк|гщ|щп|щт|щш|щг|щм|фщ|щл|щд|дщ|ьэ|чц|вй|ёц|ёэ|ёа|йа|шя|шы|ёе|йё|гю|хя|йы|ця|гь|сй|хю|хё|
ёи|ёо|яё|ёя|ёь|ёэ|ъж|эё|ъд|цё|уь|щч|чй|шй|шз|ыф|жщ|жш|жц|ыъ|ыэ|ыю|ыь|жй|ыы|жъ|жы|ъш|пй|ъщ|зщ|ъч|ъц|ъу|ъф|ъх|ъъ|ъы|ыо|жя|
зй|ъь|ъэ|ыа|нй|еь|цй|ьй|ьл|ьр|пъ|еы|еъ|ьа|шъ|ёы|ёъ|ът|щс|оь|къ|оы|щх|щщ|щъ|щц|кй|оъ|цщ|лъ|мй|шщ|ць|цъ|щй|йь|ъг|иъ|ъб|ъв|
ъи|ъй|ъп|ър|ъс|ъо|ън|ък|ъл|ъм|иы|иь|йу|щэ|йы|йъ|щы|щю|щя|ъа|мъ|йй|йж|ьу|гй|эъ|уъ|аь|чъ|хй|тй|чщ|ръ|юъ|фъ|уы|аъ|юь|аы|юы|
эь|эы|бй|яь|ьы|ьь|ьъ|яъ|яы|хщ|дй|фй
'''
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# The minimal element of this - syllable, and we need to describe it properly
# Actualy, there is a two ways to make it correct prononsed
# 1) Restrict all incorrect ways
# 2) Add something, to make it correct again
class Syllable:
    def __init__(self):
        self.vowel

    # Output one syllable
    def print(self):
        print(self.cononant_before + self.vowel + self.consonant_after)


# Here comes first letter
# What pool of possible?
# start params

letters = {
    'а': {
        "type": "vowel",
        "is_yo": False
    },
    'б': {
        "type": "consonant",
        "sound": "voiced"
    },
    'в': {
        "type": "consonant",
        "sound": "voiced"
    },
    'г': {
        "type": "consonant",
        "sound": "voiced"
    },
    'д': {
        "type": "consonant",
        "sound": "voiced"
    },
    'е': {
        "type": "vowel",
        "is_yo": True
    },
    'ё': {
        "type": "vowel",
        "is_yo": True
    },
    'ж': {
        "type": "consonant",
        "sound": "voiced"
    },
    'з': {
        "type": "consonant",
        "sound": "voiced"
    },
    'и': {
        "type": "vowel",
        "is_yo": False
    },
    'й': {
        "type": "consonant",
        "sound": "voiced"
    },
    'к': {
        "type": "consonant",
        "sound": "deaf"
    },
    'л': {
        "type": "consonant",
        "sound": "voiced"
    },
    'м': {
        "type": "consonant",
        "sound": "voiced"
    },
    'н': {
        "type": "consonant",
        "sound": "voiced"
    },
    'о': {
        "type": "vowel",
        "is_yo": False
    },
    'п': {
        "type": "consonant",
        "sound": "deaf"
    },
    'р': {
        "type": "consonant",
        "sound": "voiced"
    },
    'с': {
        "type": "consonant",
        "sound": "deaf"
    },
    'т': {
        "type": "consonant",
        "sound": "deaf"
    },
    'у': {
        "type": "vowel",
        "is_yo": False
    },
    'ф': {
        "type": "consonant",
        "sound": "deaf"
    },
    'х': {
        "type": "consonant",
        "sound": "deaf"
    },
    'ц': {
        "type": "consonant",
        "sound": "deaf"
    },
    'ч': {
        "type": "consonant",
        "sound": "deaf"
    },
    'ш': {
        "type": "consonant",
        "sound": "deaf"
    },
    'щ': {
        "type": "consonant",
        "sound": "deaf"
    },
    'ь': {
        "type": "consonant",
        "special": "soft"
    },
    'ы': {
        "type": "vowel",
        "is_yo": False
    },
    'ъ': {
        "type": "consonant",
        "special": "hard"
    },
    'э': {
        "type": "vowel",
        "is_yo": False
    },
    'ю': {
        "type": "vowel",
        "is_yo": True
    },
    'я': {
        "type": "vowel",
        "is_yo": True
    },
}

letters_reverse = {
    "vowel": {
        "no_yo": ['а', 'и', 'о', 'у', 'э'],
        "have_yo": ['е', 'ю', 'я'],
        "yo": ['ё'],
        "op": ['ы']
    },
    "consonant": {
        "deaf": ['к', 'п', 'с', 'т', 'ф', 'х', 'ц'],
        "voiced": ['б', 'в', 'г', 'д', 'з', 'л', 'м', 'н', 'р'],
        "hissed": {
            "deaf": ['ч', 'ш', 'щ'],
            "voiced": ['ж']
        },
        "yo_con": ['й']
    },
    "mark": {
        "soft": ['ь'],
        "hard": ['ъ']
    }
}

print(tools.generate_new_name())

syllable_count = 1
no_yo = False
for syl in range(0, syllable_count):
    before_consonant = 2
    after_consonant = 2
    if before_consonant <= 2 and after_consonant == 0:
        # to make words without vowel
        pass
    if syl == 0:
        print("first")
    if before_consonant == 0:
        first_letter_candidate = letters_reverse["vowel"]["no_yo"] + letters_reverse["vowel"]["have_yo"]
    elif before_consonant >= 1:
        first_letter_candidate = letters_reverse["consonant"]["deaf"] + letters_reverse["consonant"]['voiced']
    print(syl)

for k in letters:
    print(letters[k])

first_letter_vowel =            ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']
yo = ['ё']

first_letter_consonant_deaf =   ['к', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
first_letter_consonant_voiced = ['б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р']

word = ''

letters_dict = {
    "vowels": {
        "can_be_first": ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я'],
        "cannot_be_first": ['ё', 'ы']
    },
    "consonants": {
        "can_be_first": ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                         'щ'],
        "cannot_be_first": ['й', 'ь', 'ъ']
    }
}


def word_creator(syll_count=1, ):
    vowel_list = letters_dict["vowels"]["can_be_first"]
    consonant_list = letters_dict["consonants"]["can_be_first"]
    have_yo = False
    is_first = True
    for syll in range(0, syll_count):


        if is_first:
            vowel_list += letters_dict["vowels"]["cannot_be_first"]
            consonant_list += letters_dict["consonants"]["cannot_be_first"]
            is_first = False

word_creator(1)

# I suddenly catch interesting thought, that I should make the structure of this universe on english, first
# Then look, how the one tribe can speak on english between themselfes, and only after that, make structure of that
# simplified language, and then generate new on that
