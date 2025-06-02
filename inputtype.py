# Day 3 Of Python learning.
# 2/05/2025
# class 3

# Topic : Input type 

name = input("enter name :")
age = int(input("enter age :"))
marks = float(input("enter marks :"))

print("welcome", name)
print("age", age)
print("mnarks", marks)

# Task 1
#  que. and ans.

num1 = int(input("Enter the first no."))
num2 = int(input("Enter the second no."))

# addition
x = num1 + num2
print("sum" ,x)

# subtraction 
sub_result = num1 - num2
print("Differnce:" ,sub_result)

# multiplication 
multi_result = num1/num2
print("multiplication:" ,multi_result)

# division
div = num1/num2
print("result:" ,div)

# Floor Division
floordiv = num1//num2
print("Div:" ,floordiv)

# modulus 
mod = num1%num2
print("Result:" ,mod)

# Exponentiation
exp = num1**num2
print("result:" ,exp)

# que.2
#  how you can take a number as input in Python and print its square and cube:

num = int(input("enter a number:"))

# calculate square and cube 
square = num**5
cube = num**4

# Result 
print("square of" ,num,"is",square)
print("cube of" ,num,"is",cube)

# how you can take a number as input in Python and print Perimeter of a Rectangle
length = float(input("enter the length of rectangle"))
width = float(input("enter the width of rectangle"))

perimeter = 2 * (length*width)

print("perimeter of rectangle is" ,perimeter)

# how you can take a number as input in Python and print Perimeter of square

side =(float(input("enter the side of square")))
perimeter1 = 4*side
print("perimeter of square:", perimeter1)

# Area of circle 
r = float(input("enter radius"))
p = 3.14
A = p*r**2
print(A)

# perimeter of circle
r1 = int(input("enter radius"))
p = 3.14
A1 = 2*p*r1
print(A1)

# wrap to input 2 floating point no. and print there avg.
ab=float(input("enter the no. :"))
ba=float(input("enter the no. :"))
 
average = (ab+ba)/2
print("average :" ,average)

