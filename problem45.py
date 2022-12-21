def main():
    triangularList = []
    pentagonalList = []
    hexagonalList = []
    triangularNum = 0
    for i in range (1000000):
        triangularList.append(triangular(i))
        #pentagonalList.append(pentagonal(i))
    for k in range(500000):
        pentagonalList.append(pentagonal(k))
        hexagonalList.append(hexagonal(k))
    print(triangularList.count(40755))
    print(pentagonalList.count(40755))
    #print(hexagonalList.count(40755))
    for j in range (10000000):
        triangularNum = triangularList[j]
        if(pentagonalList.count(triangularNum) >= 1 and hexagonalList.count(triangularNum) >= 1):
            print(triangularNum)


def triangular(num):
    return num*(num+1)/2

def pentagonal(num):
    return num*(3 * num - 1)/2

def hexagonal(num):
    return num * (2 * num - 1)





main()