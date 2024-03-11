# Explain the results.
# x = 5
# x == 5 and 3 + 8   # 11
# x == 4 and 3 + 8   # False
# 3 + 8 and x == 5   # True
# 3 + 8 and x == 4   # False

# isinstance(True, int)    # True
# isinstance(True, bool)   # True

#Answer:
x = 5                      # Answer: This is just creation of the variable x, and assignment of the value 5 to it

#From classes (explanation for the following cases):
# 'True' and 'False' are instances of the 'bool' class which is inherited from 'int'.
# In numeric contexts (for example when used as the argument to an arithmetic operator),
# 'False' and 'True' behave like the integers 0 and 1, respectively.
#
#'and' and 'or' are short-circuit operators:
#
#    'False and Anything' returns 'False', 'Anything' is not checked,
#    'True and Anything' returns 'Anything', but not converted to 'bool',
#    'True or Anything' returns 'True', 'Anything' is not checked,
#    'False or Anything' returns 'Anything', but not converted to 'bool'.
print(x == 5 and 3 + 8)   # 11    # x == 5 returns True, as variable x stores value 5. 'True and Anything' returns 'Anything', but not converted to 'bool'.
                          # Here - 'Anything' is equal to 3 + 8 , which equals 11.
print(x == 4 and 3 + 8)   # False # 'False and Anything' returns 'False', 'Anything' is not checked,
                          # Here - x == 4 is not True, it's False. So the whole statement is False.
print(3 + 8 and x == 5)   # True # "Objects considered false: zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1), etc."
                          #"Everything else is considered true. ". 3+8 is equal 11, which is not 0. We have statement build with "and", so
                          # the boolean ccntext is considered, in which 11 means True, as nonzero value. x == 5 returns True. True and True statement is True.
print(3 + 8 and x == 4)   # False # As above. 3 + 8 is 11. 11 means True. x ==4 returns False. True and False returns False.

print(isinstance(True, int))   # True
print(isinstance(True, bool))   # True
#'True' and 'False' are instances of the 'bool' class which is inherited from 'int'. So isinstance(True, int) is True, and so is isinstance(True, bool).

