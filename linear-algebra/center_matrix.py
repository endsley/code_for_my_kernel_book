#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')
import wplotlib
import wuml
import numpy as np

x = 0.4*np.random.randn(20)
y = 0.4*np.random.randn(20)

x2 = x + 3 
y2 = y + 3 

x3 = x2 - np.mean(x2)
y3 = y2 - np.mean(y2)


#	plot the points
S = wplotlib.scatter(x2, y2, color='red', title='Original Data', xlabel='', ylabel='', figsize=(10,4), 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-5,5], ylim=[-5,5], subplot=121)


wplotlib.scatter(x3, y3, color='red', title='Centered Data', vertical_axis_loc=0, 
					horizontal_axis_loc=0, xlim=[-5,5], ylim=[-5,5], subplot=122)

S.show()

