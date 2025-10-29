import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(arr)
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]

print(str(arr))
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]

print("Size :", arr.size)
# Size : 16

res = arr.reshape((4, 4))
print(res)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

res = np.reshape(arr, (2, 8))
print(res)
# [[ 1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16]]

res = np.reshape(arr, (2, 2, -1)) # We can ignore last dimension value because it is understood, size / (dim1 * dim2) == 4
print(res)
# [[[ 1  2  3  4]
#   [ 5  6  7  8]]

#  [[ 9 10 11 12]
#   [13 14 15 16]]]

arr.resize(4, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]