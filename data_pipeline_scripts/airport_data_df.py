#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import pandas as pd

url = "https://aerodatabox.p.rapidapi.com/airports/search/location/51.1657/10.4515/km/1000/20"

querystring = {"withFlightInfoOnly":"true"}

headers = {
	"X-RapidAPI-Key": "93c57aaa12msh25b6811f4f402cdp1bd0bajsna55400397a90",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#We cann ow turn this into a dataframe using json_normalize()
# In[8]:


pd.json_normalize(response.json()['items'])


# In[9]:


icaon = pd.json_normalize(response.json()['items'])


# In[10]:


icaon.head(5)


# In[11]:


icaon.drop(icaon.columns[[1,3,5]], axis=1, inplace=True)


# In[12]:


icaon.head(5)


# In[13]:


icaon.rename(columns={"name":"airport_name", "municipalityName":"city", "location.lat":"location_lat", 
                     "location.lon":"location_lon"} ,inplace=True)


# In[14]:


icaon.head()


# In[15]:


icaon['city'].unique()


# In[16]:



icaon=icaon[icaon['city'].isin([ 'Leipzig','Paderborn','Hanover',
                                     'Nuremberg', 'Dortmund', 'Münster', 'Dresden',
                                            'Mannheim', 'Bremen','Hamburg','Erfurt','Kassel', 'Cologne', 'Berlin'])]
icaon.head(5)


# In[17]:


icaon =icaon.dropna()
icaon.head(5)


# In[18]:


#icaon[icaon['city'] == 'paderborn']


# In[19]:


icaon['icao'].unique()


# In[20]:


icaon=icaon.drop_duplicates(subset=['icao'])


# In[21]:


icaon=icaon.drop_duplicates(subset=['city'])


# In[22]:


icaon=icaon.drop_duplicates(subset=['airport_name'])


# In[23]:


icaon.head(4)


# In[24]:


import pymysql


# In[25]:


schema="my_first_db"   # name of the database you want to use here
host="database-1.cqmnrgykaxgt.eu-central-1.rds.amazonaws.com"        # to connect to your local server=127.0.0.1
user="admin"
password="mypasswordd" # your password!!!! my_lacal_password=passORD11$ amazon_server_pass= mypasswordd
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[26]:


icaon.to_sql('icaon',         # 'iss_logs'-> table name;
              if_exists='append', # if_exists -> will create new table if doesn't exist, otherwise, 'append' - will append data to existing table;
              con=con,            # con-> connection string;
              index=False)        # index = False -> will not send index column to database


# In[ ]:





# In[ ]:




