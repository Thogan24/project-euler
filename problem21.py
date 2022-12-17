# Unsolved

def main():
    #Loop through all numbers till 10000
    #Check if amicable
    #Add all amicable numbers up till 10000
    sum = 0
    for i in range(9998):
        if (isAmicable(i+2)):
            sum += i
        #print(sum)
        

def isAmicable(i):
    sumi = sumOfDivisors(i)
    for k in range (i):
        if (sumi == sumOfDivisors(k)):
            return True
    for j in range (10000 - i):
        if(sumi == sumOfDivisors(j+i)):
            return True
        
    return False

def sumOfDivisors(num):
    sum = 0
    for l in range(num-2):
        print(l+1)
        print(num-2)
        if (num-2 % l+1 == 0):
            sum += l+1

    return sum


main()