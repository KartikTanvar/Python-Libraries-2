import numpy as np 
np1 = np.array([1 , 2,3,3,4,5 ,6])

np2 = np1.copy()
np3 = np1.view()

np3[0] = 100
print(np1)
print(np3)

np2[2] = 400
print(np1)
print(np2)


