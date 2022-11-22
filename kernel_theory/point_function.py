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
XY = np.array([	[-2, -3],
				[ 3,  1],
				[2,	2],
				[-1, 1]])


x = np.arange(-5,5)
y1 = -2*x -3
y2 = 3*x +1
y3 =  2*x +2

#	plot the points
S = wplotlib.scatter(-2, -3, figsize=(10,4),
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=121)
					
wplotlib.scatter(3, 1, color='red', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=121)

wplotlib.scatter(2, 2, color='green', title='Space of Functions', xlabel=r'$a$', ylabel=r'$b$', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=121)


D = wplotlib.lines(x, y1, subplot=122,
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
wplotlib.lines(x, y2, color='red', subplot=122,
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
wplotlib.lines(x, y3, color='green', title='The Actual Functions', xlabel='x', ylabel='y', subplot=122,
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])

S.show()


