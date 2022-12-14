def main():
    number = 99
    bouncyNumbers = 0
    while (bouncyNumbers / number != 0.99):
        if (isBouncy(number)):
            bouncyNumbers += 1
        number += 1
    print(bouncyNumbers)
    print(number)
    



def isBouncy(num):
    isIncreasing = True
    isDecreasing = True
    lastDigit = 0
    if (num < 100):
        return False
    for i in range(len(str(num))):
        if (isIncreasing and isDecreasing):
            if (int(str(num)[i]) > lastDigit):
                isDecreasing = False
            if (int(str(num)[i]) < lastDigit):
                isIncreasing = False
        elif (isIncreasing):
            if (int(str(num)[i]) < lastDigit):
                return False
        elif (isDecreasing):
            if (int(str(num)[i]) > lastDigit):
                return False
    return True
    


main()