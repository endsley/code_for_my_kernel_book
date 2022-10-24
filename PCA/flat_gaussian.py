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

n = 10
lim = 5

#	Generate a new data using these code
#X = 2*np.random.randn(n,1)
#Y = 0.1*np.random.randn(n,1)
#XY = np.hstack((X,Y))
#wuml.jupyter_print(XY)

#	Use a pregenerated data
XY = np.array([	[-2.6131, -0.0134],
				[ 3.3163,  0.1078],
				[-0.2363, -0.1127],
				[-1.3604, -0.0731],
				[ 1.3328, -0.0385],
				[-0.9214,  0.0094],
				[-2.6685, -0.0042],
				[-2.6934, -0.0287],
				[ 1.3875, -0.0062],
				[-0.3191, -0.0107]])
X = XY[:,0]
Y = XY[:,1]
import pdb; pdb.set_trace()


#	plot the data
S = wplotlib.scatter(X, Y, title='Scatter Plot of the Original Data', xlabel='', ylabel='', figsize=(7,8),
					x_origin_axis_color='k', y_origin_axis_color='k', xlim=[-lim,lim], ylim=[-lim,lim], subplot=311)
Y2 = 0*np.random.randn(n,1)
wplotlib.scatter(X, Y2, title='Keeping only the x-axis', xlabel='', ylabel='', 
					x_origin_axis_color='k', y_origin_axis_color='k', xlim=[-lim,lim], ylim=[-lim,lim], subplot=312)
wplotlib.scatter(Y2, Y, title='Keeping only the y-axis', xlabel='', ylabel='', 
					x_origin_axis_color='k', y_origin_axis_color='k', xlim=[-lim,lim], ylim=[-lim,lim], subplot=313)
S.show()


