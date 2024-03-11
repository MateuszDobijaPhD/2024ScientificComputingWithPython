# Create a long positive integer. Find the number of zeros. Hint: change the number to a string.

positiveInteger = 10203300658098
positiveIntegerInString = str(positiveInteger)

# version 1
numberOfZeroes = 0

for sign in positiveIntegerInString:
    if sign == "0":
        numberOfZeroes += 1

print("Solution no. 1. Number of zeroes in integer number", positiveInteger,"equals to", numberOfZeroes)

# version 2
print("Solution no. 2. Number of zeroes in integer number", positiveInteger,"equals to", positiveIntegerInString.count('0'))
