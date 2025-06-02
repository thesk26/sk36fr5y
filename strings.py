# Day 5 Of Python learning.
# 6/05/2025
# class 5

str1 = 'The '
str2 = "Vehicle"

str3 = '''Dr.'''

str4 = """Dk"""

print(str1)
print (str2)
print(str3)
print(str4)

# concaniate meean addition
# without space add hotil
final_str = str1 + str2 +str3 +str4
print(final_str)
# adding with space 
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
# indexing giving posiotion of no. giving in square bracket 
b = "Hello, sdk!"
print(b[ 3])

# slice of string
# positive index stars from 0
b = "Hello, python!"
print(b[ 7:3])

c = "Hello, python!"
print(c[:5])

# negative slice. starts from -1 

str = "apple"

print(str[-2:-4])
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
print(a.upper())

# lowercase

a = "Hello, sdk!"
print(a.lower())

# repalce

a = "swarup, kadam!"
print(a.replace("swarup", "krishna"))

a= "swa"
print(a.replace("swa" , "kri"))

# whitespace remove

a = "      Hello, sdk! " # remove space starting and ending not mid 
print(a)

a = "   Hello,swarup! "
print(a.strip())   # strip is method but remove blank space from front and back

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
c = a + " " + b  # add with space 
print(c)

