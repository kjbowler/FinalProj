import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

combData = pd.read_csv("combData-normal.csv")
dataX = combData.drop(columns = ['guardian_y', 'traveltime_y', 'studytime_y', 'failures_y', 'schoolsup_y', 'famsup_y', 'paid_y', 'activities_y', 'higher_y', 'freetime_y', 'goout_y', 'Dalc_y', 'Walc_y', 'health_y', 'absences_y', 'G1_y', 'G2_y', 'G3_y'])
dataY = combData.drop(columns = ['guardian_x', 'traveltime_x', 'studytime_x', 'failures_x', 'schoolsup_x', 'famsup_x', 'paid_x', 'activities_x', 'higher_x', 'freetime_x', 'goout_y', 'Dalc_x', 'Walc_x', 'health_x', 'absences_x', 'G1_x', 'G2_x', 'G3_x'])
#print(combData.shape, dataX.shape, dataY.shape)
uniqueX = [0,1]
uniqueY = [0,1]
findMax = []
avgX = []
avgY = []
trac = []
for x in uniqueX:
    #newdfX = dataX[dataX["Dalc_x"] == x]
    #newdfX = dataX[dataX["failures_x"] == x]
    #newdfX = dataX[dataX["studytime_x"] == x]
    #newdfX = dataX[dataX["absences_x"] == x]
    newdfX = dataX[dataX["paid_x"] == x]
    #newdfX = dataX[dataX["internet"] == x]
    avgX.append(newdfX["G3_x"].mean())
    trac.append(x)
    #newdfY= dataY[dataY["Dalc_y"] == x]
    #newdfY = dataY[dataY["failures_y"] == x]
    #newdfY = dataY[dataY["studytime_y"] == x]
    #newdfY = dataY[dataY["absences_y"] == x]
    newdfY = dataY[dataY["paid_y"] == x]
    #newdfY = dataY[dataY["internet"] == x]
    avgY.append(newdfY["G3_y"].mean())

x_label = 'Extra Paid Classes'
y_label = 'Final Grade'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.plot(trac, avgX, marker = "x", color = 'm', label = "Math Class")
plt.plot(trac, avgY, marker = "x", color = 'c', label = "Portuguese Class")

plt.legend()
plt.show()