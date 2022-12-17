# Unsolved

def main():
    i = 1
    count = 0
    while (i < 1000000):
        if(isCircularPrime(i)):
            count += 1
        i += 1
    #print(count)


def isCircularPrime(num):
    
    for i in range(len(str(num))):
        if (isPrime(i) == False):
            return False
        lastDigit = num % 10
        num = num // 10
        stringNum = str(lastDigit) + str(num)
        num = int(stringNum)
        print(num)
    return True




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
        print('\t',f)
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True    


main()