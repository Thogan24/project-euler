# Solved

import math

def main():
    solved = False
    count = 5555
    shouldBreak = False
    while(solved == False):
        if(isComposite(count)):
            for i in range(1, count, 2):
                for j in range (count):      #int(math.sqrt(count + 1))
                    if (isPrime(i)):
                        ##print(str(count) + " | " + str(i) + " | " +  str(j))     
                        if (count == (i + 2 * (j ** 2))):
                            shouldBreak = True
                            break
                if (shouldBreak):
                    break
            if(shouldBreak == False):
                print(str(count) + " ANSWER!!!!!!!!")
                solved = True
            shouldBreak = False
        print(count)
        count += 2

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

def isComposite(n):
 
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return False
 
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return True
    i = 5
    while(i * i <= n):
         
        if (n % i == 0 or n % (i + 2) == 0):
            return True
        i = i + 6
         
    return False

main()