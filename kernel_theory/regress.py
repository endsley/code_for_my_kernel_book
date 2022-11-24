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
lim2 = 2

#	Generate a new data using these code
x = np.arange(0,4, 0.2)
y = 0.3*x + 1
y2 = 0.7*x + 0.4
t = y + np.random.randn(len(y))*0.15

#	plot the points
S = wplotlib.scatter(x, t, figsize=(10,4), vertical_axis_loc=0, horizontal_axis_loc=0, 
						xlim=[0,lim], ylim=[0,lim], subplot=121)

D = wplotlib.lines(x, y2, subplot=121, color='green', vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[0,lim], ylim=[0,lim])
wplotlib.lines(x, y, title='Fitting a line on data', xlabel=r'$x$', ylabel=r'$y$', imgText='The red line is the correct fit\nThe green line is wrong',
						yTextShift=3, subplot=121, color='red', vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[0,lim], ylim=[0,lim])



wplotlib.scatter(0.3, 1, color='red', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim2,lim2], ylim=[-lim2,lim2], subplot=122)
wplotlib.scatter(0.7, 0.4, color='green', title='Space of Functions', xlabel=r'$a$', ylabel=r'$b$', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=122)

#
#D = wplotlib.lines(x, y1, subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
#wplotlib.lines(x, y2, color='red', subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
#wplotlib.lines(x, y3, color='green', title='The Actual Functions', xlabel='x', ylabel='y', subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])

S.show()


