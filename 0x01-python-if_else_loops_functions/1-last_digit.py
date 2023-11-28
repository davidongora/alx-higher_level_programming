#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10 

print("Last digit of", number)

if last_digit > 5:
    category = "and is greater than 5"
elif last_digit == 0:
    category = "and is 0"
else:
    category = "and is less than 6 and not 0"

print(category)