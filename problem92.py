# Solved, but takes very long to compute

def main():
    num = 1
    count89 = 0
    while(num < 10000000):
        repeated = False
        numList = []
        i = num
        while(repeated == False):
            numList.append(i)
            if(numList.count(89) > 0):
                count89 += 1
                repeated = True
            elif(numList.count(1) > 0):
                repeated = True
            # elif (numList.count(i) > 1):
            #     repeated = True
            i = sumOfSquareOfDigits(i)
        print(str(num) + " | " + str(count89))
        num += 1

            

def sumOfSquareOfDigits(num):
    b = [int(x)**2 for x in str(num)]
    return sum(b)

main()