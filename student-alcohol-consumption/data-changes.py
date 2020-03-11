import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from normalizedata import normal

##################################################################################################
#Merge Data
mathData = pd.read_csv("student-mat.csv")
portData = pd.read_csv("student-por.csv")

combData = pd.merge(mathData,portData,on=["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])

# Export new DF to CSV
combData.to_csv("combData.csv")
##################################################################################################


##################################################################################################
#Change all data to numeric values

combData["school"].replace({"GP": "0", "MS": "1"}, inplace=True)
combData["sex"].replace({"M": "0", "F": "1"}, inplace=True)
combData["address"].replace({"U": "0", "R": "1"}, inplace=True)
combData["famsize"].replace({"GT3": "0", "LE3": "1"}, inplace=True)
combData["Pstatus"].replace({"A": "0", "T": "1"}, inplace=True)
combData["schoolsup_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["famsup_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["paid_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["activities_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["nursery"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["higher_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["internet"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["romantic_x"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["schoolsup_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["famsup_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["paid_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["activities_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["higher_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["romantic_y"].replace({"no": "0", "yes": "1"}, inplace=True)
combData["guardian_x"].replace({"mother": "0", "father": "1", "other": "2"}, inplace=True)
combData["guardian_y"].replace({"mother": "0", "father": "1", "other": "2"}, inplace=True)
combData["Mjob"].replace({"at_home": "0", "health": "1", "services": "2", "teacher": "3", "services": "4", "other": "5"}, inplace=True)
combData["Fjob"].replace({"at_home": "0", "health": "1", "services": "2", "teacher": "3", "services": "4", "other": "5"}, inplace=True)
combData["reason"].replace({"course": "0", "other": "1", "reputation": "2", "home": "3"}, inplace=True)


combData.loc[combData['G3_x'] < 14, 'G3_x'] = 0
combData.loc[combData['G3_x'] >= 14, 'G3_x'] = 1
combData.loc[combData['G3_y'] < 14, 'G3_y'] = 0
combData.loc[combData['G3_y'] >= 14, 'G3_y'] = 1

combData.to_csv("numericData.csv")


normal_x = normal("G3_x")
normal_y = normal("G3_y")

normal_x.to_csv("DataX.csv")
normal_y.to_csv("DataY.csv")

