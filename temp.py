# import libraries
import numpy as np
import pandas as pd

# 1
# URL object
URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
df = pd.read_html(URL)
df = df[2]

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 1 (name of country and value of GDP quoted by IMF)
df = df[[0,1]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
top = df.iloc[1:11,:]

# Assign column names as "Country" and "GDP (Million USD)"
top.columns = ['Country','GDP (Million USD)']

# 2
# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
print(top.info())
top['GDP (Million USD)'] = top['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
top['GDP (Million USD)'] = top['GDP (Million USD)']/1000

# Use numpy.round() method to round the value to 2 decimal places.
top['GDP (Million USD)'] = np.round(top['GDP (Million USD)'], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
top = top.rename(columns = {'GDP (Million USD)': 'GDP (Billion USD)'})

#3
# Load the DataFrame to the CSV/Excel file named "Largest_economies.csv"
top.to_csv("./Largest_economies.csv")
top.to_excel("./Largest_economies.xlsx")
