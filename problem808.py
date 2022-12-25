import math

def main():
    count = 0
    sumOfReversiblePrimeSquares = 0
    i = 1
    while(count <= 50):
        primeSquare = i**2
        if(isPrime(i) and isPrime(math.sqrt(reverse(primeSquare))) and (not isPalindromic(primeSquare))):
            count += 1
            sumOfReversiblePrimeSquares += i
        i += 1
    print(sumOfReversiblePrimeSquares)



def reverse(num):
    
    reverseNum = ""
    while(num > 0):
        reverseNum += str(num % 10)
        num = num // 10
    return int(reverseNum)

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

def isPalindromic(num):
    # Finish isPalindromic function
    # Must change to for loop instead
    reverseNum = str(reverse(num))
    numString = str(num)
    numLength = len(numString)
    answer = ""
    answerSecondHalf = ""
    if (numLength % 2 == 0):
        for i in range(int(numLength / 2)):
            answer += numString[i]
            answerSecondHalf += reverseNum[i]
    else:
        for k in range(int(numLength // 2)):
            answer += numString[k]
            answerSecondHalf += reverseNum[k]
    return answer == answerSecondHalf

#print(isPalindromic(12321))
main()




# Accidentally made function that makes palindromes out of numbers, not checks if they're palindromic

# if (numLength % 2 == 0):
#         for i in range(numLength / 2):
#             answer += numString[i]
#         for j in range(numLength / 2, numLength):
#             answer += numString[j]
#         #return int(numString[0, numLength / 2]) + int(reverseNum[numLength / 2, numLength])
#     else:
#         for k in range(numLength // 2 + 1):
#             answer += numString[k]
#         for l in range(numLength // 2 + 1, numLength):
#             answer += numString[j]
#         #return int(numString[0, int((numLength // 2) + 1)]) + int(reverseNum[numLength / 2, numLength])
#     return answer


144454441