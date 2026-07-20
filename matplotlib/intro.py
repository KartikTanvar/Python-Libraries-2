import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 2, 3, 4])
y = np.array([500 , 700, 600, 800])
y1 = np.array([900, 900, 900, 900])

line_style = dict(marker = "*",
                markersize= 10,
                markerfacecolor= "red" ,                         
                markeredgecolor= "white",
                linestyle= "dashed",
                linewidth= 2,
                color= "green" ) #these values can be considered as a default colour


plt.plot(x, y, **{**line_style, "marker" : "."}, label = "variable revenue")
plt.plot(x, y1, **{**line_style, "color":"blue"}, label = "fixed revenue" )

plt.title("salries",    fontsize =25,
                        family= "Arial",
                        fontweight= "bold",
                        color= "yellow"   )


plt.xlabel("days",  fontsize =25,
                        family= "Arial",
                        fontweight= "bold",
                        color= "yellow"   )
plt.ylabel("revenue",  fontsize =25,
                        family= "Arial",
                        fontweight= "bold",
                        color= "yellow"   )

plt.tick_params(axis= "both", 
                color = "red")
plt.xticks(x, ["Day1", "Day2", "Day3", "Day4"])  

y3 = np.unique(np.concatenate([y, y1]))
plt.yticks(y3 , ["Low", "Med", "High", "Peak", "blasted"])

plt.grid(axis= "y",
        linewidth= 3,
        color= "lightgray",
        linestyle= "dotted")
plt.legend(fontsize=10, loc="upper left", bbox_to_anchor=(0,0))

plt.tight_layout()
plt.show()


# we use bar(), barh() (for horizontal bar chart)  for the bar charts and everything remains the same 
