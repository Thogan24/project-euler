def main():
    pentagonalList = []
    for k in range(100000):
        pentagonalList.append(pentagonal(k))

    for i in range(100000):
        for k in range (100000):
            pentagonali = pentagonalList[i]
            pentagonalj = pentagonalList[j]
            if(pentagonalList.count(pentagonali + pentagonalj) >= 1 and pentagonalList.count(pentagonali - pentagonalj) >= 1):
                print(str(pentagonali) + " | " + str(pentagonalj) + " | " + str(minimise()))

def pentagonal(num):
    return num * (3 * num - 1)/2

def minimise(num1, num2):
    # Finish minimise code

main()