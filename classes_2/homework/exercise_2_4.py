# (a) Find Unicode code points (int) for all characters of your name.
# Example: "Andrzej" --> [65, 110, 100, 114, 122, 101, 106]
#
# (b) Prepare the periodic table (ten elements) as a list
# pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
# Use pt to print a table (3 right + 20 left + 6 center + 10 right)
# +---+--------------------+------+----------+
# |No.|Name (en)           |Symbol|Weight (u)|
# +---+--------------------+------+----------+
# |  1|Hydrogen            |  H   |         1|
# |  2|Helium              |  He  |         4|
# |   | ...                |      |          |
# +---+--------------------+------+----------+
# Hint: use the for loop:
# for (n, name, symbol, weight) in pt:
#     # use variables (n, name, symbol, weight) to create a proper line


# a)
# name: Mateusz
print("\n1st part of the exercise:\n")

name = "Mateusz"
listOfLettersIds = []

for letter in name:
    listOfLettersIds.append(ord(letter))

print("Code points of letters in name", name, "are shown below:", listOfLettersIds)

# b)
print("\n2nd part of the exercise:\n")
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3,"Hydrogen2","H2",1), (4,"Hydrogen3","H34",1), (5,"Hydrogen4","H4",1), (6,"Hydrogen5","H5",1),
      (7,"Hydrogen6","H6",1), (8,"Hydrogen7","H7",1), (9,"Hydrogen8","H8",1), (10,"Hydrogen9","H9",1)]

mainSeparatorLine = "+---+--------------------+------+----------+"
headingLine = "|No.|Name (en)           |Symbol|Weight (u)|"

maxSizeOfId = 3
maxSizeOfName = 20
maxSizeOfSymbol = 6
maxSizeOfWeight = 10

print(mainSeparatorLine)
print(headingLine)
print(mainSeparatorLine)
for elements in pt:
    n, name, symbol, weight = elements
    if (len(str(n)) > maxSizeOfId) or (len(str(name)) > maxSizeOfName) or (len(str(symbol)) > maxSizeOfSymbol) or (len(str(weight)) > maxSizeOfWeight):
        print("|Too long infomation. Resize your table    |")
        continue
    generatedRow = "|"
    numberOfBlankSpaces = maxSizeOfId - len(str(n))
    generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
    generatedRow += str(n)
    generatedRow += "|"
    numberOfBlankSpaces = maxSizeOfName - len(str(name))
    generatedRow += str(name)
    generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
    generatedRow += "|"
    numberOfBlankSpaces = maxSizeOfSymbol - len(str(symbol))
    if numberOfBlankSpaces % 2 == 0:
        numberOfBlankSpaces = int(numberOfBlankSpaces / 2)
        generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
        generatedRow += str(symbol)
        generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
    else:
        numberOfBlankSpaces = int(numberOfBlankSpaces / 2)
        generatedRow += "".join([" " for i in range(numberOfBlankSpaces+1)])
        generatedRow += str(symbol)
        generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
    generatedRow += "|"
    numberOfBlankSpaces = maxSizeOfWeight - len(str(weight))
    generatedRow += "".join([" " for i in range(numberOfBlankSpaces)])
    generatedRow += str(weight)
    generatedRow += "|"
    print(generatedRow)
     # use variables (n, name, symbol, weight) to create a proper line
print(mainSeparatorLine)