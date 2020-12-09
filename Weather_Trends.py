#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


data=pd.read_csv(r"G:/GitHub_Projects/Weather Trends/Weather Data.csv")


# In[7]:


data


# In[8]:


data.head()


# In[10]:


data.shape


# In[11]:


data.index


# In[14]:


data.columns


# In[16]:


data.dtypes


# In[17]:


data['Weather'].unique


# In[18]:


data.nunique()


# In[19]:


data.count()


# In[20]:


data['Weather'].value_counts


# In[21]:


data.info()


# In[22]:


#find all the unique "wind speed" values in data.
data.head(2)


# In[23]:


data.nunique()


# In[25]:


data['Wind Speed_km/h'].nunique()


# In[26]:


data['Wind Speed_km/h'].unique()


# In[27]:


#find the number of times when the "weather is exactly clear"
data.head(2)


# In[28]:


#value_counts()
data.Weather.value_counts()


# In[30]:


#filtering
data[data.Weather == 'Clear']


# In[31]:


#groupby()
data.groupby('Weather').get_group('Clear')


# In[32]:


#find the number of times "when wind speed is exactly 4 km/hr"
data.head(2)


# In[33]:


data[data['Wind Speed_km/h'] == 4]


# In[34]:


#find out all the null values in data
data.isnull()


# In[35]:


data.isnull().sum()


# In[37]:


data.notnull().sum()


# In[38]:


#rename the column name 'weather' of the dataframe to 'weather condition'
data.head(2)


# In[43]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[44]:


data.rename(columns = {'Weather' : 'Weather Condition'} , inplace=True)
data.head()


# In[45]:


#what is the mean 'visibility'?
data.Visibility_km.mean()


# In[46]:


#what is the standard deviation of 'pressure' in this data?
data.Press_kPa.std()


# In[47]:


#what is the variance of 'relative humidity' in this data?
data['Rel Hum_%'].var()


# In[49]:


#find all instances when 'snow' was recorded
#value_counts()
#data.head(2)
data['Weather Condition'].value_counts()


# In[50]:


#filtering
data[data['Weather Condition'] == 'Snow' ]


# In[52]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[53]:


data[data['Weather Condition'].str.contains('Snow')].tail(50)


# In[58]:


#find all instances when 'wind speed is 24' and 'visibility is 25'.
data[(data['Wind Speed_km/h'] > 24 ) & (data['Visibility_km']==25)]


# In[59]:


#what is the mean value of each column against each 'Weather Condition'?
data.groupby('Weather Condition').mean()


# In[60]:


#what is the maximum and minimum value of each column against each 'Weather Condition'?
data.groupby('Weather Condition').min()


# In[61]:


data.groupby('Weather Condition').max()


# In[63]:


#show all records where Weather Condition is Fog.
data[data["Weather Condition"] == "Fog"]


# In[65]:


#find all instances when 'Weather is Clear' or 'Visibility is above 40'
data[(data['Weather Condition']=='Clear') | (data['Visibility_km']>40)]


# In[68]:


#find all instances when: 1. 'Weather is Clear' and 'Relative Humidity is greater than 50' or 2. 'Visibility is above 40'

data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km']>40)]

