# 2. Assignment operators
# Assignment operators are used to assign values to variables: 
# (=,+=,-=,*=,/=,//=,&=,^=,>>=,<<=,:=)\

# 1. =
x=2
print(x)

# 2. +=           add with num and x value  
# method 1
num = 23       
num = num + 26 
print(num)
# method 2
num = 51
num += 45
print("num:",num)

# 3. -=          subtract with num and x value 
# method 1
num = 230       
num = num - 60 
print(num)
# method 2
num = 510
num -= 450
print("num:",num)

# 4. *=         multiply with num and x value  
# method 1
num = 15       
num = num * 6 
print(num)
# method 2
num = 5
num *= 5
print("num:",num)

# 5. /=         div. with num and x value 
# method 1
num = 20       
num = num / 4 
print(num)
# method 2
num = 50
num /= 5
print("num:",num)

# 6. %=        mod gives remainder 
# method 1
num = 23       
num = num & 2 
print(num)
# method 2
num = 51
num %= 4
print("num:",num)

# 7. //=      It gives ans. without decimal          
# method 1
num = 200       
num = num // 26 
print(num)
# method 2
num = 510
num //= 45
print("num:",num)

# 8. **=      something power something  
# method 1
num = 3       
num = num ** 2 
print(num)
# method 2
num = 5
num **= 4
print("num:",num)

# 9. &=   (and)           use from truth table 
# method 1           gives value in 0 and 1 
num = 3            # T F -->result (1)
num = num & 6      # 0 0 -->0
print(num)         # 0 1 -->0 
# method 2         # 1 0 -->0
num = 5            # 1 1 -->1
num &= 4                                               # 8bit structure : 128 64 32 16 8 4 2 1 
print("num:",num)                                                   # 1.   0  0  0  0  0 0 0 1
                                                                    # 2.                 0 1   
# 10. |=          (Or)                          Binary digits       # 3.                 0 1 1
# method 1           # T F -->result                                # 4.                 1  
num = 2              # 0 0 -->0                                     # 5.                 1   1 
num = num | 6        # 0 1 -->1                                     # 6.                 1 1
print(num)           # 1 0 -->1                                     # 7.                 1 1 1
# method 2           # 1 1 -->1                                     # 8.               1 
num = 1                                                             # 9.               1     1
num |= 5                                                            # 10.              1   1  
print("num:",num)                                                   # 11.              1   1 1
                                                                    # 12.              1 1  
# 11. ^=   (x-or)                                                   # 13.              1 1   1
# method 1          # T F -->result                                 # 14.              1 1 1
num = 2             # 0 0 -->0                                      # 15.              1 1 1 1
num = num ^ 6       # 0 1 -->1                                      # 16.            1
print(num)          # 1 0 -->1                                      # 17.            1       1
# method 2          # 1 1 -->0                                      # 18.            1     1
num = 1                                                             # 19.            1     1 1
num ^= 4                                                            # 20.            1   1
print("num:",num)                                                   # 21.            1   1   1
                                                #   this digits are use to calaulate (&,|,^) 
# eg. x=5   x &= 3     # print(x)  result is 1   # reson binary no. of 5 is 0101 and BN 3 is 0011 as a reult 0101
                                                     # 0011  = 0001 (using truth table)
# 12. >>=    sign indiactes righshift ope.                                   
# method 1                                          
num = 7                                  # eg. x=5          
num = num >> 8                           #  x >>= 3  x = x>>3 (x= 5>>3)       5= 0101 
print(num)                                                                 #  3= 0011       bn of 5 shifts right side of bn of 3                      
# method 2                                                                 #     0000   result = 0        
num = 7
num >>= 9
print("num:",num)

# 13. <<=  sign indicates leftshift ope.                 
# method 1                                    # eg. x=5                           32 16 8421 
num = 23                                      #  x <<= 3  x = x<<3 (x= 5<<3)   5=       0101
num = num << 26                                                              # 3=       0011       bn of 5 shifts left side of bn of 3
print(num)                                                                   #     1  0 1000   result = 32+8=32
# method 2
num = 51
num <<= 45
print("num:",num)

# comparison operator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

    # Equal to
print("Is num1 equal to num2?", num1 == num2)

    # Not equal to
print("Is num1 not equal to num2?", num1 != num2)

    # Greater than
print("Is num1 greater than num2?", num1 > num2)

    # Less than
print("Is num1 less than num2?", num1 < num2)

    # Greater than or equal to
print("Is num1 greater than or equal to num2?", num1 >= num2)

    # Less than or equal to
print("Is num1 less than or equal to num2?", num1 <= num2)

