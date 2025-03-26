#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("NIKHIL DATASET.csv")
df


# In[3]:


df.describe()


# In[4]:


df.isnull().sum()


# In[5]:


df.nunique()


# In[6]:


df.fillna(df.mean(), inplace=True)


# In[7]:


year_columns = df.columns[2:]
df[year_columns] = df[year_columns].apply(pd.to_numeric, errors='coerce')


# In[8]:


df[['Factors', '2023-24']].sort_values(by='2023-24', ascending=False).head(1)


# In[9]:


df.mean(numeric_only=True)


# In[10]:


df.std(numeric_only=True)


# In[11]:


df[['Factors', '2020-21']].sort_values(by='2020-21', ascending=False).head(5)


# In[12]:


df.duplicated().sum()


# In[13]:


df['% Change 2019-2023'] = ((df['2023-24'] - df['2019-20']) / df['2019-20']) * 100


# In[14]:


df


# In[15]:


increasing_factors = df[(df['2015-16'] < df['2016-17']) & (df['2016-17'] < df['2017-18']) & (df['2017-18'] < df['2018-19'])]
increasing_factors[['Factors']]


# In[17]:


decreasing_factors = df[(df['2015-16'] > df['2016-17']) & (df['2016-17'] > df['2017-18']) & (df['2017-18'] > df['2018-19'])]
decreasing_factors[['Factors']]


# In[18]:


df.groupby('Factors').mean(numeric_only=True)


# In[19]:


Q1 = df['2023-24'].quantile(0.25)
Q3 = df['2023-24'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['2023-24'] < (Q1 - 1.5 * IQR)) | (df['2023-24'] > (Q3 + 1.5 * IQR))]


# In[20]:


df['Factors'] = df['Factors'].str.lower()


# In[21]:


df['Factors'].value_counts()


# In[22]:


df.columns[df.isnull().any()].tolist()


# In[23]:


df['Avg Growth Rate'] = ((df['2023-24'] / df['2015-16']) ** (1/8)) - 1


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[25]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Factors'], y=df['2023-24'])
plt.xticks(rotation=90)
plt.title('Scatter Plot of Factors vs 2023-24 Values')
plt.show()


# In[26]:


df_pie = df[['Factors', '2023-24']].dropna()
plt.figure(figsize=(8, 8))
plt.pie(df_pie['2023-24'], labels=df_pie['Factors'], autopct='%1.1f%%')
plt.title('Pie Chart of 2023-24 Values')
plt.show()


# In[27]:


plt.figure(figsize=(10, 6))
sns.histplot(df['2023-24'].dropna(), bins=10, kde=True)
plt.title('Histogram of 2023-24 Values')
plt.show()


# In[28]:


plt.figure(figsize=(12, 6))
sns.boxplot(data=df[year_columns])
plt.xticks(rotation=45)
plt.title('Box Plot of Yearly Data')
plt.show()


# In[29]:


plt.figure(figsize=(10, 6))
sns.stripplot(x=df['Factors'], y=df['2023-24'])
plt.xticks(rotation=90)
plt.title('Dot Plot of Factors vs 2023-24')
plt.show()


# In[30]:


import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot for 2023-24
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Factors'], y=df['2023-24'])
plt.xticks(rotation=90)
plt.title('Scatter Plot of Factors vs 2023-24')
plt.show()


# In[31]:


# Box plot for yearly data
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[year_columns])
plt.xticks(rotation=45)
plt.title('Box Plot of Yearly Data')
plt.show()


# In[32]:


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['2020-21'], y=df['2023-24'])
plt.xlabel('2020-21')
plt.ylabel('2023-24')
plt.title('Scatter Plot: 2020-21 vs 2023-24')
plt.show()


# In[ ]:




