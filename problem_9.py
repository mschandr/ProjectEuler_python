"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2 or c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc
"""

def valid_trip(a, b, c):
    if a**2 + b**2 == c**2:
        return 1
    else:
        return 0

def main():
    for a in range(1,400):
        for b in range(a, 400):
            c = 1000 - a - b
            if valid_trip(a, b, c) == 1:
                if a + b + c == 1000:
                    print(f'a = {a}, b = {b}, c = {c} product = {a*b*c}')


if __name__ == "__main__":
    main()