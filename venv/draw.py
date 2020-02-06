# Let's try it another way again and again and again
# Imports
import tools
import globals
import random
import string


#minimum = 0.005
#percent = 5
#gte_amount = minimum * 100 / percent
#print(gte_amount)

MAX_SLOG_CONSONANT_IN_ROW = 2
# taken from here:
# https://pynative.com/python-generate-random-string/
# TODO work on name collisions and make them readable
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class random_language_rus():
    def __init__(self):
        self.word = ""
        self.has_yo = False
        self.no_hissing = False
        self.vowel_sounds = [
            "а", "и", "о", "у", "э",
        ]
        self.yo_no_his_vowel_sounds = [
            "ю", "я",
        ]
        self.yo_vowel_sounds = [
            "е",
        ]
        self.strange_letter = [
            "ы",
        ]
        self.yo = [
            "ё"
        ]
        self.consonant_sounds = [
            "б", "в", "г", "д", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц",
        ]
        self.mark_sweet = [
            "ь",
        ]
        self.mark_hard = [
            "ъ",
        ]
        self.hissing_consonant_sounds = [
            "ж", "ч", "ш", "щ",
        ]

    # open and close syllable defined by count of consonant after vowel, so no need to separate them
    def make_syllable(self, consonant_count_before=0, consonant_count_after=0, with_strange=True):
        consonant_before = ""
        consonant_after = ""
        # because in russian - one vowel equal one syllable, we take vowel first and control the count of consonants
        # I collect vowel list here for comfort, because vowel can be in any place
        vowel_list = self.vowel_sounds + self.yo_vowel_sounds
        # check, if hissing letter was in previous syllable - we cannot use 'ю', 'я' or 'ы' after hissing
        if not self.no_hissing:
            vowel_list += self.yo_no_his_vowel_sounds
        # we can use only one 'ё' in word, so do not pick it if it is in previous syllable
        if not self.has_yo:
            vowel_list += self.yo
        # in additional, 'ы' is not very often letter, so need to switch it
        if with_strange:
            vowel_list += self.strange_letter
        # get the vowel
        vowel = random.choice(vowel_list)
        # word cannot start word from 'ы'
        if vowel in self.strange_letter:
            consonant_count_before += 1
        # check if it's 'ё'
        if vowel in self.yo:
            self.has_yo = True
        # check if it's no hissing letter for after consonant or next syllable
        if vowel in self.yo_no_his_vowel_sounds or vowel in self.strange_letter:
            self.no_hissing = True

        for i in range(0, consonant_count_before):
            # but for consonant - it depends on the place
            if i + 1 == consonant_count_before and self.no_hissing:
                consonant_before += random.choice(self.consonant_sounds)
                self.no_hissing = False
            else:
                consonant_before += random.choice(self.consonant_sounds + self.hissing_consonant_sounds)

        for i in range(0, consonant_count_after):
            consonant_after += random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
            if i + 1 == consonant_count_after and consonant_after[-1:] in self.hissing_consonant_sounds:
                self.no_hissing = True

        #print(consonant_before + vowel + consonant_after)
        self.word += consonant_before + vowel + consonant_after

    def gimmi(self):
        print(self.word.capitalize())

name_test = random_language_rus()
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.gimmi()


yet_another_message = "New turn has start, command me your majesty! "
list_of_pc_objects = []
list_of_locations = []
# Define the main process here
class character():
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = randomName_rus(10)
        self.name = name.capitalize()

    def describe(self):
        print("Your name is " + self.name)

class location():
    def __init__(self, id, name=None):
        self.id = id
        if name is None:
            name = randomName_rus(10)
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
            char_name = random.choice(globals.LIST_STUPID_NAMES)
            print("I will call you " + char_name + " for that")
        main_PC = character("main_PC", name=char_name)
        list_of_pc_objects.append(player)
        main_PC.describe()
        start_town_name = tools.entry_point("What the name of your hometown? ", str_max=10)
        if start_town_name == "":
            print("I do not like you already")
            start_town_name = random.choice(globals.LIST_STUPID_TOWN_NAMES)
            print("I'm sure, that you from this place " + start_town_name)
        start_town = location("start_town", name=start_town_name)
        list_of_locations.append(start_town)
        start_town.describe()

    def generate_new_name(self):
        print(randomName_rus(random.randint(1,4)).capitalize())

    def running(self):
        #self.start_game()
        while self.flag_is_playing:
            command = tools.entry_point(yet_another_message)
            if command == "name":
                self.generate_new_name()
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

def initialle():
    direction = input("Do you want to go adventure? ")
    if direction.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
        print("So you drink a cup of wine, sing the song and go in nowhere!")
    else:
        print("You want to stay in your dirty old farm forever")
    print("Anyway, we start to emulate life right now!")
