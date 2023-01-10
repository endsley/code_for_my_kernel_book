#!/usr/bin/env python

import numpy as np

#	Solves Ax=b
A = np.array([[2, 2], [3, 1]])
b = np.array([1, 2])
Ainv = np.linalg.inv(A)
x = Ainv.dot(b)
print(x)



#x = np.linalg.solve(A, b)
#import pdb; pdb.set_trace()
#print(x)
