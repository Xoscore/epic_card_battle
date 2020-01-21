import globals
import string

# I keep all working functions pars here
# Usually it's just procedural ones, with clean return, not related to any objects

# I need procedural tool to make a good string from list
def tool_list_to_string(some_list, appeal=None):
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
            print(appeal    + "no any " + list_name + "s")
        elif len(some_list["contain"]) == 1:
            print(appeal + "one " + list_name + ", it is the " + str(some_list["contain"][0]))
        elif len(some_list["contain"]) <= globals.MAX_PRINT_LIST_NUMBER:
            print(appeal + str(len(some_list["contain"])) + " " + list_name + "s, it is: " +
                  ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) + " and " +
                  str(some_list["contain"][-1]))
        else:
            print(appeal + ', '.join(map(str, some_list["contain"][:4])) + " and " +
                  str(len(some_list["contain"]) - 4) + " more " + list_name + "s")
            full_list = input("Do you want to see the full list? ")
            if full_list.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
                print(appeal + str(len(some_list["contain"])) + " " + list_name + "s, it is: " +
                      ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) +
                        " and " + str(some_list["contain"][-1]))
            else:
                print("I think this is no, for sure")
                if EXTENDED_ADVICES_BOOL:
                    print('For "Yes", please input one of this: ' + globals.LIST_OF_ACCEPT_CHARACTERS)
    elif type(some_list) is list:
        if len(some_list) == 0:
            print(appeal + "no anything like this")
        elif len(some_list) == 1:
            print(appeal + "only " + str(some_list[0]))
        elif len(some_list) <= globals.MAX_PRINT_LIST_NUMBER:
            print(appeal + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1]))
        else:
            print(appeal + ', '.join(map(str, some_list[:4])) + " and " + str(len(some_list) - 4) +
                  " more of this")
            full_list = input("Do you want to see the full list? ")
            if full_list.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
                print(appeal + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1]))
            else:
                print("I think this is no, for sure")
                if globals.EXTENDED_ADVICES_BOOL:
                    print('For "Yes", please input one of this: ' + globals.LIST_OF_ACCEPT_CHARACTERS)
    else:
        raise TypeError("This function is for list or dict only")

# https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int/7588720#7588720? \
# newreg=7fd570f4fdbb465991904083fcfcf574
# Code from here, some guy `krzym` share it
# thanks for help, but I do not need this anymore
#eval_string = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or \
#                     len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x

# My own function to parse input
def entry_point(message=None, asked_type=None, int_min=None, int_max=None, strict_yes=False, str_max=None):
    if message is None:
        message = "What now? "
    if asked_type is None:
        asked_type = str
    if asked_type is int:
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