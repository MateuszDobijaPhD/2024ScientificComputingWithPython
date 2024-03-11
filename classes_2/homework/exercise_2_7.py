# Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. Use different methods.
# 1st option
dictionary = {}
dictionary["I"] = 1
dictionary["IV"] = 4
dictionary["V"] = 5
dictionary["IX"] = 9
dictionary["X"] = 10
dictionary["XL"] = 40
dictionary["L"] = 50
dictionary["XC"] = 90
dictionary["C"] = 100
dictionary["CD"] = 400
dictionary["D"] = 500
dictionary["CM"] = 900
dictionary["M"] = 1000

print("dictionary:", dictionary)

# 2nd option
dictionary = {"I" : 1, "IV" : 4, "V" : 5, "IX" : 9, "X" : 10, "XL" : 40, "L" : 50, "XC" : 90, "C" : 100, "CD" : 400, "D": 500, "CM" : 900, "M" : 1000}
print("dictionary:", dictionary)

# 3rd option
dictionary = dict([("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL",40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)])
print("dictionary:", dictionary)

# 4th option
dictionary = dict(zip(["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],[1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]))
print("dictionary:", dictionary)

