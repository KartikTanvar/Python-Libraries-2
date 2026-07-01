import numpy as np

# list1 = [1,2,3,4,5, "Hello", "World"]
# np1 = np.array([list1])

# print(np1)
# print (np1.dtype)
# print(np1.ndim)
# print (np1.shape)
# print(np1.size)
# print(np1.itemsize)
# print(list1)
# print(type(np1))

np1 = np.random.randint(1, 100, size=(3, 3))
np2 = np.random.randint(1, 100, size=(3, 3))

# print(np1)
# print(np2)
# print(np1 + np2)

#same as matrix operations
#we can do transpose, dot product, etc. with numpy arrays

print(np1)
print(np.transpose(np1))

