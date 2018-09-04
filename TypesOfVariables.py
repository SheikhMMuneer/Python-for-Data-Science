import math

#  Integer Type
x = 2
print(x)
print(type(x))

#  Float / Double Type
y = 2.5
print(y)
print(type(y))

# String
a = "hello"
b = '2'
print(a)
print(type(a))
print(b)
print(type(b))

# Logical
q1 = True
print(q1)
print(type(q1))

# Working with Variables
A = 10
B = 5
C = A + B
D = B / A

print(C)
print(D)

sqr = math.sqrt(100)
sqr_A = math.sqrt(A)
print("Square Root" ,sqr)
print(round(sqr_A))

greeting = "Hello"
name = "Bob"
message = greeting + " " + name
print("Message : " + message)

#Boolean / Logical
result = 4 < 5
print("True-False" ,result)
print(type(result))

print(" 10 > 100" , 10 > 100)
print("4 == 5", 4 == 5)
print("10 > 100" , 10 > 100)

result2 = not(5 > 1)  # means 5 is not greater than 1  (5 !=> 1) is wrong not(5 > 1)
print(result2)

# ==
# != <>
# <
# >
# <=
# >=
# and
# or
# not


result_or = (result or result2)
print("result_or : " , result_or)

result_and = (result and  result2)
print("result_and :" ,result_and)