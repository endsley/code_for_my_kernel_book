#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from wplotlib import scatter

#	Line and Scatter Plot Example
x = np.arange(0,3,0.1)
y = 0.5*x 
y1 = y + 0.1*np.random.randn(len(x))
y2 = np.random.uniform(size=len(x))


cov1 = np.round(np.cov(x,y)[0,1], 2)
cov2 = np.round(np.cov(x,y1)[0,1], 2)
cov3 = np.round(np.cov(x,y2)[0,1], 2)


#	Top image
l = scatter(x,y, 'x,y covariance=%.2f'%cov1, r'$x$', r'$y$', xlim=(-0.2,1.3), ylim=(-0.2,1.3), 
					vertical_axis_loc=0, horizontal_axis_loc=0,
					ticker_fontsize=8, xticker_rotate=90, figsize=(12,4), subplot=131)		


scatter(x,y1, 'x,y covariance=%.2f'%cov2, r'$x$', '', xlim=(-0.2,1.3), ylim=(-0.2,1.3), 
					vertical_axis_loc=0, horizontal_axis_loc=0,
					ticker_fontsize=8, xticker_rotate=90, subplot=132)		


scatter(x,y2, 'x,y covariance=%.2f'%cov3, 'x', '', xlim=(-0.2,1.3), ylim=(-0.2,1.3), 
					vertical_axis_loc=0, horizontal_axis_loc=0,
					ticker_fontsize=8, xticker_rotate=90, subplot=133)		

l.show()
