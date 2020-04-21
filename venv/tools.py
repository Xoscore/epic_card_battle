import globals
import random
import string

# I keep all working functions pars here
# Usually it's just procedural ones, with clean return, not related to any objects

# I need procedural tool to make a good string from list
# Usage:
# Just put any dict or list inside and get string outside
def tool_list_to_string(some_list, appeal=None, shorten_list=True):
    if appeal not in globals.LIST_POINT_TO:
        appeal = globals.LIST_POINT_TO["uncertain"]
    else:
        appeal = globals.LIST_POINT_TO[appeal]
    if type(some_list) is dict:
        if "name" in some_list:
            list_name = some_list["name"]
        else:
            list_name = "thing"
        if len(some_list["contain"]) == 0:
            output_string = appeal    + "no any " + list_name + "s"
        elif len(some_list["contain"]) == 1:
            output_string = appeal + "one " + list_name + ", it is the " + str(some_list["contain"][0])
        elif len(some_list["contain"]) > globals.MAX_PRINT_LIST_NUMBER and shorten_list:
            output_string = appeal + ', '.join(map(str, some_list["contain"][:4])) + " and " + \
                            str(len(some_list["contain"]) - 4) + " more " + list_name + "s"
        else:
            output_string = appeal + str(len(some_list["contain"])) + " " + list_name + "s, it is: " + \
                            ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) + " and " + \
                            str(some_list["contain"][-1])
    elif type(some_list) is list:
        if len(some_list) == 0:
            output_string = appeal + "no anything like this"
        elif len(some_list) == 1:
            output_string = appeal + "only " + str(some_list[0])
        elif len(some_list) > globals.MAX_PRINT_LIST_NUMBER and shorten_list:
            output_string = appeal + ', '.join(map(str, some_list[:4])) + " and " + str(len(some_list) - 4) + \
                  " more of this"
        else:
            output_string = appeal + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1])
    else:
        raise TypeError("This function is for list or dict only! " + str(type(some_list)) + " incoming!")
    return output_string

# My own function to parse input
# Examples:
# char_name = tools.entry_point("What is your name?", str_max=10) # - ask for string, 10 characters long, cut for longer
# char_age = tools.entry_point("What is your age?", int, int_min=12, int_max=90) # - ask for int from 12 to 90
# char_live = tools.entry_point("Are you alive?", bool, strict_yes=True) # bool entry from bool list in global
# char_sex = tools.entry_point("What is your sex?", ["male", "female"]) # string choice from several options
def entry_point(message=None, asked_type=None, int_min=None, int_max=None, strict_yes=False, str_max=None):
    if message is None:
        message = "What now? "
    if asked_type is None:
        asked_type = str
    if type(asked_type) is list:
        ask_for_type = " Choose one of this: " + tool_list_to_string(asked_type, "empty", False) + " "
        while True:
            user_command = input(message + ask_for_type)
            if len(user_command) == 0:
                message = "Do not input empty value!"
            elif user_command not in asked_type:
                message = "You can choose only from this list!"
            else :
                break
    elif asked_type is int:
        # I need to control max and min later on, but need some system default limitations
        if int_min is None:
            int_min = globals.MAX_INT_RANGE["min"]
        if int_max is None:
            int_max = globals.MAX_INT_RANGE["max"]
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
            print("It is more, then "+ globals.MAX_STRING_SIZE + ", I will cut it")
            user_command = user_command[:globals.MAX_STRING_SIZE]
    return user_command

# I cannot make it any better, on this level
'''
ёё|ёщ|ыё|ёу|йэ|гъ|кщ|щф|щз|эщ|щк|гщ|щп|щт|щш|щг|щм|фщ|щл|щд|дщ|ьэ|чц|вй|ёц|ёэ|ёа|йа|шя|шы|ёе|йё|гю|хя|йы|ця|гь|сй|хю|хё|
ёи|ёо|яё|ёя|ёь|ёэ|ъж|эё|ъд|цё|уь|щч|чй|шй|шз|ыф|жщ|жш|жц|ыъ|ыэ|ыю|ыь|жй|ыы|жъ|жы|ъш|пй|ъщ|зщ|ъч|ъц|ъу|ъф|ъх|ъъ|ъы|ыо|жя|
зй|ъь|ъэ|ыа|нй|еь|цй|ьй|ьл|ьр|пъ|еы|еъ|ьа|шъ|ёы|ёъ|ът|щс|оь|къ|оы|щх|щщ|щъ|щц|кй|оъ|цщ|лъ|мй|шщ|ць|цъ|щй|йь|ъг|иъ|ъб|ъв|
ъи|ъй|ъп|ър|ъс|ъо|ън|ък|ъл|ъм|иы|иь|йу|щэ|йы|йъ|щы|щю|щя|ъа|мъ|йй|йж|ьу|гй|эъ|уъ|аь|чъ|хй|тй|чщ|ръ|юъ|фъ|уы|аъ|юь|аы|юы|
эь|эы|бй|яь|ьы|ьь|ьъ|яъ|яы|хщ|дй|фй
'''

class random_language_rus:
    def __init__(self, syllable_count=3):
        self.word = ""
        self.has_yo = False
        self.no_hissing = False
        self.syllable_count = syllable_count
        self.state = {

        }
        if self.syllable_count < 1:
            i = abs(self.syllable_count)
            while True:
                i -= 1
                self.word += random.choice(self.mark_hard + self.mark_sweet + self.strange_letter)
                if i == 0:
                    break

        self.vowel_sounds = [
            "а", "и", "о", "у", "э",
        ]
        self.yo_no_his_vowel_sounds = [
         #   "ю", "я",
        ]
        self.yo_vowel_sounds = [
            "е",
        ]
        self.strange_letter = [
         #   "ы",
        ]
        self.yo = [
          #  "ё"
        ]
        self.consonant_sounds = [
            "б", "в", "г", "д", "з", "к", "л", "м", "н", "п", "р", "с", "т",
            #"ф", "х", "ц", "й",
        ]
        self.mark_sweet = [
            "ь",
        ]
        self.mark_hard = [
            "ъ",
        ]
        self.hissing_consonant_sounds = [
         #   "ж", "ч", "ш", "щ",
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

        # need to make separate consonant creators for before and after
        # or probably not...
        if consonant_count_before > 0:
            pass
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

    def consonant_before(self, count=1):

        # should not cycle here - it hardly depends on order and place
        for i in range(0, count):
            # but for consonant - it depends on the place
            if i + 1 == count and self.no_hissing:
                consonant_before += random.choice(self.consonant_sounds)
                self.no_hissing = False
            else:
                consonant_before += random.choice(self.consonant_sounds + self.hissing_consonant_sounds)

    def gimmi(self):
        return self.word

def generate_new_name():
    name_test = random_language_rus()
    first_letter = random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW)
    second_letter = 2
    third_letter = 0
    if first_letter == 0:
        second_letter = 0
        third_letter = 2
    name_test.make_syllable(first_letter, second_letter)
    name_test.make_syllable(third_letter, 1)
    new_name = name_test.gimmi()
    #return rus_to_eng(new_name)
    return new_name

#name_test = random_language_rus()
#name_test.make_syllable(random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW))
#name_test.make_syllable(random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW))
#name_test.make_syllable(random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW), random.randint(0, globals.MAX_SLOG_CONSONANT_IN_ROW))
#name_test.gimmi()


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
        elif L in (string.ascii_lowercase):
            eng_word += L
    return eng_word
