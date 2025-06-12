# Day 15 
# 27/05/25.  ex date
# class 15

# 3/06/25

# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

from typing import Dict


thisdict =	{
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
"name" : "any",
"subject" : ["python" , "mern " , "c" , "c++" ],
"topics" : ( "dict ","tuple" , "list" ),
"age" : 78 ,
"marks" : 94.4
}
print(info)

# add dict

info [ "name"]= "any23455"  # it will overwrite  name property
info [ "age"] = 45
print(info)

marks = {"Savita":67, "any":88, "Laxman":91, "David":49}
print ("Initial dictionary: ", marks)

marks['Kavya'] = 58
print ("Dictionary after new addition: ", marks)

marks = {"Savita":67, "Imtiaz":88  }
print ("Initial dictionary: ", marks)

marks.update({'Kavya': 58, 'Mohan': 98})
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
    "name": "ashwini hajre",
    "subject" :{
        "python" : 45,
        "mern" : 23 ,
        "math" :22
    } 
}
print (student.keys())

# casting in keys
print(list(student.keys()))

Dict.values()
print(student.values())

Dict.item()  # output  as a tuples 
print(student.items())

pairs = list(student.items())
print(pairs[0])

print(student.get("name")) 

# it should not get error
# update method

student = {
    "name": "ashwini hajre",
    "subject" :{
        "python" : 45,
        "mern" : 23 ,
        "math" :22
    } 
}
student.update({"city" : "delhi"})
print (student)

student = {
    "name": "ashwini hajre",
    "subject" :{
        "python" : 45,
        "mern" : 23 ,
        "math" :22
    } 
}

new_dict = {"city" : "delhi" , "age" : "43"}
student.update(new_dict)
print (student)

d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
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