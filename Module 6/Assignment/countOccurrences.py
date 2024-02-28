# David Fonseca
# 2/27/2024
# CSS 220 Module 6

# Count the number of occurrences of the number 7 in 
# the following sorted list: [1, 2, 2, 2, 5, 7, 7, 7, 8, 9]

def countOccurrences(arr, x, N, counter=0):
    for i in range(0, N):
        if arr[i] == x:
            counter += 1
    return counter

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 5, 7, 7, 7, 8, 9]
    x = 7

    result = countOccurrences(arr, x, len(arr))
    if result == 0:
        print(f"The number {x} is not in the list")
    else:
        print(f"The number {x} occurs {result} times")