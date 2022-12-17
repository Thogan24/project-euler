# Solved

def main():
    num = 2
    sumOfAll = 0
    while(True):
        sumOfDigitsToPower = 0
        b = [int(x) for x in str(num)]
        for i in range(len(b)):
            sumOfDigitsToPower += (b[i])**5
        if(sumOfDigitsToPower == num):
            sumOfAll += num
        num += 1
        print(sumOfAll)



main()
