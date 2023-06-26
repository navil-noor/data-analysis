# Import important libraries
# import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

# loading the data
df = pd.read_csv('Data_Analysis_1.csv')  # change location if file is in different directory

# Descriptive analysis using describe() method performs calculations and also provide
# common results such as count, mean, std, etc.
print("Descriptive Statistics")
print(df.describe())

# Using head(3) to return first 3 rows of the dataframe
print(df.head(3))
# Length of the dataframe
print("Number of datasets:", len(df))

# Number of unique values in 'intersection collisions' and 'file_index' columns
print("Number of unique values in Intersection collisions:", df['Intersection_collision'].nunique())
print("Number of unique values in file_index:", df['file_index'].nunique())

# Number of rows and columns
print("Number of rows:", df.shape[0])  # shape has 2 arguments, 0 for rows and 1 for columns
print("Number of columns:", df.shape[1])

# Checking for missing values using isnull() in the dataframe and each column
print("\nMissing values in the Dataframe:")
print(df.isnull())
print("Missing values in each column:")
print(df.isnull().sum())

# Dropping NAN values from the dataframe's rows
# We use dropna() method that removes the rows that contains NULL values
# inplace = True means it will drop all missing values from the original dataset
df.dropna(inplace=True)
# Write the new cleaned dataframe with name clean_data.csv
df.to_csv('clean_data.csv')

# Checking if new dataframe has any null values
print("\nNumber of missing values in each column")
print(df.isnull().sum())
print("\nAfter cleaning, the number of rows:", df.shape[0])

# Use histogram from matplotlib with hist() and plt.show() for plotting
df.hist()
plt.show()

# Using boxplot from matplotlib to check the outliers
df.boxplot()
plt.show()

# Grouping dataframe by death and plotting the new histogram
# For each variable a histogram is plotted for different values of death
df.groupby('Death').hist()
plt.show()

# Plotting the scatter matrix of each of the columns specified against other columns
scatter_matrix(df, alpha=0.2, figsize=(8, 8), diagonal='hist')
plt.show()
