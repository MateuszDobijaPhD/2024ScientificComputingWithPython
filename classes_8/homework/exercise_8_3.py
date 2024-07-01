# EXERCISE 8.3
#
# (a) Create a two dimensional array called m1, shape=(4,5).
# (b) Create a new array (or a view) m2 from m1, in which the elements of each row are in reverse order.
# (c) Create a new array (or a view) m3 from m1, in which the elements of each column are in reverse order.
# (d) Remove the first row, the last row, the first column, and the last column of m1, and create a new array (or a view) m4.

import numpy as np

#(a)
n=4
m=5
m1 = np.arange(n*m).reshape((n,m))

print("m1", m1)

#(b)
m2 = np.fliplr( m1)
print("m2", m2)

#(c)
m3 = np.flipud( m1)
print("m3", m3)

#(d)
m4 = np.array( m1[1:n-1, 1:n])
print("m4", m4)