import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.stack((a, b), axis = 0)
print(c)
# [[1 2 3]
#  [4 5 6]]

c = np.stack((a, b), axis = 1)
print(c)
# [[1 4]
#  [2 5]
#  [3 6]]

c = np.stack((a, b), axis = -1) # Here 2 axis are possible. 0 and 1. So, -1 is same as 1.
print(c)
# [[1 4]
#  [2 5]
#  [3 6]]

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

c = np.stack((a, b), axis = 0)
print(c)
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

c = np.stack((a, b), axis = 1)
print(c)
# [[[ 1  2  3]
#   [ 7  8  9]]

#  [[ 4  5  6]
#   [10 11 12]]]

c = np.stack((a, b), axis = 2)
print(c)
# [[[ 1  7]
#   [ 2  8]
#   [ 3  9]]

#  [[ 4 10]
#   [ 5 11]
#   [ 6 12]]]