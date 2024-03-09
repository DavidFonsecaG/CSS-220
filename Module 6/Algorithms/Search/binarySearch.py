# 3/8/2024
# David Fonseca

# Binary Search Algorithm

def binarySearch(array, number):
    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2

        if number == array[mid]:
            return mid
        elif number > array[mid]:
            l = mid + 1
        else:
            r = mid - 1

if __name__ == '__main__':
    array = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
    number = int(input("Enter a number to search >> "))

    index = binarySearch(array, number)
    if index != None:
        print(f"Number {number} is at {index} index.")
    else:
        print(f"Number {number} not found.")

