#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in range(len(my_list - 1)):
        if my_list[i] > my_list[i + 1]:
            max = my_list[i]
        else:
            max = my_list[i + 1]
    return max