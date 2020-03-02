import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mathData = pd.read_csv("student-mat.csv")
portData = pd.read_csv("student-por.csv")

combData = pd.merge(mathData,portData,on=["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])

# Export new DF to CSV
combData.to_csv("combData.csv")
