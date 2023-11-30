#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    from calculator_1 import div, mul, sub, add

    print(mul(a, b))
    print(sub(a, b))
    print(div(a, b))
    print(add(a, b))