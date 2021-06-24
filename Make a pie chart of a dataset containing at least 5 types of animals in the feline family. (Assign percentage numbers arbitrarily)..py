#!/usr/bin/env python
# coding: utf-8

# Make a pie chart of a dataset containing at least 5 types of animals in the feline family. (Assign percentage numbers arbitrarily).

# In[1]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[15]:


feline_family = ['Cat', 'Lynx', 'Lion', 'Leopard', 'Cheater', 'Puma']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = feline_family)
plt.show()


# In[ ]:




