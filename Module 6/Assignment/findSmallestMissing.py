# David Fonseca
# 2/27/2024
# CSS 220 Module 6

# Find the smallest missing element from the following sorted list: [1, 2, 3, 5, 6, 7, 9]

def findSmallestMissing(arr, N):
    for x in range(0, N-1):
        if arr[x+1] - arr[x] > 1:
            return arr[x] + 1
    return -1

if  __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 7, 9]

    sMissing = findSmallestMissing(arr, len(arr))
    if sMissing == -1:
        print("Not missing values in the list")
    else:
        print("The smallest missing value is: ", sMissing)
        
    