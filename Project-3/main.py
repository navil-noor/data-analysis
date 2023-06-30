# Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import folium

# Reading the dataset file into a dataframe
SF = pd.read_csv('Map-Crime_Incidents-Previous_Three_Months.csv')

# Checking the first 5 rows on the dataset
print("********Visualizing 5 rows********")
print(SF.head())
print("Name of columns:\n", SF.columns)  # To view the name of the variables in the DataFrame

print("\nNumber of columns:", SF.shape[1])

print("\nNumber of rows: ", len(SF))

# Using lambda function to select months and days from data transform string into integers
# Then use apply to use the lambda function on the entire column
SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))

# Checking to see if the values in the new columns are integers
# Printing the first five rows of the month and first 2 rows of day
print("\nFirst 5 rows of the month and first 2 rows of the day")
print(SF['Month'][0:5])
print(SF['Day'][0:2])

# Removing the variable in column IncidntNum as it has many NAN values, and it has no value to the analysis.
del SF['IncidntNum']

# Removing Location as it does not add value to the analysis
# drop function used, axis=1 for column, inplace=True as we do not require another value to store the result.
SF.drop('Location', axis=1, inplace=True)

# Checking the new dataframe
print("\nNew columns list:")
print(SF.columns)

# Summarize variables to obtain statistical information
CountCategory = SF['Category'].value_counts()  # value_counts(ascending=True) can be used to get ascending order
print("\nNumber of crimes by type:")
print(CountCategory)

DistrictCategory = SF['PdDistrict'].value_counts(ascending=True)
print("\nNumber of crimes by District in ascending order:")
print(DistrictCategory)

# Logical indexing can be used to select only the rows for which a given condition is satisfied.
AugustCrimes = SF[SF['Month'] == 8]  # 8th month is August, so we can use this to get crimes in August
print("\nCrimes committed in August:")
print(AugustCrimes)
print("\nNumber of crimes in August:", len(AugustCrimes))

# Burglaries committed in August
BurglaryAugust = SF.query('Month == 8 and Category == "BURGLARY"')  # checking 2 conditions using and operator
print("\nNumber of burglaries in August:", len(BurglaryAugust))

# Creating a subset of the dataframe for a specific day (Month=7, Day=4) by using the function query operand
Crime0704 = SF.query('Month == 7 and Day == 4')
print("\nCrimes committed on the 4th Day of the 7th Month:")
print(Crime0704)

# Plotting a graph of the SF dataframe using the longitude ('X') and latitude ('Y') coordinates
plt.title('First Plot')
plt.plot(SF['X'], SF['Y'], 'ro')  # Using "ro" parameter to plot in red and setting the marker shape to a circle
plt.show()

# Identify the number of police department district
pd_districts_unique = np.unique(SF['PdDistrict'])
# Creating a dictionary pd_districts to associate their string to an integer
pd_districts = dict(zip(pd_districts_unique, range(len(pd_districts_unique))))
print("\nNumber of police departments in each district")
print(pd_districts)

# Adding the police department integer id to a new column of the DataFrame: PdDistrictCode using lambda and apply
SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts[row])
# Using the PdDistrictCode to automatically change the color of the new plot
plt.title("Graph using PdDistrictCode")
plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()

# Folium requires the color of the marker to be specified using a hexadecimal value
districts = np.unique(SF['PdDistrict'])
print("\nColors selected for each districts")
print(list(colors.cnames.values())[0:len(districts)])

# Color dictionary for each police department district
color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))
print("\nColor dictionary for each police department district")
print(color_dict)

# Plotting the map using the middle coordinates of the SF Data to center the map (using mean)
# To reduce the computation time, plotEvery variable is created to limit amount of plotted data
map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start=12)
plotEvery = 50
obs = list(zip(SF['Y'], SF['X'], SF['PdDistrict']))

for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2], radius=10).add_to(map_osm)

map_osm.render()
map_osm.save("CrimeMap.html")  # Saving the created map into an HTML file to view
