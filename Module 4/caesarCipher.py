# David Fonseca
# 2/6/2024

# Module 4 - In class activity
# Encodes a message using the Caesars' Cipher

message = "ABCDEFGHIJKLMNOPPQRSTUVWXYZ"
LETTERS = 'ABCDEFGHIJKLMNOPPQRSTUVWXYZ'

for x in range(len(LETTERS)):
    encoded = ''
    for y in message:
        if y in LETTERS:
            n = LETTERS.find(y)
            n = n - x
            if n < 0:
                n = n + len(LETTERS)
            encoded = encoded + LETTERS[n]
        else:
            encoded = encoded + y
    print(f"Shift key {x}: {encoded}")
