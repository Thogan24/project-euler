# Solved

def main():
    mersenne = 2
    for i in range(7830456):
        mersenne *= 2
        mersenne %= 10000000000
        #print(mersenne)

    mersenne *= 28433
    mersenne += 1
    mersenne %= 10000000000
    print(mersenne)
main()