# Unsolved

def main():
    i = 0
    while(True):
        if(properForm(i**2)):
            print(i)
            break
        print(i)
        i += 1
        



def properForm(num):
    b = [int(x) for x in str(num)] #len = 19
    if (len(b) != 19):
        return False
    j = 1
    for i in range(0, len(b)-2, 2):
        if(b[i] != j):
            return False
        j += 1
    if (b[18] == 0):
        return True
    return False
#main()
print(1389026630**2)