#!/usr/bin/python3
 for char i in range(90, 64, -1):
    print("{:c}".format(char(i + 32 * (i % 2))), end="")
