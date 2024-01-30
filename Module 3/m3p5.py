# David Fonseca
# 1/30/2024
# CSS-220 Module 3 In-Class activity

# Write a Python program to create set difference. 
# Use sets x = {apple, mango} and y = {mango, orange}.

# Create sets x and y
x = set(["apple", "mango"])
y = set(["mango", "orange"])
print(x)
print(y)

# Check for an intersection
a = x & y
print("Intersection = ", a)

# Perform difference of x and y
b = x - y
print("Difference = ", b)
z = y - x
print("Difference = ", z)
c = z | b
print("The real difference = ", c)

