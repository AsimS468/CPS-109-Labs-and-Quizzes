#Name: Muhammad Asim Salman
# #SID: 501177482
# #Lab 1

# import math

# #----------------Question 1----------------#
# print("----------------Question 1----------------")

# print("Input temperature in celsius: ")
# C = float(input()) #use the input() function in float so the value inputted is a floating value
# F = (C*(9/5)) + 32
# K = C + 273.15

# print("Fahrenheit: " + str(F)) #To print a non-string variable, put the variable in the str() function
# print("Kelvin: " + str(K))
# print("------------------------------------------\n\n")
# #------------------------------------------#


# #----------------Question 2----------------#
# print("----------------Question 2----------------")

# print("Input a:")
# a = float(input())
# print("Input b:")
# b = float(input())
# print("Input c:")
# c = float(input())

# x1 = ((-b) + math.sqrt((b*b)-(4*a*c)))/(2*a) 
# x2 = ((-b) - math.sqrt((b*b)-(4*a*c)))/(2*a)

# print("x1 = " + str(x1) + "\nx2 = " + str(x2))
# print("------------------------------------------\n\n")
# #------------------------------------------#


# #----------------Question 3----------------#
# print("----------------Question 3----------------")
# print("Input first side length:")
# sl1 = float(input())
# print("Input second side length:")
# sl2 = float(input())
# print("Input third side length:")
# sl3 = float(input())

# maxVal = max(sl1, sl2, sl3) #max() function finds the maximum value in its arguments

# #boolean to determine if half the sum of the side lengths are greater than the greatest side length
# validate = bool(((sl1 + sl2 + sl3)/2) > maxVal)

# print(validate) #booleans return the string "True" or "False"
# print("------------------------------------------\n\n")
# #------------------------------------------#


# #----------------Question 4----------------#
# print("----------------Question 4----------------")
# print("Input the side length of a regular pentagon:")
# a = float(input())

# A = (1/4)*math.sqrt(5*(5+(2*math.sqrt(5))))*(a*a)

# print("The area of the regular pentagon is " + str(A) + ".")
# print("------------------------------------------\n\n")
# #------------------------------------------#
