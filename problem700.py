# Unsolved

# Works, but has way to slow of a runtime. Not sure what a faster algorithm would be of this
def main():
    i = 0
    sumOfEulerCoins = 1504170715041707
    currentEulerCoin = 1504170715041707
    previousEulerCoin = 0
    lowestEulerCoin = 1504170715041707
    while(True):
        previousEulerCoin = currentEulerCoin
        currentEulerCoin = (previousEulerCoin + 1504170715041707) % 4503599627370517
        if (currentEulerCoin < lowestEulerCoin):
            lowestEulerCoin = currentEulerCoin
            sumOfEulerCoins += currentEulerCoin
            print(str(sumOfEulerCoins) + " | " + str(currentEulerCoin))



main()