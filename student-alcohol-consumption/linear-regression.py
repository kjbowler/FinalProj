import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

combData = pd.read_csv("combData.csv")

y = combData.G3_x
X = combData[combData.loc[:, ['Dalc_x', 'Walc_x']]] 
print(X)

clf_0 = LinearRegression().fit(X, y)
pred_y_0 = clf_0.predict(X)
print(accuracy_score(pred_y_0, y))

plt.show()