#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


webpage = requests.get("https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population")


# In[4]:


soup = BeautifulSoup(webpage.content, "html.parser")


# In[5]:


print(soup.prettify())


# In[6]:


soup.title.text


# In[7]:


#Verifying tables and their classes
print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))


# In[8]:


# Creating list with all tables
tables = soup.find_all('table')
tables


# In[9]:


#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='wikitable sortable')
table


# In[10]:


import pandas as pd


# In[11]:


#Defining of the dataframe
#df = pd.DataFrame(columns=['Rank', 'City', 'State', 'Pop_2015', 'Pop_2011', 'Change', 'Area', 'Pop_density_2015', 'Location'])


# In[12]:


# Collecting Ddata
#for row in table.tbody.find_all('tr'):    
    # Find all data for each column
 #   columns = row.find_all('td')
    
  #  if(columns != []):
   #     rank = columns[0].text.strip()
    #    city = columns[1].text.strip()
     #   state = columns[2].text.strip()
      #  pop_2015 = columns[3].span.contents[0].strip('&0.')
       # pop_2011 = columns[4].span.contents[0].strip('&0.')
        #change = columns[5].span.contents[0].strip('&0.')
        #area = columns[6].span.contents[0].strip('&0.')
        #pop_density_2015 = columns[7].span.contents[0].strip('&0.')
        #location = columns[8].span.contents[0].strip('&0.')

        #df = df.append({'Rank': rank, 'City': city, 'Pop_2015': pop_2015, 'Pop_2011': Pop_2011, 'Change': change, 
        #'Area': area, 'Pop_density_2015': pop_density_2015, 'Location': location}, ignore_index=True)


# In[13]:


A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []


# In[14]:


#for row in table.tbody.find_all('tr'):    
    # Find all data for each column
 #   columns = row.find_all('td')

for row in table.find_all('tr'):
    cells=row.find_all('td') 
    if len(cells)==9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))


# In[15]:


df=pd.DataFrame(A,columns=['Rank']) 
df['City']=B
df['State']=C
df['Pop_2015']=D
df['Pop_2011']=E
df['Change']=F
df['Area']=G
df['Pop_density_2015']=H
df['Location']=I
df

#df = pd.DataFrame(columns=['Rank', 'City', 'State', 'Pop_2015', 'Pop_2011', 'Change', 'Area', 'Pop_density_2015', 'Location'])


# In[16]:


df['City']= ['Berlin','Hamburg','Munich', 'Cologne', 'Frankurt am main', 'Stuttgart',
'Düsseldorf', 'Dortmund', 'Essen', 'Leipzig', 'Bremen', 'Dresden', 'Hanover', 'Nuremberg',
'Duisburg', 'Bochum', 'Wuppertal', 'Bielefeld', 'Bonn', 'Münster', 'Karlsruhe',  'Mannheim', 'Augsburg', 'Wiesbaden', 
'Gelsen', 'kirchen', 'Mönchengladbach', 'Braunschweig', 'Chemnitz', 'Kiel', 'Aachen', 'Halle', 'Magdeburg', 
'Freiburg', 'Krefeld', 'Lübeck', 'Oberhausen', 'Erfurt', 'Mainz', 'Rostock', 'Kassel', 'Hagen', 'Hamm,Saabrücken', 
'Mülheim an der Ruhr', 'Potsdam', 'Ludwigshafen', 'Oldenburg', 'Leverkusen', 'Osnabrück', 'Solingen', 'Heidelberg', 'Herne',
'Neuss', 'Darmstadt', 'Paderborn', 'Regensburg', 'Ingolstadt','Würzburg', 'Fürth', 'Wolfsburg', 'Offenbach', 'Ulm', 'Heilbronn', 'Pforzheim',
'Göttingen', 'Bottrop', 'Trier', 'Recklinghausen', 'Reutlingen', 'Bremerhaven', 'Koblenz', 'Bergisch', 'Jena' 'Remscheid', 'Erlangen',
'MoersSiegen','Hildesheim', 'Salzgitter','Hildesheim', 'Salzgitter']


# In[ ]:





# In[17]:


df


# In[18]:


#dff = df[df['City'] == ' cologne']


# In[19]:


#dff


# In[20]:


#df[df['City'] == 'Hamburg']


# In[21]:


df['City'].unique()


# In[22]:


df.drop(df.columns[[0,2,5,7,8]], axis=1, inplace=True)


# In[23]:


pop_df =df


# In[24]:


pop_df


# In[25]:


#pop_df.rename(columns={ "Pop_2015":"pop_2015"} ,inplace=True)
#pop_df.head(5)

pop_df =pop_df.rename(str.lower, axis='columns')
pop_df.info()




# In[26]:


pop_df=pop_df.drop_duplicates(subset=['city'])


# In[27]:


pop_df[pop_df['city'] == 'Kassel']


# In[28]:


import pymysql


# In[ ]:





# In[31]:


schema="my_first_db"  
host="127.0.0.1"     
user="root"
password="password" 
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[32]:


pop_df.to_sql('pop_df',if_exists='append', con=con, index=False)        


# In[ ]:





# In[ ]:





# In[ ]:




