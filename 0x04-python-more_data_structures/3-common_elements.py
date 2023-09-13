#!/usr/bin/python3

def common_elements(set_1, set_2):
    ret = []
    for i in set_1:
        for num in set_2:
            if i == num:
                ret.append(num)
                break
    final_ret = {x for x in ret}
    return final_ret
