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

CSV_Math = pd.read_csv("DataX.csv")
CSV_Port = pd.read_csv("DataY.csv")
math_X = CSV_Math.drop(columns = ['guardian_y', 'traveltime_y', 'studytime_y', 'failures_y', 'schoolsup_y', 'famsup_y', 'paid_y', 'activities_y', 'higher_y', 'freetime_y', 'goout_y', 'Dalc_y', 'Walc_y', 'health_y', 'absences_y', 'G1_y', 'G2_y', 'G3_y', 'G3_x'])
math_Y = CSV_Math['G3_x']
port_X = CSV_Port.drop(columns = ['guardian_x', 'traveltime_x', 'studytime_x', 'failures_x', 'schoolsup_x', 'famsup_x', 'paid_x', 'activities_x', 'higher_x', 'freetime_x', 'goout_y', 'Dalc_x', 'Walc_x', 'health_x', 'absences_x', 'G1_x', 'G2_x', 'G3_x', 'G3_y'])
port_Y = CSV_Port['G3_y']

math_X_prot = math_X.drop(columns = ['sex', 'failures_x', 'Dalc_x', 'Walc_x', 'G1_x', 'G2_x'])
math_Y_prot = math_Y
port_X_prot = port_X.drop(columns = ['sex', 'failures_y', 'Dalc_y', 'Walc_y', 'G1_y', 'G2_y'])
port_Y_prot = port_Y
dataA = CSV_Port['sex']

math_X_train, math_X_test, math_Y_train, math_Y_test = train_test_split(math_X, math_Y, test_size=0.2)
port_X_train, port_X_test, port_Y_train, port_Y_test = train_test_split(port_X, port_Y, test_size=0.2)

math_X_prot_train, math_X_prot_test, math_Y_prot_train, math_Y_prot_test = train_test_split(math_X_prot, math_Y_prot, test_size=0.2)
port_X_prot_train, port_X_prot_test, port_Y_prot_train, port_Y_prot_test = train_test_split(port_X_prot, port_Y_prot, test_size=0.2)

clf_0 = LinearRegression().fit(math_X_train, math_Y_train)
pred_y_0 = clf_0.predict(math_X_test)

clf_1 = LinearRegression().fit(port_X_train, port_Y_train)
pred_y_1 = clf_1.predict(port_X_test)

clf_0_prot = LinearRegression().fit(math_X_prot_train, math_Y_prot_train)
pred_y_0_prot = clf_0_prot.predict(math_X_prot_test)

clf_1_prot = LinearRegression().fit(port_X_prot_train, port_Y_prot_train)
pred_y_1_prot = clf_1_prot.predict(port_X_prot_test)

pred_y = np.array(math_Y_test)
pred_y1 = np.array(port_Y_test)

pred_y_prot = np.array(math_Y_prot_test)
pred_y1_prot = np.array(port_Y_prot_test)


trac = np.arange(0, 1, 1/100)
max_0 = 0
max_1 = 0
tracA = 0
tracB = 0
max_0_prot = 0
max_1_prot = 0
tracA_prot = 0
tracB_prot = 0
for x in trac:
    #print(x)
    thresh_0 = threshold_predictions(pred_y_0, x)
    thresh_1 = threshold_predictions(pred_y_1, x)
    thresh_0_prot = threshold_predictions(pred_y_0_prot, x)
    thresh_1_prot = threshold_predictions(pred_y_1_prot, x)
    
    acc_0 = (accuracy(pred_y, thresh_0))
    acc_1 = (accuracy(pred_y1, thresh_1))
    acc_0_prot = (accuracy(pred_y_prot, thresh_0_prot))
    acc_1_prot = (accuracy(pred_y1_prot, thresh_1_prot))
    
    if acc_0 > max_0:
        tracA = x
        max_0 = acc_0
    if acc_1 > max_1:
        tracB = x
        max_1 = acc_1
    if acc_0_prot > max_0_prot:
        tracA_prot = x
        max_0_prot = acc_0_prot
    if acc_1_prot > max_1_prot:
        tracB_prot = x
        max_1_prot = acc_1_prot

print("Math threshold: ", tracA)
print("Portuguese threshold: ", tracB)
print("Math accuracy: ", max_0)
print("Portuguese accuracy: ", max_1)

print("Protected Features Math threshold: ", tracA_prot)
print("Protected Features Portuguese threshold: ", tracB_prot)
print("Protected Features Math accuracy: ", max_0_prot)
print("Protected Features Portuguese accuracy: ", max_1_prot)


def split_on_feature(dataX, dataY, dataA, thresh):
    rows_A = []
    rows_B = []
    for i in range(dataX.shape[0]):
        if dataA[i] < thresh:
            rows_A.append(i)
        else:
            rows_B.append(i)
    
    X_A = dataX[rows_A, :]
    X_B = dataX[rows_B, :]
    y_A = dataY[rows_A]
    y_B = dataY[rows_B]
    
    return X_A, X_B, y_A, y_B  


# X_A, X_B, y_A, y_B = split_on_feature(math_X_prot.values, math_Y_prot.values, dataA , .5)
X_A, X_B, y_A, y_B = split_on_feature(port_X_prot.values, port_Y_prot.values, dataA , .5)

# XA_score = clf_0_prot.predict(X_A)
# XB_score = clf_0_prot.predict(X_B)
XA_score = clf_1_prot.predict(X_A)
XB_score = clf_1_prot.predict(X_B)

tpr_A, fpr_A = compute_roc_curve(y_A, XA_score, 100)
tpr_B, fpr_B = compute_roc_curve(y_B, XB_score, 100)

x_label = 'FPR'
y_label = 'TPR'
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.plot(fpr_A, tpr_A, color = "m", marker = ".", label = "Women (portuguese class)")
plt.plot(fpr_B, tpr_B, color = "c", marker = ".", label = "Men (portuguese class)")
# plt.plot(fpr_A, tpr_A, color = "m", marker = ".", label = "Weekend Alcohol Consumption Below 2 (portuguese class)")
# plt.plot(fpr_B, tpr_B, color = "c", marker = ".", label = "Weekend Alcohol Consumption Above 2 (portuguese class)")
plt.legend()
plt.show()

