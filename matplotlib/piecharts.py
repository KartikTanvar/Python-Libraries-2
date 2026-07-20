import numpy as np
import matplotlib.pyplot as plt


characters = ["clint barton", "wong", "morbius", "iron man"]
values = np.array([1000,1500,200,3000])
colors = ["black", "orange", "green", "red"]

plt.pie(values, labels= characters,
                colors = colors,
                autopct= "%1.1f%%",
                explode= [0,0,1,0],
                shadow = True,  
                startangle= 0          ) 


plt.title("marv")       

plt.show()