#!/usr/bin/env python
# coding: utf-8

# # College Completion Rate in US States 

# ### Importing the required packages and libraries 

# In[32]:


# Importing NumPy and Pandas

import numpy as np
import pandas as pd


# In[2]:


#Import Matplotlib and Seaborn

import matplotlib.pyplot as plt
import seaborn as sns


# In[30]:


#Importing dataset into df

df = pd.read_csv('cc_state_sector_grads.csv')


# ### Performing initial explorations
# 
# We start by looking at the data and gettting familiarized 
# with indecies, features, labels, etc.
# The data quickly tells us that graduation is tracked for females, F
# males, M and combined, B.
# Moreover, graduation within 150% of timeframe includes people graduating
# withing 100% of timeframe as well.

# In[34]:


df.head(10)


# Getting some key statistics from main features

# In[33]:


df.describe().transpose()


# ### Creating lattice 
# The purpose of this lattice is to gather information about my dataset
# finding possible correlations, strange behaviors, etc.
# Graduation cohort is strongly correlated with graduation rate. 
# Graduation withing 100% of designated timeframe is also 
# correlated with gratuation withing 150% of desgnated timeframe. 
# 
# 

# In[36]:


sns.pairplot(df)


# In[14]:


#Playing around with data
df.loc[df['gender']=='B'].groupby('state')['grad_150_rate'].mean().sort_values(ascending=False)


# In[15]:


sns.distplot(df[df['gender']=='B']['grad_150_rate'])


# ### Deciding on the label and features
# 
# For the purpose of visualization, graduation at 150% of time
# which includes people graduating on time and people graduating 
# 50% later as the label, while race and gender and state of graduatio is 
# used as features for visualization
# Note: Later on in the project, when applying machine learning 
# teachniques, all features are examined again. Categorical variables
# will be converted to dummy variables.
# 
# 

# In[40]:


#Selecting the desired features for visualization using pivot tables

dfpivot=df.pivot_table(values='grad_150_rate', index='gender', columns = 'race')


# ### Using heatmap 
# to study mean graduation rate (graduation percentage) across race and gender

# In[41]:


plt.figure(figsize=(12,6))
sns.set_context('paper',font_scale=1.5)
cmap = cmap = sns.cubehelix_palette(light=1, as_cmap=True)
sns.heatmap(dfpivot, cmap = cmap, linecolor='white', linewidths = 3)


# In[20]:


#Using barplot to study graduation rate nationwide

dfs=df.pivot_table(index="state_abbr", columns="gender", values="grad_150_rate", fill_value=0)
dfs['state'] = dfs.index
dfs.head()


# In[38]:


dfs=dfs.sort_values(by='B',ascending=False)
dfs.plot(kind='bar',figsize=(20,6))
plt.ylabel('Graduate Rate')
plt.xlabel('States')
plt.title('States Graduation Rate Among Genders')


# ### Creating an interactive map of nationwide graduation rate
# Note: Other than Pandas and NumPy, "Chart Studio" must be installed too.

# In[23]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[24]:


init_notebook_mode(connected=True) 


# In[25]:


#Building data dictionary

data = dict(type = 'choropleth',
            locations = dfs['state'],
            locationmode = 'USA-states',
            colorscale= 'Greens',
            #text= ['text1','text2','text3'],
            z=dfs['B'],
            colorbar = {'title':'Graduate Rate'})


# In[26]:


#Building nested dictionary

layout = dict(geo = {'scope':'usa'})


# In[27]:


#Set up object to be passed into iplot()

choromap = go.Figure(data = [data],layout = layout)


# In[28]:


#Plotting the interactive map of US with our graduation rate data

iplot(choromap)


# In[ ]:




