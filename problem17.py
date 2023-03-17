# Unsolved

# Psuedo Code:
# Create an array with all numbers 1-9, 10-90 (tens place), 100-900 (hundreds place) in words
# Loop through all nums, add appropriate ands, tally, print

num = 0

while(num <= 1000):
    letters = 0
    numberSingleDigit = num % 10
    numberDoubleDigit = (num % 100) / 10 
    numberTripleDigit = num / 100
    

    match numberSingleDigit:
        case 1:
            letters += 3
        case 2:
            letters += 3
        case 3:
            letters += 5
        case 4:
            letters += 4
        case 5:
            letters += 4
        case 6:
            letters += 3
        case 7:
            letters += 5
        case 8:
            letters += 5
        case 9:
            letters += 4
    
    match numberDoubleDigit:
        case 1:
            letters += 
        case 2:
            letters += 6
        case 3:
            letters += 6
        case 4:
            letters += 6
        case 5:
            letters += 5
        case 6:
            letters += 5
        case 7:
            letters += 7
        case 8:
            letters += 6
        case 9:
            letters += 6
        
        
        
