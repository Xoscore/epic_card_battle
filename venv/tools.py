import globals

# I need procedural tool to make a good string from list
def tool_list_to_string(some_list):
    if type(some_list) is dict:
        list_name = str(some_list["name"])
        if len(some_list["contain"]) == 0:
            print("You do not have any " + list_name + "s")
        elif len(some_list["contain"]) == 1:
            print("You have one " + list_name +
                  ", it is the " + str(some_list["contain"][0]))
        elif len(some_list["contain"]) <= globals.MAX_PRINT_LIST_NUMBER:
            print("You have " + str(len(some_list["contain"]))
                  + " " + list_name
                  + "s, it is: " + ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) +
                  " and " + str(some_list["contain"][-1]))
        else:
            print("You have " + ', '.join(map(str, some_list["contain"][:4])) + " and " +
                  str(len(some_list["contain"]) - 4) + " more " + list_name + "s")
            full_list = input("Do you want to see the full list? ")
            if full_list.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
                print("You have " + str(len(some_list["contain"])) + " " + list_name + "s, it is: " +
                      ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) +
                        " and " + str(some_list["contain"][-1]))
            else:
                print("I think this is no, for sure")
                if EXTENDED_ADVICES_BOOL:
                    print('For "Yes", please input one of this: ' + globals.LIST_OF_ACCEPT_CHARACTERS)
    elif type(some_list) is list:
        if len(some_list) == 0:
            print("You have nothing like this")
        elif len(some_list) == 1:
            print("You have only " + str(some_list[0]))
        elif len(some_list) <= globals.MAX_PRINT_LIST_NUMBER:
            print("You have " + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1]))
        else:
            print("You have " + ', '.join(map(str, some_list[:4])) + " and " + str(len(some_list) - 4) +
                  " more of this")
            full_list = input("Do you want to see the full list? ")
            if full_list.upper() in globals.LIST_OF_ACCEPT_CHARACTERS:
                print("You have " + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1]))
            else:
                print("I think this is no, for sure")
                if globals.EXTENDED_ADVICES_BOOL:
                    print('For "Yes", please input one of this: ' + globals.LIST_OF_ACCEPT_CHARACTERS)
    else:
        raise TypeError("This function is for list or dict only")