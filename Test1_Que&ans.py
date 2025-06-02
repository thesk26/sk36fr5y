# 1) Wrap to input 2 floating point number and print their average

# a=float(input("Enter the first number:"))
# b=float(input("enter the second number:"))
# c=(a+b)/2
# print("The average of the two given numbers is ",c)

# 2) write a program to input 2 nos and print their sum 

# a=float(input("Enter the first no"))
# b=float(input("Enter the second no"))
# c=(a+b)
# print("the sum of 2 nos is ",c)

#  3) write a program to input the side of square and print its area

# a=float(input("Enter the side of square"))
# area=a**2
# print("The area of square is ",area)

# 4) write a program to find the volume of a sphere and a cylinder(1 is sphere,2 is cylinder)

# a=int(input("Select the vessel whose volume you want to find \n 1 is sphere \n 2 is cylinder"))
# pi = 3.14
# a = int(input("Enter 1 for sphere or 2 for cylinder: "))
# if a == 1:
#     b = float(input("Enter the radius of the sphere: "))
#     vol = (4/3) * pi * b**3
#     print("The volume of the sphere is", vol)
# elif a == 2:
#     b = float(input("Enter the radius of the cylinder: "))   
#     c = float(input("Enter the height of the cylinder: "))
#     vol = pi * b**2 * c
#     print("The volume of the cylinder is", vol)
# else:
#     print("Invalid input")

#   5 ) write a program to input side of square and print its perimeter

# a=float(input("Enter the side of square"))
# per=4*a
# print("The perimeter is ",per)

# 6)  write a program to input to input l and b and print area of rectangle

# l=float(input("enter length of rectangle"))
# b=float(input("enter width of rectangle"))
# area=l*b
# print("the area of rectangle is",area)

# 7) write a code to input a number and print whether it is odd or even

# a=int(input("Enter a number"))
# if(a%2==0):
#     print("The number is even")
# elif(a%2!=0):
#     print("The number is odd")
# else:
#     print("invalid")

#  8) write a code to input radius of circle and print its area

# a=float(input("enter the radius "))
# pi=3.14
# area=pi*a**2
# print("area of circle is",area)

# 9)  write a code to find whether the given number is positive or negative

# a=float(input("enter a number"))
# if(a>0):
#     print("This is a positive number")
# elif(a<0):
#     print("This is a negative number")
# else:
#     print("this number is zero")

# 10) write a code to find the greatest number among the 3 entered 

# a=float(input("enter the first number"))
# b=float(input("enter the second number"))
# c=float(input("enter the third number"))
# if(a>b and a>c):
#     print(a,"is the largest number")
# elif(b>a and b>c):
#     print(b,"is the largest number")
# elif(c>a and c>b):
#     print(c,"is the largest number")
# else:
#     print("any of the two numbers are equal")

# 11) WAP to input a name and return its length

# a=str(input("enter your name"))
# a1=a.strip()
# len1=len(a1)
# print("the length of your name is ",len1)

# 12) WAP to concatenate two strings

# a=str(input("enter a 1st word"))
# b=str(input("enter the second word"))
# c=a+" "+b
# print(c)

# 13) WAP to input three numbers and print the product of the two larger numbers

# a=float(input("enter the 1st no"))
# b=float(input("enter the second no"))
# c=float(input("enter the third no"))
# if(a>c and b>c):
#     prod=a*b
#     print("the product of the larger numbers is",prod)
# elif(b>a and c>a):
#     prod=b*c
#     print("the product of the two larger numbers is",prod)
# elif(c>b and a>b):
#     prod=c*a
#     print("the product of the two larger numbers is",prod)
# else:
#     print("any of the two nos are equal")

# 14) WAP to input two nos and if they are divisible by each other print their product and if not then print their remainder

# a=float(input("enter first no"))
# b=float(input("enter the second no"))
# if(a%b==0):
#     prod=a*b
#     print("they are divisible so their product is",prod)
# elif(a%b!=0):
#     rem=a%b
#     print("they are not divisible so their remainder is",rem)
# else:
#     print("invalid")

#   15) WAP to return only the last two letters of a string in uppercase

# a=str(input("enter a word:"))
# a1=a[-2:]
# print(a1.upper())

# 16) WAP to read the value from the console and find the square and cube of that number

# a=int(input("Enter a number"))
# sq=a**2
# cube=a**3
# print("the square of the number is:",sq , "the cube of the number is:", cube)

# 17 ) if the marks obtained by a student in five different subjects are input through keybboard.find aggregate marks and percentage

# a=float(input("enter marks in first subject"))
# b=float(input("enter marks in second subject"))
# c=float(input("enter marks in third subject"))
# d=float(input("enter marks in fourth subject"))
# e=float(input("enter marks in fifth subject"))
# agg=a+b+c+d+e
# per=(agg/500)*100
# print("the aggregate and percentage are:",agg," ",per)

#18) temp of a city in fahrenhite degree is input through keyboard,wap to convertthis temp in centigrade

# f = float(input("Enter temperature in Fahrenheit: "))
# c = (f - 32) * 5 / 9
# print("The temperature in Celsius is:", c)

# 19) two nos are input through the keboard into two location c and d.write a program to interchange the contents 

# c=int(input("enter the first number"))
# d=int(input("enter the second number"))
# e=c
# c=d 
# d=e
# print("c=",c)
# print("d=",d)

# 20) in a town the percentage of men is 52,the percentage of total literacy is 48,if total literate men is 35 
# of the total population wap to find the total number of literate men and women if the population of town is 80000

# noofmen=0.52*80000
# totalliteracy=0.48*80000
# litmen=0.35*80000
# litwomen=totalliteracy-litmen
# print("The number of literate men=",litmen)
# print("The number of literate women=",litwomen)

# 21) if the total selling price of 15 items and the total profit earned on them is input through the
#  keyboard wap to find the cost price of one item

# sp=float(input("enter the sp of 15 items:"))
# profit=float(input("enter the profit earned on 15 items:"))
# spof1= sp/15
# profitof1= profit/15
# cp=spof1-profitof1 
# print("the cost price of one item is:",cp)

# 22) the distance between two cities is entered through the keyboard.write a program to convert it
#  into metres feets inches and centimetres

# a=float(input("Enter distance between two cities"))
# met=  a* 1000
# feet= met* 3.2808399
# cm= met* 100
# inch= met* 39.37
# print("the distance in metres is:",met)
# print("the distance in feet:",feet)
# print("the distance in cm is:",cm)
# print("the distance in inch is:",inch)

# 23) ramesh basic salary is input through the keyboard.his da is 40% and hr is 20%.wap to calculate gross salary

# basicsalary=float(input("enter the basic salary"))
# da= 0.4* basicsalary
# hr= 0.2* basicsalary
# grosssalary= basicsalary+da+hr
# print("the gross salary=",grosssalary)

#  24) WAP to input sp and cp and find total percentage profit earned

# sp=float(input("enter the selling price"))
# cp=float(input("enter the cost price"))
# perpro=((sp-cp) / cp)*100
# print("the percentage profit earned is",perpro)

# QUESTIONS on string

#  25) print 2nd character from the string Itech system

# a="Itech system"
# print(a[1:2])

#  26) print yste from Itech system 
# a="Itech system"
# print(a[7:11])

# 27) print length of the string Learn python 
# a="Learn python"
# print(len(a))

# 28)remove spaces from the string "  i like to learn python  "
# a="  i like to learn python  "
# print(a.strip())


# 29) print string in lower and upper case "python is fun"
# a="Python is fun"
# print(a.lower())
# print(a.upper())

# 30) replace the string java is a programming language with kava is a programming language
# a="java is a programming language"
# print(a.replace("java","kava"))

# 31) Find the greater no from two

# a=float(input("Enter 1st number"))
# b=float(input("Enter second number"))
# if(a>b):
#     print(a,"is greater")
# elif(b>a):
#     print(b,"is greater")
# else:
#     print("both are equal")


# 32) WAP to find whether the given number is positive or negative
# a=float(input("enter a number"))
# if(a>0):
#     print("This is a positive number")
# elif(a<0):
#     print("This is a negative number")
# else:
#     print("this number is zero")

# 33) pass or fail  
# a=float(input("Enter the percentage marks of the student"))
# if(a>=35):
#     print("The student has passed the exam")
# else:
#     print("The student has failed the exam")

# WAP to input a number and print whether it is odd or even
# a=int(input("Enter a number"))
# if(a%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")

#34) WAP to input 2 numbers and write them in form of x raised to t
# a=float(input("enter first number"))
# b=float(input("enter second number"))
# c=a**b
# print("the answer is",c)

###########################################################################################################################################################

# WHILE LOOp

#  1)Write A program to print the multiplication table of any number   by using while loop in python 

# num = int(input("Enter a number to print its multiplication table: "))
# i = 1
# print("\nMultiplication Table of", num, ":")
# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1

# 2)Write A Program To Find The Average of any 10 No.s

# Program to find the average of 10 numbers using a while loop
# count = 0
# total = 0
# while count < 10:
#     # Concatenate "Enter number " with the count number
#     num = float(input("Enter number " + str(count + 1) + ": "))
#     total += num
#     count += 1
# average = total / 10
# print("The average of the 10 numbers is:", average)

# 3)Write a program to find wheather the number is pallindrome 
# or not(the revers of 111 is 111 i.e. the number 
# 111 is pallindrome)

# number = int(input("Enter a number: "))
# original_number = number
# reversed_number = 0
# while number> 0 :
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10
# if original_number == reversed_number:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

# Write a program to find whether the given number is armstrong or not .
# (if sum of cubes of each digit of the number is equal to the number itself
#   then the number is called an armstrong number.
# (153=(1*1*1)+(5*5*5)+(3*3*3)

# number = int(input("Enter a number: "))
# original_number = number
# sum_of_cubes = 0

# while number > 0:
#     digit = number % 10
#     sum_of_cubes = sum_of_cubes + (digit * digit * digit)
#     number = number // 10
# if original_number == sum_of_cubes:
#     print("It is an Armstrong number.")
# else:
#     print("It is not an Armstrong number.")

# Original number = 153
# Step 1: 3³ = 27
# Step 2: 5³ = 125
# Step 3: 1³ = 1
# Total: 27 + 125 + 1 = 153 ✅ Same as original

# 4) Write a program to calculate p,n,r for 3 sets of values or for 3 persons
# person = 1
# while person <= 3:
#     print("Enter details for person " + str(person) + ":")
#     P = float(input("Enter Principal (P): "))
#     N = float(input("Enter Number of years (N): "))
#     R = float(input("Enter Rate of Interest (R): "))    
#     # Formula for simple interest: SI = (P * N * R) / 100
#     SI = (P * N * R) / 100
#     print("The Simple Interest for person " + str(person) + " is: " + str(SI) + "\n")
#     person += 1

# 5  Write A program to print all the ascii values and their equivalent characters using a while loop. 
# the ASCII values vary from 0-255

# ascii_value = 0
# while ascii_value <= 255:
#     print("ASCII value " + str(ascii_value) + " is: " + chr(ascii_value))
#     ascii_value += 1

# 6 Write A program to reverse the number i.e. if the number
#  entered by the user is 129 then it will display 921

# number = int(input("Enter a number: "))
# reversed_number = 0
# while number > 0:
#     digit = number % 10  # Get the last digit of the number
#     reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
#     number = number // 10  # Remove the last digit from the number
# print("Reversed number is: " + str(reversed_number))
# 1 WAP to reverse a number 

###############################################################################################################################

# WHILE LOOP

# num=int(input("Enter a number"))
# rev=0
# while num>0:
#     digit = num % 10
#     rev = (rev * 10) + digit
#     num=num//10
# print("The reversed number is :" ,rev)

# FOR LOOP 

# num=int(input("enter a number"))
# rev=""
# for digit in str(num):
#     rev=digit+rev 
# print("The reversed number is : ",rev)

##################################################################################################################################
# 2  WAP to print whether the number is palindrome or not 

# WHILE LOOP 

# number=int(input("Enter a number"))
# rev=0
# original_number=number

# while number>0:
#     digit=number%10
#     rev=(rev*10)+digit
#     number=number//10
# print("The reversed number is :",rev)

# if(original_number==rev):
#     print("The number is a palindrome")
# else:
#     print("the no is not a palindrome")

# FOR LOOP 

# num=int(input("Enter a number:"))
# rev=""
# for digit in str(num):
#     rev=digit+rev
# print("The reversed digit is:",rev)
# if (str(num)==rev):
#     print("The no is a palindrome")
# else:
#     print("The number is not a palindrome")

#############################################################################################################################################################################
# 3  WAP to print whether the number is  Armstrong NUMBER or not 
# 153=(1*1*1)+(5*5*5)+(3*3*3) -armstrong number

# num=int(input("enter a number"))
# original_num=num
# sum_of_cubes=0
# while num>0:
#     digit=num%10
#     cube=digit**3
#     sum_of_cubes+=cube
#     num=num//10
# print("the sum of cubes is:",sum_of_cubes)
# if(original_num==sum_of_cubes):
#     print("This is a armstrong number")
# else:
#     print("This is not an armstrong number")

# FOR LOOP 

# num=int(input("enter a number"))
# sum_of_cubes=0
# for digit in str(num):
#     digit=int(digit)
#     cube=digit**3
#     sum_of_cubes+=cube
# print("the sum of cubes is:",sum_of_cubes)

# if(num==sum_of_cubes):
#     print("This is a armstrong number")
# else:
#     print("This is not an armstrong number")

#############################################################################################################################################################################
# 4  WAP to print the sum of all digits in the number 

# WHILE LOOP 

# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print("The sum of digits in number is :",sum)

# FOR LOOP 

# num=int(input("Enter a number:"))
# sum=""
# sum1=0
# for digit in str(num):
#     digit=int(digit)
#     sum1+=digit
#     sum=str(sum1)
# print("The sum of digits in number is :",sum)

#############################################################################################################################################################################
# 5  WAP to calculate the factorial of given number 

# WHILE LOOP 

# num=int(input("Enter a number:"))
# factorial=1
# i=1
# while i<=num:
#     factorial*=i
#     i+=1
# print("The factorial of the given number is:",factorial)

# FOR LOOP 

# num=int(input("Enter a number:"))
# factorial=1
# for i in range(1,(num+1)):
#     factorial*=i
# print("The factorial of the given number is:",factorial)

#############################################################################################################################################################################
# input level :-  Get two numbers from the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# Addition
# z = num1 + num2
# print("Sum:", z)

# Subtraction
# diff_result = num1 - num2
# print("Difference:", diff_result)

# Multiplication
# prod_result = num1 * num2
# print("Product:", prod_result)

# Division
# div_result = num1 / num2
# print("Division:", div_result)

# Floor Division (integer division)
# floor_div_result = num1 // num2
# print("Floor Division:", floor_div_result)

# Modulus (remainder)
# mod_result = num1 % num2
# print("Modulus:", mod_result)

# Exponentiation (power)
# exp_result = num1 ** num2
# print("Exponentiation:", exp_result)

# comparison operator

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# Equal to
# print("Is num1 equal to num2?", num1 == num2)

# Not equal to
# print("Is num1 not equal to num2?", num1 != num2)

# Greater than
# print("Is num1 greater than num2?", num1 > num2)

# Less than
# print("Is num1 less than num2?", num1 < num2)

# Greater than or equal to
# print("Is num1 greater than or equal to num2?", num1 >= num2)

# Less than or equal to
# print("Is num1 less than or equal to num2?", num1 <= num2)

#  how you can take a number as input in Python and print its square and cube:

# Get input from user
# num = int(input("Enter a number: "))

# Calculate square and cube
# square = num ** 2
# cube = num ** 3

# Display results
# print("Square of", num, "is", square)
# print("Cube of", num, "is", cube)

# how you can take a number as input in Python and print Perimeter of a Rectangle

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# perimeter = 2 * (length + width)
# print("Perimeter of the rectangle is:", perimeter)

# how you can take a number as input in Python and print Perimeter of square
# side = float(input("Enter the side of the square: "))
# perimeter = 4 * side
# print("Perimeter of the square is:", perimeter)

#############################################################################################################################################################################
# LIST QUESTION ANSWER

# 1 sum items in list
# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list)
# print("Sum:", total)

# my_list = [1, 2, 3, 4, 5]
# total = (1+2+3+4+5)
# print("Sum:", total)

# 2 multply items in list
# my_list = [1, 2, 3, 4, 5]
# result = 1       
# for num in my_list:
#     result *= num
# print("Product:", result)

# if we put 0 then anything multiply by 0 is 0
# result = 1
# result *= 1  # result = 1
# result *= 2  # result = 2
# result *= 3  # result = 6
# result *= 4  # result = 24
# result *= 5  # result = 120

# 3 get largest number in list
# numbers = [10, 45, 23, 89, 2, 77]
# largest = numbers[0]  # Assume the first number is the largest
# for num in numbers:
#     if num > largest:
#         largest = num  # Update if a bigger number is found
# print("The largest number is:", largest)

# 4 get smaller number in  list
# numbers = [10, 45, 23, 89, 2, 77]
# smallest = numbers[0]  # Assume the first number is the smallest
# for num in numbers:
#     if num < smallest:
#         smallest = num  # Update if a smaller number is found
# print("The smallest number is:", smallest)

# Start with smallest = 10
# Compare 45 → not smaller
# Compare 23 → not smaller
# Compare 89 → not smaller
# Compare 2 → ✅ YES! 2 is smaller → smallest = 2
# Compare 77 → not smaller
# Result: ✅ 2 is the smallest.

# 5 count string with same start and end
# my_list = ["apple", "banana", "cherry", "radar", "level", "orange"]
# count = 0
# for word in my_list:
#     if word[0] == word[-1]:
#         count += 1
# print("Count of words with same start and end:", count)

# my_list = ["apple", "banana", "cherry", "radar", "level", "orange"]
# a = []
# for word in my_list:
#     if word[0] == word[-1]:
#         a.append(word)
# print("Words with same start and end:", a)

# 6 remove duplicates from list 
# set(dup) removes duplicates from the list dup.

# dup = [1, 2, 3, 4, 5, 1, 2, 3]
# new_list = list(set(dup))
# print("List without duplicates:", new_list)

# 7 check if list is empty
# my_list = []
# if not my_list:
#     print("The list is empty.")
# else:
#     print("The list is not empty.")

# 8 clone or copy the list
# original_list = [1, 2, 3, 4]
# copied_list = original_list.copy()
# print("Copied List:", copied_list)

# 9 write a program in python to find list of 
# words are longer than n from given list of words

# words = ["apple", "banana", "kiwi", "cherry", "grape"]
# n = 5
# longer_words = []
# for word in words:
#     if len(word) > n:
#         longer_words.append(word)
# print("Words longer than", n, "characters:", longer_words)

# longer_words holds the filtered words that are longer than n.

# 10 check comman memeber between 2 list
# list1 = [1, 2, 3, 4, 5, 5, 4]
# list2 = [4, 5, 6, 7, 7, 8]
# # Initialize an empty list to store common elements
# common_elements = []

# Initialize index variables for both lists
# i = 0
# while i < len(list1):
#     # Check if the current element in list1 is in list2 and not already in common_elements
#     if list1[i] in list2 and list1[i] not in common_elements:
#         common_elements.append(list1[i])
#     i += 1
# print("Common elements:", common_elements)

# 11 remove secefic elements from list
# my_list = [1, 2, 3, 4, 5, 3, 6]
# my_list.remove(3)
# print(my_list)
# my_list = [1, 2, 3, 4, 5]
# removed_element = my_list.pop(2)
# print("Removed element:", removed_element)  # Output: 3
# print("Updated list:", my_list)  # Output: [1, 2, 4, 5]

# 12 remove even number from list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []    # Create an empty list to store odd numbers
# for num in my_list:
#     if num % 2 != 0:            # Check if the number is odd
#         new_list.append(num)     # Add the odd number to the new list
# print("List after removing even numbers:", new_list)

# 13 generate square num in rame 1 to 30

# Initialize an empty list to store the perfect squares
# squares = []
# Loop through numbers from 1 to 30
# for num in range(1, 31):
#     square = num ** 2  # Calculate the square of the number
#     if square <= 30:  # Check if the square is within the range
#         squares.append(square)  # Add the square to the list
#     if len(squares) == 5:  # Stop when we have the first 5 squares
#         break
# # Print the list of first 5 perfect squares
# print(squares)

# 14 find the index of the item in a spescific list 
# my_list = [10, 20, 30, 40, 50]
# index_of_item = my_list.index(30)
# print("Index of 30:", index_of_item)

# 15 append 1 list to other  (extend is option )
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# for item in list2:
#     list1.append(item)
# print("Updated list1:", list1)

# 17 find second small number in list
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# smallest = thislist[0]
# second_smallest = thislist[1]
# print("Smallest:", smallest)
# print("Second smallest:", second_smallest)

# 18 find second larget number in list
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# largest = thislist[0]
# second_largest = thislist[1]
# print("Largest:", largest)
# print("Second largest:", second_largest)

#  19 creat a multiple list
# List of lists (multiple lists in a single list)
# list_of_lists = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Accessing each list
# print("List 1:", list_of_lists[0])
# print("List 2:", list_of_lists[1])
# print("List 3:", list_of_lists[2])

