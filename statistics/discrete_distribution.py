#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from sklearn.cluster import SpectralClustering
from wplotlib import bar


X = ['2', '3', '4', '5']
Y = [0.5, 0.25, 0, 0.25]
B = bar(X,Y, 'Discrete Distributions', 'Outcome Value', 'Probability')


