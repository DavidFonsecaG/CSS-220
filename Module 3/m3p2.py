# David Fonseca
# 1/30/2024
# CSS-220 Module 3 In-Class activity

# Write a Python program to add members to a set.
# Start off with an empty set. 
# Add “Red” to the set. 
# Update the set with “Blue” and “Green”.

# Create an empty set
colorSet = set()
print(colorSet)

# Add “Red” to the set. 
colorSet.add("Red")
print("colorSet = ", colorSet)

# Update the set with “Blue” and “Green”.
colorSet.update(["Blue", "Green"]) # Allows you to add multiple numbers
print("colorSet = ", colorSet)

