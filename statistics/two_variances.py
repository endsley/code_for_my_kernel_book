#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from wplotlib import scatter

#	Line and Scatter Plot Example
x = np.array([0,0,0,0,0,0,0])
y1 = np.array([1,2,5,6,7,4,10])
y2 = np.array([4,5,6,5.3,4.5,4.1,5.7])

μ1 = np.mean(y1)
μ2 = np.mean(y2)

v1 = np.var(y1)
v2 = np.var(y2)

print(v1, v2)

#	Top image
l = scatter(y1,x, 'Data Variation for x', 'values of x', '', xlim=(0,10), ylim=(-1,1), 
					vertical_axis_loc=μ1, horizontal_axis_loc=0,
					ticker_fontsize=8, xticker_rotate=90, figsize=(8,4), subplot=121)		


scatter(y2,x, 'Data Variation for y', 'values of y', '', xlim=(0,10), ylim=(-1,1), 
					vertical_axis_loc=μ2, horizontal_axis_loc=0,
					ticker_fontsize=8, xticker_rotate=90, subplot=122)		

l.show()
