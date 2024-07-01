# EXERCISE 9.1 (PLOT)
#
# Plot functions sin(x), cos(x), and exp(-x) in a range [0,10] in the same figure. Colors are red, green, and blue,
# respectively. Lines are solid, dashed, and dotted, respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
a = 1.0
y_sin = np.sin(x)
y_cos = np.cos(x)
y_exp = np.exp(-x)
plt.plot(x, y_sin, color='r', label='f(x) = sin(x)', linestyle='solid')
plt.plot(x, y_cos, color='g', label='f(x) = cos(x)', linestyle='dashed')
plt.plot(x, y_exp, color='b', label='f(x) = exp(-x)', linestyle='dotted')
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='best')
plt.show()