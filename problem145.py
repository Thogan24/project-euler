# Unsolved

def main():
    count = 0
    for i in range (10**9):
        if(allDigitsOdd(i + reverse(i))):
            count += 1
            #print(str(i) + " | " + str(count))
    print(count)




def reverse(num):
    reverseNum = 0
    while(num > 1):
        reverseNum += (num % 10)
        num = num // 10
    return reverseNum
        



def allDigitsOdd(num):
    numString = str(num)
    for i in range(len(numString)):
        if(int(numString[i]) % 2 == 0):
            return False
    return True
main()