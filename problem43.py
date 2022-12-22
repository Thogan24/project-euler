# Unsolved

def main():
    firstPrimeList = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1000000000, 9999999999):
        if(isPandigital(i)):
            for i in range()

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