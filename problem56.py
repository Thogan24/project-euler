def main():
    maxDigitSum = 0
    i = 99
    j = 99
    while(i > 0):
        while (j > 0):
            if(sumOfDigits(i**j) > maxDigitSum):
                maxDigitSum = sumOfDigits(i**j)
            print(maxDigitSum)
            j -= 1
        i -= 1
    print(maxDigitSum)

def sumOfDigits(num):
    b = [int(x) for x in str(num)]
    return sum(b)

main()