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
marks5 = 55

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