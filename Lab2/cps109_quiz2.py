#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 2: Write a python program that reads an inputted integer and outputs its factors

print("Input your integer:")
inputtedInt = int(input())
factors = []

for x in range(2, 11):
    if inputtedInt % x == 0: #determine if the inputtedInt divided by x is an int
        factors.append(x) #adds the number to the list if it is an int
        
if len(factors) == 0: #to determine if the list is empty
    print("This number has no factors between 2 and 10.")
else: print("the factors of " + str(inputtedInt) + " between 2 and 10 are " + str(factors) + ".")

    
