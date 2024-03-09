# David Fonseca
# 3/7/2024

# Linear Search Algorithm
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

if __name__ == '__main__':
    arr = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
    x = int(input("Enter a number to search >> "))

    index = linearSearch(arr, x)
    if index != None:
        print(f"Number {x} is at {index} index.")
    else:
        print(f"Number {x} not found.")

