# David Fonseca
# 3/17/2024

# Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively

def sum(x):
	print(x) 
	# base case
	if x == 1:
		return 1
	else:
    # recursively compute and return
		return x + sum(x-1)


print(sum(10))
