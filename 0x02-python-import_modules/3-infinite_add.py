#!/usr/bin/python3
"""Program that prints the result of the addition of all arguments"""

if __name__ == "__main__":
    import sys

    sum_ = 0
    for arg in sys.argv[1:]:
        sum_ += int(arg)

    print(sum_)
