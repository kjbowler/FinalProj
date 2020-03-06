import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def accuracy(y, y_hat):
    acc = 0
    for x in range(len(y_hat)):
        if y[x] == y_hat[x]:
            acc = acc + 1
    acc = acc/len(y_hat)
    return acc

def threshold_predictions(y_hat_score, threshold):
    new_score = y_hat_score.copy()
    for x in range(len(y_hat_score)):
        if new_score[x] > threshold:
            new_score[x] = 1
        if y_hat_score[x] <= threshold:
            new_score[x] = 0
    return new_score

def compute_roc_curve(y, y_hat_score, num_thresholds):
    trac = np.arange(0, 1, 1/num_thresholds)
    tpr = []
    fpr = []
    for x in trac:
        y_hat_scorea = threshold_predictions(y_hat_score, x)
        tpr.append(true_positive_rate(y, y_hat_scorea))
        fpr.append(false_positive_rate(y, y_hat_scorea))
    # End of your code
    return tpr, fpr

def true_positive_rate(y, y_hat):
    TP = 0
    FN = 0
    for x in range(len(y_hat)):
        if y[x] == 1 and y_hat[x] == 1:
            TP = TP + 1
        if y[x] == 1 and y_hat[x] == 0:
            FN = FN + 1
    TPR = TP/(TP + FN)
    return TPR

def false_positive_rate(y, y_hat):
    FP = 0
    TN = 0
    for x in range(len(y_hat)):
        if y[x] == 0 and y_hat[x] == 1:
            FP = FP + 1
        if y[x] == 0 and y_hat[x] == 0:
            TN = TN + 1
    TPR = FP/(FP + TN)
    return TPR

DataXCSV = pd.read_csv("DataX.csv")
DataYCSV = pd.read_csv("DataY.csv")
dataXX = DataXCSV.drop(columns = ['guardian_y', 'traveltime_y', 'studytime_y', 'failures_y', 'schoolsup_y', 'famsup_y', 'paid_y', 'activities_y', 'higher_y', 'freetime_y', 'goout_y', 'Dalc_y', 'Walc_y', 'health_y', 'absences_y', 'G1_y', 'G2_y', 'G3_y', 'G3_x'])
dataXY = DataXCSV['G3_x']
dataYX = DataYCSV.drop(columns = ['guardian_x', 'traveltime_x', 'studytime_x', 'failures_x', 'schoolsup_x', 'famsup_x', 'paid_x', 'activities_x', 'higher_x', 'freetime_x', 'goout_y', 'Dalc_x', 'Walc_x', 'health_x', 'absences_x', 'G1_x', 'G2_x', 'G3_x', 'G3_y'])
dataYY = DataYCSV['G3_y']

dataXX_train, dataXX_test, dataXY_train, dataXY_test = train_test_split(dataXX, dataXY, test_size=0.2)
dataYX_train, dataYX_test, dataYY_train, dataYY_test = train_test_split(dataYX, dataYY, test_size=0.2)

clf_0 = LinearRegression().fit(dataXX_train, dataXY_train)
pred_y_0 = clf_0.predict(dataXX_test)

clf_1 = LinearRegression().fit(dataYX_train, dataYY_train)
pred_y_1 = clf_1.predict(dataYX_test)

pred_y = np.array(dataXY_test)
pred_y1 = np.array(dataYY_test)

tpr_A, fpr_A = compute_roc_curve(pred_y, pred_y_0, 100)
tpr_B, fpr_B = compute_roc_curve(pred_y1, pred_y_1, 100)

# x_label = 'FPR'
# y_label = 'TPR'
# plt.xlabel(x_label)
# plt.ylabel(y_label)

# plt.plot(fpr_A, tpr_A, color = "m", marker = ".", label = "A")
# plt.plot(fpr_B, tpr_B, color = "c", marker = ".", label = "B")
# plt.legend()
# plt.show()



trac = np.arange(0, 1, 1/100)
max_0 = 0
max_1 = 0
tracA = 0
tracB = 0
for x in trac:
    #print(x)
    thresh_0 = threshold_predictions(pred_y_0, x)
    thresh_1 = threshold_predictions(pred_y_1, x)
    
    acc_0 = (accuracy(pred_y, thresh_0))
    acc_1 = (accuracy(pred_y1, thresh_1))
    
    if acc_0 > max_0:
        tracA = x
        max_0 = acc_0
    if acc_1 > max_1:
        tracB = x
        max_1 = acc_1

print(tracA)
print(tracB)
print(max_0)
print(max_1)

finthresh_0 = threshold_predictions(pred_y_0, tracA)
finthresh_1 = threshold_predictions(pred_y_1, tracB)

