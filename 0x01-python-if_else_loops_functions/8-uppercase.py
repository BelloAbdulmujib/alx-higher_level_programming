#!/usr/bin/python3
def uppercase(s):
    for c in s:
        print("{:c}".format(ord(c) - 32), end="")
    print()
