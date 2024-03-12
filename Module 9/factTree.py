from turtle import *

# David Fonseca
# 3/12/2024
# Factral Tree example (T-tree)

# change speed
speed('fastest')
# Reorient the trunk of the tree to vertical
rt(-90)
# branching amgle for the base
angle = 30

# function for the Y-tree
# size = lenght of first line. depth = number of iterations
def yTree(size, depth):
    if depth > 0:
        # colormode
        colormode(255)

        # add in color
        pencolor(0, 255 // depth, 0)

        # draw the base (a vertical line)
        fd(size)
        rt(angle)

        # recursive call to build right branches
        yTree(size * 0.9, depth - 1)

        # rotates left 60 degrees
        lt(2 * angle)

        # recursive call to build left branches
        yTree(size * 0.8, depth - 1)

        # add in color
        pencolor(0, 255 // depth, 0)

        # reset position
        rt(angle)
        fd(-size)

if __name__ == "__main__":
    yTree(80, 8)
    Screen().exitonclick()
