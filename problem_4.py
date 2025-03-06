# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit number is 9009 = 91*99
# Find the largest palindrome made from the product of two 3-digit numbers.

def test_product(i):
    test = str(i)
    i=0
    while i < len(test):
        if test[i] != test[-i-1]:
            return 0
        else:
            i += 1
            continue
    return 1

def main():
    digit_1 = range(100,1000)
    digit_2 = range(100,1000)
    product = 0
    greatest_product = 0
    for x in digit_1:
        for y in digit_2:
            product = x*y
            if test_product(product) == 1:
                print(f'{product}')
                if product > greatest_product:
                    greatest_product = product
    return print(f'greatest product {greatest_product}')



if __name__ == main():
    main()
