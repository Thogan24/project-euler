# Solved

import math
def main():
    factorial100 = list(str(math.factorial(100)))
    print(factorial100)
    print(sumOfDigits(factorial100))

def factorial(num):
    product = 1
    for i in range (num-1):
        product *= (i+1)
    return product

def sumOfDigits(num):
    # numString = str(num)
    # sum = 0
    # for i in range (num):
    #     print(i)
    #     sum += int(numString[i])
    # return sum
    b = [int(x) for x in num]
    return sum(b)



main()