#!/usr/bin/python3
for first in range(8):
    for second in range(first + 1, 10):
        print("{}{}, ".format(first, second), end="")
else:
    print("89")
