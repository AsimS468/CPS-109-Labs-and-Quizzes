#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 6: Prime Number Checker

def primeNumChecker(n):
    if n < 1:
        return "Invalid number!"
    
    x = 0
    y = 1
    for i in range(n):
        if n % y == 0:
            x = x + 1
        y = y+1
    if x == 2:
        return str(n) + " is a prime number!"
    else:
        return str(n) + " is not a prime number!"
    

num = int(input("Input a positive number: "))

print(primeNumChecker(num))