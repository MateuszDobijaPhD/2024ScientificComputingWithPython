#Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum() and range()].
startNumber = 1
endNumber = 2021
step = 2
result = 0

for number in range(startNumber, endNumber+1, step):
    result += number * number

print("Result:", result)
