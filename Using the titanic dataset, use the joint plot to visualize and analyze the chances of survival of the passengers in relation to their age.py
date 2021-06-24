#!/usr/bin/env python
# coding: utf-8

# Using the titanic dataset, use the joint plot to visualize and analyze the chances of survival of the passengers in relation to their age

# In[2]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = sns.load_dataset("titanic")
data


# In[5]:


sns.jointplot(x = "age", y = "survived", kind = "reg", data=data)
plt.show()


# In[ ]:




