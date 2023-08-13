#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    mod = number % -10
else:
    mod = number % 10

if (mod > 5):
    status = "greater than 5"
elif (mod < 6):
    status = "less than 6 and not 0"
else:
    status = "0"

print(f"Last digit of {number} is {mod:d} and is {status}")
