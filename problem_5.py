# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import sys

max_int = sys.maxsize

def divides_evenly(x):
    for i in (range(20, 1, -1)):
        if x % i != 0:
            return 0
        else:
            continue
    return 1

def main():
    for x in range(1, max_int):
        if divides_evenly(x) == 1:
            print(x)
            break

if __name__ == main():
    main()