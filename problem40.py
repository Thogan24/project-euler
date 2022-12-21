# Solved

# Create the number
# Get digits in the number

def main():
    # Creating the number
    digitNumber = 1
    answer = 1
    stringNum = "0123456789"
    concatenationNumber = 1
    currentCycles = 0
    numberOfCycles = 100000
    while(currentCycles < numberOfCycles):
        for i in range(10):
            stringNum += (str(concatenationNumber) + str(i))
        currentCycles += 1
        concatenationNumber += 1

    print(stringNum[1])
    
    # Get digits in the number
    while(digitNumber <= 1000000):
        print(digitNumber)
        answer *= float(stringNum[digitNumber])
        digitNumber *= 10
    print(answer)

main()