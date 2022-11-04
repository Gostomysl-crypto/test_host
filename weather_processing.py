"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import numpy as np

# TODO Import the dataset

path = r'./data/weather_dataset.data'
missing_values = ["n/a", "na", "--", "*", 'None', 'nan', 'NaN', 'nodata', 'NONE', '1.0k']

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data = pd.read_csv(path, delim_whitespace=True, na_values=missing_values)

data["Date"] = pd.to_datetime(data[["Yr", "Mo", "Dy"]].astype(str).agg('-'.join, axis=1))

data = data.drop(columns=["Yr", "Mo", "Dy"])

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

data["loc1"] = data["loc1"].str.replace(",", ".").astype(float)
data["loc2"] = data["loc2"].str.replace(",", ".").astype(float)
data["loc3"] = data["loc3"].str.replace(",", ".").astype(float)
data["loc4"] = data["loc4"].str.replace(",", ".").astype(float)
data["loc5"] = data["loc5"].str.replace(",", ".").astype(float)
data["loc6"] = data["loc6"].str.replace(",", ".").astype(float)
data["loc7"] = data["loc7"].str.replace(",", ".").astype(float)
data["loc8"] = data["loc8"].str.replace(",", ".").astype(float)
data["loc11"] = data["loc11"].str.replace(",", ".").astype(float)
data["loc12"] = data["loc12"].str.replace(",", ".").replace('-123*None', -123).astype(float)

data.drop(data[data['loc9'] >= max(data['loc9'])].index, inplace=True)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it

data["Date"] = np.where(pd.DatetimeIndex(data["Date"]).year < 2000, data.Date, data.Date - pd.offsets.DateOffset(years=100))

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

newData = data.set_index("Date")
newData.index.astype("datetime64[ns]")

# TODO Compute how many values are missing for each location over the entire record
print("How many values are missing for each location over the entire record: ")
print(newData.isnull().values.ravel().sum())

# TODO Compute how many non-missing values there are in total
x = newData.count()
print("Total Non-missing values are :", x.sum())

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

y = newData.mean()

print("The mean windspeeds of the windspeeds over all the locations and all the times: ")

print(y.mean())

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

def stats(x):
    x = pd.Series(x)
    Min = x.min()
    Max = x.max()
    Mean = x.mean()
    Std = x.std()
    res = [Min, Max, Mean, Std]
    indx = ["Min", "Max", "Mean", "Std"]
    res = pd.Series(res, index=indx)
    return res
loc_stats = newData.apply(stats)


# TODO Find the average windspeed in January for each location

january_data = newData[newData.index.month == 1]
print("January windspeeds:")
print(january_data.mean())


# TODO Downsample the record to a yearly frequency for each location

print("Yearly:\n", newData.resample('A').mean())

# TODO Downsample the record to a monthly frequency for each location

print("Monthly:", newData.resample('M').mean())

# TODO Downsample the record to a weekly frequency for each location

print("Weekly:", newData.resample('W').mean())

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

first_year = newData[newData.index.year == 1961]
stats1 = newData.resample('W').mean().apply(lambda x: x.describe())
print(stats1)