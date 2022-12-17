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

x = np.arange(0, 5, 0.1)
y = 3*np.exp(-x)*np.sin(10*x) + 3
x2 = np.arange(0, 5, 0.5)
y2 = 3*np.exp(-x2)*np.sin(10*x2) + 3

x3 = np.arange(0, 20, 0.5)
y3 = 20*np.exp(-x3/10)

x4 = np.arange(0, 20, 1)
y4 = 20*np.exp(-x4/10)


#	plot the points
S = wplotlib.lines(x, y, figsize=(10,4), 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[0,5], ylim=[0,6], subplot=121)
wplotlib.scatter(x2, y2, color='red', title='Height of oscillating spring over time', xlabel='time (s)', ylabel='height', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[0,5], ylim=[0,6], show=False)

wplotlib.lines(x3, y3, vertical_axis_loc=0, 
					horizontal_axis_loc=0, xlim=[0,20], ylim=[0,22], subplot=122)

wplotlib.scatter(x4, y4, vertical_axis_loc=0, title='Value of a Car after bought', xlabel='years', ylabel='Thousands',
					color='red', horizontal_axis_loc=0, xlim=[0,20], ylim=[0,22])



					
#wplotlib.scatter(3, 1, color='red', 
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=121)
#
#
#
#
#wplotlib.scatter(2, 2, color='green', title='Space of Functions', xlabel=r'$a$', ylabel=r'$b$', 
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim], subplot=121)
#
#
#D = wplotlib.lines(x, y1, subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
#wplotlib.lines(x, y2, color='red', subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
#wplotlib.lines(x, y3, color='green', title='The Actual Functions', xlabel='x', ylabel='y', subplot=122,
#					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
#
#S.show()


