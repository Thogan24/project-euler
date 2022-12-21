# Solved

def main():
    i = 1
    nthPowerCount = 0
    while(True):
        for j in range(1, 10):
            if (len(str(j**i)) == i):
                nthPowerCount += 1
        i += 1
        print(nthPowerCount)


main()