def main():
    #print(pow(2, 1000))
    sumOfAllDigits(pow(2, 1000))

def sumOfAllDigits(num):
    sum = 0
    stringNum = str(num)
    for element in range(0, len(stringNum)):
        sum += int(stringNum[element])
    print(sum)
    return sum

main()