import pandas as pd
import numpy as np


#The primary data structures in pandas are implemented as two classes:

#DataFrame, which you can imagine as a relational data table, with rows and named columns.
#Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.


california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

california_housing_dataframe.describe(include='all')
california_housing_dataframe.head
california_housing_dataframe.hist('housing_median_age')

#print(california_housing_dataframe)



#DataFrame objects can be created by passing a dict mapping string column names to their respective Series. If the Series don't match in length, missing values are filled with special NA/NaN values. Example:
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print (cities['City name'])





np.log(population)   


#Modifying DataFrames is also straightforward. For example, the following code adds two Series to an existing DataFrame:
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']


 

# The example below creates a new Series that indicates whether population is over one million:
population.apply(lambda val: val > 1000000)





#Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:

#The city is named after a saint.
#The city has an area greater than 50 square miles.

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
cities.reindex([2, 0, 1])
print(cities)