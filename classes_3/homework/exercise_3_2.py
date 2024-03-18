# Make a loop over integer numbers from 1 to 40.
# If x is divided by 5 then print a message 'x is divided by 5'.
# If x is divided by 7 then print a message 'x is divided by 7'.
# If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
# Skip x = 13.
# If x is not divided by 5 and x is not divided by 7
# then print a message 'x is not important'.
# Prepare two solutions with 'while' and 'for' loops.
#

startNumber = 1
endNumber = 40

print("Solution no. 1")

for number in range(startNumber, endNumber + 1):
    if number == 13:
        continue

    divisibleBy5 = (number % 5 == 0)
    divisibleBy7 = (number % 7 == 0)

    if divisibleBy5 and divisibleBy7:
        print(number," is divided by 5 and 7")
        continue
    if divisibleBy5:
        print(number," is divided by 5")
        continue
    if divisibleBy7:
        print(number," is divided by 7")
        continue

    print(number," is not important")

print("\n\nSolution no. 2")

number = startNumber
while number <= endNumber:
    currentNumber = number
    number += 1

    if currentNumber == 13:
        continue

    divisibleBy5 = (currentNumber % 5 == 0)
    divisibleBy7 = (currentNumber % 7 == 0)

    if divisibleBy5 and divisibleBy7:
        print(currentNumber," is divided by 5 and 7")
        continue
    if divisibleBy5:
        print(currentNumber," is divided by 5")
        continue
    if divisibleBy7:
        print(currentNumber," is divided by 7")
        continue

    print(currentNumber," is not important")