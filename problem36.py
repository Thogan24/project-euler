def main():
    d = 0
    sum = 0
    
    while (d < 1000000):
        if (isPalindromic(int(bin(d) [2: ])) and isPalindromic(d)):
            sum += d
        
        print(str(d) + " | " + str(sum))
        d += 1
    print(sum)

def isPalindromic(num):
    originalNum = num
    reverseNumber = 0
    while (num > 0):
        remainder = num % 10  
        reverseNumber = (reverseNumber * 10) + remainder  
        num /= 10
    if (originalNum == reverseNumber):
        return True
    return False
main()