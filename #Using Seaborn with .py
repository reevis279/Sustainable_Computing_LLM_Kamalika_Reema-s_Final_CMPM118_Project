#Using Seaborn with .csv file

# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#will have to change teh .csv file below to the data we need
dataset = pd.read_csv("Survival.csv")

# KDE plot 
sns.kdeplot(dataset["Age"], color = "green", 
            shade = True)
plt.show()
plt.figure()