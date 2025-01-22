<h1 align="center">:globe_with_meridians: GDP Data from different countries</h1>
<h1 align="center">Data extraction and processing</h1>

<h2>💻 Tool I Used:</h2>
<ul>
   <li>APIs process</li>
   <li>Python Language</li>
   <li>Spyder IDE</li>
   <li>Pandas & Numpy libraries</li>
</ul>

<h2>ℹ️ Scenario</h2>
<p>An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).</p>
<p>The required data seems to be available on the URL: <a href="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29">List of countries by GDP</a></p>

<h2>🔎 Objectives</h2>
<ul>
   <li>Use Webscraping to extract required information from a website.</li>
   <li>Use Pandas to load and process the tabular data as a dataframe.</li>
   <li>Use Numpy to manipulate the information contatined in the dataframe.</li>
   <li>Load the updated dataframe to CSV file.</li>
</ul>

<h2>📊 The Analysis</h2>
<h3>Import required libraries</h3>
<p>Import <b>numpy</b> and <b>pandas</b> library</p>

```python
import numpy as np
import pandas as pd
```

<h3>Extract data using Web Scraping</h3>
<p>You use Pandas library to extract the required table directly as a DataFrame. Note that the required table is the third one on the website, as shown in the image below.</p>

```python
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
```

![image](https://github.com/user-attachments/assets/3ffb8ab7-bd94-45ad-8575-49d2acce64b8)


<h3>Customize Data</h3>
<p>Modify the GDP column of the DataFrame, converting the value available in Million USD to Billion USD. The round() method of Numpy library is to round the value to 2 decimal places. Modify the header of the DataFrame to GDP (Billion USD).</p>

```python
# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
print(top.info())
top['GDP (Million USD)'] = top['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
top['GDP (Million USD)'] = top['GDP (Million USD)']/1000

# Use numpy.round() method to round the value to 2 decimal places.
top['GDP (Million USD)'] = np.round(top['GDP (Million USD)'], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
top = top.rename(columns = {'GDP (Million USD)': 'GDP (Billion USD)'})
```
![image](https://github.com/user-attachments/assets/657ee273-9fc2-4959-a1d1-911b75f757b6)

<h3>Export Data</h3>
<p>Load the DataFrame to the CSV file named "Largest_economies.csv"</p>

```python
top.to_csv("./Largest_economies.csv")
top.to_excel("./Largest_economies.xlsx")
```

![image](https://github.com/user-attachments/assets/0e8e3203-e330-492f-9a51-7c28c30ff033)

<h2>📍 Conclusion</h2>
<p>The top 10 largest economies in the world, ranked by their GDP in Billion USD as reported by the International Monetary Fund (IMF), include countries such as the USA, China, Germany, Japan, India, the UK, France, Italy, Canada, and Brazil.</p> 
<p>The United States leads with the highest GDP, totaling 30,337.2 billion USD, followed by China at 19,534.9 billion USD.</p> 
<p>This list also features European Union members, including Germany (4,921.56 billion USD), France (3,283.43 billion USD), and Italy (2,459.6 billion USD).</p>
