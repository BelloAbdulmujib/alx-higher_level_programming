#!/usr/bin/python3
 for i in range(90, 64, -1):
    print("{:c}".format(i + 32 * (i % 2)), end="")
