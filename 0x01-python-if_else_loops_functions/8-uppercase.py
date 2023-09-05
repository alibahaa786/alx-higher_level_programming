#!/usr/bin/python3
def uppercase(str):
    for l in str:
        letter = l
        if ord(l) > 96 and ord(l) < 123:
            letter = chr(ord(l) - 32)
        print("{}".format(letter), end="")
    else:
        print("")
