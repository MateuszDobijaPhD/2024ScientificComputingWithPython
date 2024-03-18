# For a given word (you may use your name), print it in squares.
# If word = "Python", then the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+

word = input("Please type some word: ")

borderLine = ""
midLine = ""

if not word:
    print("Your word is empty!")

for letter in word:
    borderLine += "+"
    midLine += "|"

    borderLine += "---"
    midLine += " " + letter + " "

borderLine += "+"
midLine += "|"

print(borderLine)
print(midLine)
print(borderLine)