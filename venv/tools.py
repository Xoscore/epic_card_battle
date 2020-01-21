import globals
import string

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
eval_string = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or \
                     len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x

