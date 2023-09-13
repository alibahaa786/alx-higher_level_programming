#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = {num for num in my_list}
    sum = 0
    for num in uniq:
        sum += num
    return sum
