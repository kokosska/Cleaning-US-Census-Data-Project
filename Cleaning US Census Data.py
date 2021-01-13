#!/usr/bin/env python
# coding: utf-8

# **Cleaning US Census Data**

# Exercise from Codecademy

# You just got hired as a Data Analyst at the Census Bureau, which collects census data and creates interesting visualizations and insights from it. The first visualization your boss wants you to make is a scatterplot that shows average income in a state vs proportion of women in that state.

# First thing need to be done is import all libraries I will use in this exercise.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import glob


# 
# It will be easier to inspect this data once we have it in a DataFrame.

# *Using glob, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census.*

# In[2]:


files = glob.glob('states*.csv')
us_census = []
for filename in files:
  data = pd.read_csv(filename)
  us_census.append(data)
us_census_df = pd.concat(us_census)
print(us_census_df.head())


# *Look at the .columns of the us_census DataFrame.*

# In[3]:


print(us_census_df.columns)


# *Look at the .dtypes of the us_census DataFrame.*

# In[4]:


print(us_census_df.dtypes)


# *Use regex to turn the Income column into a format that is ready for conversion into a numerical type.*

# In[5]:


us_census_df.Income = us_census_df['Income'].replace('[\$,]', '', regex=True)
us_census_df.Income = pd.to_numeric(us_census_df.Income)
print(us_census_df.dtypes)


# *Look at the GenderPop column - separate this into two columns, the Men column, and the Women column.*

# *Convert both of the columns into numerical datatypes.*

# In[6]:


gender_split = us_census_df.GenderPop.str.split('_')
us_census_df['Men'] = gender_split.str.get(0)
us_census_df['Women'] = gender_split.str.get(1)
us_census_df['Men'] = us_census_df.Men.str[0:-1]
us_census_df['Women'] = us_census_df.Women.str[0:-1]
us_census_df.Men = pd.to_numeric(us_census_df.Men)
us_census_df.Women = pd.to_numeric(us_census_df.Women)
print(us_census_df.dtypes)
print(us_census_df.head())


# *Check the number of NaN value in Women column and fill in by using pandas’ .fillna() function.*

# In[7]:


women_nan = us_census_df.Women.isna()
print(women_nan.value_counts())


# In[8]:


us_census_df = us_census_df.fillna(value = {'Women': us_census_df.TotalPop - us_census_df.Men})
print(us_census_df.Women.isna().value_counts())


# *Check for duplicates and if they occur drop those duplicates using the .drop_duplicates() function.*

# In[9]:


duplicates = us_census_df.duplicated()
#print(duplicates)
print(duplicates.value_counts())


# *Make the scatterplot that shows average income in a state vs proportion of women in that state.*

# In[10]:


scatter = pyplot.scatter(us_census_df.Women, us_census_df.Income)
pyplot.show()


# *Your boss wants you to make a bunch of histograms out of the race data that you have.*

# *Remove % sign in all columns: Hispanic, White, Black, Native, Asian, Pacific*

# In[11]:


us_census_df.Hispanic = us_census_df['Hispanic'].replace('[\%,]', '', regex=True)
us_census_df.White = us_census_df['White'].replace('[\%,]', '', regex=True)
us_census_df.Black = us_census_df['Black'].replace('[\%,]', '', regex=True)
us_census_df.Native = us_census_df['Native'].replace('[\%,]', '', regex=True)
us_census_df.Asian = us_census_df['Asian'].replace('[\%,]', '', regex=True)
us_census_df.Pacific = us_census_df['Pacific'].replace('[\%,]', '', regex=True)
print(us_census_df.head())


# *Change the data type from object to numeric in those columns*

# In[12]:


us_census_df.Hispanic = pd.to_numeric(us_census_df.Hispanic)
us_census_df.White = pd.to_numeric(us_census_df.White)
us_census_df.Black = pd.to_numeric(us_census_df.Black)
us_census_df.Native = pd.to_numeric(us_census_df.Native)
us_census_df.Asian = pd.to_numeric(us_census_df.Asian)
us_census_df.Pacific = pd.to_numeric(us_census_df.Pacific)
print(us_census_df.dtypes)


# *Check the number of NaN value in those columns and fill in by using pandas’ .fillna() function.*

# In[13]:


hispanic = us_census_df.Hispanic.isna()
#print(hispanic)
print(hispanic.value_counts())

white = us_census_df.White.isna()
#print(white)
print(white.value_counts())

black = us_census_df.Black.isna()
#print(black)
print(black.value_counts())

native = us_census_df.Native.isna()
#print(native)
print(native.value_counts())

asian = us_census_df.Asian.isna()
#print(asian)
print(asian.value_counts())

pacific = us_census_df.Pacific.isna()
#print(pacific)
print(pacific.value_counts())


# In[14]:


us_census_df = us_census_df.fillna( value = {'Pacific' : us_census_df.Pacific.mean()})
pacific = us_census_df.Pacific.isna()
#print(pacific)
print(pacific.value_counts())


# *Check for duplicates and if they occur drop those duplicates using the .drop_duplicates() function.*

# In[15]:


duplicates2 = us_census_df.duplicated()
#print(duplicates2)
print(duplicates2.value_counts())


# *Plotting the histogram*

# In[16]:


fig, ax = pyplot.subplots(2,3)
ax[0][0].hist(us_census_df['Hispanic'])
ax[0][1].hist(us_census_df['Pacific'])
ax[0][2].hist(us_census_df['White'])
ax[1][0].hist(us_census_df['Black'])
ax[1][1].hist(us_census_df['Native'])
ax[1][2].hist(us_census_df['Asian'])
ax[0][0].set(title='Hispanic', xlabel='% of population', ylabel='Frequency of occurrence')
ax[0][1].set(title='Pacific', xlabel='% of population', ylabel='Frequency of occurrence')
ax[0][2].set(title='White', xlabel='% of population', ylabel='Frequency of occurrence')
ax[1][0].set(title='Black', xlabel='% of population', ylabel='Frequency of occurrence')
ax[1][1].set(title='Native', xlabel='% of population', ylabel='Frequency of occurrence')
ax[1][2].set(title='Asian', xlabel='% of population', ylabel='Frequency of occurrence')
fig.suptitle('Histograms for different races', y=1.05, fontsize=15)
fig.tight_layout()
pyplot.show()

