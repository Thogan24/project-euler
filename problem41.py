# Solved

def main():
    i = 0
    largestPandigitalPrime = 0
    while(i < 987654321):
        if(isPandigital(i) and isPrime(i) and i > largestPandigitalPrime):
            largestPandigitalPrime = i
            print(largestPandigitalPrime)
        i += 1



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


main()
