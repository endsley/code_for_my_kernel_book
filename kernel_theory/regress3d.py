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

lim = 5

dataMatrix = np.array([[1,1,0.3]])
dataMatrix2 = np.array([[1,1,0]])

x = np.arange(-4,4,0.2)
y1= 0.3*x*x + x + 1
y2= x + 1
y= y1 + 0.2*np.random.randn(len(y1))


S = wplotlib.scatter3d(dataMatrix=dataMatrix,  color='green', add_horizontal_surface_at=0, xlim=[0,2], ylim=[0,2], 
						subplot=121, zlim=[-2,5], ticker_fontsize=5, show=False)

S.add_scatter(dataMatrix=dataMatrix2, title='3d plot', title_font=13, color='red', add_horizontal_surface_at=0, xlim=[0,2], ylim=[0,2], 
					subplot=121, zlim=[-2,1], ticker_fontsize=5)


D = wplotlib.lines(x, y1, subplot=122, color='green', vertical_axis_loc=0, horizontal_axis_loc=0)

wplotlib.lines(x, y2, title='Fitting a line on data', xlabel=r'$x$', ylabel=r'$y$', subplot=122, color='red', vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[-lim,lim])
S2 = wplotlib.scatter(x, y, subplot=122, color='blue')

S.show()
