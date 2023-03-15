def main():
    pentagonalList = []
    length = 10000
    for k in range(1, length+2):
        pentagonalList.append(pentagonal(k))

    for i in range(length):
        for j in range (length):
            pentagonali = pentagonalList[i]
            pentagonalj = pentagonalList[j]
            print(str(pentagonali) + " | " + str(pentagonalj) + " | ")

            # This if statement doesn't work
            if(pentagonalList.count(pentagonali + pentagonalj) >= 1 and pentagonalList.count(abs(pentagonali - pentagonalj)) >= 1):
                print(str(pentagonali) + " | " + str(pentagonalj) + " | " + str(pentagonali - pentagonalj)) # Find smallest one of these
                break
            


def pentagonal(num):
    return num * (3 * num - 1)/2


main()