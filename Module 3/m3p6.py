# David Fonseca
# 1/30/2024
# CSS-220 Module 3 In-Class activity

# Write a Python program to check if a set is a subset of another set. 
# Use sets x = {apple, mango}, y = {mango, orange}, and z = {mango}. 
# This program should use the issubset() method.

# Create sets x, y, and z
x = set(["apple", "mango"])
y = set(["mango", "orange"])
z = set(["mango"])
print(x)
print(y)
print(z)

print(f"Is x a subset of y?")
print(x.issubset(y))

print(f"Is x a subset of z?")
print(x.issubset(z))

print(f"Is y a subset of x?")
print(y.issubset(x))

print(f"Is y a subset of z?")
print(y.issubset(z))

print(f"Is z a subset of x?")
print(z.issubset(x))

print(f"Is z a subset of y?")
print(z.issubset(y))
