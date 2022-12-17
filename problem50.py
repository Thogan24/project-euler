# Unsolved

# Runtime too slow and the answer might not come out as correct 
# Algorithm only checks for the list + another random prime number from that list till the end 

def main():
    i = 9743 
    listOfPrimes = [0]
    currentListOfPrimes = [0]
    largestPrimeSum = 0
    # Setting up list of primes
    for k in range(1000000):
        if (isPrime(k)):
            listOfPrimes.append(k)

    while (i > 0):
        if (isPrime(i)):
            currentListOfPrimes.append(i)
            for j in range(len(currentListOfPrimes), len(listOfPrimes)-1):
                if(largestPrimeSum < 1000000 and isPrime(sum(currentListOfPrimes) + listOfPrimes[j]) and largestPrimeSum < sum(listOfPrimes)):
                  largestPrimeSum = sum(currentListOfPrimes)  

        #print(sum(listOfPrimes))
        #if (isPrime(sum(currentListOfPrimes)) and largestPrimeSum < sum(listOfPrimes) and largestPrimeSum < 1000000):
        #    largestPrimeSum = sum(currentListOfPrimes)
        i -= 1
        print(str(isPrime(sum(currentListOfPrimes))) + " | " + str(i) + " | " + str(largestPrimeSum))

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

main()