import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

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

y = combData.G3_x
X = combData[combData.loc[:, ['Dalc_x', 'Walc_x']]] 
print(X)



clf_0 = LinearRegression().fit(X, y)
pred_y_0 = clf_0.predict(X)
print(accuracy_score(pred_y_0, y))



plt.show()