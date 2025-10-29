import numpy as np

arr = np.zeros((2, 3))
print(arr)
# [[0. 0. 0.]
#  [0. 0. 0.]]

arr = np.ones((2, 3))
print(arr)
# [[1. 1. 1.]
#  [1. 1. 1.]]

arr = np.full((2, 2), 7) # Dim, value
print(arr)
# [[7 7]
#  [7 7]]

arr = np.arange(0, 10, 2) # start, stop (exclusive), steps
print(arr)
# [0 2 4 6 8]

arr = np.linspace(0, 1, 5) # start, stop (inclusive), no. of element
print(arr)
# [0.   0.25 0.5  0.75 1.  ]

arr = np.random.rand(2, 3) # Uniform Distribution over [0, 1)
print(arr)
# [[0.8232986  0.04693213 0.21612834]
#  [0.06802489 0.01740907 0.27093813]]

arr = np.random.randn(2, 2) # Normal Distribution
print(arr)
# [[-0.33907261  1.21961456]
#  [-0.3717234  -1.27483389]]

arr = np.random.randint(1, 10, size=(2, 3)) # start, end (exclusive), Dim
print(arr)
# [[5 5 2]
#  [5 7 8]]

arr = np.eye(3) # Dim
print(arr)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

arr = np.diag([1, 2, 3])
print(arr)
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

arr = np.zeros_like(arr) # Create array of zeros with same shape and type
print(arr)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

arr = np.ones_like(arr) # Create array of ones with same shape and type
print(arr)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]