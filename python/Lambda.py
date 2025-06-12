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