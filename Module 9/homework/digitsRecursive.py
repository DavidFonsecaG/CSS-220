# David Fonseca
# 3/17/2024

def digits(n):
    # base case
    if n < 10:
        return 1
    else:
        return 1 + digits(n // 10)

if __name__ == "__main__":
    print(digits(15))

