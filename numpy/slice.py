import numpy as np

np1 = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np1)

print(np1.shape)  

print(np1.ndim)

print(np1.size)

print(np1[0,2])
print(np1[1:2 , 0:2])
print(np1[0:2 , 1:3])

np2 = np.arange(10)
print(np2)
          