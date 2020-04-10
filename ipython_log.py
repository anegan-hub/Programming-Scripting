# # IPython log file

# This program displays a plot of the functions 
# if(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# This program requires two imports 'numpy' and 'matplotlib.pyplot'

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4)
g = x **2
h = x **3

# plots g, in the colour blue 'b' with label as "g(x)=x2
plt.plot(x, g, 'b.', label = "g(x)=x2")  

# plots g, in the colour blue 'r' with label as "h(x)=x3"
plt.plot(x, h, 'r.', label = "h(x)=x3")

plt.legend()
plt.title("Function Plot")
plt.xlabel("Range, f(x)=x")
plt.ylabel("Comparsion between g(x) and h(x)")

plt.show()
