import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
#school
countSchool = 0
for x in combData['school']:
    if x == 'GP':
        combData.school[countSchool] = 0
    if x == 'MS':
        combData.school[countSchool] = 1
    countSchool = countSchool + 1

countSex = 0
for x in combData['sex']:
    if x == 'F':
        combData.sex[countSex] = 0
    if x == 'M':
        combData.sex[countSex] = 1
    countSex = countSex + 1

countAddress = 0
for x in combData['address']:
    if x == 'U':
        combData.address[countAddress] = 0
    if x == 'R':
        combData.address[countAddress] = 1
    countAddress = countAddress + 1

countFamsize = 0
for x in combData['famsize']:
    if x == 'GT3':
        combData.famsize[countFamsize] = 0
    if x == 'LE3':
        combData.famsize[countFamsize] = 1
    countFamsize = countFamsize + 1

countPstatus = 0
for x in combData['Pstatus']:
    if x == 'A':
        combData.Pstatus[countPstatus] = 0
    if x == 'T':
        combData.Pstatus[countPstatus] = 1
    countPstatus = countPstatus + 1


def yesno(col):
    count = 0
    for x in col:
        if x == 'yes':
            col[count] = 0
        if x == 'no':
            col[count] = 1
        count = count + 1


yesno(combData.schoolsup_x)
yesno(combData.famsup_x)
yesno(combData.paid_x)
yesno(combData.activities_x)
yesno(combData.nursery)
yesno(combData.higher_x)
yesno(combData.internet)
yesno(combData.romantic_x)

yesno(combData.schoolsup_y)
yesno(combData.famsup_y)
yesno(combData.paid_y)
yesno(combData.activities_y)
yesno(combData.higher_y)
yesno(combData.romantic_y)

combData["guardian_x"].replace({"mother": "0", "father": "1", "other": "2"}, inplace=True)
combData["guardian_y"].replace({"mother": "0", "father": "1", "other": "2"}, inplace=True)
combData["Mjob"].replace({"at_home": "0", "health": "1", "services": "2", "teacher": "3", "services": "4", "other": "5"}, inplace=True)
combData["Fjob"].replace({"at_home": "0", "health": "1", "services": "2", "teacher": "3", "services": "4", "other": "5"}, inplace=True)
combData["reason"].replace({"course": "0", "other": "1", "reputation": "2", "home": "3"}, inplace=True)

combData.to_csv("numericData.csv")

