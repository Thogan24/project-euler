# Unsolved

# Every possible combination must be tried, not just sum of digits.
def main():
    answer = 0
    for i in range(100):
        stringSquaredNum = str(i ** 2)
        sumOfDigits = 0
        for j in range(len(stringSquaredNum)):
            sumOfDigits += int(stringSquaredNum[j])
        print(sumOfDigits)
        
        if (sumOfDigits == i):
            answer += int(stringSquaredNum)
        print("int: " + str(i) + " answer: " + str(answer))
        #print(answer)
    print(answer)




main()