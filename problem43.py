# Unsolved

# find a way for 000000000 to not go to 0
def main():
    firstPrimeList = [2, 3, 5, 7, 11, 13, 17]
    sumOfPandigitalProperties = 0
    for i in range(000000000, 9999999999): #406357289 000000000 9999999999
        broke = False
        if(isPandigital(i)):
            for j in range(7):
                #print(float((str(i[1+j]) + str(i[2+j]) + str(i[3+j]))))
                numString = str(i)
                if(not (int((str(numString[1+j]) + str(numString[2+j]) + str(numString[3+j]))) % int(firstPrimeList[j]) == 0)):
                    broke = True
                    break
            if(not broke):
                sumOfPandigitalProperties += i
                print(sumOfPandigitalProperties)
        #print(i)
        
    #print(sumOfPandigitalProperties)
    #print(isPandigital(1406357289))
                    

# isPandigital working properly now
def isPandigital(num):
    listWithAllDigits = []
    for i in range(len(str(num))):
        listWithAllDigits += str(i)
    
    for j in range(len(str(num))):
        #print(listWithAllDigits)
        #print(listWithAllDigits.count(str(num)[j]))
        if(listWithAllDigits.count(str(num)[j]) == 1):
            listWithAllDigits.remove(str(num)[j])
        else:
            
            return False
    if(len(listWithAllDigits) == 0):
        
        return True
    print(listWithAllDigits)
    return False # Not sure if it should be able to get to this point or not



main()