import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

combData = pd.read_csv("numericData.csv")
unique = combData.Dalc_x.unique()
findMax = []
for x in unique:
    newdf = combData[combData["Dalc_x"] == x]
    avgx = newdf["G3_x"].mean()
    findMax.append(newdf.shape[0])
    #print(newdf)
    plt.plot(x, avgx, marker = "x", color = 'm')
# combData.plot.scatter(x = "Dalc_y", y = "G3_y", marker = ".", color = 'blue')
print(findMax)


plt.show()