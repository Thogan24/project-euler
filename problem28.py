# Solved

def main():
    sum = 0
    i = 1
    spiralOutwardsCounter = 2
    spiralOutwardsCounterAdd = 1

    while (i <= 1002001):
        sum += i
        print(i)
        i += spiralOutwardsCounter
        spiralOutwardsCounterAdd += 1    
        if (spiralOutwardsCounterAdd > 4):
            spiralOutwardsCounter += 2
            spiralOutwardsCounterAdd = 1
        
    
    print(sum)



main()