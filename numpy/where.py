import numpy as np

np1 = np.array([[1, 2, 3, 4]])

# np2 = np.where(np1 > 3)
# print(np2)
print(np.where(np1 > 3, 'Yes', 'No'))