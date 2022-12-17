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
y= y1 + 0.2*np.random.randn(len(y1))


data = wuml.wData(X_npArray=x, Y_npArray=y)
reg = wuml.regression(data, regressor='linear')
coef = reg.get_coefs()
y2= coef[0][0]*x + 1*coef[1]


S = wplotlib.scatter3d(dataMatrix=dataMatrix,  color='green', subplot=121, show=False, figsize=(12,6))
S.add_scatter(dataMatrix=dataMatrix2, title='Function Space', title_font=12, color='red', add_horizontal_surface_at=0, xlim=[0,2], ylim=[0,2], 
					subplot=121, zlim=[-0.4,1], ticker_fontsize=8, xlabel='a', ylabel='b', zlabel='c')


D = wplotlib.lines(x, y1, subplot=122, color='green', vertical_axis_loc=0, horizontal_axis_loc=0)

wplotlib.lines(x, y2, subplot=122, color='red', vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-lim,lim], ylim=[0,lim])
S2 = wplotlib.scatter(x, y, subplot=122, color='blue', xlabel=r'$x$', ylabel=r'$y$', title='Fitting a line on data', title_font=12, ticker_fontsize=8, xfont=10, yfont=10 )

S.show()
