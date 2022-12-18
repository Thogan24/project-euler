# Solved

def main():
    maxNumOfPrimes = 0
    prodOfCoef = 0
    for a in range(-999, 1000):
        for b in range (-999, 1000):
            num = consecutivePrimes(a, b)
            if(maxNumOfPrimes < num):
                maxNumOfPrimes = num
                prodOfCoef = a * b
    print(prodOfCoef)
            



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
        #print('\t',f)
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True 

def consecutivePrimes(a, b):
    i = 0
    while(True):
        if(not isPrime(i**2 + a * i + b)):
            break
        i += 1
    return i


main()