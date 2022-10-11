#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')
import wplotlib

import numpy as np



X = 2*np.random.randn(100,1)
Y = 0.1*np.random.randn(100,1)
S = wplotlib.scatter(X, Y, title='Scatter Plot of the Data', xlabel='', ylabel='', 
					x_origin_axis_color='k', y_origin_axis_color='k', show=True, xlim=[-5,5], ylim=[-5,5])


