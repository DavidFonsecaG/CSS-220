# David Fonseca
# 2/20/2024
# CSS 220 Module 6

# Binary Search Algorithm

numberList = [1, 4, 6, 9, 20, 40, 64, 65, 70, 74, 90, 102, 105, 120, 200, 235, 236, 237, 400, 500, 756, 1000]
number = 500
l = 0
nLenght = len(numberList)
iterations = 0

def bSearch(numberList, number, nLenght, l, iterations):
    while l <= nLenght:
        iterations += 1
        mid = l + (nLenght - l) // 2

        if numberList[mid] == number:
            return mid, iterations
        elif numberList[mid] < number:
            l = mid + 1
        else:
            nLenght = mid - 1

i, ite = bSearch(numberList, number, nLenght, l, iterations)
print("The number is at index: ", i)
print("Total iterations: ", ite)