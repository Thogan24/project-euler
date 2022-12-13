def main():
    i = 1
    while(i < 10000000):
        print(str(i) + " | " + str(fibonacci(i)))
        if (len(str(fibonacci(i))) >= 1000):
            print (len(str(fibonacci(i))))
            print(str(i-1) + " | " + str(fibonacci(i)))
            break
        i += 1

def fibonacci(num):
    first = 0
    second = 1
    sum = 0
    if (num == 0):
        return first
    elif (num == 1):
        return second
    else:
        for i in range(2, num):
            sum = first + second
            first = second
            second = sum
        return sum


main()