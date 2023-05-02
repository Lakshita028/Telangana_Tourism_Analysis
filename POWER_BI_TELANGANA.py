#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[41]:


data = pd.read_csv("/Users/lakshitasethi/Downloads/Telangana.csv")


# In[42]:


data.head()


# In[43]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[44]:


data1 = data.sort_values("Population/Tourist_2019").head(5)


# In[45]:


data1.head()


# In[46]:


fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=data1,x='District',y='Population/Tourist_2019')
plt.title("5 Districts with least Population to Tourist Ratio in 2019")
plt.show()


# In[47]:


data2 = data.sort_values("Population/Tourist_2019",ascending = False).head(5)


# In[48]:


fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=data2,x='District',y='Population/Tourist_2019')
plt.title("Top 5 Districts with maximum Population to Tourist Ratio in 2019")
plt.show()


# In[ ]:




