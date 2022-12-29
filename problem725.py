# Unsolved

# Don't create something that checks if a number is equal to it, but rather one that creates these numbers. Any number past 9 digits is just combinatorics with 0s added on
def main():
    sumOfDigitNums = 0
    currentN = 0
    while(currentN <= 2020):
        # Not going to work with two for loops, going to need one for every N so doesn't work
        for i in range(10):
            for j in range(10):
                sumOfDigitNums += int(str(i) + str(j) + str(i + j)) #Add all possible combinations of nums
        currentN += 1
        





main()