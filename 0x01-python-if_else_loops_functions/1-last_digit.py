#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
u_number = number
if number < 0:
    u_number *= -1
last_digit = u_number % 10
if number < 0:
    last_digit *= -1
print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print(f"and is greater than 5")
elif last_digit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
