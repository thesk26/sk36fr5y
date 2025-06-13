# Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
# It is used for:
# web development (server-side),
# software development,
# mathematics,
# system scripting.
# (python is interpretor language)

# Day 1 Of Python learning.
# 28/04/2025
# class 1
# basic of python 
print("hello")
print(9+9)

# 1.Arithmetic operators.
# variables 
#  Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
#  In Python, we don't need to specify the type of variable because Python is a infer language and smart enough to get variable type.
#  Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore. 

a=7 # 7 is value and a is variable  
b=8 # same as given on last line
c=a+b
print(c)
                        #  operators
                        # arithmatic ope. (+,-,*,/,**,//,%)
                        # % modulus ope. it gives remainder 
                        # / mean gives ans in detail with decimal
                        # // (Floor division)ans without decimal 
                        # **(Expotential) something power something (eg. 2 ki power 5=32)
a2=877
b2=99
print(a2-b2)

# Data type 
a = "any name" # String ""
b= 44 # integer 
v =22.899 # Float
z= True # boolean 
c= 1j # complex 
print(type(a)) # to check data type of variable
print(type (c)) # to check data type of variable

# Day 2 Of Python learning.
# 29/04/2025
# class 2

# 2. Assignment operators
# Assignment operators are used to assign values to variables: 
# (=,+=,-=,*=,/=,//=,&=,^=,>>=,<<=,:=)\

# 1. =
x=2
print(x)

# 2. +=           add with num and x value  
# method 1
num = 23       
num = num + 26 
print(num)
# method 2
num = 51
num += 45
print("num:",num)

# 3. -=          subtract with num and x value 
# method 1
num = 230       
num = num - 60 
print(num)
# method 2
num = 510
num -= 450
print("num:",num)

# 4. *=         multiply with num and x value  
# method 1
num = 15       
num = num * 6 
print(num)
# method 2
num = 5
num *= 5
print("num:",num)

# 5. /=         div. with num and x value 
# method 1
num = 20       
num = num / 4 
print(num)
# method 2
num = 50
num /= 5
print("num:",num)

# 6. %=        mod gives remainder 
# method 1
num = 23       
num = num & 2 
print(num)
# method 2
num = 51
num %= 4
print("num:",num)

# 7. //=      It gives ans. without decimal          
# method 1
num = 200       
num = num // 26 
print(num)
# method 2
num = 510
num //= 45
print("num:",num)

# 8. **=      something power something  
# method 1
num = 3       
num = num ** 2 
print(num)
# method 2
num = 5
num **= 4
print("num:",num)

# 9. &=   (and)           use from truth table 
# method 1           gives value in 0 and 1 
num = 3            # T F -->result (1)
num = num & 6      # 0 0 -->0
print(num)         # 0 1 -->0 
# method 2         # 1 0 -->0
num = 5            # 1 1 -->1
num &= 4                                               # 8bit structure : 128 64 32 16 8 4 2 1 
print("num:",num)                                                   # 1.   0  0  0  0  0 0 0 1
                                                                    # 2.   0  0  0  0  0 0 1 0
# 10. |=          (Or)                          Binary digits       # 3.   0  0  0  0  0 0 1 1
# method 1           # T F -->result                                # 4.   0  0  0  0  0 1 1 0
num = 2              # 0 0 -->0                                     # 5.   0  0  0  0  0 1 0 1 
num = num | 6        # 0 1 -->1                                     # 6.   0  0  0  0  0 1 1 0
print(num)           # 1 0 -->1                                     # 7.   0  0  0  0  0 1 1 1
# method 2           # 1 1 -->1                                     # 8.   0  0  0  0  1 0 0 0
num = 1                                                             # 9.   0  0  0  0  1 0 0 1
num |= 5                                                            # 10.  0  0  0  0  1 0 1 0
print("num:",num)                                                   # 11.  0  0  0  0  1 0 1 1
                                                                    # 12.  0  0  0  0  1 1 0 0
# 11. ^=   (x-or)                                                   # 13.  0  0  0  0  1 1 0 1
# method 1          # T F -->result                                 # 14.  0  0  0  0  1 1 1 0
num = 2             # 0 0 -->0                                      # 15.  0  0  0  0  1 1 1 1
num = num ^ 6       # 0 1 -->1                                      # 16.  0  0  0   1 0 0 0 0
print(num)          # 1 0 -->1                                      # 17.  0  0  0   1 0 0 0 1
# method 2          # 1 1 -->0                                      # 18.  0  0  0   1 0 0 1 0
num = 1                                                             # 19.  0  0  0   1 0 0 1 1
num ^= 4                                                            # 20.  0  0  0   1 0 1 0 0
print("num:",num)                                                   # 21.  0  0  0   1 0 1 0 0
                                                #   this digits are use to calaulate (&,|,^) 
# eg. x=5   x &= 3     # print(x)  result is 1   # reson binary no. of 5 is 0101 and BN 3 is 0011 as a reult 0101
                                                     # 0011  = 0001 (using truth table)
# 12. >>=    sign indiactes righshift ope.                                   
# method 1                                          
num = 7                                  # eg. x=5          
num = num >> 8                           #  x >>= 3  x = x>>3 (x= 5>>3)       5= 0101 
print(num)                                                                 #  3= 0011       bn of 5 shifts right side of bn of 3                      
# method 2                                                                 #     0000   result = 0        
num = 7
num >>= 9
print("num:",num)

# 13. <<=  sign indicates leftshift ope.                 
# method 1                                    # eg. x=5                           32 16 8421 
num = 23                                      #  x <<= 3  x = x<<3 (x= 5<<3)   5=       0101
num = num << 26                                                              # 3=       0011       bn of 5 shifts left side of bn of 3
print(num)                                                                   #     1  0 1000   result = 32+8=32
# method 2
num = 51
num <<= 45
print("num:",num)

# Day 3 Of Python learning.
# 2/05/2025
# class 3

# Topic : Input type 

name = input("enter name :")
age = int(input("enter age :"))
marks = float(input("enter marks :"))

print("welcome", name)
print("age", age)
print("marks", marks)

# Task 1
#  que. and ans.

num1 = int(input("Enter the first no. :"))
num2 = int(input("Enter the second no. :"))

# addition
s = num1 + num2
print("sum" ,s)

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

# comparison operator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

    # Equal to
print("Is num1 equal to num2?", num1 == num2)

    # Not equal to
print("Is num1 not equal to num2?", num1 != num2)

    # Greater than
print("Is num1 greater than num2?", num1 > num2)

    # Less than
print("Is num1 less than num2?", num1 < num2)

    # Greater than or equal to
print("Is num1 greater than or equal to num2?", num1 >= num2)

    # Less than or equal to
print("Is num1 less than or equal to num2?", num1 <= num2)

# que.2
#  how you can take a number as input in Python and print its square and cube:

num = int(input("enter a number:"))

# calculate square and cube 
square = num**5
cube = num**4

# Result 
print("square of" ,num,"is :",square)
print("cube of" ,num,"is :",cube)

# how you can take a number as input in Python and print Perimeter of a Rectangle
length = float(input("enter the length of rectangle :"))
width = float(input("enter the width of rectangle :")) 

perimeter = 2 * (length*width)

print("perimeter of rectangle is :" ,perimeter)

# how you can take a number as input in Python and print Perimeter of square

side =(float(input("enter the side of square :")))
perimeter1 = 4*side
print("perimeter of square :", perimeter1)

# Area of circle 
r = float(input("enter radius :"))
p = 3.14
A = p*r**2
print(A)

# perimeter of circle
r1 = int(input("enter radius :"))
p = 3.14
A1 = 2*p*r1
print(A1)

# Day 4 Of Python learning.
# 5/05/2025
# class 4

# Revision of python from day 1 to day 3

# Day 5 Of Python learning.
# 6/05/2025
# class 5

# String 
str1 = 'The '
str2 = "Vehicle"

str3 = '''Dr.'''
# """ """ for. multiple line comment.
str4 = """Dk"""

print(str1)
print(str2)
print(str3)
print(str4)

# concaniate meean addition

final_str = str1 + str2 +str3
print(final_str)

a = "Hello"
b = "SDk"
c = a + " " + b
print(c)

# length of string

str1 = "ToadyIsMyThirdDayOfLearningPython"
len1 = len(str1)
print(len1)

str2 = "python"
len2 = len(str2)
print(len2)

final_str = str1  + str2
print(final_str)
print (len(final_str))

b = "Hello, sdk!"
print(b[ 3])      # Indexing mean starts from 0 and counts from given no. in square bracket 

# slice of string

b = "Hello, python!"
print(b[ 7:3])


c = "Hello, python!"
print(c[:5])

# negative slice

str = "apple"

print(str[-5:-2])
# Index:   0  1  2  3  4
        # 'a','p','p','l','e'

# Negative Index:
#         -5 -4 -3 -2 -1

b = "Hello, World!"
print(b[-9:-1])

# Index:     0   1   2   3   4   5   6   7   8   9   10  11  12
# Characters:H   e   l   l   o   ,       W   o   r   l   d   !
# Neg Index:-13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Go up to but not including index -2 (which is 'l')
# Includes the character at start index ✅
# Excludes the character at end index ❌
# check whether is present the word or not

a = "The best things in  our life is the language python !"
print("best" in a)

# uppercase string

a = "Hello, sdk!"
print(a.lower())

# lowercase

a = "Hello, sdk!"
print(a.lower())

# repalce

a = "swarup, kadam!"
print(a.replace("swarup", "krishna"))

a= "swa"
print(a.replace("swa" , "kri"))

# whitespace remove

a = "      Hello, sdk! "
print (a)

a = "   Hello,swarup! "
print(a.strip())

#  split the string

# method 1
a = 'firstname, lastname!'
b = a.split(",")
print(b)

# method 2
a = "Swarup"
b = "KAdam"
c = a + b
print(c)

# method 3
a = "SDk"
b = "leaning python"
c = a + " " + b
print(c)

# Day 6 of learning python
# 7/05/2025
# class 6

# Conditional statement
 
 # if statement    we can add only once (in if statement condition will applyed )
a = 33
b = 200

if b>a:
  print("b is greater than a")

a=150
b=20
if a<b:
    print ("a<b")
else:
    print("a>b")

# else statement    we can add only once (in if statement condition will not applyed)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a <= b:
  print("a and b are equal")
elif a >= b:
  print("a is greater than b")
else:
  print("a not b")

# elif condition
                            # we can add elif infinte time 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Day 7 of lerning python
# 8/05/2025
# class 7

 # if statement
a = 33
b = 200
if b>a:
  print("b is greater than a")

a=150
b=20
if a<b:
    print ("a<b")
else:
    print("a>b")

# else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a <= b:
  print("a and b are equal")
elif a >= b:
  print("a is greater than b")
else:
  print("a not b")

# elif condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# shorthand properties of if else
a = 200
b = 33
if a > b: print("a is greater than b")

a = 20
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b  else print("=") 

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a>b or a == c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Day 9 of lerning python
# 12/05/2025
# class 9

# while conditional statement
# in while loop we can add infinite time
# while loop with else statement
# With the while loop we can execute a set of statements as long as a condition is true. 
i = 0
while i < 10:
  print(i)
  i += 1
i = 0
while i < 70:
  print(i)
  i = i+1
else:
  print("i is no longer less than 70")

# for conditional statement
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Example

classes = ["classA", "classB" , "classC"]
for x in classes:
  print(x)
for x in "AnyName":
  print ( x)

# The range() Function in for loop
for x in range(9):
  print(x) 
for x in range(2, 18):
  print(x)

# in this function 2 is an starting index and  20 is an ending index 2 is an increment or decrement operator
for x in range(2, 20, 2 ):  
  print(x)        

# Using For Loop   With the break statement we can stop the loop even if the while condition is true
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

# Using While Loop
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1

for i in range(8):
    if i == 3:
        continue  # Skip the rest of the code for i = 3
    print(i)

# MATCH CONDITIONAL STATEMENT

day  = 7
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
value = "hello"

match value:
    case int():
        print("It's an integer")
    case str():
        print("It's a string")
    case list():
        print("It's a list")
    case _:
        print("Unknown type")

fruit = "apple"

match fruit:
    case "apple" | "banana":
        print("It's a fruit!")
    case "carrot" | "spinach":
        print("It's a vegetable!")
    case _:
        print("Unknown food")

# Day 10 of lerning python
# 14/05/2025
# class 10

# Lists are mutable, ordered collections of items
# Lists can contain any data type, including other lists
# Lists are defined using square brackets []
# Lists can be empty or contain multiple items
# Lists can be indexed and sliced
# Lists can be nested
# Lists can be iterated over    
# Lists can be sorted
# Lists can be reversed
# Lists can be concatenated
# Lists can be repeated
# Lists can be copied
# Lists can be extended 
# Lists can be joined
# Lists can be unpacked
# Lists can be compared
# Lists can be converted to strings
# Lists can be converted to tuples
# Lists can be converted to sets
# Lists can be converted to dictionaries
# Lists can be converted to arrays
# Lists can be converted to JSON
# Lists can be converted to XML
# Lists can be converted to CSV
# Lists can be converted to HTML
# Lists can be converted to Markdown
# Lists can be converted to YAML
# Lists can be converted to INI

marks1 = 29
marks2 = 100
marks3 = 29
marks4 = 66
marks5 =55

# and marks of student is just no 5 they ae many so we make list
marks = [29, 100, 129, 66, 55]
print(marks)
print (type(marks))
print(marks[0])
print(marks[1])
print (len(marks))
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# slicing of list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-1])

# indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

# change list item
thislist = ["apple", "banana", "cherry"]
thislist[2] = "blackcurrant"
print(thislist)

#############################################################################################################################################################################
# Day 11 of learning python
# 15/05/2025
# class 11

# insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

# methods in list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

print(type(thislist) ) 

list = [2 ,1 ,3 ]
list.append(4)
print(list)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana",]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#  first occurace removed index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

list = [ 2, 1 , 3, 1]
list.remove(1)
print(list)

# The pop() method removes the specified index.
# The .pop() method removes the last item in the list by default.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# join the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# loop list

thislist = ["apple", "banana", "cherry"]
for x1 in thislist: print(x1)

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

##########################################################################################################################
# day 13 of learning python
# 21/05/2025
# class 13

# Tuples are immutable, ordered collections of items
# Tuples can contain any data type, including other tuples
# Tuples are defined using parentheses ()
# Tuples can be empty or contain multiple items
# Tuples can be indexed and sliced
# Tuples can be nested
# Tuples can be iterated over
# Tuples can be concatenated
# Tuples can be repeated
# Tuples can be copied
# Tuples can be converted to lists
# Tuples can be converted to strings

# Tuples
# A tuple is a collection which is ordered and unchangeable.

tup =()
print(tup)
print(type(tup))

tup =(2.9)
print(tup)
print(type(tup))
 
tup =("ashwini")
 
tup =("ashwin " )
  
print(tup)
print(type(tup))

# if you want to create its type as a tuple then you have to add ,

tup =("ashwin" ,)
print(tup)
print(type(tup))

tup =( 1 , 2 , 3 , 4 ,5)
print(tup [1:3])

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# update  tuple 

x = ("apple", "banana", "cherry")

y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x)
print(type(x ,))

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
 
print(tuple3)

print(type(tuple3 ,))

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
 
print(tuple3)

print(type(tuple3 ,))

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
  
print(mytuple)

# methods in tuples 

# index

tup = ( 1 ,2 ,3 , 4)
print(tup.index(4))

# ans is 1 because we call it index of value 2 in tuple

tup = ( 1 ,2 ,3 , 4 , 2 , 2)
print(tup.index(2))

# This method searches the tuple for the first occurrence of the value 2 and returns its index.

# Tuple indexing starts at 0.

# In the tuple (1, 2, 3, 4, 2, 2), the first 2 appears at index 1.

# count

tup = ( 1 ,2 ,3 , 4 , 2 , 2 , 2 ,2)
print(tup.count(3))

################################################################################################################
# Day 14 of learning python
# 26/05/2025  
# class 14

# QUESTION ANSWER ON tuple
    
# 1 create a tuple 

# Creating a tuple
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)

# 2.0 add the integer in tuple 
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total += num
print("Total =", total)

# 2 Write a Python program to create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# 3 Write a Python program to create a tuple of numbers and print one item.

tuplex = 5, 10, 15, 20, 25
print(tuplex)
tuplex = 5,
print(tuplex)

# 4 Write a Python program to unpack a tuple into several variables.

tuplex = 4, 8, 3
print(tuplex)
n1, n2, n3 = tuplex
print(n1 + n2 + n3)

# 5 Write a Python program to add an item to a tuple

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = tuplex + (9,)

print(tuplex)

listx = list(tuplex)

listx.append(30)

tuplex = tuple(listx)

print(tuplex) 

# 6 Write a Python program to get the 4th element from the last element of a tuple.

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex)

# Get the 4th element of the tuple (index 3)
item = tuplex[3]
print(item)

# Get the 4th element from the end of the tuple (index -4)
item1 = tuplex[-4]
print(item1) 

# 7Write a Python program to remove an item from a tuple.

tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
  
listx = list(tuplex)

listx.remove("c")
tuplex = tuple(listx)
print(tuplex)

##############################################################################
# Day 15 
# 27/05/25.  ex date
# class 15

# 3/06/25

# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# from typing import Dict

listx = list(tuplex)

thisdict ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
 }
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
print(thisdict["model"])
print(type(thisdict))

# Dictionaries cannot have two items with the same key:

thisdict = { 
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "year": 3000
}
print(thisdict)

info = {
"name" : "Nothing",
"subject" : ["python" , "mern " , "c" , "c++" ],
"topics" : ( "dict ","tuple" , "list" ),
"age" : 78 ,
"marks" : 94.4
}
print(info)

# add dict

info [ "name"]= "any23455"  # it will overwrite  name property
info [ "age"] = 40
print(info)

marks = {"Swarup":67, "Kartik":88, "Ram":91, "Aditya":49}
print ("Initial dictionary: ", marks)

marks['Yash'] = 58
print ("Dictionary after new addition: ", marks)

marks = {"Swarup":67, "Om":88  }
print ("Initial dictionary: ", marks)

marks.update({'Kavya': 58, 'Mohit': 98})
print ("Dictionary after new addition: ", marks)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))    #duplicates not allowed

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# remove dict

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

# del key word

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation:\n ", numbers)

del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)

# pop method

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)

val = numbers.pop(20)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

# clear method

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers)
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)

# Nested Dictionaries

student = {
    "name": "any name ",
    "subject" :{
        "python" : 45,
        "mern" : 23 ,
        "math" :22
    } 
}
print(student ["subject"] ["python"])
print(student ["subject"] ["mern"])
print(student ["name"] )

# Dictionary methods

student = {
    "name": "Swarup",
    "subject" :{
        "python" : 55,
        "mern" : 53 ,
        "math" : 25
    } 
}
print (student.keys())

# casting in keys
print(list(student.keys()))

student.values()
print(student.values())

student.items()  # output  as a tuples 
print(student.items())

pairs = list(student.items())
print(pairs[0])

print(student.get("name")) 

# it should not get error
# update method

student = {
    "name": "Swaarup",
    "subject" :{
        "python" : 405,
        "mern" : 203 ,
        "math" :220
    } 
}
student.update({"city" : "delhi"})
print (student)

student = {
    "name": "sdk",
    "subject" :{
        "python" : 400,
        "mern" : 230 ,
        "math" :220
    } 
}

new_dict = {"city" : "Nashik" , "age" : "18"}
student.update(new_dict)
print (student)

d1 = {"Fruit":["Watermelon","Banana"], "Flower":["LILI", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

# this is the end.
# questions on DICTIONARY
#1 Write a Python program to add a key to a dictionary.

d = {0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d) 

# 2 Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary 'dic4' that will store the combined key-value pairs from 'dic1', 'dic2', and 'dic3'.

dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) 

# 3 Write a Python program to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present(2)
is_key_present(1) 

# 4 Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
# Print the key followed by '->' and the corresponding value.
  print(dict_key, '->', dict_value)	

# 5 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Input a number "))
d = dict()
for x in range(1, n + 1):
    d[x] = x * x
print(d) 

# 6 Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d) 

# 7 Write a Python program to sum all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = sum(my_dict.values())
print(result) 

# 8 Write a Python program to multiply all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1
for key in my_dict:
    result = result * my_dict[key]
print(result) 

# 9 Write a Python program to remove a key from a dictionary.

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)

# 10 Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# 11 Write a Python program to get the maximum and minimum values of a dictionary.

my_dict = {'x': 500, 'y': 5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda l: my_dict[l]))
print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])

# End 

# Day 16 
# 28/05/25.  ex date
# class 16

# 3/06/25
#  python set  
# it does no allow a duplicate value in set does not allow  it ignore it  and it is unordered it does nt hav order 
# it have unquie value

collection = { 1 , 2 ,2 ,2 , "hello" , "world" , "world"}
print(collection)
print(type(collection))
print(len(collection))

my_set = {1, 2, 3, 4, 5}
print (my_set)

my_set = set([1, 2, 3, 4, 5])
print (my_set)

my_set = {1, 2, 2, 3, 3, 4, 5, 5} 
print (my_set)                         #does not allow duplicte member

# empty set

collection = set()
print(type(collection))

# set method
# we cam pass the tuple
# but we can not pass list

collection = set()             # Create an empty set
collection.add(1)              # Add integer 1
collection.add(2)              # Add integer 2
collection.add(3)              # Add integer 3
collection.add(4)              # Add integer 4
collection.add("ashwini")      # Add string "ashwini"
collection.add((1,2,3))        # Add tuple (1,2,3) — tuples are immutable, so allowed

print(collection)

collection.remove(4)
print(collection)          # collection.discard(3)

collection.clear()  #all set get null 
print(collection)
 
print(len(collection))

# values are we get is randamaly pop
print (collection.pop())
print (collection.pop())
print (collection.pop())
print (collection.pop())

#  remove and we also use dicard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# The .pop() method removes and returns an arbitrary item from the set.
# Since sets are unordered, you cannot predict which item will be removed.
# The removed item is stored in the variable x.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

#  if we remove cherry specific

thisset = {"apple", "banana", "cherry"}
thisset.remove("cherry")
print(thisset)

# sets method
# union set no duplicates 

set1 = {1, 2, 3 , 4}
set2 = {1, 2, 3 ,5 ,6,7}
set3 = set1.union(set2)
print(set3)

# one and same as it is like union it givs same output

set1 = {"a", "b", "c" ,3}
set2 = {1, 2, 3}
set3 = set1 & set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# intersection  only common element are in output

set1 = {1, 2, 3 , 4}
set2 = {1, 2, 3}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# same as intesection and will use 

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# join the sets

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)

# using union method

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)

# End 
# question on set

#  1 Create a set containing the numbers 0 to 5:

num_set = set([0, 1, 2, 3, 4, 5])
print(num_set)

# 2 Create a new empty set 'color_set':

color_set = set()
print(color_set)

# 3 add anything in set

color_set = set()
print(color_set)
color_set.add("Red")
print(color_set)

# 4 update a set

color_set = set()
color_set.update(["Blue", "Green"])
print(color_set) 

# 5 Create a new set 'num_set' with the elements 0, 1, 2, 3, 4, and 5 using a list:

num_set = set([0, 1, 2, 3, 4, 5])
print(num_set)
num_set.discard(4)
print(num_set)

#  6 Convert list [1, 2, 2, 3, 4, 4, 5] to a set.

lst = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(lst)
print(unique_set)  

# 7  Create a set with elements "apple", "banana", "cherry" and print it.

fruits = {"apple", "banana", "cherry"}
print(fruits)

# 8  Check if "banana" is in the set.

fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)

# 9 Add "orange" to the set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# 10) Remove "banana" using remove() and discard() – what's the difference?

fruits = {"apple", "banana", "cherry"}

# Using remove - throws error if item not found
fruits.remove("banana")  
print(fruits)

# Using discard - no error if item not found
fruits.discard("orange")  # Safe to use even if "orange" not in set
print(fruits)

# ✅ remove() raises KeyError if item doesn't exist.
# ✅ discard() does not raise error

# 11 ) Convert list [1, 2, 2, 3, 4, 4, 5] to a set.

lst = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(lst)
print(unique_set)

# 12) Perform union, intersection, and difference.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)             # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)     # {3, 4}
print("Difference A - B:", A - B) # {1, 2}

# 13) Symmetric Difference (in A or B, not both)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Symmetric Difference:", A ^ B)

# 14 ) Convert string "hello" to a set

s = "hello"
print(set(s))

# 15) Remove duplicates from list using set

lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

# End.

# Day 17
# 4/06/25
# class 17

# function
# to define a function def is used

def function():   # def stands for defination 
    print("I am learning python function ")

function()

def my(fname):
    
    print(fname + " surname")

my("a")
my("b")
my("c")
  
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Swarup","Kadam")

# *means we passed one arument
def my_function(*name):
    print("my pet names are  " + name[0] +  " " + name[1])
my_function("alpha", "beta", "xyz")

# **means 2 argument we passed

def my_function(**name):
    print(" suname of the family is " + name["lname"])
    for k, val in name.items():
        print(k, val)
my_function(fname = "Kartik", lname = "Gamne")

# *args example

def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

# default parameter

def my_function(state = "maharastra"):

    print("I am from " + state)

my_function("arunachal pradesh")
my_function(" punjab")
my_function()
my_function("jammu&kashmir")

def sum(a,b):

    s= a+b
    return s
print(sum(2, 4) ) 

def muliply(x):
  return 5 * x

print(muliply(3))
print(muliply(5))
print(muliply(9))

def avg( a, b , c ,d):
    sum = a + b + c + d

    avg = sum / 4
    print (avg)
    return avg 

avg ( 2 ,3 ,4, 5)
# end 

# Day 18
# 9/06/2025
# class 18

# when a function call itself called  recursion

def show(n):
    if n == 0:
        return

    print(n)
    print("end")

    show(n - 1)  #function calls itself with a smaller value (n - 1),
show(9)

def fact(n):
    if(n == 1 or n == 0):    #This function keeps calling itself with n-1 until it hits the base case (n == 1 or n == 0).
        return 1
    return fact(n-1) * n

print(fact (4)) 

# n! = n × (n-1) × (n-2) × ... × 1
# fact(4)
# = fact(3) * 
# fact(3)
# = fact(2) * 
# fact(2)
# = fact(1) * 2
# fact(1) 
# # = 1  ← base case
# fact(2) = fact(1) * 2 = 1 * 2 = 2
# fact(3) = fact(2) * 3 = 2 * 3 = 6
# fact(4) = fact(3) * 4 = 6 * 4 = 24

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

#This is the recursive call, because the function tri_recursion 
# is calling itself with a smaller value: k - 1.

# T(n) = n + (n - 1) + (n - 2) + ... + 1
# tri_recursion(1) = 1 + 0 = 1 → prints 2
# tri_recursion(2) = 2 + 1 = 3 → prints 3
# tri_recursion(3) = 3 + 3 = 6 → prints 6
# tri_recursion(4) = 4 + 6 = 10 → prints 10
# tri_recursion(5) = 5 + 10 = 15 → prints 15
# tri_recursion(6) = 6 + 15 = 21 → prints 21

# day 18
# 9/06/25
# class 18
# Lambda Functions in Python
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
# Example: Basic Lambda Function        
# lambda arguments: expression
# Example: Square of a number
# square = lambda x: x ** 2
# print(square(5))  # Output: 25
# Example: Add two numbers
# add = lambda x, y: x + y
# print(add(3, 4))  # Output: 7
# Example: Check if a number is even or odd
# is_even = lambda x: x % 2 == 0
# print(is_even(4))  # Output: True
# print(is_even(5))  # Output: False
# Example: Using Lambda with map
# map(function, iterable)
# Example: Using Lambda with map
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Example: Using Lambda with filter
# filter(function, iterable)
# Example: Using Lambda with filter
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6]
# Example: Using Lambda with reduce
# from functools import reduce
# reduce(function, iterable)
# Example: Using Lambda with reduce
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 120

s1 = 'Swarup'
s2 = lambda func: func.upper()
print(s2(s1))

s2 = lambda func: func.lower()
print(s2("Swarup"))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0)) 

# Using lambda

sq = lambda x: x ** 2
print(sq(3))

# Using def

def sq(x):
    return x ** 2
print(sq(3)) 

add = lambda a:a+10
print(add)
print(add(90))

# as we are using function as 

def add( a , b ):
    return a+b 
print (add(10,20))

# we in lamba we just have to do this 

add=lambda a,b:a+b
print(add(10,20))

a=lambda a,b:(a+b , a-b , a*b)
add, sub , mul =a(10,20)
print(add)
print(sub)
print(mul)
# add = lambda a, b: (a + b, a - b)
# add, sub = add(10, 20)
# print(add)
# print(sub)
# add = lambda a, b: (a + b, a - b, a * b)

# you can pass any type of argument

add=lambda  a,  b=50:(a+b , a-b)
add, sub = add(90)
print(add)
print(sub)

add = lambda b, a=90,  : (a + b, a - b)
add, sub = add(50)
print(add)
print(sub)

add = lambda a=90, b=50: (a + b, a - b)
add, sub = add()
print(add)
print(sub)

double = lambda x: x * 2
print(double(5))

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

def myfunc(n):
    return lambda a: a * n

mytripler = myfunc(8)
print(mytripler(11))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  
print(mytripler(11))  

# Example: Filter even numbers from a list

n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0 , n)
print(list(even))

n = (1, 2, 3, 4, 5, 6)
even = filter(lambda x: x % 2 == 0 , n)
print(tuple(even))

# Example: Check if a number is even or odd

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7)) 

# Example: Perform addition and multiplication in a single line

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

#########End of Day 18#########

# Day 19 
# 10/06/2025
# class 19

# File Handling in Python
# File handling is a crucial aspect of programming that allows you to read from and write to files.
# In Python, file handling is done using built-in functions and methods that allow you to open, read, write, and close files.       
# Opening a file
file = open('example.txt', 'w')  # 'w' mode opens the file for writing (creates it if it doesn't exist)
# Writing to a file
file.write('Hello, World!\n')
# Closing a file
file.close()
# Reading from a file
file = open('example.txt', 'r')  # 'r' mode opens the file for reading
content = file.read()  # Read the entire content of the file
print(content)  # Output: Hello, World!
# Closing the file after reading
file.close()
# Using 'with' statement for file handling
with open('example.txt', 'a') as file:  # 'a' mode opens the file for appending
    file.write('Appending a new line.\n')  # Appending a new line to the file
# Reading the file again to see the appended content
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nAppending a new line.
# Working with file paths
import os
# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")
# Joining paths
file_path = os.path.join(current_directory, 'example.txt')
print(f"File Path: {file_path}")
# Checking if a file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
# Deleting a file
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted.")
else:
    print("File does not exist, cannot delete.")
# Creating a new file and writing multiple lines
with open('multi_line.txt', 'w') as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)  # Writing multiple lines to the file
# Reading the multi-line file
with open('multi_line.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Line 1\nLine 2\nLine 3\n
# Appending more lines to the multi-line file
with open('multi_line.txt', 'a') as file:
    file.write("Line 4\n")  # Appending a new line
# Reading the updated multi-line file
with open('multi_line.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Line 1\nLine 2\nLine 3\nLine 4\n
# Reading a file line by line
with open('multi_line.txt', 'r') as file:
    for line in file:  # Iterating through each line in the file
        print(line.strip())  # Output: Line 1\nLine 2\nLine 3\nLine 4\n (without extra newlines)
# Reading a file with a specific encoding       
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nAppending a new line.
# Handling file exceptions
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
# Writing binary data to a file
with open('binary_file.bin', 'wb') as file:  # 'wb' mode opens the file for writing in binary mode
    file.write(b'\x00\x01\x02\x03\x04')  # Writing binary data
# Reading binary data from a file
with open('binary_file.bin', 'rb') as file:  # 'rb' mode opens the file for reading in binary mode
    binary_content = file.read()  # Reading the binary content
    print(binary_content)  # Output: b'\x00\x01\x02\x03\x04'
# Working with CSV files
import csv
# Writing to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])  # Writing header
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
# Reading from a CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles']
# Working with JSON files
import json
# Writing to a JSON file
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)  # Writing JSON data with indentation
# Reading from a JSON file
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)  # Loading JSON data
    print(data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Working with XML files
import xml.etree.ElementTree as ET
# Writing to an XML file
root = ET.Element("data")
child1 = ET.SubElement(root, "person")
child1.set("name", "Alice")
child1.set("age", "30")
child1.set("city", "New York")
child2 = ET.SubElement(root, "person")
child2.set("name", "Bob")
child2.set("age", "25")
child2.set("city", "Los Angeles")
tree = ET.ElementTree(root)
tree.write("data.xml")  # Writing XML data to a file
# Reading from an XML file
tree = ET.parse('data.xml')  # Parsing the XML file
root = tree.getroot()  # Getting the root element
for person in root.findall('person'):
    name = person.get('name')
    age = person.get('age')
    city = person.get('city')
    print(f"Name: {name}, Age: {age}, City: {city}")  # Output: Name: Alice, Age: 30, City: New York
# Name: Bob, Age: 25, City: Los Angeles
# Working with file permissions
import stat
# Changing file permissions
def change_file_permissions(file_path, mode):
    os.chmod(file_path, mode)  # Changing the file permissions
    print(f"Permissions for {file_path} changed to {oct(mode)}")
# Example usage
change_file_permissions('example.txt', stat.S_IRUSR | stat.S_IWUSR)  # Read and write permissions for the owner
# Checking file permissions
def check_file_permissions(file_path):
    permissions = stat.filemode(os.stat(file_path).st_mode)  # Getting the file permissions
    print(f"Permissions for {file_path}: {permissions}")
# Example usage
check_file_permissions('example.txt')  # Checking the permissions of the file
# Working with temporary files
import tempfile
# Creating a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'This is a temporary file.\n')  # Writing to the temporary file
    temp_file_path = temp_file.name  # Getting the path of the temporary file
print(f"Temporary file created at: {temp_file_path}")
# Reading from the temporary file
with open(temp_file_path, 'r') as file:
    content = file.read()  # Reading the content of the temporary file
    print(content)  # Output: This is a temporary file.
# Deleting the temporary file
os.remove(temp_file_path)  # Deleting the temporary file
# Confirming deletion
if not os.path.exists(temp_file_path):
    print("Temporary file deleted successfully.")
else:
    print("Temporary file still exists.")
# Working with file locks
import fcntl
# Locking a file
def lock_file(file_path):
    with open(file_path, 'r+') as file:
        fcntl.flock(file, fcntl.LOCK_EX)  # Locking the file for exclusive access
        print(f"File {file_path} is locked.")
        # Perform file operations here
        fcntl.flock(file, fcntl.LOCK_UN)  # Unlocking the file
        print(f"File {file_path} is unlocked.")
# Example usage
lock_file('example.txt')  # Locking the example file
# Working with file encodings
def write_file_with_encoding(file_path, content, encoding='utf-8'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)  # Writing content with specified encoding
# Example usage
write_file_with_encoding('encoded_file.txt', 'Hello, World!', encoding='utf-8')  # Writing with UTF-8 encoding
# Reading a file with a specific encoding
def read_file_with_encoding(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()  # Reading content with specified encoding
        return content
# Example usage
content = read_file_with_encoding('encoded_file.txt', encoding='utf-8')  # Reading with UTF-8 encoding
print(content)  # Output: Hello, World!
# Working with file metadata
import os
def get_file_metadata(file_path):
    metadata = os.stat(file_path)  # Getting file metadata
    print(f"File: {file_path}")
    print(f"Size: {metadata.st_size} bytes")
    print(f"Last modified: {metadata.st_mtime}")
    print(f"Creation time: {metadata.st_ctime}")
    print(f"Permissions: {oct(metadata.st_mode)}")
# Example usage
get_file_metadata('example.txt')  # Getting metadata for the example file
# Working with file compression
import zipfile
def compress_files(file_paths, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for file in file_paths:
            zipf.write(file)  # Adding files to the zip archive
    print(f"Files compressed into {zip_file_name}")
# Example usage
compress_files(['example.txt', 'multi_line.txt'], 'compressed_files.zip')  # Compressing files into a zip archive
# Extracting files from a zip archive
def extract_files(zip_file_name, extract_to):
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zipf.extractall(extract_to)  # Extracting all files to the specified directory
    print(f"Files extracted to {extract_to}")
# Example usage
extract_files('compressed_files.zip', 'extracted_files')  # Extracting files from the zip archive
# Confirming extraction
import os
extracted_files_path = 'extracted_files'
if os.path.exists(extracted_files_path):
    print(f"Files extracted successfully to {extracted_files_path}.")
else:
    print("Extraction failed, directory does not exist.")
# Working with file globbing
import glob
def list_files_with_pattern(pattern):
    files = glob.glob(pattern)  # Listing files matching the specified pattern
    print(f"Files matching pattern '{pattern}':")
    for file in files:
        print(file)  # Output: List of files matching the pattern
# Example usage
list_files_with_pattern('*.txt')  # Listing all text files in the current directory
# Working with file timestamps
import time
def get_file_timestamp(file_path):
    timestamp = os.path.getmtime(file_path)  # Getting the last modified time of the file
    print(f"Last modified time for {file_path}: {time.ctime(timestamp)}")  # Converting timestamp to human-readable format
# Example usage     
get_file_timestamp('example.txt')  # Getting the last modified time for the example file
# Working with file system operations
import shutil
def copy_file(src, dst):
    shutil.copy(src, dst)  # Copying a file from source to destination
    print(f"File copied from {src} to {dst}")
# Example usage
copy_file('example.txt', 'example_copy.txt')  # Copying the example file
# Moving a file
def move_file(src, dst):
    shutil.move(src, dst)  # Moving a file from source to destination
    print(f"File moved from {src} to {dst}")
# Example usage
move_file('example_copy.txt', 'moved_example.txt')  # Moving the copied file
# Deleting a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  # Deleting the specified file
        print(f"File {file_path} deleted.")
    else:
        print(f"File {file_path} does not exist, cannot delete.")

######################

# create a text file

with open("demo.txt", "w") as f:
    f.write("Hello World! This is a test.")    #optional

# wring a file 
# repalce all the data i the file

#  1code

f = open("demo1.txt" , "w")
f = open("demo1.txt" , "a")                # append the data add it to the file
f.write("i want to learn a python as well as a javascript from tommorow")
f.write("\n then i will move to the react.js")      # append the data add it to the file 
f.close()

# readfile

f = open("demo1.txt", "r")
data = f.read(15)    # Read only first 9 characters from the file
print(data)
print(type(data))
f.close()          #  close a file

# line by line read a data line1 function have \n space whih is recognised by line 1 so there is space 

f = open("demo1.txt" , "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

f = open("demo.txt", "r")
for x in f:
    print(x)

# reading and writing

f = open("demo.txt", "r+")   # this is show i text file
f.write("This")
print(f.read())
f.close()         

# with  syntax
# read data by using with ther is no need to close fiel it auto cloases it

with open("demo1.txt", "r") as f:
    data = f.read()
    print(data) 

with open("demo.txt", "w") as f:
        f.write("new data")
        f.write("\n new data")

with open("demo.txt", "w") as file:
    file.write("\nHello, World!")
    print ("Content added Successfully!!")

file = open("demo.txt", "w")
file.write("This is an example.\n")
file.close()
print ("File closed successfully!!")

file = open("demo.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")

# READ files

# Open the file in read mode
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

f = open("demo.txt", "w")  
f.write("Woops! I have deleted the content!")  
f.close()

# open and read the file after writing
f = open("demo.txt", "r")  
print(f.read())

# Step 1: Create and write to a text file

with open("demo3.txt", "w") as f:
    f.write("Python is awesome\n")
    f.write("File handling is powerful\n")
    f.write("We are learning split function\n")

# Step 2: Read and split lines

with open("demo3.txt", "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()  # split by default on spaces
        print(words)

# Step 3: Create a new file and write the split words
with open("split_words.txt", "w") as new_file:
    for line in data:
        words = line.split()
        for word in words:
            new_file.write(word + "\n")  # write each word on a new line

# Step 4: Read the new file to verify

# try:
try:
    f = open("myfile2.txt", "x")
    print("File created!")
except FileExistsError:
    print("File already exists!")

f = open("myfile.txt", "w")
f.write("ashwini")

# in short
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# DElete the filed .txt
import os

# Remove a file
os.remove("demo3.txt")

# Day 19
# 10/06/2025
# class 19

cars = ["a", "b", "c" ]
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# accessing array

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# addinga array

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# remove array

cars = ["Ford", "Volvo", "BMW" ]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW" ]
cars.remove("Volvo")
print(cars)

numbers = [5, 3, 9, 1, 7 ]
numbers.sort()
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

original = [1, 2, 3, 4]
copied_list = original.copy()
original.append(5)
print("Original List:", original) 
print("Copied List:", copied_list)  

original = [1, 2, 3 ,4 , 5 ]
additional = [4, 5, 6 ,1 ,3]
original.extend(additional)
print("Extended List:", original)

# Day 19
# 10/06/2025
# class 19

cars = ["a", "b", "c" ]
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# accessing array

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# addinga array

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# remove array

cars = ["Ford", "Volvo", "BMW" ]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW" ]
cars.remove("Volvo")
print(cars)

numbers = [5, 3, 9, 1, 7 ]
numbers.sort()
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

original = [1, 2, 3, 4]
copied_list = original.copy()
original.append(5)
print("Original List:", original) 
print("Copied List:", copied_list)  

original = [1, 2, 3 ,4 , 5 ]
additional = [4, 5, 6 ,1 ,3]
original.extend(additional)
print("Extended List:", original)

####################################################################
# Day 19
# 10/06/2025
# class 19
# Try Except
# This code demonstrates the use of try-except blocks in Python to handle exceptions gracefully.
# It includes examples of catching specific exceptions and using a general exception handler.

# Example 1: Basic try-except block
try:
    print("Hello")
except Exception as e:
    print("An error occurred:", e)
# Example 2: Catching a specific exception
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
# Example 3: Catching multiple exceptions
try:
    x = int("Hello")
except (ValueError, TypeError) as e:
    print("An error occurred with value conversion:", e)
# Example 4: Using a general exception handler
try:
    x = 5 / 0
except Exception as e:
    print("An unexpected error occurred:", e)
# Example 5: Finally block
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
finally:
    print("This block always executes, regardless of an error.")
# Example 6: Using else with try-except
try:
    x = 5 / 1
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
else:
    print("Division successful, result is:", x)
# Example 7: Raising an exception               
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    result = divide(5, 0)
except ValueError as e:
    print("Error:", e)
# Example 8: Custom exception class
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error message")
except CustomError as e:
    print("Caught a custom error:", e)
# Example 9: Nested try-except blocks
try:
    try:
        x = int("Hello")
    except ValueError as e:
        print("Inner exception caught:", e)
    x = 5 / 0
except ZeroDivisionError as e:
    print("Outer exception caught:", e)
# Example 10: Using try-except with file operations
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("File not found:", e)
# Example 11: Handling multiple exceptions in a single except block
try:
    x = int("Hello")
    y = 5 / 0
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)
# Example 12: Using try-except with user input
try:
    user_input = int(input("Enter a number: "))
    print("You entered:", user_input)
except ValueError as e:
    print("Invalid input, please enter a valid number:", e)
# Example 13: Using try-except with a function call
def risky_function():
    return 1 / 0
try:
    risky_function()
except ZeroDivisionError as e:
    print("Caught an error in risky_function:", e)
# Example 14: Using try-except with a loop
numbers = [1, 2, 3, 0, 4]
for number in numbers:
    try:
        result = 10 / number
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Cannot divide by zero for number:", number, "Error:", e)
# Example 15: Using try-except with a context manager
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("An error occurred:", exc_value)
        print("Exiting the context")
try:
    with MyContextManager() as cm:
        print("Inside the context")
        x = 5 / 0  # This will raise an exception
except ZeroDivisionError as e:
    print("Caught an error in the context manager:", e)
# Example 16: Using try-except with assertions
try:
    assert 1 == 2, "This assertion will fail"
except AssertionError as e:
    print("Assertion error caught:", e)
# Example 17: Using try-except with a decorator 
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("An error occurred in the decorated function:", e)
    return wrapper
@error_handler
def risky_function():
    return 1 / 0
risky_function()
# Example 18: Using try-except with a generator
def generator_function():
    yield 1
    yield 2
    raise ValueError("An error occurred in the generator")
try:
    gen = generator_function()
    for value in gen:
        print("Value from generator:", value)
except ValueError as e:
    print("Caught an error from the generator:", e)
# Example 19: Using try-except with a class method
class MyClass:
    def method(self):
        raise RuntimeError("An error occurred in the class method")
try:
    obj = MyClass()
    obj.method()
except RuntimeError as e:
    print("Caught an error from the class method:", e)
# Example 20: Using try-except with a lambda function
try:
    risky_lambda = lambda x: 1 / x
    result = risky_lambda(0)
except ZeroDivisionError as e:
    print("Caught an error from the lambda function:", e)
# Example 21: Using try-except with a list comprehension
try:
    numbers = [1, 2, 0, 4]
    results = [10 / num for num in numbers]
except ZeroDivisionError as e:
    print("Caught an error in list comprehension:", e)
# Example 22: Using try-except with a while loop
try:
    count = 0
    while count < 5:
        if count == 3:
            raise ValueError("An error occurred at count 3")
        print("Count:", count)
        count += 1
except ValueError as e:
    print("Caught an error in the while loop:", e)
# Example 23: Using try-except with a for loop and exception handling
try:
    for i in range(5):
        if i == 2:
            raise IndexError("An error occurred at index 2")
        print("Index:", i)
except IndexError as e:
    print("Caught an error in the for loop:", e)
# Example 24: Using try-except with a function that raises an exception
def function_that_raises():
    raise KeyError("This is a key error")
try:
    function_that_raises()
except KeyError as e:
    print("Caught a key error:", e)
# Example 25: Using try-except with a function that handles exceptions
def function_with_exception_handling():
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        print("Handled division by zero:", e)
        return None
try:
    result = function_with_exception_handling()
    print("Result from function:", result)
except Exception as e:
    print("Caught an unexpected error:", e)

    ##################################################################

try:
    print(x)
except:
    print("An exception occurred")

# The try block raises an exception, so the except block is executed:
try:
    x="Swarup"
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#The try block does not raise any errors, so the else block is executed:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# The try block raises an exception, so the except block is executed:
# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except:
    print("Something went wrong. Please enter a valid number.")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a number.")
else:
    print("You entered age:", age)

try:
    fruits = ["apple", "banana", "mango"]
    print(fruits[8])  
except IndexError:
    print("That index is out of range!")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
else:
    print("Division successful! Result is:", result)
finally:
    print("This block always runs — thank you!")

    ##################################################


    # End of python Basics course in I tech. 
    # Course completed on 10/06/2025 By Ashwini Mam.
# Thank you for the course, I have learned a lot.
# The course has covered various topics in Python, including:
# 1. Basic syntax and data types
# 2. Control flow statements (if, for, while)
# 3. Functions and modules
# 4. File handling
# 5. Exception handling
# 6. Object-oriented programming
# 7. Lambda functions
# 8. List comprehensions
