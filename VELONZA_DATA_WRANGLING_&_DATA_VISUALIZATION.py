#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('board2.csv')


# In[4]:


df


# In[8]:


df.describe()


# In[16]:


Vis = df.loc[(df['Hometown'] == 'Visayas') & (df['Math'] < 70), ['Name', 'Gender', 'Track', 'Math']]


# In[17]:


Vis


# In[48]:


Instru = df.loc[(df['Hometown'] == 'Luzon') & (df['Math'])& (df['Electronics'] > 70), ['Name', 'GEAS', 'Electronics']]


# In[49]:


Instru


# In[31]:


df['Average'] = (df['Math'] + df['Electronics'] + df['GEAS'] + df['Communication']) / 4


# In[32]:


Mindy = df.loc[(df['Gender'] == 'Female') & (df['Hometown'] == 'Mindanao') & (df['Average'] >= 55), ['Name', 'Track', 'Electronics','Average']]


# In[33]:


Mindy


# In[34]:


import matplotlib.pyplot as plt


# In[41]:


track_gender_avg = df.groupby(['Track', 'Gender'])['Average'].mean().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
track_gender_avg.plot(kind='bar', ax=plt.gca(), width=0.8, alpha=0.7, edgecolor='black')
plt.xlabel('Track')
plt.ylabel('Mean Average Grade')
plt.title('Mean Average by Track and Gender\n(Compare bars within each track)')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()


# In[47]:


gender_avg = df.groupby('Gender')['Average'].mean()
plt.figure(figsize=(8, 5))
bars = plt.bar(gender_avg.index, gender_avg.values, color=['pink', 'lightblue'], alpha=0.7, edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Mean Average Grade')
plt.title('Mean Average Grade by Gender\n(Similar heights suggest low contribution)')
for bar, value in zip(bars, gender_avg.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{value:.1f}', 
             ha='center', va='bottom')
plt.tight_layout()
plt.show()


# In[45]:


hometown_avg = df.groupby('Hometown')['Average'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
bars = plt.bar(hometown_avg.index, hometown_avg.values, color=['Blue', 'yellow', 'Red'], alpha=0.7, edgecolor='black')
plt.xlabel('Hometown')
plt.ylabel('Mean Average Grade')
plt.title('Mean Average Grade by Hometown\n(Higher bars indicate contribution to higher scores)')
plt.xticks(rotation=45)
for bar, value in zip(bars, hometown_avg.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{value:.1f}', 
             ha='center', va='bottom')
plt.tight_layout()
plt.show()


# In[ ]:




