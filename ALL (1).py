#!/usr/bin/env python
# coding: utf-8

# ## RQ1

# Let's import the libraries

# In[2]:


import pandas as pd
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",10)


# Let's read the data from the different months:

# In[3]:


Location_Jan = r"/Users/daniele/Documents/yellow_tripdata_2018-01.csv"
Location_Feb = r"/Users/daniele/Documents/yellow_tripdata_2018-02.csv"
Location_Mar = r"/Users/daniele/Documents/yellow_tripdata_2018-03.csv"
Location_Apr = r"/Users/daniele/Documents/yellow_tripdata_2018-04.csv"
Location_May = r"/Users/daniele/Documents/yellow_tripdata_2018-05.csv"
Location_Jun = r"/Users/daniele/Documents/yellow_tripdata_2018-06.csv"


# We start the analysis for the january month.

# In[4]:


nytaxi = pd.read_csv(Location_Jan, usecols=[0,1,2,7]) 


# In[46]:


nytaxi.head()


# In[5]:


Location_2 =r"/Users/daniele/Documents/taxi_zone_lookup .csv"
nyBorough =pd.read_csv(Location_2, usecols=[0,1], sep = ';')
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.head()


# For each of the borough in NY, without considering the Unknown borough, we compute the average numbers of trips. To do this we select the number of rows (each row is a trip) for the specific borough and considering the variable tpep_pickup_datetime when takes value in 2018-01 and then we divide for the number of days in each month.

# 

# In[48]:


df = df_full


# In[49]:


df_Man_Jan = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_Man_Jan = len(df_Man_Jan)/31
df_Bro_Jan = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_Bro_Jan = len(df_Bro_Jan)/31
df_Bru_Jan = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_Bru_Jan = len(df_Bru_Jan)/31
df_EWR_Jan = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_EWR_Jan = len(df_EWR_Jan)/31
df_Queens_Jan = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_Queens_Jan = len(df_Queens_Jan)/31
df_Staten_Jan = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
av_Staten_Jan = len(df_Staten_Jan)/31


# Let's do the same for February...

# In[50]:


Location_Feb = r"/Users/daniele/Documents/yellow_tripdata_2018-02.csv"
nytaxi = pd.read_csv(Location_Feb, usecols=[0,1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[51]:


df.head()


# In[53]:


df_Man = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_Man_Feb = len(df_Man)/28
df_Bro = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_Bro_Feb = len(df_Bro)/28
df_Bru = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_Bru_Feb = len(df_Bru)/28
df_EWR = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_EWR_Feb = len(df_EWR)/28
df_Queens = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_Queens_Feb = len(df_Queens)/28
df_Staten = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
av_Staten_Feb = len(df_Staten)/28


# Now March and so on...

# In[54]:


Location_March = r"/Users/daniele/Documents/yellow_tripdata_2018-03.csv"
nytaxi = pd.read_csv(Location_March, usecols=[0,1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[56]:


df_Man = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_Man_March = len(df_Man)/31
df_Bro = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_Bro_March = len(df_Bro)/31
df_Bru = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_Bru_March = len(df_Bru)/31
df_EWR = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_EWR_March = len(df_EWR)/31
df_Queens = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_Queens_March = len(df_Queens)/31
df_Staten = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
av_Staten_March = len(df_Staten)/31


# In[57]:


Location_April = r"/Users/daniele/Documents/yellow_tripdata_2018-04.csv"
nytaxi = pd.read_csv(Location_April, usecols=[0,1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[58]:


df_Man = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_Man_April = len(df_Man)/30
df_Bro = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_Bro_April = len(df_Bro)/30
df_Bru = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_Bru_April = len(df_Bru)/30
df_EWR = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_EWR_April = len(df_EWR)/30
df_Queens = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_Queens_April = len(df_Queens)/30
df_Staten = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
av_Staten_April = len(df_Staten)/30


# In[59]:


Location_May = r"/Users/daniele/Documents/yellow_tripdata_2018-05.csv"
nytaxi = pd.read_csv(Location_May, usecols=[0,1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[60]:


df_Man = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_Man_May = len(df_Man)/31
df_Bro = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_Bro_May = len(df_Bro)/31
df_Bru = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_Bru_May = len(df_Bru)/31
df_EWR = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_EWR_May = len(df_EWR)/31
df_Queens = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_Queens_May = len(df_Queens)/31
df_Staten = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
av_Staten_May = len(df_Staten)/31


# In[61]:


Location_June = r"/Users/daniele/Documents/yellow_tripdata_2018-06.csv"
nytaxi = pd.read_csv(Location_June, usecols=[0,1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[62]:


df_Man = df.loc[(df['Borough']=='Manhattan')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_Man_June = len(df_Man)/30
df_Bro = df.loc[(df['Borough']=='Bronx')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_Bro_June = len(df_Bro)/30
df_Bru = df.loc[(df['Borough']=='Brooklyn')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_Bru_June = len(df_Bru)/30
df_EWR = df.loc[(df['Borough']=='EWR')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_EWR_June = len(df_EWR)/30
df_Queens = df.loc[(df['Borough']=='Queens')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_Queens_June = len(df_Queens)/30
df_Staten = df.loc[(df['Borough']=='Staten Island')  & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
av_Staten_June = len(df_Staten)/30


# Now we collect all the averages together and then we plot them in order to have a time series of averages for each borough considered.

# In[63]:


average_Man = [av_Man_Jan, av_Man_Feb, av_Man_March, av_Man_April, av_Man_May, av_Man_June]
average_Bronx = [av_Bro_Jan, av_Bro_Feb, av_Bro_March, av_Bro_April, av_Bro_May, av_Bro_June]
average_Bru = [av_Bru_Jan, av_Bru_Feb, av_Bru_March, av_Bru_April, av_Bru_May, av_Bru_June]
average_EWR = [av_EWR_Jan, av_EWR_Feb, av_EWR_March, av_EWR_April, av_EWR_May, av_EWR_June]
average_Queens = [av_Queens_Jan, av_Queens_Feb, av_Queens_March, av_Queens_April, av_Queens_May, av_Queens_June]
average_Staten = [av_Staten_Jan, av_Staten_Feb, av_Staten_March, av_Staten_April, av_Staten_May, av_Staten_June]
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June']


# In[80]:


plt.plot(months,average_Man)
plt.title('TS for Man')
plt.xlabel('Months')
plt.ylabel('Averages')


# In[81]:


plt.plot(months,average_Bronx)
plt.title('TS for Bronx')
plt.xlabel('Months')
plt.ylabel('Averages')


# In[82]:


plt.plot(months,average_Bru)
plt.title('TS for Brooklyn')
plt.xlabel('Months')
plt.ylabel('Averages')


# In[83]:


plt.plot(months,average_Queens)
plt.title('TS for Queens')
plt.xlabel('Months')
plt.ylabel('Averages')


# In[76]:


plt.plot(months,average_EWR)
plt.title('TS for EWR')
plt.xlabel('Months')
plt.ylabel('Averages')


# In[84]:


plt.plot(months,average_Staten)
plt.title('TS for Staten Island')
plt.xlabel('Months')
plt.ylabel('Averages')


# From this analisys we can see that there is a huge increment of trips from January to Febrary in each borough. After the number of trips tends to stay around a certain value.

# ## RQ2

# Let's start the analisys for the month January. Than we repeat the same for each month.

# In[85]:


nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full
df.head()


# We choose a time slot of six hours. So, each day is divided in 4 slots. Then, for all the days in the month we count the number of passengers for the trips in this slot.

# In[86]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# We divide the days in slot and count the number of passengers for the trips in each slot.

# In[87]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[88]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[89]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[90]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[91]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[92]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[93]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[94]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[95]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[96]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-01'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[97]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# In[69]:


Man1 = 189212
Man2 = 411099
Man3 = 547834
Man4 = 389335
Bron1 = 693
Bron2 = 604
Bron3 = 492
Bron4 = 243
Bru1 = 7341
Bru2 = 5001
Bru3 = 4802
Bru4 = 4861
EWR1 = 22
EWR2 = 42
EWR3 = 104
EWR4 = 38
Q1 = 14649
Q2 = 27584
Q3 = 42391
Q4 = 38347
St1 = 9
St2 = 1
St3 = 2
St4 = 1
Man = [Man1, Man2, Man3, Man4]
Bro = [Bron1, Bron2, Bron3, Bron4]
Bru = [Bru1, Bru2, Bru3, Bru4]
EWR = [EWR1, EWR2, EWR3, EWR4]
Q = [Q1, Q2, Q3, Q4]
S = [St1, St2, St3, St4]


# In January the boroughs wichi resultd to be with the biggest number of passengers were Manhattan, Brooklyn and Queen.

# In[98]:


nytaxi = pd.read_csv(Location_Feb, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full
df.head()


# In[ ]:





# In[99]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# In[100]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[101]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[102]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[103]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[104]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[105]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[106]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[107]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[108]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[109]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-02'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[110]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# In[111]:


############## March
nytaxi = pd.read_csv(Location_March, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[112]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# In[113]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[115]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[116]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[117]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[118]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[119]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[120]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[122]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[123]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[124]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-03'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[125]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# In[126]:


######## April
nytaxi = pd.read_csv(Location_April, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[127]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# In[128]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[129]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[130]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[131]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[132]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[133]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[134]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[135]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[136]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[137]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-04'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[138]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# In[139]:


######## May
nytaxi = pd.read_csv(Location_May, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[140]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# In[141]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[142]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[143]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[144]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[145]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[146]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[147]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[148]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[149]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[150]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-05'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[151]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# In[152]:


######## June
nytaxi = pd.read_csv(Location_June, usecols=[1,2,3,7])  
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[153]:


df_Man = df.loc[(df['Borough'] == "Manhattan") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_Man['tpep_pickup_datetime'] = pd.to_datetime(df_Man['tpep_pickup_datetime'])
hours = df_Man['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Man['hours'] = hours


# In[154]:


df_Man_slot1 = df_Man[(df_Man['hours'] >= 0) & (df_Man['hours'] < 6)]
df_Man_slot2 = df_Man[(df_Man['hours'] >= 6) & (df_Man['hours'] < 12)]
df_Man_slot3 = df_Man[(df_Man['hours'] >= 12) & (df_Man['hours'] < 18)]
df_Man_slot4 = df_Man[(df_Man['hours'] >= 18) & (df_Man['hours'] < 24)]
Total_Man_1 = df_Man_slot1['passenger_count'].sum()
print(Total_Man_1)
Total_Man_2 = df_Man_slot2['passenger_count'].sum()
print(Total_Man_2)
Total_Man_3 = df_Man_slot3['passenger_count'].sum()
print(Total_Man_3)
Total_Man_4 = df_Man_slot4['passenger_count'].sum()
print(Total_Man_4)


# In[157]:


df_Bronx = df.loc[(df['Borough'] == "Bronx") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_Bronx['tpep_pickup_datetime'] = pd.to_datetime(df_Bronx['tpep_pickup_datetime'])
hours = df_Bronx['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bronx['hours'] = hours


# In[158]:


df_Bronx_slot1 = df_Bronx[(df_Bronx['hours'] >= 0) & (df_Bronx['hours'] < 6)]
df_Bronx_slot2 = df_Bronx[(df_Bronx['hours'] >= 6) & (df_Bronx['hours'] < 12)]
df_Bronx_slot3 = df_Bronx[(df_Bronx['hours'] >= 12) & (df_Bronx['hours'] < 18)]
df_Bronx_slot4 = df_Bronx[(df_Bronx['hours'] >= 18) & (df_Bronx['hours'] < 24)]
Total_Bronx_1 = df_Bronx_slot1['passenger_count'].sum()
print(Total_Bronx_1)
Total_Bronx_2 = df_Bronx_slot2['passenger_count'].sum()
print(Total_Bronx_2)
Total_Bronx_3 = df_Bronx_slot3['passenger_count'].sum()
print(Total_Bronx_3)
Total_Bronx_4 = df_Bronx_slot4['passenger_count'].sum()
print(Total_Bronx_4)


# In[159]:


df_Bru = df.loc[(df['Borough'] == "Brooklyn") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_Bru['tpep_pickup_datetime'] = pd.to_datetime(df_Bru['tpep_pickup_datetime'])
hours = df_Bru['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Bru['hours'] = hours


# In[160]:


df_Bru_slot1 = df_Bru[(df_Bru['hours'] >= 0) & (df_Bru['hours'] < 6)]
df_Bru_slot2 = df_Bru[(df_Bru['hours'] >= 6) & (df_Bru['hours'] < 12)]
df_Bru_slot3 = df_Bru[(df_Bru['hours'] >= 12) & (df_Bru['hours'] < 18)]
df_Bru_slot4 = df_Bru[(df_Bru['hours'] >= 18) & (df_Bru['hours'] < 24)]
Total_Bru_1 = df_Bru_slot1['passenger_count'].sum()
print(Total_Bru_1)
Total_Bru_2 = df_Bru_slot2['passenger_count'].sum()
print(Total_Bru_2)
Total_Bru_3 = df_Bru_slot3['passenger_count'].sum()
print(Total_Bru_3)
Total_Bru_4 = df_Bru_slot4['passenger_count'].sum()
print(Total_Bru_4)


# In[161]:


df_EWR = df.loc[(df['Borough'] == "EWR") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_EWR['tpep_pickup_datetime'] = pd.to_datetime(df_EWR['tpep_pickup_datetime'])
hours = df_EWR['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_EWR['hours'] = hours


# In[162]:


df_EWR_slot1 = df_EWR[(df_EWR['hours'] >= 0) & (df_EWR['hours'] < 6)]
df_EWR_slot2 = df_EWR[(df_EWR['hours'] >= 6) & (df_EWR['hours'] < 12)]
df_EWR_slot3 = df_EWR[(df_EWR['hours'] >= 12) & (df_EWR['hours'] < 18)]
df_EWR_slot4 = df_EWR[(df_EWR['hours'] >= 18) & (df_EWR['hours'] < 24)]
Total_EWR_1 = df_EWR_slot1['passenger_count'].sum()
print(Total_EWR_1)
Total_EWR_2 = df_EWR_slot2['passenger_count'].sum()
print(Total_EWR_2)
Total_EWR_3 = df_EWR_slot3['passenger_count'].sum()
print(Total_EWR_3)
Total_EWR_4 = df_EWR_slot4['passenger_count'].sum()
print(Total_EWR_4)


# In[163]:


df_Queens = df.loc[(df['Borough'] == "Queens") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_Queens['tpep_pickup_datetime'] = pd.to_datetime(df_Queens['tpep_pickup_datetime'])
hours = df_Queens['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Queens['hours'] = hours


# In[164]:


df_Queens_slot1 = df_Queens[(df_Queens['hours'] >= 0) & (df_Queens['hours'] < 6)]
df_Queens_slot2 = df_Queens[(df_Queens['hours'] >= 6) & (df_Queens['hours'] < 12)]
df_Queens_slot3 = df_Queens[(df_Queens['hours'] >= 12) & (df_Queens['hours'] < 18)]
df_Queens_slot4 = df_Queens[(df_Queens['hours'] >= 18) & (df_Queens['hours'] < 24)]
Total_Queens_1 = df_Queens_slot1['passenger_count'].sum()
print(Total_Queens_1)
Total_Queens_2 = df_Queens_slot2['passenger_count'].sum()
print(Total_Queens_2)
Total_Queens_3 = df_Queens_slot3['passenger_count'].sum()
print(Total_Queens_3)
Total_Queens_4 = df_Queens_slot4['passenger_count'].sum()
print(Total_Queens_4)


# In[165]:


df_Stat = df.loc[(df['Borough'] == "Staten Island") & (df['tpep_pickup_datetime'].str.startswith('2018-06'))]
df_Stat['tpep_pickup_datetime'] = pd.to_datetime(df_Stat['tpep_pickup_datetime'])
hours = df_Stat['tpep_pickup_datetime'].apply(lambda x: x.hour)
df_Stat['hours'] = hours


# In[166]:


df_Stat_slot1 = df_Stat[(df_Stat['hours'] >= 0) & (df_Stat['hours'] < 6)]
df_Stat_slot2 = df_Stat[(df_Stat['hours'] >= 6) & (df_Stat['hours'] < 12)]
df_Stat_slot3 = df_Stat[(df_Stat['hours'] >= 12) & (df_Stat['hours'] < 18)]
df_Stat_slot4 = df_Stat[(df_Stat['hours'] >= 18) & (df_Stat['hours'] < 24)]
Total_Stat_1 = df_Stat_slot1['passenger_count'].sum()
print(Total_Stat_1)
Total_Stat_2 = df_Stat_slot2['passenger_count'].sum()
print(Total_Stat_2)
Total_Stat_3 = df_Stat_slot3['passenger_count'].sum()
print(Total_Stat_3)
Total_Stat_4 = df_Stat_slot4['passenger_count'].sum()
print(Total_Stat_4)


# ## RQ3

# We start the analisys for the month in January. So, first of all, We upload the data in January. Due to time constraints and since our pc is not able to perform the analisys for all the month together, via function concat, we consider just month and february separately. The other months it is the same.

# In[184]:


nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,7]) 
nyBorough =pd.read_csv(Location_2, usecols=[0,1], sep = ';')
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[185]:


df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]


# In[186]:


dfMan = df_full.loc[df['Borough']=='Manhattan']


# In[180]:


dfMan['trip_duration'].plot.box()


# In[182]:


dfMan['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Man in Jan")


# In[187]:


dfBronx = df_full.loc[df['Borough']=='Bronx']


# In[188]:


dfBronx['trip_duration'].plot.box()


# In[189]:


dfBronx = dfBronx.drop(dfBronx[dfBronx.trip_duration > 40000].index) # remove rows with trip_duration > 40000


# In[190]:


dfBronx['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Bronx in Jan")


# In[191]:


dfBru = df_full.loc[df['Borough']=='Brooklyn']


# In[192]:


dfBru['trip_duration'].plot.box()


# In[193]:


dfBru['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Brooklyn in Jan")


# In[194]:


dfEWR = df_full.loc[df['Borough']=='EWR']


# In[196]:


dfEWR['trip_duration'].plot.box()


# In[197]:


dfEWR = dfEWR.drop(dfEWR[dfEWR.trip_duration > 1000].index) # remove rows with trip_duration > 1000


# In[198]:


dfEWR['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in EWR in Jan")


# In[205]:


dfQueens = df_full.loc[df['Borough']=='Queens']


# In[206]:


dfQueens['trip_duration'].plot.box()


# In[201]:





# In[207]:


dfQueens['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Queens in Jan")


# In[208]:


dfStat = df_full.loc[df['Borough']=='Staten Island']


# In[209]:


dfQueens['trip_duration'].plot.box()


# In[210]:


dfStat['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Staten Island in Jan")


# In[212]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[204]:


nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]
df = df_full


# In[212]:


data = df.loc[df['Borough']=='Manhattan']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration'")


# In[214]:


df = df_full
data = df.loc[df['Borough']=='Bronx']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration'")


# In[215]:


df = df_full
data = df.loc[df['Borough']=='Brooklyn']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Brooklyn")


# In[216]:


df = df_full
data = df.loc[df['Borough']=='EWR']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in EWR")


# In[217]:


df = df_full
data = df.loc[df['Borough']=='Queens']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Queens")


# In[218]:


df = df_full
data = df.loc[df['Borough']=='Staten Island']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Staten Island")


# In[226]:


nytaxi = pd.read_csv(Location_Feb, usecols=[1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]


# In[236]:


df = df_full
data = df.loc[df['Borough']=='Manhattan']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Manhattan in Feb")


# In[237]:


df = df_full
data = df.loc[df['Borough']=='Bronx']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Bronx in Feb")


# In[238]:


df = df_full
data = df.loc[df['Borough']=='Brooklyn']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Brooklyn in Feb")


# In[239]:


df = df_full
data = df.loc[df['Borough']=='EWR']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in EWR in Feb")


# In[240]:


df = df_full
data = df.loc[df['Borough']=='Queens']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Queens in Feb")


# In[241]:


df = df_full
data = df.loc[df['Borough']=='Staten Island']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Staten Island in Feb")


# In[242]:


nytaxi = pd.read_csv(Location_March, usecols=[1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]


# In[243]:


df = df_full
data = df.loc[df['Borough']=='Manhattan']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Manhattan in March")


# In[244]:


df = df_full
data = df.loc[df['Borough']=='Bronx']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Bronx in March")


# In[245]:


df = df_full
data = df.loc[df['Borough']=='Brooklyn']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Brooklyn in March")


# In[246]:


df = df_full
data = df.loc[df['Borough']=='EWR']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in EWR in March")


# In[247]:


df = df_full
data = df.loc[df['Borough']=='Queens']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Queens in March")


# In[248]:


df = df_full
data = df.loc[df['Borough']=='Staten Island']
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Staten Island in March")


# In[249]:


nytaxi = pd.read_csv(Location_April, usecols=[1,2,7]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]


# In[259]:


df = df_full
data = df.loc[df['Borough']=='Manhattan']
data = data.drop(data[data.trip_duration > 10000].index) # remove rows with trip distance > 35
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Manhattan in April")


# In[258]:


df = df_full
data = df.loc[df['Borough']=='Bronx']
data = data.drop(data[data.trip_duration > 10000].index) # remove rows with trip distance > 35
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Bronx in April")


# In[257]:


df = df_full
data = df.loc[df['Borough']=='Brooklyn']
data = data.drop(data[data.trip_duration > 10000].index) # remove rows with trip distance > 35
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Brooklyn in April")


# In[264]:


df = df_full
data = df.loc[df['Borough']=='EWR']
data = data.drop(data[data.trip_duration > 2000].index) 
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in EWR in April")


# In[267]:


df = df_full
data = df.loc[df['Borough']=='Queens']
data = data.drop(data[data.trip_duration > 100000].index) 
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Queens in April")


# In[274]:


df = df_full
data = df.loc[df['Borough']=='Staten Island']
data = data.drop(data[data.trip_duration > 100000].index) 
df = pd.DataFrame(data)
df['trip_duration'].plot.hist(bins=100, title="Distribution of 'trip_duration' in Staten Island in April")


# ## RQ 4

# In[6]:


nytaxi = pd.read_csv(Location_Jan, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[7]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# In[10]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# In[12]:


nytaxi = pd.read_csv(Location_Feb, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[13]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# In[14]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# In[16]:


nytaxi = pd.read_csv(Location_Apr, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[17]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# 

# In[18]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# 

# In[300]:


nytaxi = pd.read_csv(Location_March, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[301]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# In[302]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# In[19]:


nytaxi = pd.read_csv(Location_May, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[20]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# In[21]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# In[22]:


nytaxi = pd.read_csv(Location_Jun, usecols=[7,9]) 
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df = df_full


# In[23]:


n1_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 1)]) # n° of payments of type 1 in Manhattan
n2_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 2)]) # n° of payments of type 2 in Manhattan
n3_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 3)]) # n° of payments of type 3 in Manhattan
n4_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 4)]) # n° of payments of type 4 in Manhattan
n5_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 5)]) # n° of payments of type 5 in Manhattan
n6_Man = len(df.loc[(df['Borough']=='Manhattan') & (df.payment_type == 6)]) # n° of payments of type 6 in Manhattan

n1_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 1)]) 
n2_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 2)]) 
n3_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 3)]) 
n4_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 4)]) 
n5_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 5)]) 
n6_Bro = len(df.loc[(df['Borough']=='Bronx') & (df.payment_type == 6)]) 

n1_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 1)]) 
n2_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 2)])
n3_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 3)])
n4_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 4)])
n5_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 5)])
n6_Bru = len(df.loc[(df['Borough']=='Brookling') & (df.payment_type == 6)])

n1_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 1)]) 
n2_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 2)])
n3_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 3)])
n4_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 4)])
n5_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 5)])
n6_EWR = len(df.loc[(df['Borough']=='EWR') & (df.payment_type == 6)])

n1_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 1)]) 
n2_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 2)])
n3_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 3)])
n4_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 4)])
n5_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 5)])
n6_Queens = len(df.loc[(df['Borough']=='Queens') & (df.payment_type == 6)])

n1_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 1)]) 
n2_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 2)])
n3_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 3)])
n4_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 4)])
n5_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 5)])
n6_Staten = len(df.loc[(df['Borough']=='Staten Island') & (df.payment_type == 6)])


# In[24]:


a1 = [n1_Man,n1_Bro,n1_Bru,n1_EWR,n1_Queens,n1_Staten]
a2 = [n2_Man,n2_Bro,n2_Bru,n2_EWR,n2_Queens,n2_Staten]
a3 = [n3_Man,n3_Bro,n3_Bru,n3_EWR,n3_Queens,n3_Staten]
a4 = [n4_Man,n4_Bro,n4_Bru,n4_EWR,n4_Queens,n4_Staten]
a5 = [n5_Man,n5_Bro,n5_Bru,n5_EWR,n5_Queens,n5_Staten]
a6 = [n6_Man,n6_Bro,n6_Bru,n6_EWR,n6_Queens,n6_Staten]
obs = np.array([a1, a2, a3, a4, a5, a6])
from scipy.stats import chisquare
chisquare(obs)


# Given the results of the Chi test for all the months we cac conclued that we can never accept the hypotesis that the two variables are correlated, since p value is always 0, so less than each threshold.

# ## CR1

# In[8]:


nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,4,7,8,10,16]) 


# In[9]:


nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[1,2,4,7,8,10,16])])


# .... and so on adding the rows for the other months. But we stop here beacuse our computers are not enough powerful. When we will work for Mc (hopefully not as cashiers, but as data scientists in NY) they will give us beautiful pcs :)....

# In[10]:


df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')
df_full.head()


# In[11]:


df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)
df_full['trip_duration'] = (df_full.tpep_dropoff_datetime - df_full.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_full = df_full[df_full.trip_duration > 0]


# In[12]:


grouped_mean = df_full.groupby(['Borough']).mean()
grouped_mean= grouped_mean.drop(columns=['PULocationID','DOLocationID']) 
grouped_mean


# In[13]:


df_full['trip_distance'].plot.box()


# In[15]:


df_full = df_full[df_full.trip_distance < 400]
df_full['trip_distance'].plot.hist(bins=100, title="Distribution of 'trip_distance'")


# In[15]:


df_full = df_full.drop(df_full[df_full.total_amount < 2.5].index)


# In[18]:


df_full['fare_amount'].plot.box()


# We can cut out the outlier over 1500.

# In[16]:


df_full = df_full.drop(df_full[df_full.fare_amount <= 0].index) # remove rows with fare_amount <= 0
df_full = df_full.drop(df_full[df_full.fare_amount > 1500].index) # remove rows with fare_amount > 1500
df_full['fare_amount'].plot.box()


# In[17]:


df_full = df_full.drop(df_full[df_full.fare_amount > 1500].index) # remove rows with fare_amount > 1500
df_full['fare_amount'].plot.hist(bins=100, title="Distribution of 'fare_amount'")


# In[18]:


df_full.trip_duration.plot.box()


# There is one outlier, so we can cut him out from our analysis.

# In[19]:


df_full = df_full.drop(df_full[df_full.trip_duration > 15000].index)
df_full.trip_duration.plot.hist(bins=100, title="Distribution of 'trip_duration'")


# Let's compute the 'price_per_mile', ratio between the trip 'fare_amount' and 'trip_distance'.

# In[22]:


df_full['price_per_mile'] = df_full.fare_amount / df_full.trip_distance


# In[23]:


df_full.price_per_mile.plot.box()


# Let's remove the two outliers

# In[26]:


df_full = df_full.drop(df_full[df_full.price_per_mile > 15].index) # remove rows with 'price_per_mile' > 25
df_full = df_full.drop(df_full[df_full.price_per_mile < 1].index) # remove rows with 'price_per_mile' < 1

df_full.price_per_mile.plot.hist(bins=100, title="Distribution of 'price_per_mile'")


# Let's calulate means and sds on these data

# In[28]:


grouped_mean = df_full.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_mean


# In[29]:


grouped_std = df_full.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])
grouped_std


# In[31]:


sns.kdeplot(df_full.price_per_mile[df_full.Borough == "Queens"],label='Queens', bw=0.5)
sns.kdeplot(df_full.price_per_mile[df_full.Borough == "Manhattan"],label='Manhattan', bw=0.5)
sns.kdeplot(df_full.price_per_mile[df_full.Borough == "Brooklyn"],label='Brooklyn', bw=0.5)
sns.kdeplot(df_full.price_per_mile[df_full.Borough == "Bronx"],label='Bronx', bw=0.5)
sns.kdeplot(df_full.price_per_mile[df_full.Borough == "Staten Island"],label='Staten Island', bw=0.5)

plt.xlabel('$/mile')
plt.ylabel('KDE')
plt.title('\'price_per_mile\' distribution over Boroughs')
plt.show()


# Now let's do a t-test on the 'price_per_mile' series
# 
# H0: means are the same
# H1: means are different
# Our p-value treshold is p-value = 0.05

# In[34]:


ttest_matrix = pd.DataFrame(index=df_full.Borough.unique(), columns=df_full.Borough.unique())

for col1 in df_full.Borough.unique():
    for col2 in df_full.Borough.unique():
        ttest_matrix.loc[col1,col2] = stats.ttest_ind(df_full[df_full.Borough == col1]['price_per_mile'], df_full[df_full.Borough == col2]['price_per_mile']).pvalue
        if col1==col2:
            break
            
ttest_matrix = ttest_matrix.apply(pd.to_numeric)
ttest_matrix


# We can accept the null hypothesis at threshold p = 0.05 only for EWR-Brroklyn, Staten Isalnd - Brooklyn and Staten Island-EWR. 

# Now we create a new column with the adjusted price per mile.

# In[35]:


df_full['ppm_adj'] = df_full.fare_amount/df_full.trip_duration
df_full.head()


# Let's plot

# In[36]:


sns.kdeplot(df_full.ppm_adj[df_full.Borough == "Queens"],label='Queens', bw=0.5)
sns.kdeplot(df_full.ppm_adj[df_full.Borough == "Manhattan"],label='Manhattan', bw=0.5)
sns.kdeplot(df_full.ppm_adj[df_full.Borough == "Brooklyn"],label='Brooklyn', bw=0.5)
sns.kdeplot(df_full.ppm_adj[df_full.Borough == "Bronx"],label='Bronx', bw=0.5)
sns.kdeplot(df_full.ppm_adj[df_full.Borough == "Staten Island"],label='Staten Island', bw=0.5)

plt.xlabel('$/miles s')
plt.ylabel('KDE')
plt.title('Price per mile adjusted distribution over Boroughs')
plt.show()


# In[38]:


grouped_mean = df_full.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_mean


# In[39]:


grouped_std = df_full.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])
grouped_std


# We perform again the t test with the new feature.

# In[40]:


ttest_matrix_adj = pd.DataFrame(index=df_full.Borough.unique(), columns=df_full.Borough.unique())

for col1 in df_full.Borough.unique():
    for col2 in df_full.Borough.unique():
        ttest_matrix_adj.loc[col1,col2] = stats.ttest_ind(df_full[df_full.Borough == col1]['ppm_adj'], df_full[df_full.Borough == col2]['ppm_adj']).pvalue
        if col1==col2:
            break

ttest_matrix_adj = ttest_matrix_adj.apply(pd.to_numeric)
ttest_matrix_adj    


# We refuse the null hypothese for all the boroughs.

# ## RQ 5

# In[25]:


yellow_cabs_data = pd.read_csv('Documents/yellow_tripdata_2018-01.csv')


# In[27]:


# to get the trip duration of january using 2 columns 
columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
yellow_cabs_data = pd.read_csv('Documents/yellow_tripdata_2018-01.csv', usecols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime','trip_distance'], parse_dates = columns)
yellow_cabs_data['trip_duration']=yellow_cabs_data['tpep_dropoff_datetime']-yellow_cabs_data['tpep_pickup_datetime']


# In[28]:


# consider only 2018 for drop datetime
trip_jan = yellow_cabs_data[yellow_cabs_data['tpep_pickup_datetime'].dt.year == 2018]


# In[29]:


# consider only 2018 for drop datetime

trip_jan = trip_jan[trip_jan['tpep_dropoff_datetime'].dt.year == 2018]


# In[30]:


# consider only january for pickup datetime

trip_jan = trip_jan[trip_jan['tpep_pickup_datetime'].dt.month == 1]


# In[31]:


# consider only january for drop datetime

trip_jan = trip_jan[trip_jan['tpep_dropoff_datetime'].dt.month == 1]


# In[32]:


#Filtering data having trip_distance>0.01

trip_jan=trip_jan[trip_jan['trip_distance']>0.01]


# In[33]:


# getting the trip duration in seconds:
trip_jan['trip_duration_in_sec']=trip_jan['trip_duration'].dt.total_seconds()


# In[34]:


#Cleansing  data for trip_duration_in_sec having more than 0 seconds

trip_jan=trip_jan[trip_jan['trip_duration_in_sec']>0]


# In[35]:


#filtering data for longer trips that is greater than 50 miles

trip_jan50=trip_jan[trip_jan['trip_distance']>50]


# In[36]:


# To Scatter Plot:

import matplotlib.pyplot as plt
plt.scatter(trip_jan50['trip_duration_in_sec'], trip_jan50['trip_distance'])
plt.xlabel("Trip duration")
plt.ylabel("Trip distance")
plt.show()


# In[37]:


#To get Perasson Coefficient
from scipy.stats import pearsonr
x = trip_jan50['trip_duration_in_sec']
y = trip_jan50['trip_distance']

r,p = pearsonr(x,y)
print (r)
print (p)


# In[38]:


# to get the trip duration of feburary using 2 columns 
columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
yellow_cabs_data_feb = pd.read_csv('Documents/yellow_tripdata_2018-02.csv', usecols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime','trip_distance'], parse_dates = columns)
yellow_cabs_data_feb['trip_duration']=yellow_cabs_data_feb['tpep_dropoff_datetime']-yellow_cabs_data_feb['tpep_pickup_datetime']
yellow_cabs_data_feb['trip_duration'].dt.total_seconds()


# In[41]:


# consider only 2018 for drop datetime
trip_feb = yellow_cabs_data_feb[yellow_cabs_data_feb['tpep_pickup_datetime'].dt.year == 2018]


# In[42]:


# consider only 2018 for drop datetime

trip_feb = trip_feb[trip_feb['tpep_dropoff_datetime'].dt.year == 2018]


# In[43]:


# consider only feburary for pickup datetime

trip_feb = trip_feb[trip_feb['tpep_pickup_datetime'].dt.month == 2]


# In[44]:


# consider only feburary for drop datetime

trip_feb = trip_feb[trip_feb['tpep_dropoff_datetime'].dt.month == 2]


# In[45]:


#Filtering data having trip_distance>0.01

trip_feb=trip_feb[trip_feb['trip_distance']>0.01]


# In[46]:


# getting the trip duration in seconds:
trip_feb['trip_duration_in_sec']=trip_feb['trip_duration'].dt.total_seconds()


# In[47]:


#filtering data for longer trips that is greater than 50 miles

trip_feb50=trip_feb[trip_feb['trip_distance']>50]


# In[48]:


# To Scatter Plot:

import matplotlib.pyplot as plt
plt.scatter(trip_feb50['trip_duration_in_sec'], trip_feb50['trip_distance'])
plt.xlabel("Trip duration")
plt.ylabel("Trip distance")
plt.show()


# In[49]:


#To get Perasson Coefficient
from scipy.stats import pearsonr
x = trip_feb50['trip_duration_in_sec']
y = trip_feb50['trip_distance']

r,p = pearsonr(x,y)
print (r)
print (p)


# In[50]:


# to get the trip duration of march using 2 columns 
columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
yellow_cabs_data_mar = pd.read_csv('Documents/yellow_tripdata_2018-03.csv', usecols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime','trip_distance'], parse_dates = columns)
yellow_cabs_data_mar['trip_duration']=yellow_cabs_data_mar['tpep_dropoff_datetime']-yellow_cabs_data['tpep_pickup_datetime']
yellow_cabs_data_mar['trip_duration'].dt.total_seconds()


# In[51]:


# consider only 2018 for drop datetime
trip_mar = yellow_cabs_data_mar[yellow_cabs_data_mar['tpep_pickup_datetime'].dt.year == 2018]


# In[52]:


# consider only 2018 for drop datetime
trip_mar = trip_mar[trip_mar['tpep_dropoff_datetime'].dt.year == 2018]


# In[53]:


# consider only march for pickup datetime

trip_mar = trip_mar[trip_mar['tpep_pickup_datetime'].dt.month == 3]


# In[54]:


# consider only mar for drop datetime

trip_mar = trip_mar[trip_mar['tpep_dropoff_datetime'].dt.month == 3]


# In[55]:


#Filtering data having trip_distance>0.01

trip_mar=trip_mar[trip_mar['trip_distance']>0.01]


# In[56]:


# getting the trip duration in seconds:
trip_mar['trip_duration_in_sec']=trip_mar['trip_duration'].dt.total_seconds()


# In[57]:


#Cleansing  data for trip_duration_in_sec having more than 0 seconds

trip_mar=trip_mar[trip_mar['trip_duration_in_sec']>0]


# In[58]:


#filtering data for longer trips that is greater than 50 miles

trip_mar50=trip_mar[trip_mar['trip_distance']>50]


# In[59]:


# To Scatter Plot:

import matplotlib.pyplot as plt
plt.scatter(trip_mar50['trip_duration_in_sec'], trip_mar50['trip_distance'])
plt.xlabel("Trip duration")
plt.ylabel("Trip distance")
plt.show()


# In[60]:


#To get Pearson Coefficient
from scipy.stats import pearsonr
x = trip_mar50['trip_duration_in_sec']
y = trip_mar50['trip_distance']

r,p = pearsonr(x,y)
print (r)
print (p)


# In[61]:


# to get the trip duration of april using 2 columns 
columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
yellow_cabs_data_apr = pd.read_csv('Documents/yellow_tripdata_2018-04.csv', usecols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime','trip_distance'], parse_dates = columns)
yellow_cabs_data_apr['trip_duration']=yellow_cabs_data_apr['tpep_dropoff_datetime']-yellow_cabs_data_apr['tpep_pickup_datetime']
yellow_cabs_data_apr['trip_duration'].dt.total_seconds()


# In[62]:


# consider only 2018 for drop datetime
trip_apr = yellow_cabs_data_apr[yellow_cabs_data_apr['tpep_pickup_datetime'].dt.year == 2018]


# In[63]:


# consider only 2018 for drop datetime

trip_apr = trip_apr[trip_apr['tpep_dropoff_datetime'].dt.year == 2018]


# In[64]:


# consider only april for pickup datetime

trip_apr = trip_apr[trip_apr['tpep_pickup_datetime'].dt.month == 4]


# In[65]:


# consider only january for drop datetime

trip_apr = trip_apr[trip_apr['tpep_dropoff_datetime'].dt.month == 4]


# In[66]:


#Filtering data having trip_distance>0.01

trip_apr=trip_apr[trip_apr['trip_distance']>0.01]


# In[67]:


# getting the trip duration in seconds:
trip_apr['trip_duration_in_sec']=trip_apr['trip_duration'].dt.total_seconds()


# In[68]:


#Cleansing  data for trip_duration_in_sec having more than 0 seconds

trip_apr=trip_apr[trip_jan['trip_duration_in_sec']>0]


# In[ ]:




