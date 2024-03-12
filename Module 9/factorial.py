# David Fonseca
# 3/12/2024

# Factorial recursion example

def factRecursion(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n - 1)!
    else:
        return n * factRecursion(n - 1)
    
if __name__ == "__main__":
    print(factRecursion(5))
