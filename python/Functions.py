# Day 17
# 4/06/25
# class 17

# function
# to define a function def is used

def function():
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
