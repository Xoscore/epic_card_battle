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


MAX_SLOG_CONSONANT_IN_ROW = 1
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

    def make_syllable(self, consonant_count_before=0, consonant_count_after=0):
        consonant_before = ""
        consonant_after = ""
        vowel_list = self.vowel_sounds + self.yo_vowel_sounds
        if not self.no_hissing:
            vowel_list += self.yo_no_his_vowel_sounds + self.strange_letter
        if not self.has_yo:
            vowel_list += self.yo
        #vowel = random.choice(vowel_list)
        vowel = random.choice(self.strange_letter)
        if vowel == 'ё':
            self.has_yo = True
        if vowel in self.yo_no_his_vowel_sounds or vowel in self.strange_letter:
            self.no_hissing = True
        for i in range(0, consonant_count_before):
            if i == consonant_count_before and self.no_hissing:
                consonant_before += random.choice(self.consonant_sounds)
                self.no_hissing = False
            else:
                consonant_before += random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
        for i in range(0, consonant_count_after):
            consonant_after += random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
            if i == consonant_count_after and consonant_after in self.hissing_consonant_sounds:
                self.no_hissing = True
        print(consonant_before + vowel + consonant_after)
        self.word += consonant_before + vowel + consonant_after

    def open_slog(self, consonant_count=None):
        if consonant_count is None:
            consonant_count = random.randint(0, MAX_SLOG_CONSONANT_IN_ROW)
        for i in range (0,consonant_count):
            consonant = random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
            self.word += consonant
        if not self.has_yo:
            vowel = random.choice(self.vowel_sounds + self.yo)
            if vowel == 'ё':
                self.has_yo = True
        else:
            vowel = random.choice(self.vowel_sounds)
        self.word += vowel


    def closed_slog(self, consonant_count_before=None, consonant_count_after=None):
        if consonant_count_before is None:
            consonant_count_before = random.randint(0, MAX_SLOG_CONSONANT_IN_ROW)
        if consonant_count_after is None:
            consonant_count_after = 1
        for i in range(0,consonant_count_before):
            consonant = random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
            self.word += consonant
        if not self.has_yo:
            vowel = random.choice(self.vowel_sounds + self.yo)
            if vowel == 'ё':
                self.has_yo = True
        else:
            vowel = random.choice(self.vowel_sounds)
        self.word += vowel
        for i in range(0, consonant_count_after):
            consonant = random.choice(self.consonant_sounds + self.hissing_consonant_sounds)
            self.word += consonant

    def gimmi(self):
        print(self.word.capitalize())

name_test = random_language_rus()
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.make_syllable(random.randint(0, MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, MAX_SLOG_CONSONANT_IN_ROW))
name_test.gimmi()


def randomName_rus(stringLenght=10):
    yo_slogs = [
        "бё", "вё", "гё", "дё", "зё", "кё", "лё", "мё", "нё", "пё", "рё", "сё", "тё", "фё", "хё", "цё", "ё",
        "ёб", "ёв", "ёг", "ёд", "ёз", "ёк", "ёл", "ём", "ён", "ёп", "ёр", "ёс", "ёт", "ёф", "ёх", "ёц", "ёй",
        "ёж", "ёш", "ёч", "ёщ",
    ]
    sweet_slogs = [
        "бь", "вь", "гь", "дь", "жь", "зь", "кь", "ль", "мь", "нь", "пь", "рь", "сь", "ть", "фь", "хь", "шь", "щь",
    ]
    special_slogs = [
        "ъ", "й", "ы",
    ]
    j_slogs = [
        "йа", "йо", "йу", "йэ",
    ]
    snaky_slogs = [

        "жа", "же", "жи", "жо", "жу",
        "ца", "це", "ци", "цо", "цу",
        "ча", "че", "чи", "чо", "чу",
        "ша", "ше", "ши", "шо", "шу",
        "ща", "ще", "щи", "що", "щу",
        "аж", "еж", "иж", "ож", "уж",
        "ац", "ец", "иц", "оц", "уц",
        "ач", "еч", "ич", "оч", "уч",
        "аш", "еш", "иш", "ош", "уш",
        "ащ", "ещ", "ищ", "ощ", "ущ",
    ]
    snaky_not_second_slogs = [
        "ыж", "эж", "юж", "яж",
        "ыц", "эц", "юц", "яц",
        "ыч", "эч", "юч", "яч",
        "ыш", "эш", "юш", "яш",
        "ыщ", "эщ", "ющ", "ящ",
    ]
    slogs = [
        "ба", "бе", "би", "бо", "бу", "бы", "бэ", "бю", "бя",
        "ва", "ве", "ви", "во", "ву", "вы", "вэ", "вю", "вя",
        "га", "ге", "ги", "го", "гу", "гы", "гэ", "гю", "гя",
        "да", "де", "ди", "до", "ду", "ды", "дэ", "дю", "дя",
        "за", "зе", "зи", "зо", "зу", "зы", "зэ", "зю", "зя",
        "ка", "ке", "ки", "ко", "ку", "кы", "кэ", "кю", "кя",
        "ла", "ле", "ли", "ло", "лу", "лы", "лэ", "лю", "ля",
        "ма", "ме", "ми", "мо", "му", "мы", "мэ", "мю", "мя",
        "на", "не", "ни", "но", "ну", "ны", "нэ", "ню", "ня",
        "па", "пе", "пи", "по", "пу", "пы", "пэ", "пю", "пя",
        "ра", "ре", "ри", "ро", "ру", "ры", "рэ", "рю", "ря",
        "са", "се", "си", "со", "су", "сы", "сэ", "сю", "ся",
        "та", "те", "ти", "то", "ту", "ты", "тэ", "тю", "тя",
        "фа", "фе", "фи", "фо", "фу", "фы", "фэ", "фю", "фя",
        "ха", "хе", "хи", "хо", "ху", "хы", "хэ", "хю", "хя",

        "аб", "еб", "иб", "об", "уб", "ыб", "эб", "юб", "яб",
        "ав", "ев", "ив", "ов", "ув", "ыв", "эв", "юв", "яв",
        "аг", "ег", "иг", "ог", "уг", "ыг", "эг", "юг", "яг",
        "ад", "ед", "ид", "од", "уд", "ыд", "эд", "юд", "яд",
        "аз", "ез", "из", "оз", "уз", "ыз", "эз", "юз", "яз",
        "ай", "ей", "ий", "ой", "уй", "ый", "эй", "юй", "яй",
        "ак", "ек", "ик", "ок", "ук", "ык", "эк", "юк", "як",
        "ал", "ел", "ил", "ол", "ул", "ыл", "эл", "юл", "ял",
        "ам", "ем", "им", "ом", "ум", "ым", "эм", "юм", "ям",
        "ан", "ен", "ин", "он", "ун", "ын", "эн", "юн", "ян",
        "ап", "еп", "ип", "оп", "уп", "ып", "эп", "юп", "яп",
        "ар", "ер", "ир", "ор", "ур", "ыр", "эр", "юр", "яр",
        "ас", "ес", "ис", "ос", "ус", "ыс", "эс", "юс", "яс",
        "ат", "ет", "ит", "от", "ут", "ыт", "эт", "ют", "ят",
        "аф", "еф", "иф", "оф", "уф", "ыф", "эф", "юф", "яф",
        "ах", "ех", "их", "ох", "ух", "ых", "эх", "юх", "ях",
    ]
    solo_slogs = [
        "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",
    ]
    #print(slogs[38:])
    name = ''.join(random.choice(slogs) for i in range(stringLenght))
    return name

# really bad, I will try to make it in russian first
def randomName(stringLenght=10):
    slogs = [
        "qe", "qy", "qu", "qi", "qo", "qa",
        "we", "wy", "wu", "wi", "wo", "wa",
        "re", "ry", "ru", "ri", "ro", "ra",
        "te", "ty", "tu", "ti", "to", "ta",
        "pe", "py", "pu", "pi", "po", "pa",
        "se", "sy", "su", "si", "so", "sa",
        "de", "dy", "du", "di", "do", "da",
        "fe", "fy", "fu", "fi", "fo", "fa",
        "ge", "gy", "gu", "gi", "go", "ga",
        "he", "hy", "hu", "hi", "ho", "ha",
        "je", "jy", "ju", "ji", "jo", "ja",
        "ke", "ky", "ku", "ki", "ko", "ka",
        "le", "ly", "lu", "li", "lo", "la",
        "ze", "zy", "zu", "zi", "zo", "za",
        "xe", "xy", "xu", "xi", "xo", "xa",
        "ce", "cy", "cu", "ci", "co", "ca",
        "ve", "vy", "vu", "vi", "vo", "va",
        "be", "by", "bu", "bi", "bo", "ba",
        "ne", "ny", "nu", "ni", "no", "na",
        "me", "my", "mu", "mi", "mo", "ma",
    ]
    name = ''.join(random.choice(slogs) for i in range(stringLenght))
    return name
#for i in range(0,10,1):
#print(randomName_rus(random.randint(1,4)).capitalize())


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
