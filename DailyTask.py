# Day 1 Of Python learning.
# 28/04/2025
# class 1

# 1. print function
print("hello")
print("hello","friend")
print("hello"+"friend")
print("hello","friend",sep="$")       # sep mean seprator 
print("hello","friend",sep="$",end="%" "\n")   # sep mean seprator \n for break 
print("sdk","friends",end="!")
print()
print(1234)
print("friend")
print("hello",end="!")
print("friend")
print("hello","friend","welcome",sep="%",end="@")
print()
print("I am in class", 12)
a=5
b=25
print("sum of two numbers is" + str(a+b))  # str mean string

# 2. OPERATORS
a=26
b=14
c=(a+b)
print(c)

a1=126
b1=26
c1=(a1-b1)
print(c1)

a2=260
b2=26
c2=(a2/b2)
print(c2)

a3=126
b3=2
c3=(a3*b3)
print(c3)

a4=126
b4=6
c4=(a4//b4)
print(c4)

a5=6
b5=2
c5=(a5**b5)
print(c5)

a6=665
b6=2
c6=(a6%b6)
print(c6)

# casting 
a7=int(3.5)
print(a7)
a8=float(4)
print(a8)

# Day 2 Of Python learning.
# 29/04/2025
# class 2
# Nothing

# Day 5 Of Python learning.
# 6/05/2025
# class 5
# Que answer

# 1) print 2nd character from the string Itech system

a="Itech system"
print(a[1:2])

# 2) print yste from Itech system 
a="Itech system"
print(a[7:11])

# 3) print length of the string Learn python 
a="Learn python"
print(len(a))

# 4)remove spaces from the string "  i like to learn python  "
a="  i like to learn python  "
print(a.strip())

# 5) print string in lower and upper case "python is fun"
a="Python is fun"
print(a.lower())
print(a.upper())

# 6) replace the string java is a programming language with kava is a programming language
a="java is a programming language"
print(a.replace("java","kava"))

# Strings method question and anser 
string1 = "Hello"
string2 = 'World'
string3 = """ This is a multi-line string """

# 1
string1 = "Hello this is a python"
string2 = 'language'

concatenated = string1 + " " + string2 
print(concatenated)

split_string = concatenated.split(" ")  
print(split_string )

# 2
string1 = "we are learning python"
string2 = 'language'

first_char = string1[0]  
print(first_char)

substring = string2[1:4] 
print(substring)

length = len(string1) 
print(length)

# 3
string1 = "we are learning python"
string2 = 'language'
uppercase = string1.upper() 
print(uppercase)

index = string1.find("l") 
print(index)

replaced = string1.replace("we", "v")  
print(replaced)

# 4
name = "Any name "
age = 22
concatenated_string = "Name: " + name + ", Age: " + str(age)
print(concatenated_string)  

age = 36
txt = f"My name is John, I am {age}"
print(txt)

age = 10
txt = "My name is abc, I am " + str(age)
print(txt)

# Day 7 of lerning python
# 8/05/2025
# class 7

# easy question on ifelse loop

# write a program to check whether a person is eligible for voting or not(accept age from user)
age=int(input("enter your age"))
if age>18:
    print("eligible for voting")
else:
    ("not eligible for voting")


# check whether a number entered by user is even or odd.
num=int(input("enter your number"))
if num%2==0:
    print("the numbe is even")
else:
    print("the number is odd")

# write a program to check whether the number is divisible by 7 or not
num=int(input("enter your number"))
if num%7==0:
    print("the number is divisible by 7")
else:
    print("the number is not divisible by 7")

# write a program to display "hello" if entered value is divisible by 5 otherwise enter "bye"
num=int(input("enter your number"))
if num%5==0:
    print("hello")
else:
    print("bye")


# write a program to calculate the electricity bill from following criteria
# Unit                               price
# first 100 Unit                   no charge
# next 100 unit                    rs 5 per unit
# after 200 units                  rs 10 per unit

amt=0
nu=int(input("enter number of electric unit"))
if nu<=100:
    amt=0
    if nu>100 and nu<=200:
        amt(nu-100)*5
    print("amount to pay:,amt")

# write a program to display the last digit of a number is divisible by 3 or not
num=int(input("enter your number"))
if num%3==0:
    print("last digit is divisible by 3")
else:
    print("the number is not divisible by 3")

# write a program to find largest number out of two numbers except from user
num1=int(input("enter first number"))
num2=int(input("eneter second number"))
if num1>num2:
    print("greatest no. is, num1")
else:
    print("greatest no is ,num2")

# write a program to check no. is even or odd
num1=int(input("enter your first value"))
if num1%2==0:
    print("the no. is even")
else:
    print("the no, is odd")

# write a program to check whether a person is senior citizen or not
age=int(input("enter age"))
if age>=60:
    print("senior citizen")
else:
    print("not a senior citizen")

# write a program to check the number is positive or negative
num=int(input("enter your value"))
if num>=0:
    print("number is positive")
else:
    print("number is negative")

# Day 8 of lerning python
# 09/05/2025
# class 8
# if els question answer 

# 01) pass or fail  
a=float(input("Enter the percentage marks of the student"))
if(a>=35):
    print("The student has passed the exam")
else:
    print("The student has failed the exam")

# 02) WAP to input a number and print whether it is odd or even
a=int(input("Enter a number"))
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")

# 03) WAP to find whether the given number is positive or negative
a=float(input("enter a number"))
if(a>0):
    print("This is a positive number")
elif(a<0):
    print("This is a negative number")
else:
    print("this number is zero")

# 04) WAP to input two nos and if they are divisible by each other print their product and if not then print their remainder
a=float(input("enter first no"))
b=float(input("enter the second no"))
if(a%b==0):           
    prod=a*b
    print("they are divisible so their product is",prod)
elif(a%b!=0):                              # != the sign indicates (not equal to)
    rem=a%b
    print("they are not divisible so their remainder is",rem)
else:
    print("invalid")

# 05) WAP to input three numbers and print the product of the two larger numbers
a=float(input("enter the 1st no"))
b=float(input("enter the second no"))
c=float(input("enter the third no"))
if(a>c and b>c):
    prod=a*b
    print("the product of the larger numbers is",prod)
elif(b>a and c>a):
    prod=b*c
    print("the product of the two larger numbers is",prod)
elif(c>b and a>b):
    prod=c*a
    print("the product of the two larger numbers is",prod)
else:
    print("any of the two nos are equal")

# 06) write a code to find the greatest number among the 3 entered 
a=float(input("enter the first number"))
b=float(input("enter the second number"))
c=float(input("enter the third number"))
if(a>b and a>c):
    print(a,"is the largest number")
elif(b>a and b>c):
    print(b,"is the largest number")
elif(c>a and c>b):
    print(c,"is the largest number")
else:
    print("any of the two numbers are equal")

# 07) write a program to find the volume of a sphere and a cylinder(1 is sphere,2 is cylinder)
a=int(input("Select the vessel whose volume you want to find \n 1 is sphere \n 2 is cylinder"))
pi = 3.14
a = int(input("Enter 1 for sphere or 2 for cylinder: "))
if a == 1:
    b = float(input("Enter the radius of the sphere: "))
    vol = (4/3) * pi * b**3
    print("The volume of the sphere is", vol)
elif a == 2:
    b = float(input("Enter the radius of the cylinder: "))   
    c = float(input("Enter the height of the cylinder: "))
    vol = pi * b**2 * c
    print("The volume of the cylinder is", vol)
else:
    print("Invalid input") 

# Day 8 of lerning python
# 12/05/2025
# class 9

# WHILE LOOp

#  1)Write A program to print the multiplication table of any number by using while loop in python 

num = int(input("Enter a number to print its multiplication table: "))
i = 1
print("\nMultiplication Table of", num, ":")
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# 2)Write A Program To Find The Average of any 10 No.s
# Program to find the average of 10 numbers using a while loop

count = 0
total = 0
while count < 10:
    # Concatenate "Enter number " with the count number
    num = float(input("Enter number " + str(count + 1) + ": "))
    total += num
    count += 1
average = total / 10
print("The average of the 10 numbers is:", average)

# 3)Write a program to find wheather the number is pallindrome or not(the revers of 111 is 111 i.e. the number 111 is pallindrome)

number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if original_number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# 4) Write a program to find whether the given number is armstrong or not .
# (if sum of cubes of each digit of the number is equal to the number itself
#   then the number is called an armstrong number.
# (153=(1*1*1)+(5*5*5)+(3*3*3)

number = int(input("Enter a number: "))
original_number = number
sum_of_cubes = 0

while number > 0:
    digit = number % 10
    sum_of_cubes = sum_of_cubes + (digit * digit * digit)
    number = number // 10

if original_number == sum_of_cubes:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")

# Example: 153 is an Armstrong number because:
# Original number = 153
# Step 1: 3³ = 27
# Step 2: 5³ = 125
# Step 3: 1³ = 1
# Total: 27 + 125 + 1 = 153 ✅ Same as original

# 5) Write a program to calculate p,n,r for 3 sets of values or for 3 persons

person = 1
while person <= 3:
    print("Enter details for person " + str(person) + ":")
    P = float(input("Enter Principal (P): "))
    N = float(input("Enter Number of years (N): "))
    R = float(input("Enter Rate of Interest (R): "))  
    # Formula for simple interest: SI = (P * N * R) / 100
    SI = (P * N * R) / 100
    print("The Simple Interest for person " + str(person) + " is: " + str(SI) + "\n")
    person += 1

# 5  Write A program to print all the ascii values and their equivalent characters using a while loop. 
# the ASCII values vary from 0-255

ascii_value = 0
while ascii_value <= 255:
    print("ASCII value " + str(ascii_value) + " is: " + chr(ascii_value))
    ascii_value += 1

# 6 Write A program to reverse the number i.e. if the number
#  entered by the user is 129 then it will display 921

number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    digit = number % 10  # Get the last digit of the number
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the number

print("Reversed number is: " + str(reversed_number))

# Day 12 of lerning python
# 16/05/2025
# class 12

# LIST QUESTION ANSWER
#1 sum items in list

my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print("Sum:", total)

my_list = [1, 2, 3, 4, 5]
total = (1+2+3+4+5)
print("Sum:", total)

# 2 multply items in list

my_list = [1, 2, 3, 4, 5]
result = 1      
for num in my_list:
    result *= num
print("Product:", result)


#if we put 0 then anything multiply by 0 is 0
result = 1
result *= 1  # result = 1
result *= 2  # result = 2
result *= 3  # result = 6
result *= 4  # result = 24
result *= 5  # result = 120
print("Product:", result)  # Output: Product: 120

# 3 get largest number in list
numbers = [10, 45, 23, 89, 2, 77]
largest = numbers[0]  # Assume the first number is the largest
for num in numbers:
    if num > largest:
        largest = num  # Update if a bigger number is found

print("The largest number is:", largest)

# 4 get smaller number in  list
numbers = [10, 45, 23, 89, 2, 77]
smallest = numbers[0]  # Assume the first number is the smallest
for num in numbers:
    if num < smallest:
        smallest = num  # Update if a smaller number is found

print("The smallest number is:", smallest)

# Start with smallest = 10
# Compare 45 → not smaller
# Compare 23 → not smaller
# Compare 89 → not smaller
# Compare 2 → ✅ YES! 2 is smaller → smallest = 2
# Compare 77 → not smaller
# Result: ✅ 2 is the smallest.

# 5 count string with same start and end
my_list = ["apple", "banana", "cherry", "radar", "level", "orange"]
count = 0
for word in my_list:
    if word[0] == word[-1]:
        count += 1
print("Count of words with same start and end:", count)

my_list = ["apple", "banana", "cherry", "radar", "level", "orange"]
a = []
for word in my_list:
    if word[0] == word[-1]:
        a.append(word)
print("Words with same start and end:", a)

# 6 remove duplicates from list 
# set(dup) removes duplicates from the list dup.

dup = [1, 2, 3, 4, 5, 1, 2, 3]
new_list = list(set(dup))
print("List without duplicates:", new_list)

# 7 check if list is empty
my_list = []
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")

# 8 clone or copy the list
original_list = [1, 2, 3, 4]
copied_list = original_list.copy()
print("Copied List:", copied_list)

# 9 write a program in python to find list of 
# words are longer than n from given list of words
words = ["apple", "banana", "kiwi", "cherry", "grape"]
n = 5
longer_words = []
for word in words:
    if len(word) > n:
        longer_words.append(word)
print("Words longer than", n, "characters:", longer_words)
# longer_words holds the filtered words that are longer than n.

# 10 check comman memeber between 2 list

list1 = [1, 2, 3, 4, 5, 5, 4]
list2 = [4, 5, 6, 7, 7, 8]

# Initialize an empty list to store common elements
common_elements = []

# Initialize index variables for both lists
i = 0
while i < len(list1):
    # Check if the current element in list1 is in list2 and not already in common_elements
    if list1[i] in list2 and list1[i] not in common_elements:
        common_elements.append(list1[i])
    i += 1
print("Common elements:", common_elements)

# 11 remove secefic elements from list
my_list = [1, 2, 3, 4, 5, 3, 6]
my_list.remove(3)
print(my_list)
my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)
print("Removed element:", removed_element)  # Output: 3
print("Updated list:", my_list)  # Output: [1, 2, 4, 5]

# 12 remove even number from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []    # Create an empty list to store odd numbers
for num in my_list:
    if num % 2 != 0:            # Check if the number is odd
        new_list.append(num)     # Add the odd number to the new list

print("List after removing even numbers:", new_list)
# 13 generate square num in rame 1 to 30
# Initialize an empty list to store the perfect squares
squares = []
# Loop through numbers from 1 to 30
for num in range(1, 31):
    square = num ** 2  # Calculate the square of the number
    if square <= 30:  # Check if the square is within the range
        squares.append(square)  # Add the square to the list
    if len(squares) == 5:  # Stop when we have the first 5 squares
        break

# Print the list of first 5 perfect squares
print(squares)

# 14 find the index of the item in a spescific list 
my_list = [10, 20, 30, 40, 50]
index_of_item = my_list.index(30)
print("Index of 30:", index_of_item)

# 15 append 1 list to other  (extend is option )
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print("Updated list1:", list1)

# 17 find second small number in list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
smallest = thislist[0]
second_smallest = thislist[1]
print("Smallest:", smallest)
print("Second smallest:", second_smallest)

# 18 find second larget number in list
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
largest = thislist[0]
second_largest = thislist[1]
print("Largest:", largest)
print("Second largest:", second_largest)

#  19 creat a multiple list
# List of lists (multiple lists in a single list)
list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing each list
print("List 1:", list_of_lists[0])
print("List 2:", list_of_lists[1])
print("List 3:", list_of_lists[2])
