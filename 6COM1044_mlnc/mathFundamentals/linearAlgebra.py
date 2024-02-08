## 6COM1044-0105-Machine Learning and Neural Computing
### Math Fundamentals: Linear Algebra
import numpy as np
from numpy.linalg import inv
from scipy.linalg import svd

# Define two vectors
x = [82, 90, 65, 78, 46, 50, 51] # A list
print('Vector x = ', x)

# Define a matrix
M = [[82, 90, 65, 78, 46],[76, 78, 60, 50, 60]] # A list of lists = a column vector
print('Matrix M = ', M)

# Finding the inverse of a matrix
a = np.array([[1., 2.], [3., 4.]])
print('Matrix a:')
print(a)
print()

a_inv = inv(a)
print('Inverse of matrix a:')
print(a_inv)


# Finding the transpose of a matrix
a = np.array([[2., 4.], [6., 5.], [1., 0.]])
print('Matrix a:')
print(a)
print()

aT = a.transpose()
print('Transpose of matrix a:')
print(aT)


# Computing the trace of a matrix
a = np.array([[1., 5., 0.], [2., 4., 10.], [-1., 2., 3.]])
print('Matrix a:')
print(a)
print()

b = a.trace()
print('Trace of matrix a (SUM of main diagonal):')
print(b)

# Matrix Single Value Decomposition (SVD)
A = np.array([[1, 2], [3, 4], [5, 6]])
print('Matrix A:')
print(A)
print()

# Perform SVD on matrix A
U, S, VT = svd(A)
print('SVD of matrix A:')
print('U:')
print(U)
print('S:')
print(S)
print('VT:')
print(VT)
print()

# Compress ratio exercise (PPT Linear Algebra II - Slide 40)
n = 230 # width
d = 219 # height
k = 50 # number of singular values

image_size = n*d # original image size
print('Original image size =', image_size, 'pixels')
print()

image_size_reduced = n*k + k*k + d*k 
print('Reduced image size =', image_size_reduced, 'pixels')
print()

compressRatio = (1 - (image_size_reduced/image_size))*100
print('The compress ratio using', k, 'singular values is =', compressRatio, '%')