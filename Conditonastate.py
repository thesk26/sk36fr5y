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

# Real shorthand properties of if else
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
if a > b and c > a:print("Both conditions are True")

a = 200
b = 33
c = 500
if a>b or a == c:print("At least one of the conditions is True")

a = 33
b = 200
if not a > b: print("a is NOT greater than b")

