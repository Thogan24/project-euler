def main():
    number = 99
    bouncyNumbers = 0
    while (bouncyNumbers / number != 0.99):
        if (isBouncy(number)):
            bouncyNumbers += 1
        number += 1
        print(str(bouncyNumbers) + " " + str(number))
    print(number)
    



def isBouncy(num):
    isIncreasing = True
    isDecreasing = True
    lastDigit = int(str(num)[1])
    if (num < 100):
        return False
        #100
    for i in range(1, len(str(num))):
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