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