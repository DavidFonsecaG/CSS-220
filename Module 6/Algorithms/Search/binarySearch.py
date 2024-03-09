# David Fonseca
# 3/8/2024

# Binary Search Algorithm

def binarySearch(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2

        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == '__main__':
    arr = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
    x = int(input("Enter a number to search >> "))

    index = binarySearch(arr, x)
    if index != -1:
        print(f"Number {x} is at {index} index.")
    else:
        print(f"Number {x} not found.")

