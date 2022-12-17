def main():
    i = 1
    potentialAnswer = True
    while(True):
        print(i)
        for j in range(1, 6):
            if (sameDigits(i, j*i) == False):
                potentialAnswer = False
                break
            else:
                potentialAnswer = True
        if (potentialAnswer):
            print(i)
            break
        potentialAnswer = True
        i += 1


def sameDigits(initialNum, num):
    initialNumList = list(str(initialNum))
    initialNumListLength = len(initialNumList)
    print(str(initialNumList) + " | " + str(num))
    for i in range(len(str(num))):
        # While loop that changes value of the length
        # Everytime object is removed subtract one from that length and don't add j
        j = 0
        while(j < initialNumListLength):
            if(str(num)[i] == initialNumList[j]):
                initialNumList.pop(j)
                initialNumListLength -= 1
                break
            else:
                j += 1
        
        # for j in range(len(initialNumList)):
        #     if(str(num)[i] == initialNumList[j]):
        #         initialNumList.pop(j)
    
    if(len(initialNumList) == 0):
        return True

    return False


main()