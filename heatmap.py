
# coding: utf-8

# In[ ]:


from gmplot import gmplot
import pandas as pd
import numpy as np


# In[ ]:


# Import cities dataframe
cities_df = pd.read_csv("output/cities_sample.csv")
cities_df.head()

# Import Temperature gradient hex codes
hex_code_df = pd.read_csv("data/temp_gradient_hex_codes.csv", header=None)

# Reverse order (Cold -> Hot)
arr = np.array(hex_code_df[1])
arr = arr[::-1]
hex_code_df[1] = arr


# In[ ]:


# Number of bins
num_bins = hex_code_df.shape[0]-1

# Organize data
temp = np.array(cities_df["Temp"])

# Min temp
temp_min = np.min(temp)

# Max temp
temp_max = np.max(temp)

# Bins
bins = np.linspace(temp_min, temp_max, num=num_bins)

# Assign values temps to bin
temp_bin = np.digitize(temp, bins)

# Append to cities dataframe
cities_df["Bin Value"] = temp_bin


# In[ ]:


# Center lat, long
center_lat = cities_df["Latitude"].mean()
center_lng = cities_df["Longitude"].mean()

# Create gmap object
gmap = gmplot.GoogleMapPlotter(center_lat=center_lat, center_lng=center_lng, zoom=3)


# In[ ]:


# Loop through to create scatter plot
for index, row in cities_df.iterrows():
    
    lat = row["Latitude"]
    
    lng = row["Longitude"]
    
    lat_zip, lng_zip = zip(*[(lat,lng)])
    
    idx = row["Bin Value"]
    
    color = hex_code_df.iloc[idx, -1]
    color = "#" + color[1:]
    ##color = color[1:]
    color = color.upper()
    
    #gmap.scatter(lat_zip, lng_zip, color=, size=60, marker=False)
    gmap.circle(lat, lng, 50000, color=color, ew=2)


# In[ ]:


gmap.draw("heatmap.html")

