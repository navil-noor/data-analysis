# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the csv file
salesDist = pd.read_csv('stores-dist.csv')
print(salesDist.head())  # checking first 5 rows

# as column headings have spaces we rename them for easier data processing
# district column has no relevance here, so it can be dropped
salesDist = salesDist.rename(columns={'annual net sales': 'sales', 'number of stores in district': 'stores'})
print(salesDist.head())

# We check correlation using the corr method
print(salesDist.corr(method='pearson'))

# the correlation coefficient of district is low compared to others so it can be dropped
sales = salesDist.drop(columns={'district'})  # district is removed using drop method
print(sales.head())  # checking new dataframe without district

# Plotting the data, assigning stores to independent variable x and sales to dependant variable y
x = sales.stores
y = sales['sales']
plt.figure(figsize=(10, 5))  # increasing the size of the plot
plt.plot(x, y, 'o', markersize=10)  # scatter plot with number of stores  vs annual net sales

# adding labels to the axis and increasing the size of the font
plt.xlabel('No. of stores in the District', fontsize=20)
plt.ylabel('Annual Net Sales', fontsize=20)

# increasing the ticks' font size on the axis
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()  # to plot the figure

# Numpy polyfit is used for linear regression to fit the data
m, b = np.polyfit(x, y, 1)  # Producing the slope of the line (m) and y-intercept (b)
print('The slope of line is {:.2f}.'.format(m))
print('The y-intercept is {:.2f}.'.format(b))
print('The best fit simple linear regression line is {:.2f}x + {:.2f}.'.format(m, b))

# The centroid of the dataset is calculated by using the mean function
x_mean = x.mean()
y_mean = y.mean()
print('The centroid is x = {:.2f} and y = {:.2f}.'.format(x_mean, y_mean))

# On the plot we overlay the regression line and the centroid point
plt.figure(figsize=(10, 5))  # enlarging the plot size
plt.plot(x, y, 'o', markersize=12, label="Annual Net Sales")  # plotting scatter plot
plt.plot(x_mean, y_mean, '*', markersize=20, color='r')  # plotting the centroid point
plt.plot(x, m * x + b, '-', label='Simple Linear Regression Line', linewidth=4)  # plotting the linear regression line

# Generating the axis labels
plt.xlabel('Number of Stores in District', fontsize=20)
plt.ylabel('Annual Net Sales', fontsize=20)

# increasing the ticks' font size on the axis
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# Pointing out the centroid point
plt.annotate('Centroid', xy=(x_mean - 0.1, y_mean - 5), xytext=(x_mean - 3, y_mean - 20),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=20)

# Creating the legend
plt.legend(loc='upper right', fontsize=10)
plt.title('Plot with Centroid point')  # labeling the plot
plt.show()


# Defining a function to predict the net sales from the regression line
def predict(number):
    if number >= 1:
        predict = m * number + b
        return predict
    else:
        print("At least 1 store is needed to predict annual net sales")


# testing out the function
print(predict(4))
