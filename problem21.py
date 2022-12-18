# Unsolved

def main():
    #Loop through all numbers till 10000
    #Check if amicable
    #Add all amicable numbers up till 10000
    sumOfAmicables = 0
    for i in range(1, 10000):
        if (isAmicable(i)):
            sumOfAmicables += i
        print(sumOfAmicables)
        

def isAmicable(i):
    sumi = sumOfDivisors(i)
    #print(sumOfDivisors(sumOfDivisors(sumi)))
    if(sumOfDivisors(sumi) == sumi):
        return False
    elif(sumOfDivisors(sumOfDivisors(sumi)) == sumi):
        return True
    return False


    # for k in range (i):
    #     if (sumi == sumOfDivisors(k)):
    #         return True
    # for j in range (10000 - i):
    #     if(sumi == sumOfDivisors(j+i)):
    #         return True


def sumOfDivisors(num):
    sumDivisors = 0
    for i in range(1, num):
        if (num % i == 0):
            sumDivisors += i
    return sumDivisors

#print(isAmicable(1))
main()