#messing with Seaborn Library here

#prereqs of seaborn libraries: numpy, pandas, matplotlib, scipy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

sns.set(style="white")

# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")

plt.show()

print("Something happened")
