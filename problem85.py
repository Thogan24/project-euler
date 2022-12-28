# Solved

# Loop through all digits going up till first x axis
# Loop through all digits going up till y axis that fills every combination
def main():

    closestsToTwoMillion = 0
    lengthFromTwoMillion = 10000000000
    for yAxisLength in range(1000):
        for xAxisLength in range (1000):
            area = 0
            for y in range(yAxisLength + 1):
                for x in range(xAxisLength + 1):
                    area += (y * x)
            if(abs(2000000 - area) < lengthFromTwoMillion):
                lengthFromTwoMillion = abs(2000000 - area)
                closestsToTwoMillion = area
                print(str(closestsToTwoMillion) + " | " + str(xAxisLength) + ", " + str(yAxisLength) + ", Area: " + str(yAxisLength * xAxisLength))





main()