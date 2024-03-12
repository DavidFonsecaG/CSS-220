# David Fonseca
# 3/12/2024
# CSS 220 Module 9
# Fibonacci

def fib(n):
    # user test for 0
    if n < 0:
        print("Value should be greater than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))



