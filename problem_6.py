# The sum of the squares of the first ten natural numbers is, 1^2, 2^2, 3^2...10^2 = 385
# The square of the sum of the first ten natural numbers is (1+2+3+...10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def main():
    sum_of_squares = 0
    square_of_sums = 0
    difference     = 0
    for i in range(1,101):
        sum_of_squares += i**2
        square_of_sums += i
    square_of_sums = square_of_sums**2
    difference = square_of_sums-sum_of_squares
    print(f'difference is {difference}')

if __name__ == main():
    main()

