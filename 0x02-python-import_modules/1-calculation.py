#!/usr/bin/python3
"""Program that imports functions from the file calculator_1.py, does some Maths, and prints the result"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("a = {:d}".format(a))
    print("b = {:d}".format(b))
    print("10 + 5 = {:d}".format(add(a, b)))
    print("10 - 5 = {:d}".format(sub(a, b)))
    print("10 * 5 = {:d}".format(mul(a, b)))
    print("10 / 5 = {:d}".format(div(a, b)))
