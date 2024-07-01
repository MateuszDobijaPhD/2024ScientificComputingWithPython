# EXERCISE 8.2
#
# (a) Create an arbitrary one dimensional array called v1.
# (b) Create a new array (or a view) v2 which consists of items with odd indices of v1.
# (c) Create a new array (or a view) v3 in backwards ordering from v1.

import numpy as np

#(a)
v1 = np.array( [2, 3, 4, 5, 6, 7, 8] )
print("v1", v1)
#(b)
v2 = np.array( v1[1::2] )
print("v2", v2)

#(c)
v3 = np.array( v1[::-1])
print("v3", v3)