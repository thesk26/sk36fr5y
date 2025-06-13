# Day 19
# 10/06/2025
# class 19

cars = ["a", "b", "c" ]
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# accessing array

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# addinga array

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# remove array

cars = ["Ford", "Volvo", "BMW" ]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW" ]
cars.remove("Volvo")
print(cars)

numbers = [5, 3, 9, 1, 7 ]
numbers.sort()
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

original = [1, 2, 3, 4]
copied_list = original.copy()
original.append(5)
print("Original List:", original) 
print("Copied List:", copied_list)  

original = [1, 2, 3 ,4 , 5 ]
additional = [4, 5, 6 ,1 ,3]
original.extend(additional)
print("Extended List:", original)

