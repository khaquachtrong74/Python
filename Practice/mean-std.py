import numpy as np 
arr1 = np.random.random(100000)

arr2 = np.random.random(100000)
print(np.convolve(arr1,arr2))
