#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 1: Calculate the area of an n-sided regular polygon

import math #Import math library to do more complex mathematical calculations

print("Input the number of sides in the polygon:")
sideNum = int(input()) #number of sides in the polygon

print("Input the length of the sides in the polygon:")
sideLength = float(input()) #length of each side of the polygon

perimeter = sideNum * sideLength #Calculate the perimeter of the polygon

#calculate the apothem. Uses the tan() function from the math library
#the radians() function converts the numerical value from degrees to radians
apothem = (sideLength)/(2*(math.tan(math.radians(180/sideNum))))
area = (perimeter * apothem)/2 #Calculate the area of the polygon
roundedArea = round(area, 2) #round function used to round the final answer to the first two decimal points

print("The area of your polygon is " + str(roundedArea) + ".") #print the area





