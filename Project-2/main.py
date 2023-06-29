# Import library
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loading the data
brainFile = 'brainsize.csv'
brainFrame = pd.read_csv(brainFile)

# Verifying the dataframe has been loaded by printing first five entries
print(brainFrame.head())

# Descriptive analysis using describe() method performs calculations and also provide
# common results such as count, mean, std, etc.
print("\nDescriptive Statistics")
print(brainFrame.describe())

# Separating the data into male and female category
menDf = brainFrame[(brainFrame.Gender == 'Male')]
womenDf = brainFrame[(brainFrame.Gender == 'Female')]

# Plotting the graphs of men IQ with the 3 different measures (PIQ, FSIQ, VIQ)
menMeanSmarts = menDf[['PIQ', 'FSIQ', 'VIQ']].mean(axis=1)  # Calculating mean value of the 3 measures
plt.scatter(menMeanSmarts, menDf['MRI_Count'])  # Scatterplot graph between mean and MRI count
plt.show()

# Plotting the graphs of women IQ with the 3 different measures (PIQ, FSIQ, VIQ)
womenMeanSmarts = womenDf[['PIQ', 'FSIQ', 'VIQ']].mean(axis=1)
plt.scatter(womenMeanSmarts, womenDf['MRI_Count'])
plt.show()

# Converting string values into floats to perform correlation
womenNoGenderDf = womenDf.drop('Gender', axis=1)
womenNoGenderDf = womenNoGenderDf[womenNoGenderDf.columns].astype(float)

menNoGenderDf = menDf.drop('Gender', axis=1)
menNoGenderDf = menNoGenderDf[menNoGenderDf.columns].astype(float)

# Calculating the Correlation against brainFrame for the female-only data using corr(method='pearson')
print("\nCorrelation for female-only data")
print(womenNoGenderDf.corr(method='pearson'))  # Same method can be used for menDf

# Plotting the correlation heatmap using seaborn library
wCorr = womenNoGenderDf.corr()  # Generates a correlation table based on the womenNoGenderDf dataframe and stores it
# on wcorr.
sns.heatmap(wCorr)  # Uses the seaborn heatmap() method to generate and plot the heatmap.
plt.title('Women Correlation')  # Title name to differentiate between the two plots
plt.show()
"""Weight and height variables almost don't have any correlation with FSIQ, VIQ, and PIQ for their correlation values 
are close to 0.0. MRI_Count has slightly correlation between all the variables for the correlation values are between 
0.2 to 0.6."""

mCorr = menNoGenderDf.corr()
sns.heatmap(mCorr)
plt.title('Men Correlation')
plt.show()
"""Weight and height variables almost don't have any correlation with FSIQ, VIQ, and PIQ for their correlation values 
are close to 0.0. MRI_Count has a fairly high correlation between all the variables for the correlation values are 
between 0.4 to 0.8."""
