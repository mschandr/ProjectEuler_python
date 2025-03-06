# By listing the first six prime numbers:t 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

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

def find_nth_prime(n):
    prime_count = 0
    num = 1  # Start checking from 1

    while prime_count < n:
        num += 1
        if is_prime(num):
            prime_count += 1

    return num  # Return the nth prime

def main():
    nth_prime = find_nth_prime(10001)
    print(f"The 10001st prime number is: {nth_prime}")

if __name__ == "__main__":
    main()