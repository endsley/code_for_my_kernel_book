#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot an arrow using the `arrow` function
ax.arrow(0, 0, 0.95, 0, head_width=0.05, head_length=0.05, fc='b', ec='b')
ax.arrow(1, 0, 0, 0.95, head_width=0.05, head_length=0.05, fc='b', ec='b')
ax.arrow(0, 0, 0.95, 0.95, head_width=0.05, head_length=0.05, fc='k', ec='k')

ax.set_title("1-norm vs 2-norm")
# Show the plot
plt.show()





## Define the matrices
#M1 = np.array([[1, 2, 3], [4, 5, 6]])
#M2 = np.array([[1, 0], [3, 1]])
#
## Example of transpose and trace
#transposed_M1 = M1.T
#trace_M2 = np.trace(M2)
#
#print(transposed_M1)
#print(trace_M2)
#


