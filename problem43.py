# Unsolved

def main():
    firstPrimeList = [2, 3, 5, 7, 11, 13, 17]
    sumOfPandigitalProperties = 0
    for i in range(1000000000, 9999999999):
        broke = False
        if(isPandigital(i)):
            for j in range(7):
                if(not (str(i[2+j]) + str(i[3+j]) + str(i[4+j]) % firstPrimeList[j] == 0)):
                    broke = True
                    break
            if(not broke):
                sumOfPandigitalProperties += i
                print(sumOfPandigitalProperties)
        
    print(sumOfPandigitalProperties)
                    


def isPandigital(num):
    listWithAllDigits = []
    for i in range(1, len(str(num)) + 1):
        listWithAllDigits += str(i)
    
    for j in range(len(str(num))):
        if(listWithAllDigits.count(str(num)[j])):
            listWithAllDigits.remove(str(num)[j])
        else:
            return False
    if(len(listWithAllDigits) == 0):
        return True

    return False # Not sure if it should be able to get to this point or not



main()