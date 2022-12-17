# Solved

def main():
    listOfNumbers = []
    

    for a in range(2, 101):
        for b in range (2, 101):
            if (listOfNumbers.count(a**b) == 0):
                listOfNumbers.append(a**b)
    
    print(len(listOfNumbers))

main()