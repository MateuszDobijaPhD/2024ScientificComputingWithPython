# # Find and explain the results.
# t = (2, 4)
# print(t[2])
# t.append(6)
# a, b = t ; print(a, b)


t = (2, 4)      # We create a tuple
#print(t[2])
# Traceback (most recent call last):
#   File "D:\obliczenia_naukowe_w_jezyku_python\classes_2\homework\exercise_2_6.py", line 9, in <module>
#     print(t[2])
# IndexError: tuple index out of range
# Elements of tuple have indices 0 and 1. Index 2 is out of range, so the error was raised.
#
#
# t.append(6)
#
# Traceback (most recent call last):
#   File "D:\obliczenia_naukowe_w_jezyku_python\classes_2\homework\exercise_2_6.py", line 15, in <module>
#     t.append(6)
# AttributeError: 'tuple' object has no attribute 'append'
# We can't add  any element to tuple (from Python language specification). As a result - the error was raised.
#
#
a, b = t ; print(a, b)
# We assign the first element of the tuple to newly created variable a, and the second element of the tuple
# to newly created variable b.
# We print variables a and b (their content)
