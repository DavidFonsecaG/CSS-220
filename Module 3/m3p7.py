# David Fonseca
# 1/30/2024
# CSS-220 Module 3 In-Class activity

# Write a Python program to check if two given sets have no elements in common. 
#Use sets x = {1, 2, 3, 4}, y = { 4, 5, 6, 7}, and z = {8}. 
# This program should use the isdisjoint() method.

# Create sets x, y, and z
x = set([1, 2, 3, 4])
y = set([4, 5, 6, 7])
z = set([8])
print(x)
print(y)
print(z)

# Chekc if sets are disjoint
print("Are x and y disjoint?")
print(x.isdisjoint(y))

print("Are x and z disjoint?")
print(x.isdisjoint(z))

print("Are y and y disjoint?")
print(y.isdisjoint(z))