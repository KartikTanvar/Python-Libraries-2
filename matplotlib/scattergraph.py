import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.arange(10)

plt.scatter(x, y,   color = "green",
                    alpha = 0.5,
                    s = 100,
                    
                    )

xti_ck = range(11)
plt.xticks(xti_ck)
plt.yticks(xti_ck)


plt.show()