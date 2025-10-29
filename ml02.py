import numpy as np

var = "rafat"
arr = np.fromiter(var, dtype = 'U2', count = -1)
print(arr)
# ['r' 'a' 'f' 'a' 't']

arr = np.arange(1, 20 , 2, dtype = np.float32)
print(arr)
# [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19.]


arr = np.empty([4, 3], dtype = np.int32, order = 'f') # garbage value
print(arr)
# [[  948277570   955741642          20]
#  [-2147482956         692           0]
#  [  660637849   955741684          51]
#  [ 1689416820         692           0]]

arr = np.ones([4, 3], dtype = np.int32, order = 'f')
print(arr)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]
#  [1 1 1]]

arr = np.zeros([4, 3], dtype = np.int32, order = 'f')
print(arr)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]
#  [0 0 0]]

