# Let S be a long string (many lines).
#
# Find the number of black characters in S [not whitespace, see the method S.isspace()].
#
# Find the number of words in S (a word is a sequence of black characters).
#
# Find the longest word in S.
#
# Sort words from S according to (1) the lexicographic order, (2) the length.

S = ("Ala ma kota. "
     "Ala ma psa. "
     "Ala ma rybki. "
     "Ala ma kucyka. ")

# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
spaceCharacter = ' '
numberOfBlackCharacters = len(S) - S.count(spaceCharacter)
S = S.replace(",", " ")
S = S.replace(".", " ")
S = S.replace("-", " ")
S = S.replace(":", " ")
S = S.replace("?", " ")
S = S.replace("!", " ")

words = S.split()
numberOfWords = len(words)
words = sorted(words, key=len)
longestWord = words[-1]
wordsSortedByLexicographicOrder = sorted(words, key=str.lower)
wordsSortedByLengths = words

print("Number of black characters in S:", numberOfBlackCharacters)
print("Number of words in S:", numberOfWords)
print("The longest word in S:", longestWord)
print("Words sorted - lexicographic order:", wordsSortedByLexicographicOrder)
print("Words sorted - length:", wordsSortedByLengths)