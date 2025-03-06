"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million
"""

import math

def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False  # Eliminate even numbers

    for i in range(3, math.isqrt(x) + 1, 2):  # Check odd divisors up to sqrt(x)
        if x % i == 0:
            return False  # Not prime if divisible

    return True  # Prime if no divisors found


def main():
    primes = []
    total = 0
    for i in range(1_999_999, 3, -2):
        if is_prime(i) == 1:
           primes.append(i)
    primes.extend([3, 2])

    for x in primes:
        total += x
        print(x)

    print(total)
    return total

if __name__ == "__main__":
    main()