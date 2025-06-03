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
