# David Fonseca
# 2/27/2024
# CSS 220 Module 6

# Find the smallest and largest numbers in the following unsorted list: [4, 2, 7, 3, 8, 5]

def findSmallestLargest(arr, s, l, N):
    for x in range(0, N):
        if arr[x] < s:
            s = arr[x]
        if arr[x] > l:
            l = arr[x]
    return s, l


if __name__ == "__main__":
    arr = [4, 2, 7, 3, 8, 5]

    smallest, largest = findSmallestLargest(arr, 1000, -1000, len(arr))
    print("The smallest value is: ", smallest)
    print("The largest value is: ", largest)

