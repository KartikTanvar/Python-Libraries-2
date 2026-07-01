# import numpy as np


# np2 = np.array(["John", "tina", "Aaron", "Zed"])
# # print(np2)
# # print(np.sort(np2))


# # for i in np2:
# #     if i[0].islower():
# #         i = i.capitalize()
# #     else:
# #         i = i
   


# np2_sorted = np.array(sorted(np2, key=str.lower))
# print(np2_sorted)
# print(type(np2_sorted))   

names = ["John", "tina", "Aaron", "Zed"]

for idx, val in enumerate(names):
    if val[0].islower():
        names[idx] = val.capitalize()

print(names)
names.sort()
print(names)

    
    

