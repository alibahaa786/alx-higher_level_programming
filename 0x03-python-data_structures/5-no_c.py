#!/usr/bin/python3
def no_c(my_string):
    array_string = [letter for letter in my_string if
                    letter != 'c' and letter != 'C']
    my_string = ""
    for letter in array_string:
        my_string += letter
    return my_string
