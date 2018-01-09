# numpy library

# multidimensional array objects with a collection of routines for processing the arrays.

import numpy as np

"""
In numpy arrays, dimensionality refers to the number of axes needed to index it, 
not the dimensionality of any geometrical space. For example, you can describe 
the locations of points in 3D space with a 2D array:
array([[0, 0, 0],
       [1, 2, 3],
       [2, 2, 2],
       [9, 9, 9]])
"""

a = np.random.rand(2,3)
print a
'''
array([[ 0.52799499,  0.81067127,  0.73445975],
       [ 0.46718562,  0.6537916 ,  0.9125332 ]])
'''
print a.ndim	# 2



b = np.random.rand(1,2,3)		# (dimension1, dimension2, ... , dimensionN, num_rows, num_cols)
print b
'''
array([[[ 0.46136639,  0.9014226 ,  0.81172557],
        [ 0.23262449,  0.07877792,  0.48654593]]])
'''
print b.ndim	# 3



c = np.random.rand(2,2,3)
print c
'''
array([[[ 0.59074391,  0.50019247,  0.10501063],
        [ 0.63351677,  0.73058669,  0.4197894 ]],

       [[ 0.14744331,  0.63865537,  0.77344808],
        [ 0.09391716,  0.74613763,  0.59703912]]])
'''
print c.ndim	# 3




""" Array generation """
a = np.array([1,2,3], dtype=complex)		# array([ 1.+0.j,  2.+0.j,  3.+0.j])
a.size										# 3
a.shape										# (3,)
a.ndim										# 1

a = np.array([[1,2,3], [4,5,6], [7,8,9], [1,1,1]])
a.size										# 12
a.shape										# (4,3)
a.ndim										# 2

np.zeros([3,2])
'''
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
'''

""" Array generation from numerical ranges """
# numpy.arange(start, stop, step, dtype)
a = np.arange(10)				# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = np.arange(25, 30)			# array([25, 26, 27, 28, 29])
a = np.arange(10, 20, 2)		# array([10, 12, 14, 16, 18])
a = np.arange(10, 20, 2, float)	# array([ 10.,  12.,  14.,  16.,  18.])

a = np.linspace(1, 2, 9)		# array([ 1.,  1.125,  1.25 ,  1.375,  1.5,  1.625,  1.75 ,  1.875,  2.])




""" Array slicing """

a = np.arange(10)
print a 			# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print a[:5]			# array([0, 1, 2, 3, 4])
print a[5:]			# array([5, 6, 7, 8, 9])
print a[5:8]		# array([5, 6, 7])


a = np.arange(81).reshape(9,9)
print a
'''
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23, 24, 25, 26],
       [27, 28, 29, 30, 31, 32, 33, 34, 35],
       [36, 37, 38, 39, 40, 41, 42, 43, 44],
       [45, 46, 47, 48, 49, 50, 51, 52, 53],
       [54, 55, 56, 57, 58, 59, 60, 61, 62],
       [63, 64, 65, 66, 67, 68, 69, 70, 71],
       [72, 73, 74, 75, 76, 77, 78, 79, 80]])
'''       
print a[:, 3][:5]		# array([ 3, 12, 21, 30, 39])



# iterate through elements
a = np.arange(30).reshape(10,3)
print a.shape			# (10, 3)


for row in range(a.shape[0]):
	for col in range(a.shape[1]):
		print a[row][col]
