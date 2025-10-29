import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

res = np.array_split(arr, 3)
print(res)
# [array([1, 2]), array([3, 4]), array([5, 6])]

res = np.split(arr, 2)
print(res)
# [array([1, 2, 3]), array([4, 5, 6])]

arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5], [10, 11, 12]])

res = np.split(arr, 3, axis = 1)
print(res)
# [array([[ 3],
#        [ 8],
#        [ 4],
#        [10]]), array([[ 2],
#        [ 9],
#        [ 6],
#        [11]]), array([[ 1],
#        [ 7],
#        [ 5],
#        [12]])]

res = np.vsplit(arr, 2) # axis = 0
print(res)
# [array([[3, 2, 1],
#        [8, 9, 7]]), array([[ 4,  6,  5],
#        [10, 11, 12]])]

res = np.hsplit(arr, 3) # axis = 1
print(res)
# [array([[ 3],
#        [ 8],
#        [ 4],
#        [10]]), array([[ 2],
#        [ 9],
#        [ 6],
#        [11]]), array([[ 1],
#        [ 7],
#        [ 5],
#        [12]])]

arr = np.arange(24).reshape((2, 3, 4))
print(arr)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

res = np.dsplit(arr, 2) # axis = 2
print(res)
# [array([[[ 0,  1],
#         [ 4,  5],
#         [ 8,  9]],

#        [[12, 13],
#         [16, 17],
#         [20, 21]]]), array([[[ 2,  3],
#         [ 6,  7],
#         [10, 11]],

#        [[14, 15],
#         [18, 19],
#         [22, 23]]])]