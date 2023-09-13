#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    lst = []
    check = 0
    for i in set_1:
        for num in set_2:
            if i == num:
                check = 1
                break
        if not check:
            lst.append(i)
        check = 0
    for i in set_2:
        for num in set_1:
            if i == num:
                check = 1
                break
        if not check:
            lst.append(i)
        check = 0
    ret = {x for x in lst}
    return ret
