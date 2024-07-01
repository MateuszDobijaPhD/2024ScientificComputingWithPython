# EXERCISE 8.1
#
# Create the following NumPy arrays:
# (a) float from 0.0 to 1.0 step 0.1, shape=(11,),
# (b) int zeros (1 byte) with shape=(5,6),
# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.

import numpy as np
#(a)

array1 = np.arange(0.0, 1.1, 0.1, dtype=float).reshape(11,)
print("array1: ", array1)

#(b)

array2 = np.zeros(shape=(5,6), dtype=np.int8, order='C')
print("array2: ", array2)

#(c)
#l = [2**i for i in range(n)]
x = 2
powers = np.arange(0, 9, 1, dtype=np.int8).reshape(9,)
print("powers", powers)
array3 = np.power(x, powers, dtype=complex)
print("array3: ", array3)