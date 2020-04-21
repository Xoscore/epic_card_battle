

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