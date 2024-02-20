# David Fonseca
# 2/20/2024
# CSS 220 Module 6

# Bubble sort

numberList = [99, 5, 30, 15, 29, 63, 7]
nLenght = len(numberList)
iterations = 0

def bubbleSort(numberList, nLenght, iterations):
    for i in range(nLenght):
        for j in range(0, nLenght-i-1):
            iterations += 1
            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]
            print(numberList)
    print("Number of Iterations: ", iterations)


print("Pre Sort: ", numberList)
bubbleSort(numberList, nLenght, iterations)
print("Bubble Sort: ", numberList)