# David Fonseca
# 3/9/2024

# Jump Search Algorithm
import math

def jumpSearch(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
        
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
        
    if arr[prev] == x:
        return prev
    
    return -1

if __name__ == '__main__':
    arr = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
    x = int(input("Enter a number to search >> "))

    index = jumpSearch(arr, x)
    if index != -1:
        print(f"Number {x} is at index {index}.")
    else:
        print(f"Number {x} not found.")

