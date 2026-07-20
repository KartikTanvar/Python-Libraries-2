import numpy as np 
import matplotlib.pyplot as plt

figures, axes = plt.subplots(2,2)

x= np.array([1,2,3,4,5])

line_style = dict(marker = "*",
                markersize= 10,
                markerfacecolor= "red" ,                         
                markeredgecolor= "white",
                linestyle= "dashed",
                linewidth= 2,
                color= "green" )

axes[0, 0].plot(x, x**2, **line_style)
axes[0, 0].set_title("x**2")

axes[0, 1].plot(x, x**x, **line_style)
axes[0, 1].set_title("x**x")

axes[1, 0].plot(x, x**3 , **line_style)
axes[1, 0].set_title("x**3")

axes[1, 1].plot(x, x**5 , **line_style)
axes[1, 1].set_title("x**5")

plt.tight_layout()


plt.show()