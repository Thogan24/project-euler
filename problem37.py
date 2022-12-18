def main():
    num = 10
    sumOfTruncatablePrimes = 0
    while(True):
        if(isPrime(num) and isTruncatable(num)):
            sumOfTruncatablePrimes += num
        num += 1
        print(str(num) + " | " + str(sumOfTruncatablePrimes))
        #print(str(num) + " | " + str(sumOfTruncatablePrimes))
    
        
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True   


def isTruncatable(num):
    digitList = [int(x) for x in str(num)]
    currentNumber = ""
    # Right Truncatable Checker
    for i in range(len(digitList)):
        currentNumber = ""
        for j in range (i, len(digitList)):
            currentNumber += str(digitList[j])
        if(isPrime(int(currentNumber)) == False):
            return False
    
    #Left Truncatable Checker
    while(num > 0):
        if(isPrime(num) == False):
            return False
        num = num // 10
    return True


main()