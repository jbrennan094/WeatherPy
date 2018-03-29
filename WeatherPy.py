
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
from citipy import City
from random import sample
import json
import matplotlib.pyplot as plt
import datetime


# In[ ]:


# Read in csv file
df = pd.read_csv("worldcities.csv")
df.head()


# In[ ]:


# Create new column (temp)
df["Temp"] = ""
df["Humidity"] = ""
df["Cloudiness"] = ""
df["Wind Speed"] = ""


# In[ ]:


# Number of rows in dataframe
nrows = df.shape[0]

# Choose 500 random cities
idx = sample(range(nrows), 500)

# Create sample dataframe
sample_df = df.iloc[idx,:]


# In[ ]:


## Get temp for 500 random cities

# Today's date (for plots)
now = datetime.datetime.now()

# Loop counter
n = 0

# Base Url for openweather api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# My api key
api_key = "&APPID=78328d7bbd5d23c60c8a243e00bbe313"

# Loop through the sample dataframe and request temperature to append the dataframe
for index, row in sample_df.iterrows():
    
    # Get Latitude value from sample df
    lat_value = row["Latitude"]
    
    # Get Longitude value from sample df
    long_value = row["Longitude"]
    
    # Construct url for the request
    target_url = base_url + "lat=" + str(lat_value) + "&lon=" + str(long_value) + api_key
    
    # Make the request
    response = requests.get(target_url).json()
    
    # Extract temperature value
    tmp_value = float(response["main"]["temp"])
    
    # Extract humidity value
    humidity_value = float(response["main"]["humidity"])
    
    # Extract Cloudiness value
    cloudiness_value = float(response["clouds"]["all"])
    
    # Extract Wind Speed value
    wind_speed_value = float(response["wind"]["speed"])
    
    # Print log
    print(n)
    print("City number: ", index)
    print("City Name: ", row["City"])
    print("Request URL: ", target_url)
    print("--------------------------------------------------------------")
    
    # Update counter
    n += 1
    
    # View json, pretty format 
    #print(json.dumps(response, indent=4, sort_keys=True))
    
    # Append sample df
    sample_df.set_value(index, "Temp", tmp_value)
    sample_df.set_value(index, "Humidity", humidity_value)
    sample_df.set_value(index, "Cloudiness", cloudiness_value)
    sample_df.set_value(index, "Wind Speed", wind_speed_value)
      
# Create new csv file for sample_df
# (This way you won't have to make 500 requests again.)
sample_df.to_csv("sample_df.csv", sep=",")


# In[ ]:


## Transform the columns to be numer
sample_df.head()


# In[ ]:


# Temperature vs Latitude
plt.scatter(sample_df["Temp"], sample_df["Latitude"])

plt.title("Temperature across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Temperature")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Humidity vs Latitude
plt.scatter(sample_df["Humidity"], sample_df["Latitude"])

plt.title("Humidity across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Humidity")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Cloudiness vs Latitude
plt.scatter(sample_df["Cloudiness"], sample_df["Latitude"])

plt.title("Cloudiness across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Cloudiness")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Wind Speed vs Latitude
plt.scatter(sample_df["Wind Speed"], sample_df["Latitude"])

plt.title("Wind Speed across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Wind Speed")
plt.ylabel("Latitude")
plt.grid()

