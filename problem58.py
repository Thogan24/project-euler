# Solved

def main():
    primeCount = 0
    count = 0
    ratio = 0
    sidelength = 3
    i = 1
    spiralOutwardsCounter = 2
    spiralOutwardsCounterAdd = 1
    solved = False
    while (solved == False):
        print(i)
        if(isPrime(i)):
            primeCount += 1
        count += 1
        i += spiralOutwardsCounter
        spiralOutwardsCounterAdd += 1    
        if (spiralOutwardsCounterAdd > 4):
            spiralOutwardsCounter += 2
            spiralOutwardsCounterAdd = 1
            ratio = primeCount / count
            print("ratio: " + str(primeCount) + " / " + str(count) + " | " + str(ratio))
            if(ratio <= 0.10):
                print(sidelength)
                solved = True
                break
                
            sidelength += 2

            
            
        
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

main()