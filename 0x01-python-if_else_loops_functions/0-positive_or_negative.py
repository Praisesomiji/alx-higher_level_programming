#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    output = "is positive"
elif number < 0:
    output = "is negative"
else:
    output = "is zero"
print(f"{number} is {output}")
