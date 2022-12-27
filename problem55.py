# Unsolved

# Not sure what the problem here is at it produces an answer very close to the correct one, but not the correct one
def main():
    lyrchrelNumberCount = 0
    for i in range(0, 10000):
        lyrchrel = True
        num = i
        cycleCount = 0
        while(cycleCount < 50):
            if (isPalindromic(num)):
                lyrchrel = False
                break
            num += int(reverse(num))
            cycleCount += 1
        if(lyrchrel):
            lyrchrelNumberCount += 1
        print(str(i) + " | " + str(lyrchrelNumberCount))



# Changed this function so that it returns a string
def reverse(num):
    
    reverseNum = ""
    while(num > 0):
        reverseNum += str(num % 10)
        #print(str(num % 10))
        num = num // 10
    return (reverseNum)

def isPalindromic(num):
    reverseNum = reverse(num)
    numString = str(num)
    numLength = len(numString)
    answer = ""
    answerSecondHalf = ""
    if (numLength % 2 == 0):
        for i in range(int(numLength / 2)):
            #print(reverseNum)
            answer += numString[i]
            answerSecondHalf += reverseNum[i]
    else:
        for k in range(int(numLength // 2)):
            answer += numString[k]
            answerSecondHalf += reverseNum[k]
    return answer == answerSecondHalf

# def isPandigital(num):
#     listWithAllDigits = []
#     for i in range(1, len(str(num)) + 1):
#         listWithAllDigits += str(i)
    
#     for j in range(len(str(num))):
#         if(listWithAllDigits.count(str(num)[j])):
#             listWithAllDigits.remove(str(num)[j])
#         else:
#             return False
#     if(len(listWithAllDigits) == 0):
#         return True

#     return False # Not sure if it should be able to get to this point or not

main()