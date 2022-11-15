#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


countries_data = pd.read_excel('GDP_PPP.xls')


# In[3]:


countries_data


# The World Bank dataset includes mixed information, so there're 2 types of information in the column countries_data['Country Name']: names of the countries and aggregated information of regions, so need to split them in order to get the info only from countries.

# In[5]:


region_list = ['Africa Eastern and Southern', 
 'Africa Western and Central',
 'Arab World', 
 'Central Europe and the Baltics',
 'Caribbean small states',
 'East Asia & Pacific (excluding high income)',
 'East Asia & Pacific',
 'Europe & Central Asia (excluding high income)',
 'Europe & Central Asia',
 'Euro area',
 'European Union',
 'Early-demographic dividend',
 'Fragile and conflict affected situations',
 'High income',
 'Heavily indebted poor countries (HIPC)',
 'IBRD only',
 'IDA & IBRD total',
 'IDA total',
 'IDA blend',
 'IDA only',
 'Not classified',
 'Latin America & Caribbean',
 'Latin America & Caribbean (excluding high income)',
 'Least developed countries: UN classification',
 'Low income',
 'Lower middle income',
 'Low & middle income',
 'Late-demographic dividend',
 'Middle East & North Africa',
 'Middle East & North Africa (excluding high income)',
 'OECD members',
 'Other small states',
 'Pre-demographic dividend',
 'Pacific island small states',
 'Post-demographic dividend',
 'South Asia',
 'Sub-Saharan Africa (excluding high income)',
 'Sub-Saharan Africa',
 'Small states',
 'East Asia & Pacific (IDA & IBRD countries)',
 'Europe & Central Asia (IDA & IBRD countries)',
 'Latin America & the Caribbean (IDA & IBRD countries)',
 'Middle East & North Africa (IDA & IBRD countries)',
 'South Asia (IDA & IBRD)',
 'Sub-Saharan Africa (IDA & IBRD countries)',
 'Upper middle income',
 'World',
 ]


# In[6]:


region_data = countries_data.loc[countries_data['Country Name'].isin(region_list)]
countries_data = countries_data.loc[~countries_data['Country Name'].isin(region_list)]


# Let's find out the % of the countries which provided their data to the World Bank:

# In[8]:


countries_data[[2021]].count()


# In[9]:


countries_data[[2021]].count()/countries_data['Country Name'].count()


# As a result we can claim that the world bank calculates GDP PPP per capita for ~85% of countries in the word. 
# For the purpose of simplification, we drop the countries we can't get the data in 2021.
# 

# In[11]:


countries_data_2021 = countries_data[['Country Name',2021]].dropna(subset = [2021])
countries_data_2021.reset_index(drop = True, inplace = True)


# In[12]:


countries_data_2021


# In[13]:


np.median(countries_data_2021[2021])


# In[14]:


np.mean(countries_data_2021[2021])


# We can conclude that 90 countries has GDP per capita less then 14319.98. 90 countries - more than than number. 
# The average number is 23038.

# In[ ]:





# As long as I'm from Belarus, I'd like to know the average GDP ppp per capita for my homecountry and compare it with other countries in a dataset

# In[17]:


countries_data_2021[countries_data_2021['Country Name'] == 'Belarus']
belarus = countries_data_2021[countries_data_2021['Country Name'] == 'Belarus']
belarus


# In[18]:


countries_data_2021[countries_data_2021[2021]> belarus.iloc[0,1]]


# In[19]:


#Number of countries with GDP PPP per capita bigger than Belarus:
countries_data_2021[countries_data_2021[2021]> belarus.iloc[0,1]].count().iloc[0]


# In[20]:


#Number of countries with GDP PPP per capita smaller than Belarus:
countries_data_2021[countries_data_2021[2021]< belarus.iloc[0,1]].count().iloc[0]


# In[21]:


import matplotlib.pyplot as plt


# In[22]:


vals = [countries_data_2021[countries_data_2021[2021]> belarus.iloc[0,1]].count().iloc[0], countries_data_2021[countries_data_2021[2021]< belarus.iloc[0,1]].count().iloc[0]]
labels = ['Richer countries', 'Poorer countries']


# In[23]:


fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
ax.axis("equal")
plt.show()


# It can be concluded that 36.3% of the countries have higher GPD PPP per capita than Belarus 63.7% have lower GPD PPP per capita than Belarus

# In[ ]:





# Let's separate the countries into 10 different levels to find interesting insights:
# Let's add the column with the rank of the country in the rating GDP_PPP_per_capita 

# In[26]:


countries_data_2021['level']= np.nan
countries_data_2021['rank_GPD_PPP']= np.nan
countries_data_2021.sort_values(by = 2021, ascending = False, inplace = True)
countries_data_2021.reset_index(drop = True, inplace = True)


# In[27]:


int(countries_data_2021.count().iloc[0]/10)


# In[28]:


list_of_levels = [i for i in range(0,180,18)]
list_of_levels


# In[29]:


for i in range(180):
    if i< list_of_levels[1]:
        countries_data_2021.iloc[i,2]='level1'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[2]:
        countries_data_2021.iloc[i,2]='level2'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[3]:
        countries_data_2021.iloc[i,2]='level3'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[4]:
        countries_data_2021.iloc[i,2]='level4'
        countries_data_2021.iloc[i,3]= i+1
    elif i<list_of_levels[5]:
        countries_data_2021.iloc[i,2]='level5'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[6]:
        countries_data_2021.iloc[i,2]='level6'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[7]:
        countries_data_2021.iloc[i,2]='level7'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[8]:
        countries_data_2021.iloc[i,2]='level8'
        countries_data_2021.iloc[i,3]= i+1
    elif i< list_of_levels[9]:
        countries_data_2021.iloc[i,2]='level9'
        countries_data_2021.iloc[i,3]= i+1
    elif i>= list_of_levels[9]:
        countries_data_2021.iloc[i,2]='level10'
        countries_data_2021.iloc[i,3]= i+1


# In[30]:


countries_data_2021.rank_GPD_PPP = countries_data_2021.rank_GPD_PPP.apply(np.int64)


# In[31]:


countries_data_2021


# In[32]:


countries_data_2021.to_csv('countries_data_2021')


# In[33]:


countries_data_2021_grouped = countries_data_2021.groupby('level').agg({2021:'mean'})                              .sort_values(by =2021,ascending = False)
countries_data_2021_grouped


# In[34]:


difference_max_min = countries_data_2021_grouped.iloc[0]-countries_data_2021_grouped.iloc[9]
difference_max_min.iloc[0]


# We can conclude that the difference between mean value of GDP PPP per capita in level1 and level10 is $75960.86

# In[36]:


countries_data_2021.loc[countries_data_2021['level'] =='level1'][2021].std()


# In[37]:


countries_data_2021


# In[38]:


countries_data_2021.loc[countries_data_2021['level'] =='level10'][2021].std()


# In[39]:


[countries_data_2021.loc[countries_data_2021['level'] == 'level'+str(i)][2021].std() for i in range(1,11)]


# We can concude that as long as the country GDP PPP per capita rises, the GDP PPP per capita in most groups rises as well.
# 

# In[41]:


countries_data_2021


# We'd like to find if the corruption level is correlated with the GDP PPP per capita.
# With this purpose I parsed data from World economics report. 
# According to this DB, the higher Corruption PerceptionIndex, the lower the level of corruption

# In[43]:


title_corruption = pd.read_html('https://www.worldeconomics.com/Rankings/Economies-By-Corruption.aspx')[0].iloc[0]


# In[44]:


corruption = pd.read_html('https://www.worldeconomics.com/Rankings/Economies-By-Corruption.aspx')[1]                  .rename(columns = title_corruption).drop('RegionRank', axis = 1)


# In[45]:


corruption


# In[46]:


corruprtion_GDP_PPP = corruption.merge(countries_data_2021,left_on= 'Country',how = 'inner', right_on = 'Country Name').drop(['Country Name'], axis =1)


# In[47]:


corruprtion_GDP_PPP


# In[48]:


corruprtion_GDP_PPP.groupby('level').agg({'Corruption PerceptionIndex':'mean',2021:'mean' }).sort_values(by ='Corruption PerceptionIndex', ascending = False)


# In[49]:


corruprtion_GDP_PPP.corr()


# According to the information, we can conclude that there's a correlation between Corruption Perception Index and the level of GDP per capita. The higher Corruption PerceptionIndex,
# the less corruption in the country, the stronger the economy and vice verca.
# !correlation is not a causal relationship, so further research is needed to establish a causal relationship.

# In[ ]:





# I'm wondering if there're countries  with strong difference in their places in GDP PPP per capita and corruption level:

# In[52]:


big_gap = pd.Series([corruprtion_GDP_PPP.Country[i] for i in range(len(corruprtion_GDP_PPP))          if abs(corruprtion_GDP_PPP.GlobalRank[i] - corruprtion_GDP_PPP.rank_GPD_PPP[i])>70])


# In[53]:


corruprtion_GDP_PPP[corruprtion_GDP_PPP['Country'].isin(big_gap)]


# We can see from the list the most countries from Africa have low corruption ratings. The resons for these could be:
# - low data quality
# - traditions of population 
# - unknown reason

# I'd like to figure out the correlation between GDP PPP per capita and life expectancy: 

# In[56]:


life_expectancy = pd.read_html('https://www.worldeconomics.com/Indicator-Data/ESG/Social/Life-Expectancy/')[0]


# In[57]:


life_expectancy.rename(columns = {'Human Development Data: All Countries':'Country'}, inplace = True)


# In[58]:


life_expectancy = life_expectancy.merge(countries_data_2021,left_on= 'Country',how = 'inner', right_on = 'Country Name').drop(['Country Name'], axis =1)


# In[59]:


life_expectancy


# In[63]:


corruprtion_GDP_PPP.to_csv('corruprtion_GDP_PPP')


# In[61]:


life_expectancy.corr()


# In[62]:


life_expectancy.groupby('level').agg({'Life Expectancy(Years)':'std'}).sort_values(by ='Life Expectancy(Years)', ascending = False)


# Сonclusion of the Life Expectancy(Years)/GDP PPP per capita
# 
# 1) There's a pretty strong correlation between Life Expectancy and GDP PPP per capita, so the higher GDP PPP per capita, the higher Life Expectancy.
# 
# 2) As long as the GPD PPP per capita increases, the standard deviation of Life Expectancy narrows down,even though the difference in  GPD PPP per capita increases. It seems that there's a biological limit which can't be overcome with the increase of the level of life. 

# In[ ]:




