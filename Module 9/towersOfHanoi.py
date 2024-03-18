# David Fonseca
# 3/12/2024
# Towers of hanoi

# def TowersOfHanoi(n , r1, r3, r2): 
#     if n == 1:
#         print("Move disk 1 from rod", r1,"to rod", r3)
#         return
#     else:
#         TowersOfHanoi(n-1, r1, r2, r3) 
#         print("Move disk",n,"from rod", r1, "to rod", r3)
#         TowersOfHanoi(n-1, r2, r3, r1)

# TowersOfHanoi(3,"A","C","B")

def xfunction(n):
    if n == 1:
        return 1
    else:
        return n + xfunction(n - 1)

print(xfunction(4))