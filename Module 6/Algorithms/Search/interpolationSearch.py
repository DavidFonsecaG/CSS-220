# David Fonseca
# 3/9/2024

# Interpolation Search Algorithm
import math

def interpolationSearch(arr, low, high, x):

    if low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            return interpolationSearch(arr, pos + 1, high, x)
        else:
            return interpolationSearch(arr, low, pos - 1, x)

    return -1

if __name__ == '__main__':
    arr = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
    x = int(input("Enter a number to search >> "))

    index = interpolationSearch(arr, 0, len(arr)-1, x)
    if index != -1:
        print(f"Number {x} is at index {index}.")
    else:
        print(f"Number {x} not found.")

