import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(loc=100, scale=100, size=100)
scores = np.clip(scores, 0,100)

plt.hist(scores, bins = 10,
                 color= "red",
                 edgecolor= "black",
                 alpha= 0.5)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Distribution of Scores (0–100)")
plt.grid(True, linestyle="--", alpha=0.7)

plt.xticks(list(range(0,101,10)))

plt.show()