#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
sns.set(style='darkgrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df_race = pd.merge(df_race, df_pop, on='race')
df_race['deaths_per_million'] = df_race['number_of_deaths'] / df_race['population']
df_race.head()


# In[9]:


#load the csv
df = pd.read_csv (r'C:\Users\me\Documents\shootings.csv')
print (df)


# In[11]:


df.isna().sum()


# In[21]:


df.flee.value_counts()


# In[22]:


df.armed.value_counts()


# In[24]:


df.armed.fillna(df.armed.value_counts().index[0], inplace=True)


# In[25]:


df.dropna(axis=0, how='any', inplace=True)
print("There are {}".format(df.isna().sum().sum()), "missing values left in the dataframe")


# In[27]:


df['date'] = pd.to_datetime(df['date'])
df['year'] = pd.to_datetime(df['date']).dt.year
df['month'] = pd.to_datetime(df['date']).dt.month


# In[28]:


df_date = df[['date','armed']].groupby('date').count().sort_values(by='date')
df_date.rename(columns={'armed':'count'}, inplace=True)
df_date.head()


# In[30]:


plt.figure(figsize=(14,6))
plt.title('Daily Fatal Shootings', fontsize=17)
sns.lineplot(x=df_date.index, y='count', data=df_date)


# In[32]:


df_date.resample('10D').mean().plot(figsize=(14,6))
plt.title('Fatal Shootings - 10 day average', fontsize=16)


# In[36]:


get_ipython().system('pip install sidetable')
import sidetable


# In[35]:


df.stb.freq(['state'], thresh=50)


# In[37]:


plt.figure(figsize=(12,8))
plt.title('Age Distribution of Deaths', fontsize=15)
sns.distplot(df.age)


# In[38]:


df_race = df[['race','year','armed']].groupby(['race','year']).count().reset_index()
df_race.rename(columns={'armed':'number_of_deaths'}, inplace=True)
df_race.head()


# In[39]:


df_pop = pd.DataFrame({'race':['W','B','A','H','N','O'],
'population':[0.601, 0.134, 0.059, 0.185, 0.013, 0.008]})
df_pop['population'] = df_pop['population']*328
df_pop


# In[9]:


y = np.array([3073, 820, 642, 360])
x = ["not fleeing", "car", "foot", "other"]
plt.title('flee value counts', fontsize=15)
plt.pie(y, labels = x, startangle = 90)
plt.show()


# In[ ]:




