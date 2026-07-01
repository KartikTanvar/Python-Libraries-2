import numpy as np

# np1 = np.array([[1, 2, 8],
#                 [4, 5, 6]])
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


#method 1 
#it gives a list of elements which are greater than 3
filtered = np.where(np1 > 3)
print(np1[filtered])


#method 2
#it also gives a list of elements which are greater than 3

filtered = np1[np1 > 3]
print(filtered)

# or 
filtered = np1 > 2
print(np1[filtered])


# for loops can also be used 
filtered = []
for thing in np1:
	if thing % 2 == 0:
		filtered.append(True)
	else:
		filtered.append(False)


print(np1)
print(filtered)
print(np1[filtered])  #but only for 1D arrays, for 2D arrays, use np.where() or boolean indexing