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