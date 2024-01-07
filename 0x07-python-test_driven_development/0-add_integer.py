#!/usr/bin/python3
"""this module has a function that adds up 2 integrs"""
def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""

    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        return int(a) + int(b)
    else:
        return "a must be an integer"
    
print(add_integer(2))
