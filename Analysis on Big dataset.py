#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


raw = pd.read_csv('multipleChoiceResponses.csv')
new_header = raw.iloc[0] 
raw = raw[1:] 
raw.columns = new_header
new_header.head()


# In[3]:


raw.head()


# In[4]:


raw.shape


# In[5]:


raw.columns[:11]


# In[6]:


first_dataset = raw[['Duration (in seconds)', 'What is your gender? - Selected Choice',
       'What is your gender? - Prefer to self-describe - Text',
       'What is your age (# years)?',
       'In which country do you currently reside?',
       'What is the highest level of formal education that you have attained or plan to attain within the next 2 years?',
       'Which best describes your undergraduate major? - Selected Choice',
       'Select the title most similar to your current role (or most recent title if retired): - Selected Choice',
       'Select the title most similar to your current role (or most recent title if retired): - Other - Text',
       'In what industry is your current employer/contract (or your most recent employer if retired)? - Selected Choice',
       'In what industry is your current employer/contract (or your most recent employer if retired)? - Other - Text']]
first_dataset.head()


# In[7]:


first_dataset.info()


# In[8]:


first_dataset=first_dataset.drop('What is your gender? - Prefer to self-describe - Text',axis=1)
first_dataset=first_dataset.drop('Select the title most similar to your current role (or most recent title if retired): - Other - Text',axis=1)
first_dataset=first_dataset.drop('In what industry is your current employer/contract (or your most recent employer if retired)? - Other - Text',axis=1)
first_dataset.head()


# In[9]:


first_dataset['Duration (in seconds)']= first_dataset['Duration (in seconds)'].astype('int')
first_dataset['Duration (in seconds)'] = first_dataset['Duration (in seconds)'] / 60
first_dataset = first_dataset.rename(columns={'Duration (in seconds)':'Duration (in hours)'})
first_dataset.head()


# In[10]:


first_dataset['Duration (in hours)'].describe()


# OMG !! mean is much more greater than median so we have highly right skewed distribution .We have outliers in Maximum side

# In[11]:


plt.figure(figsize=(5,6),dpi=300)
plt.hist(first_dataset['Duration (in hours)'],color='green')
plt.show()


# In[12]:


first_dataset['What is your gender? - Selected Choice'].value_counts()


# In[13]:


plt.figure(figsize=(5,6),dpi=300)
plt.pie(first_dataset['What is your gender? - Selected Choice'].value_counts(),labels=first_dataset['What is your gender? - Selected Choice'].value_counts().index,autopct='%1.0f%%')
plt.legend()
plt.show()


# So , why 81% male candidates are mostly likely to Data fields as a career..little bit surprised!!!!! 

# In[14]:


first_dataset['What is your age (# years)?'].value_counts()


# In[15]:


plt.figure(figsize=(5,6),dpi=300)
plt.barh(first_dataset['What is your age (# years)?'].value_counts().index,first_dataset['What is your age (# years)?'].value_counts())
plt.show()


# so  80% of the people comes under 22-34 .So data field is fastest emerging field.

# In[16]:


first_dataset['In which country do you currently reside?'].value_counts()


# In[17]:


plt.figure(figsize=(5,6),dpi=300)
plt.pie(first_dataset['In which country do you currently reside?'].value_counts(),labels=first_dataset['In which country do you currently reside?'].value_counts().index,autopct='%1.0f%%')
plt.show()


# USA and india are the close competition for producing more data related workers

# In[18]:


first_dataset['What is the highest level of formal education that you have attained or plan to attain within the next 2 years?'].value_counts()


# In[19]:


plt.figure(figsize=(5,6),dpi=300)
plt.pie(first_dataset['What is the highest level of formal education that you have attained or plan to attain within the next 2 years?'].value_counts(),labels=first_dataset['What is the highest level of formal education that you have attained or plan to attain within the next 2 years?'].value_counts().index,autopct='%1.0f%%')
plt.show()


# so Master's Degree / Bachelor's degree playing a vital role in data fields

# In[20]:


first_dataset['Which best describes your undergraduate major? - Selected Choice'].value_counts()


# In[21]:


plt.figure(figsize=(5,6),dpi=300)
plt.pie(first_dataset['Which best describes your undergraduate major? - Selected Choice'].value_counts(),labels=first_dataset['Which best describes your undergraduate major? - Selected Choice'].value_counts().index,autopct='%1.0f%%')


# so non-computer science students can get job in data fields

# In[24]:


first_dataset['Select the title most similar to your current role (or most recent title if retired): - Selected Choice'].value_counts()


# In[30]:


plt.figure(figsize=(5,6),dpi=300)
plt.barh(first_dataset['Select the title most similar to your current role (or most recent title if retired): - Selected Choice'].value_counts().index,first_dataset['Select the title most similar to your current role (or most recent title if retired): - Selected Choice'].value_counts())
plt.show()


# SO "STUDENTS","DATA SCIENTIST","SOFTWARE ENGINEER","DATA ANALYST" ARE THE MOST COMMON JOB ROLE IN DATA FIELDS

# In[31]:


first_dataset['In what industry is your current employer/contract (or your most recent employer if retired)? - Selected Choice'].value_counts()


# In[32]:


plt.figure(figsize=(5,6),dpi=300)
plt.barh(first_dataset['In what industry is your current employer/contract (or your most recent employer if retired)? - Selected Choice'].value_counts().index,first_dataset['In what industry is your current employer/contract (or your most recent employer if retired)? - Selected Choice'].value_counts())
plt.show()


# So aspiring students are computers science departments good to see.

# In[33]:


salary_exp = raw[['How many years of experience do you have in your current role?','What is your current yearly compensation (approximate $USD)?','Does your current employer incorporate machine learning methods into their business?']]
salary_exp.head()


# In[34]:


salary_exp['How many years of experience do you have in your current role?'].value_counts()


# In[35]:


plt.figure(figsize=(5,6),dpi=300)
plt.barh(salary_exp['How many years of experience do you have in your current role?'].value_counts().index,salary_exp['How many years of experience do you have in your current role?'].value_counts())
plt.show()


# so "Freshers" are most likely to chose data field as a career

# In[36]:


plt.figure(figsize=(5,6),dpi=300)
plt.barh(salary_exp['What is your current yearly compensation (approximate $USD)?'].value_counts().index,salary_exp['What is your current yearly compensation (approximate $USD)?'].value_counts())
plt.show()


# OMG! Lots of people dont want said there salary...Yeah right..

# In[42]:



plt.figure(figsize=(10,6),dpi=300)
plt.pie(salary_exp['Does your current employer incorporate machine learning methods into their business?'].value_counts(),labels=salary_exp['Does your current employer incorporate machine learning methods into their business?'].value_counts().index,autopct='%1.0f%%')
plt.show()


# Most of them want to apply machine learning algorithm to that .okay..!

# In[46]:


part_of_role = raw[['Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Analyze and understand data to influence product or business decisions',
                   'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Build and/or run a machine learning service that operationally improves my product or workflows',
                   'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data',
                   'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Build prototypes to explore applying machine learning to new areas',
                  'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Do research that advances the state of the art of machine learning',
                  'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - None of these activities are an important part of my role at work',
                  'Select any activities that make up an important part of your role at work: (Select all that apply) - Selected Choice - Other' ]]         
part_of_role.head()


# In[55]:


list=[]
for i in part_of_role.columns:
    i.value_counts()[0]
    i.append(list)


# In[ ]:





# In[ ]:




