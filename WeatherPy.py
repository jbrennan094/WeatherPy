
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from random import sample
import matplotlib.pyplot as plt
import datetime
import sys


# In[ ]:


# Read in csv file
df = pd.read_csv("data/worldcities.csv")
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
cities_sample = df.iloc[idx,:]


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
for index, row in cities_sample.iterrows():
    
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
    
    # Append sample df
    cities_sample.set_value(index, "Temp", tmp_value)
    cities_sample.set_value(index, "Humidity", humidity_value)
    cities_sample.set_value(index, "Cloudiness", cloudiness_value)
    cities_sample.set_value(index, "Wind Speed", wind_speed_value)
      
# Create new csv file for cities_sample
# (This way you won't have to make 500 requests again.)
cities_sample.to_csv("output/cities_sample.csv", sep=",")


# In[ ]:


## Check out appended dataframe
cities_sample.head()


# In[ ]:


# Temperature vs Latitude
plt.scatter(cities_sample["Temp"], cities_sample["Latitude"])

plt.title("Temperature across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Temperature")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Humidity vs Latitude
plt.scatter(cities_sample["Humidity"], cities_sample["Latitude"])

plt.title("Humidity across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Humidity")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Cloudiness vs Latitude
plt.scatter(cities_sample["Cloudiness"], cities_sample["Latitude"])

plt.title("Cloudiness across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Cloudiness")
plt.ylabel("Latitude")
plt.grid()


# In[ ]:


# Wind Speed vs Latitude
plt.scatter(cities_sample["Wind Speed"], cities_sample["Latitude"])

plt.title("Wind Speed across Latitude, " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
plt.xlabel("Wind Speed")
plt.ylabel("Latitude")
plt.grid()

