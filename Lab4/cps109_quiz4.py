#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 4: FizzBuzz

def fizzBuzz(n):
    for x in range(1, n+1):
        if x < 1:
            print('N must be greater than 1.')
        elif x > 100:
            print('Too much work, no thanks.')
        elif x%3==0 and x%5==0:
            print('FizzBuzz')
        elif x%3==0 and x%5!=0:
            print('Fizz')
        elif x%3!=0 and x%5==0:
            print('Buzz')
        elif x%3!=0 and x%5!=0:
            print(x)

Num = int(input("Enter a number: "))
#Num = int(input())

fizzBuzz(Num)