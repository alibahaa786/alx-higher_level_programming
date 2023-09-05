#!/usr/bin/python3
def uppercase(str):
    for let in str:
        letter = let
        if ord(let) > 96 and ord(let) < 123:
            letter = chr(ord(let) - 32)
        print("{}".format(letter), end="")
    else:
        print("")
