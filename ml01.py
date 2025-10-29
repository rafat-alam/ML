import numpy as np

a = np.zeros((3, 3)) # Dimension 3 x 3
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
a = np.ones((3, 3)) # Dimension 3 x 3
print(a)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
a = np.arange(0, 10, 2) # start, stop (exclusive), step
print(a)
# [0 2 4 6 8]
a = np.full((2, 2), 7) # Dimension 2 x 2, val
print(a)
# [[7 7]
#  [7 7]]

x = np.array([[1, 2, 3], [-4, 5, 6]])
print(x)
# [[1 2 3]
#  [-4 5 6]]
print(x[0])
# [1 2 3]
print(x[0][:2]) # Array Slicing -> [start:end (exclusive)] 
# [1, 2]
y = np.array([0, 1])
print(x[1][[0, 1]])
# [-4, 5]
print(x[x != 0])
# [1 2 3 5 6]
y  = np.absolute(x)
print(y)
# [[1 2 3]
#  [4 5 6]]
y = np.add(x[0], x[1])
print(y)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)
# [5 7 9]
print(x - y)
# [-3 -3 -3]
print(x * y)
# [ 4 10 18]
print(x / y)
# [0.25 0.4  0.5 ]

a = np.array([0, np.pi/2, np.pi])
print(np.sin(a))
# [0.0000000e+00 1.0000000e+00 1.2246468e-16]
print(np.exp(a))
# [ 1.          4.81047738 23.14069263]
print(np.sqrt(a))
# [0.         1.25331414 1.77245385]

print(type(a)) # <class 'numpy.ndarray'>
print("No. of dimensions: ", a.ndim) # 1
print("Shape of array: ", a.shape) # (3,)
print("Size of array: ", a.size) # 3
print("Array stores elements of type: ", a.dtype) # float64

dtypes = [('name', 'S10'), ('1', int), ('2', int)]
values = [('rafat', 5, 10), ('sufiya', 5, 2), ('arman', 4, 2)]

arr = np.array(values, dtype=dtypes)

print(np.sort(arr, order = ['1', '2']))