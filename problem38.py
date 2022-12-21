# Unsolved

#
def main():
    stringCurrentDigits = ""
    n = 1
    largestConcatenatedPandigital = 0
    for i in range(1000000000):
        stringCurrentDigits = ""
        while(len(stringCurrentDigits) < 9):
            stringCurrentDigits += str(i * n)
            n += 1
        if (len(stringCurrentDigits) == 9 and isPandigital(int(stringCurrentDigits)) and int(stringCurrentDigits) > largestConcatenatedPandigital):
            largestConcatenatedPandigital = int(stringCurrentDigits)
        print(str(i) + " | " + str(largestConcatenatedPandigital))
        
        #print(i)

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