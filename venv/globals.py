# Globals

# To print long lists in comfortable way, should be > 5
MAX_PRINT_LIST_NUMBER = 10

# List of characters, that accepted as "Yes"
LIST_OF_ACCEPT_CHARACTERS = ["Y", "YES", "YEP", "Д", "ДА"]

# To control advices for newbie players
EXTENDED_ADVICES_BOOL = True

# Need to point on something
LIST_POINT_TO = {
    "personal": "You have ",
    "uncertain": "There are ",
}

# I need to keep some stupid names just for fun
LIST_STUPID_NAMES = [
    "Mr. Dick",
    "putin-sasay",
    "kadyrov-pidor",
]

# Need to keep Debug switcher somewhere
FLAG_DEBUG = False

# Some buttons, I want to keep and work separately
LIST_SYSTEM_CALLS = {
    "?": "'ESC' to exit\n'?' to help",
    "t": {
        "action": "tester",
        "description": "To test it",
    },
    "q": {
        "action": "on_exit",
        "description": "To exit from game",
    }
}

# Some buttons, which not ended the turn
LIST_NO_TIME_CONSUMPTION = {
    "o": "You observe everything",
    "b": "Your backpack is full of shit",
}