#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = -1
else:
    sign = 1
rem = (number * sign) % 10
print(f"Last digit of {number} is {rem * sign}", end=" ")
if rem * sign == 0:
    print(f"and is 0")
elif rem * sign < 6:
    print(f"and is less than 6 and not 0")
else:
    print(f"and is greater than 5")
