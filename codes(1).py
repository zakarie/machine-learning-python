
# coding: utf-8

# In[1]:

import graphlab


# In[2]:

sf = graphlab.SFrame('people-example.csv')


# In[3]:

sf


# In[5]:

# take any data structure in graph lab create 
sf.show()


# In[6]:

graphlab.canvas.set_target('ipynb')


# In[7]:

sf['age'].show('Categorical')


# # inspect columns of dataset

# In[8]:

sf['Country']


# In[9]:

sf['age']


# In[10]:

sf['age'].mean()


# In[11]:

sf['age'].max()


# # create new columns in our sframe

# In[13]:

sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']


# In[14]:

sf


# In[15]:

sf['age'] * sf['age']


# # use the apply function to do advanced our data

# In[16]:

sf['Country']


# In[19]:

sf['Country'].show()


# In[20]:

def transform_country (country):
    if country == 'USA':
        return 'United States'
    else :
        return country


# In[21]:

transform_country('USA')


# In[23]:

sf['Country'].apply(transform_country)


# In[24]:

sf['Country'] = sf['Country'].apply(transform_country)


# In[25]:

sf


# In[ ]:

sf


# In[ ]:



