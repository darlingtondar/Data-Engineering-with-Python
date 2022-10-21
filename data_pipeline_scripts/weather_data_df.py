#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from datetime import datetime
import pytz


# In[2]:


city = 'Berlin'
API_key = '3d65e33bcfce58283b276eceea8b4f69'

# check out the docs for more info on making an api call https://openweathermap.org/forecast5
url = (f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric")

response = requests.get(url)
json = response.json()

json


# In[3]:


tz = pytz.timezone('Europe/Berlin')
now = datetime.now().astimezone(tz)

now


# In[4]:


# we'll store the information in this dicitonary:
weather_dict = {'city': [],
                'country': [],
                'forecast_time': [],
                'outlook': [],
                'detailed_outlook': [],
                'temperature': [],
                'temperature_feels_like': [],
                'clouds': [],
                'rain': [],
                'snow': [],
                'wind_speed': [],
                'wind_deg': [],
                'humidity': [],
                'pressure': []}
                #'information_retrieved_at': []}

# let's begin the loop
for i in json['list']:
  weather_dict['city'].append(json['city']['name'])
  weather_dict['country'].append(json['city']['country'])
  weather_dict['forecast_time'].append(i['dt_txt'])
  weather_dict['outlook'].append(i['weather'][0]['main'])
  weather_dict['detailed_outlook'].append(i['weather'][0]['description'])
  weather_dict['temperature'].append(i['main']['temp'])
  weather_dict['temperature_feels_like'].append(i['main']['feels_like'])
  weather_dict['clouds'].append(i['clouds']['all'])
  # sometimes the data is missing for rain and snow. As it is not always raining or snowing
  # we cannot make a DataFrame unless the lists are all the same length, therefore missing values are bad
  # here we say try to append a value if there is one. If not, append a 0
  try:
      weather_dict['rain'].append(i['rain']['3h'])
  except:
      weather_dict['rain'].append('0')
  try:
      weather_dict['snow'].append(i['snow']['3h'])
  except:
      weather_dict['snow'].append('0')
  weather_dict['wind_speed'].append(i['wind']['speed'])
  weather_dict['wind_deg'].append(i['wind']['deg'])
  weather_dict['humidity'].append(i['main']['humidity'])
  weather_dict['pressure'].append(i['main']['pressure'])
  #weather_dict['information_retrieved_at'].append(now.strftime("%d/%m/%Y %H:%M:%S"))
  


# In[5]:


json['list'][0]['main']['temp']


# In[6]:


weather_from_dict_df = pd.DataFrame(weather_dict)


# In[7]:


weather_from_dict_df.head(5)


# In[8]:



#cities = ["Düsseldorf", "Dortmund", "Essen", "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg","Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", "Karlsruhe",  "Mannheim", "Augsburg", "Wiesbaden",  "Gelsen", "kirchen", "Mönchengladbach", "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Halle", "Magdeburg",  "Freiburg", "Krefeld", "Lübeck", "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Hamm","Saabrücken", "Mülheim an der Ruhr", "Potsdam", "Ludwigshafen", "Oldenburg", "Leverkusen", "Osnabrück", "Solingen", "Heidelberg", "Herne", "Neuss", "Darmstadt", "Paderborn", "Regensburg", "Ingolstadt","Würzburg", "Fürth", "Wolfsburg", "Offenbach","Ulm", "Heilbronn", "Pforzheim","Göttingen", "Bottrop", "Trier", "Recklinghausen", "Reutlingen", "Bremerhaven", "Koblenz", "Bergisch", "Jena", "Remscheid", "Erlangen", "MoersSiegen","Hildesheim", "Salzgitter","Hildesheim", "Salzgitter"]
#"Erfurt","Kassel", "Leipzig", "Paderborn",  "Hanover", "Frankfurt am main", "Nuremberg", "Münster",  "Dresden","Mannheim",  "Bremen", "Hahn",  "Enschede", "Hamburg"

cities = ["Düsseldorf", "Dortmund", "Essen", "Erfurt","Kassel","Paderborn",  "Hanover", "Frankfurt am main", "Nuremberg", "Münster",  "Dresden","Mannheim", "Leipzig","Bremen", "Hahn",  "Enschede", "Hamburg"]

tz = pytz.timezone('Europe/Berlin')
now = datetime.now().astimezone(tz)

weather_dict = {'city': [],
              'country': [],
              'forecast_time': [],
              'outlook': [],
              'detailed_outlook': [],
              'temperature': [],
              'temperature_feels_like': [],
              'clouds': [],
              'rain': [],
              'snow': [],
              'wind_speed': [],
              'wind_deg': [],
              'humidity': [],
              'pressure': [],
              'information_retrieved_at': []}

for city in cities:
  API_key = '4fe53ee5e34a7d900ed58bd74bbbb0b7'
  url = (f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric")
  response = requests.get(url)
  json = response.json()

  for i in json['list']:
    weather_dict['city'].append(json['city']['name'])
    weather_dict['country'].append(json['city']['country'])
    weather_dict['forecast_time'].append(i['dt_txt'])
    weather_dict['outlook'].append(i['weather'][0]['main'])
    weather_dict['detailed_outlook'].append(i['weather'][0]['description'])
    weather_dict['temperature'].append(i['main']['temp'])
    weather_dict['temperature_feels_like'].append(i['main']['feels_like'])
    weather_dict['clouds'].append(i['clouds']['all'])
    try:
        weather_dict['rain'].append(i['rain']['3h'])
    except:
        weather_dict['rain'].append('0')
    try:
        weather_dict['snow'].append(i['snow']['3h'])
    except:
        weather_dict['snow'].append('0')
    weather_dict['wind_speed'].append(i['wind']['speed'])
    weather_dict['wind_deg'].append(i['wind']['deg'])
    weather_dict['humidity'].append(i['main']['humidity'])
    weather_dict['pressure'].append(i['main']['pressure'])
    weather_dict['information_retrieved_at'].append(now.strftime("%d/%m/%Y %H:%M:%S"))

weather_df = pd.DataFrame(weather_dict)
weather_df


# In[9]:


weather_df.info()


# In[10]:


weather_df.drop(weather_df.columns[[4,6,7,8, 9, 11, 14]], axis=1, inplace=True)


# In[11]:


weather_df


# In[12]:


weather_df['city'].unique()


# In[13]:


weather_df=weather_df[weather_df['city'].isin(['Düsseldorf', 'Dortmund', 'Essen', 'Erfurt', 'Kassel', 'Paderborn','Hanover','Nuremberg', 'Münster', 'Dresden', 'Mannheim', 'Leipzig', 'Bremen', 'Hamburg' ])]
weather_df


# In[14]:


#pip install sqlalchemy 
import sqlalchemy # install if needed


# In[15]:


weather_df =weather_df.dropna()
weather_df


# In[16]:


weather_df['city'].unique()


# In[17]:


import pymysql


# In[18]:


#weather_df = weather_df[weather_df['city'] == 'Hamburg']


#weather_df = weather_df[weather_df["city"].isin(['Cologne'])]



# In[19]:


weather_df


# In[20]:


schema="my_first_db"   # name of the database you want to use here
host="database-1.cqmnrgykaxgt.eu-central-1.rds.amazonaws.com"        # to connect to your local server=127.0.0.1
user="admin"
password="mypasswordd" # your password!!!! my_lacal_password=passORD11$ amazon_server_pass= mypasswordd
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
        


# In[21]:


weather_df.to_sql('weather_df',         # 'iss_logs'-> table name;
              if_exists='append', # if_exists -> will create new table if doesn't exist, otherwise, 'append' - will append data to existing table;
              con=con,            # con-> connection string;
              index=False)        # index = False -> will not send index column to database


                            


# In[ ]:





# In[ ]:





# In[ ]:




