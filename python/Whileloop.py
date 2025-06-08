
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


