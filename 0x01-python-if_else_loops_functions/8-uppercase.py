#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            uppercase_char = chr(ord(str[i]) - 32)
            print(uppercase_char, end='')
        else:
            print(str[i], end='')
    print()