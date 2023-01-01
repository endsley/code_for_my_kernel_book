#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')

import numpy as np
import wuml
import wplotlib

c = np.array([[1, 0]])
cov = np.array([[1, 0.80], [0.80, 1]])
x = np.random.multivariate_normal([0, 0], cov, size=30) + 5

x2 = wuml.center_data(x)
Q = x2.T.dot(x2)
[U, σ, Σ] = wuml.eigh(Q, q=2, eig_order='largest_first')
Xᵈ = wuml.dimension_reduction(x, 1, method='PCA')

V = wuml.ensure_vector_is_a_column_format(Xᵈ.eig_vectors.values[:,0])
V2 = wuml.ensure_vector_is_a_column_format(Xᵈ.eig_vectors.values[:,1])

l = np.arange(-6,6)
y = V[0]*l/V[1]
y2 = V2[0]*l/V2[1]

pX = (x2.dot(V)).dot(V.T)
pX2 = (x2.dot(V)).dot(c)

S = wplotlib.scatter(x[:,0], x[:,1], color='red', title='Original Data', xlabel='', ylabel='', figsize=(10,10), 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-10,10], ylim=[-10,10], subplot=221)

wplotlib.lines(l,y, color='blue', subplot=222)
wplotlib.lines(l,y2, color='green', show=False)
wplotlib.scatter(x2[:,0], x2[:,1], color='red', title='Centered Data', xlabel='', ylabel='', 
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-10,10], ylim=[-10,10], show=False)


wplotlib.lines(l,y, color='blue', subplot=223)
wplotlib.lines(l,y2, color='green', show=False)
wplotlib.scatter(pX[:,0], pX[:,1], color='red', title='Removed Low Variance Direction', xlabel='', ylabel='',  
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-10,10], ylim=[-10,10], show=False)


wplotlib.scatter(pX2[:,0], pX2[:,1], color='red', title='Rotate Data to keep 1 dimension', xlabel='', ylabel='',  subplot=224,
					vertical_axis_loc=0, horizontal_axis_loc=0, xlim=[-10,10], ylim=[-10,10], show=False)

S.show()

