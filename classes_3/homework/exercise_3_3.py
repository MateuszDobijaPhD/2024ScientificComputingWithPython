# Create the following variables:
# n = 2022
# x = math.pi   # save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"   # 'book' in English
# Write the variables to a text file "vars.txt",
# one line for one variable.
# Print the file content on the screen.

import math

n = 2022
x = math.pi                                                             # save with 5 digits after a dot (import 'math' first!)
word = "Python"
polish = "książka"                                                      # 'book' in English

with open('vars.txt', 'w') as outfile:                                  # outfile will be closed
    outfile.write("{}\n{}\n{}\n{}\n".format(n, x, word, polish))  # 4 lines

with open('vars.txt', 'r') as infile:                                   # infile will be closed
    text = infile.read()

print(text)