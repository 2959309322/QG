#2.8
#practise
import numpy as np

matrix = np.arange(12).reshape(3,4)
print(matrix)
print(matrix.shape)
print(matrix.dtype)
print(matrix.ndim)
matrix_flattened = matrix.flatten()
print(matrix_flattened)

#关于-1的实验
print(matrix[0][-1])
matrix_re = matrix_flattened.reshape(2,-1)
print(matrix_re)

#关于广播的实验
a = np.array([[1],[2],[3]])
print(matrix+a)