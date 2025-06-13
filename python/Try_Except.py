# Day 19
# 10/06/2025
# class 19
# Try Except
# This code demonstrates the use of try-except blocks in Python to handle exceptions gracefully.
# It includes examples of catching specific exceptions and using a general exception handler.

# Example 1: Basic try-except block
try:
    print("Hello")
except Exception as e:
    print("An error occurred:", e)
# Example 2: Catching a specific exception
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
# Example 3: Catching multiple exceptions
try:
    x = int("Hello")
except (ValueError, TypeError) as e:
    print("An error occurred with value conversion:", e)
# Example 4: Using a general exception handler
try:
    x = 5 / 0
except Exception as e:
    print("An unexpected error occurred:", e)
# Example 5: Finally block
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
finally:
    print("This block always executes, regardless of an error.")
# Example 6: Using else with try-except
try:
    x = 5 / 1
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
else:
    print("Division successful, result is:", x)
# Example 7: Raising an exception               
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    result = divide(5, 0)
except ValueError as e:
    print("Error:", e)
# Example 8: Custom exception class
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error message")
except CustomError as e:
    print("Caught a custom error:", e)
# Example 9: Nested try-except blocks
try:
    try:
        x = int("Hello")
    except ValueError as e:
        print("Inner exception caught:", e)
    x = 5 / 0
except ZeroDivisionError as e:
    print("Outer exception caught:", e)
# Example 10: Using try-except with file operations
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("File not found:", e)
# Example 11: Handling multiple exceptions in a single except block
try:
    x = int("Hello")
    y = 5 / 0
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)
# Example 12: Using try-except with user input
try:
    user_input = int(input("Enter a number: "))
    print("You entered:", user_input)
except ValueError as e:
    print("Invalid input, please enter a valid number:", e)
# Example 13: Using try-except with a function call
def risky_function():
    return 1 / 0
try:
    risky_function()
except ZeroDivisionError as e:
    print("Caught an error in risky_function:", e)
# Example 14: Using try-except with a loop
numbers = [1, 2, 3, 0, 4]
for number in numbers:
    try:
        result = 10 / number
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Cannot divide by zero for number:", number, "Error:", e)
# Example 15: Using try-except with a context manager
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("An error occurred:", exc_value)
        print("Exiting the context")
try:
    with MyContextManager() as cm:
        print("Inside the context")
        x = 5 / 0  # This will raise an exception
except ZeroDivisionError as e:
    print("Caught an error in the context manager:", e)
# Example 16: Using try-except with assertions
try:
    assert 1 == 2, "This assertion will fail"
except AssertionError as e:
    print("Assertion error caught:", e)
# Example 17: Using try-except with a decorator 
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("An error occurred in the decorated function:", e)
    return wrapper
@error_handler
def risky_function():
    return 1 / 0
risky_function()
# Example 18: Using try-except with a generator
def generator_function():
    yield 1
    yield 2
    raise ValueError("An error occurred in the generator")
try:
    gen = generator_function()
    for value in gen:
        print("Value from generator:", value)
except ValueError as e:
    print("Caught an error from the generator:", e)
# Example 19: Using try-except with a class method
class MyClass:
    def method(self):
        raise RuntimeError("An error occurred in the class method")
try:
    obj = MyClass()
    obj.method()
except RuntimeError as e:
    print("Caught an error from the class method:", e)
# Example 20: Using try-except with a lambda function
try:
    risky_lambda = lambda x: 1 / x
    result = risky_lambda(0)
except ZeroDivisionError as e:
    print("Caught an error from the lambda function:", e)
# Example 21: Using try-except with a list comprehension
try:
    numbers = [1, 2, 0, 4]
    results = [10 / num for num in numbers]
except ZeroDivisionError as e:
    print("Caught an error in list comprehension:", e)
# Example 22: Using try-except with a while loop
try:
    count = 0
    while count < 5:
        if count == 3:
            raise ValueError("An error occurred at count 3")
        print("Count:", count)
        count += 1
except ValueError as e:
    print("Caught an error in the while loop:", e)
# Example 23: Using try-except with a for loop and exception handling
try:
    for i in range(5):
        if i == 2:
            raise IndexError("An error occurred at index 2")
        print("Index:", i)
except IndexError as e:
    print("Caught an error in the for loop:", e)
# Example 24: Using try-except with a function that raises an exception
def function_that_raises():
    raise KeyError("This is a key error")
try:
    function_that_raises()
except KeyError as e:
    print("Caught a key error:", e)
# Example 25: Using try-except with a function that handles exceptions
def function_with_exception_handling():
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        print("Handled division by zero:", e)
        return None
try:
    result = function_with_exception_handling()
    print("Result from function:", result)
except Exception as e:
    print("Caught an unexpected error:", e)

    ##################################################################

try:
    print(x)
except:
    print("An exception occurred")

# The try block raises an exception, so the except block is executed:
try:
    x="Swarup"
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#The try block does not raise any errors, so the else block is executed:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# The try block raises an exception, so the except block is executed:
# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except:
    print("Something went wrong. Please enter a valid number.")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a number.")
else:
    print("You entered age:", age)

try:
    fruits = ["apple", "banana", "mango"]
    print(fruits[8])  
except IndexError:
    print("That index is out of range!")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
else:
    print("Division successful! Result is:", result)
finally:
    print("This block always runs — thank you!")