#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from datetime import datetime, date, timedelta
import requests
from pytz import timezone


# In[7]:


def tomorrows_flight_arrivals(icao_list):
  

  today = datetime.now().astimezone(timezone('Europe/Berlin')).date()
  tomorrow = (today + timedelta(days=1))

  list_for_df = []

  for icao in icao_list:
    times = [["00:00","11:59"],["12:00","23:59"]]

    for time in times:
      url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T{time[0]}/{tomorrow}T{time[1]}"
      querystring = {"withLeg":"true","direction":"both","withCancelled":"false","withCodeshared":"true","withCargo":"false","withPrivate":"false"}
      headers = {
          'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
          'x-rapidapi-key': "ba0443fa50msha2f701cd01554f4p1c3963jsnde9cd3f96ab8" 
          }
      response = requests.request("GET", url, headers=headers, params=querystring)
      flights_json = response.json()

      for flight in flights_json['arrivals']:
        flights_dict = {}
        flights_dict['arrival_icao'] = icao
        # .get() is another way of ensuring our code doesn't break
        # in the previous 2 notebooks you learnt about 'if' (cities) and 'try/except' (weather)
        # .get() works similar, it will get the text if possible, if there is no text a None value will be inserted instead
        flights_dict['arrival_time_local'] = flight['arrival'].get('scheduledTimeLocal', None)
        flights_dict['arrival_terminal'] = flight['arrival'].get('terminal', None)
        flights_dict['departure_city'] = flight['departure']['airport'].get('name', None)
        flights_dict['departure_icao'] = flight['departure']['airport'].get('icao', None)
        flights_dict['departure_time_local'] = flight['departure'].get('scheduledTimeLocal', None)
        flights_dict['airline'] = flight['airline'].get('name', None)
        flights_dict['flight_number'] = flight.get('number', None)
        flights_dict['data_retrieved_on'] = datetime.now().astimezone(timezone('Europe/Berlin')).date()
        list_for_df.append(flights_dict)

  return pd.DataFrame(list_for_df)


# In[9]:


airports = ['EDDB','EDDC','EDDE', 'EDDG', 'EDDH', 'EDDK', 'EDDN', 'EDDP', 'EDDV', 'EDDW', 'EDLP', 'EDFM', 'EDLP', 'EDLW', 'EDVK']
flights_data = tomorrows_flight_arrivals(airports)
flights_data.head(5)


# In[10]:


flights_data.drop(flights_data.columns[[3,4]], axis=1, inplace=True)


# In[11]:


flights_data.head(5)


# In[12]:


flights_data.rename(columns={"arrival_icao":"icao", "arrival_time_local":"arrival_time", "departure_time_local":"departure_time", 
                     "location.lon":"location_lon"} ,inplace=True)


# In[13]:


flights_data.head(5)


# In[14]:


#flights_data["city"]= ["Erfurt", "Kasse", "Leipzig",  "Braunschweig Wolfsburg",  "Paderborn", "Hanover", "Frankfurt-am-Main", "Nuremberg", "Dortmund", "Münster", "Dresden",    
#"Mannheim", "Cologne", "Bremen", "Berlin", "Berlin", "Duesseldorf", "Hahn", "Enschede" "Hamburg"]


# In[15]:


flights_data= flights_data.dropna()
flights_data.head(5)


# In[164]:


#flights_data =flights_data.dropna()


# In[16]:


flights_data= flights_data.drop_duplicates(subset=['icao'])


# In[17]:


#flights_data=flights_data[flights_data['icao'].isin(['EDDE', 'EDVK', 'EDDP', 'EDLP', 'EDDV', 'EDDN', 'EDLW', 'EDDG',
                                                    #'EDDC', 'EDFM', 'EDDK', 'EDDW', 'EDDB', 'EDDH'])]

#flights_data = flights_data[flights_data['icao'].isin(['EDDF'])]

#'EDVK', 'EDDP', 'EDLP', 'EDDV', 'EDDN', 'EDLW', 'EDDG','EDDC', 'EDFM', 'EDDK', 'EDDW', 'EDDB', 'EDDH'


# In[18]:


flights_data 


# In[19]:


import pymysql


# In[20]:


schema="my_first_db"   # name of the database you want to use here
host="database-1.cqmnrgykaxgt.eu-central-1.rds.amazonaws.com"        # to connect to your local server=127.0.0.1
user="admin"
password="mypasswordd" # your password!!!! my_lacal_password=passORD11$ amazon_server_pass= mypasswordd
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[21]:


flights_data.to_sql('flights_data',         # 'iss_logs'-> table name;
              if_exists='append', # if_exists -> will create new table if doesn't exist, otherwise, 'append' - will append data to existing table;
              con=con,            # con-> connection string;
              index=False)        # index = False -> will not send index column to database


# In[ ]:





# In[ ]:





# In[ ]:




