#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from sklearn.cluster import SpectralClustering
from wplotlib import lines
from wplotlib import scatter

#	Line and Scatter Plot Example
x = np.linspace(0, 5, 20)
y = (2/25)*x

#	Top image
l = lines(x, y, 'Probability Distribution from 0 to 5', 'x', 'P(x)', fill_area=(None,None,'pink'),
					xlim=(0,6), ylim=(0,1), 
					ticker_fontsize=8, xticker_rotate=90, figsize=(6,4))		# (width, height)

