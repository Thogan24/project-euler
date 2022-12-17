# Solved

def main():
    sum = 0
    mod = 10000000000

    for i in range (1, 1000):
        temp = i
        for j in range (1, i):
            temp *= i
            temp %= mod
        sum += temp
        sum %= mod
    print(sum)


main()