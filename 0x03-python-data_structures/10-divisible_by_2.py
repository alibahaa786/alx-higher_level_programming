#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        if num % 2:
            result.append(False)
        else:
            result.append(True)
    return result
