import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def get_count(data, col):
    vals = [0,0,0,0,0]
    for i, row in data.iterrows():
        v = row[col]-1
        vals[v] += 1
    return vals

def normalize_col(data, all_col_names, col, col_counts):
    new_df = pd.DataFrame(columns=all_col_names)
    high = max(col_counts)
    for i, row in data.iterrows():
        index = row[col]-1
        count_of_col = col_counts[index]

        times_to_dupe = math.ceil(high/count_of_col)

        for i in range(0, times_to_dupe):
            new_df = new_df.append(row)
    return new_df

# Normalize each col in the list
def normalize_all(data, all_cols):
    for col in all_cols:
        print("Normalizing " + col + "...")
        count = get_count(data, col)
        data = normalize_col(data, data.columns, col, count)
    return data

def print_counts(data, cols):
    for col in cols: print(str(col) + ": " + str(get_count(data, col)))    

# setup
data = pd.read_csv("combData.csv")
cols_to_normalize = ["Dalc_y"] # for some reason we can only normalize on on col???

# Print the current counts
print("Before:")
print_counts(data, cols_to_normalize)

# Normalize on all
normalized_df = normalize_all(data, cols_to_normalize)

# Print the new counts
print("After:")
print_counts(normalized_df, cols_to_normalize)

# Write to csv
normalized_df.to_csv("combData-normal.csv")