# Solved

def main():
    sumOfProducts = 0
    stringAllNumbers = ""
    noRepeatList = []
    for multiplicand in range(1000):
        for multiplier in range(10000):
            product = multiplicand*multiplier
            stringAllNumbers = str(multiplicand) + str(multiplier) + str(product)
            if((len(stringAllNumbers) == 9) and isPandigital(stringAllNumbers) and noRepeatList.count(product) < 1):
                print(str(multiplicand) + " | " + str(multiplier) + " | " + str(product) + " | " + stringAllNumbers)
                sumOfProducts += product
                noRepeatList.append(product)
    print(sumOfProducts)



def isPandigital(num):
    listWithAllDigits = []
    for i in range(1, len(str(num)) + 1):
        listWithAllDigits += str(i)
    
    for j in range(len(str(num))):
        if(listWithAllDigits.count(str(num[j]))):
            listWithAllDigits.remove(num[j])
        else:
            return False
    if(len(listWithAllDigits) == 0):
        return True

    return False # Not sure if it should be able to get to this point or not

main()
