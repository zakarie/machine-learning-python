
# coding: utf-8

# # Getting started with Python

# In[ ]:

print 'Hello World!'


# ## Create some variables in Python

# In[ ]:

i = 4  # int


# In[ ]:

type(i)


# In[ ]:

f = 4.1  # float


# In[ ]:

type(f)


# In[ ]:

b = True  # boolean variable


# In[ ]:

s = "This is a string!"


# In[ ]:

print s


# ## Advanced python types

# In[ ]:

l = [3,1,2]  # list


# In[ ]:

print l


# In[ ]:

d = {'foo':1, 'bar':2.3, 's':'my first dictionary'}  # dictionary


# In[ ]:

print d


# In[ ]:

print d['foo']  # element of a dictionary


# In[ ]:

n = None  # Python's null type


# In[ ]:

type(n)


# ## Advanced printing

# In[ ]:

print "Our float value is %s. Our int value is %s." % (f,i)  # Python is pretty good with strings


# ## Conditional statements in python

# In[ ]:

if i == 1 and f > 4:
    print "The value of i is 1 and f is greater than 4."
elif i > 4 or f > 4:
    print "i or f are both greater than 4."
else:
    print "both i and f are less than or equal to 4"


# ## Conditional loops

# In[ ]:

print l


# In[ ]:

for e in l:
    print e


# Note that in Python, we don't use {} or other markers to indicate the part of the loop that gets iterated.  Instead, we just indent and align each of the iterated statements with spaces or tabs. (You can use as many as you want, as long as the lines are aligned.)

# In[ ]:

counter = 6
while counter < 10:
    print counter
    counter += 1


# # Creating functions in Python
# 
# Again, we don't use {}, but just indent the lines that are part of the function.

# In[ ]:

def add2(x):
    y = x + 2
    return y


# In[ ]:

i = 5


# In[ ]:

add2(i)


# We can also define simple functions with lambdas:

# In[ ]:

square = lambda x: x*x

print 'hellow world'
# In[1]:

print 'hellow world'


# # getting started with python
# ## we have done so far
# * installed 
# * hi
# ## creating some variables in python

# In[4]:

i = 4 #int


# In[5]:

type(i)


# In[6]:

i


# In[7]:

f = 4.1


# In[8]:

type(f)


# In[11]:

b = True # boolen variable


# In[12]:

type(b)


# In[13]:

l = [2,3,4]


# In[14]:

l


# In[15]:

d = {'d' :2, 'h':4.1}


# In[16]:

d


# In[17]:

print(d)


# In[20]:

print d['h']


# ## advanced printing

# In[23]:

print"our fload value is %s and int value is %s" %(f,i)


# ## conditional statement in python

# In[ ]:

import graphlab


# In[ ]:

sales = graphlabSFrame('home_data.gl/')


# In[ ]:

sales


# In[ ]:

print(sales)


# In[ ]:



