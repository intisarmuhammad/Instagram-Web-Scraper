#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
insta_scrape=pd.read_csv('/Users/intisarmuhammad/Downloads/final_project_with_hsh.csv')


# In[21]:


insta_scrape.head()


# In[22]:


import re
import numpy as np
def find_hashtags(comment):
    hashtags = re.findall('#[A-Za-z]+', comment)
    return hashtags

def change_time(time):
    new_age = re.findall('\d{2}:\d{2}', time)
    return new_age

insta_scrape['time_posted'] = insta_scrape['age'].apply(lambda x: change_time(x))
insta_scrape['hashtags'] = insta_scrape['caption'].apply(lambda x: find_hashtags(x))
insta_scrape['likes'] = insta_scrape['likes'].astype(str)
insta_scrape['likes'] = insta_scrape['likes'].str.replace("likes","")
insta_scrape['likes'] = insta_scrape['likes'].str.replace(",","")
insta_scrape.replace(to_replace=['None'], value='', inplace=True)
insta_scrape['likes'] = pd.to_numeric(insta_scrape['likes'])

insta_scrape.head()


# In[23]:


import math
insta_scrape.time_posted = insta_scrape.time_posted.astype("str")
insta_scrape['time_posted'] = insta_scrape['time_posted'].str.replace("'","")
insta_scrape['time_posted'] = insta_scrape['time_posted'].str.replace("]","")
insta_scrape['time_posted'] = insta_scrape['time_posted'].str.replace("[","")
insta_scrape['caption'] = insta_scrape['caption'].str.replace("\n"," ")
#insta_scrape['time_posted'] = insta_scrape['time_posted'].str.replace(":",".")
insta_scrape['hours'] = insta_scrape['time_posted']
insta_scrape['hours'] = insta_scrape['hours'].str.replace(":", ".")
insta_scrape['hours'] = pd.to_numeric(insta_scrape['hours'])
insta_scrape['hours'] = insta_scrape['hours'].round()
insta_scrape.head()


# In[31]:


#create new variable time_of_day
insta_scrape['time_of_day'] = pd.cut(insta_scrape['hours'], bins = ['6', '12', '16', '21', '24'], labels = ['morning','afternoon', 'evening', "late night"])
#insta_scrape['time_of_day'] = insta_scrape['hours']
insta_scrape.tail(20)


# In[25]:


captions = []
for cap in insta_scrape['caption']:
    captions.append(cap)
print(captions)


# In[26]:


all_hashtags = []
for tag in insta_scrape['hashtags']:
    all_hashtags.append(tag)
print(all_hashtags)


# In[27]:


print(len(all_hashtags))


# In[28]:


#flatten the list into one
import itertools
flat=itertools.chain.from_iterable(all_hashtags)
print (list(flat))


# In[30]:


insta_scrape['time_of_day'].hist()


# In[33]:


insta_scrape['time_of_day'].describe()


# In[ ]:




