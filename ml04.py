import numpy as np

arr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
print(arr)
# [[10 20 30]
#  [40  5 66]
#  [70 88 94]]

res = arr[[0,2]]
print(res)
# [[10 20 30]
#  [70 88 94]]

res = arr[1]
print(res)
# [40  5 66]

res = arr[:, [1]]
print(res)
# [[20]
#  [ 5]
#  [88]]

res = arr[:,[0, 2]]
print(res)
# [[10 30]
#  [40 66]
#  [70 94]]