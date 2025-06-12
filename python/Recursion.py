# Day 18
# 9/06/2025
# class 18

# when a function call itself called  recursion

def show(n):
    if n == 0:
        return

    print(n)
    print("end")

    show(n - 1)  #function calls itself with a smaller value (n - 1),
show(9)

def fact(n):
    if(n == 1 or n == 0):    #This function keeps calling itself with n-1 until it hits the base case (n == 1 or n == 0).
        return 1
    return fact(n-1) * n

print(fact (4)) 

# n! = n × (n-1) × (n-2) × ... × 1
# fact(4)
# = fact(3) * 
# fact(3)
# = fact(2) * 
# fact(2)
# = fact(1) * 2
# fact(1) 
# # = 1  ← base case
# fact(2) = fact(1) * 2 = 1 * 2 = 2
# fact(3) = fact(2) * 3 = 2 * 3 = 6
# fact(4) = fact(3) * 4 = 6 * 4 = 24

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

#This is the recursive call, because the function tri_recursion 
# is calling itself with a smaller value: k - 1.

# T(n) = n + (n - 1) + (n - 2) + ... + 1
# tri_recursion(1) = 1 + 0 = 1 → prints 2
# tri_recursion(2) = 2 + 1 = 3 → prints 3
# tri_recursion(3) = 3 + 3 = 6 → prints 6
# tri_recursion(4) = 4 + 6 = 10 → prints 10
# tri_recursion(5) = 5 + 10 = 15 → prints 15
# tri_recursion(6) = 6 + 15 = 21 → prints 21
