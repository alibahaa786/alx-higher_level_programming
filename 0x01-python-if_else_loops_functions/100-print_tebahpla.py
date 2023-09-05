#!/usr/bin/python3
for num in range(-122, -96):
    number = num * -1
    if number % 2 != 0:
        number -= 32
    print("{}".format(chr(number)), end="")
