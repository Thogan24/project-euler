# Solved

def main():
    sumOfNumbers = 0
    num = 3
    while(True):
        sum = 0
        b = [int(x) for x in str(num)]
        for i in range(len(b)):
            sum += factorial(int(b[i]))
            #print(factorial(int(b[i])))
        if(sum == num):
            sumOfNumbers += sum
        num += 1
        print(str(num) + " | " + str(sumOfNumbers))

def factorial(num):
    fact = 1
 
    for i in range(1, num+1):
        fact = fact * i
    return fact

main()