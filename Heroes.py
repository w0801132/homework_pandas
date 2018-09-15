
# coding: utf-8

# In[221]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
ogfile = "C:/Users/ginaf/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
ogdata = pd.read_csv(ogfile)
ogdata.head()


# In[222]:


list(ogdata)


# In[223]:


#Display the total number of players
ddupdata=ogdata.SN.drop_duplicates()
ddupdata.describe()


# In[224]:


ddupdata.head()


# In[225]:


nadrop=ogdata.drop_duplicates(['SN'], 'first')
nadrop.head()


# In[226]:


nadrop.describe()


# In[227]:


totalpl={'Total Players': [576]}
distotal = pd.DataFrame(data=totalpl)
distotal
#there's probably a way better way of doing this, but I'm just thrilled I got it to work this way


# In[228]:


#Run basic calculations to obtain number of unique items, average price, etc.
uitems=ogdata.drop_duplicates(['Item ID'], 'first')
uitems.head()


# In[229]:


uitems.describe()


# In[230]:


ogdata.describe()


# In[231]:


len(ogdata['Purchase ID'])


# In[232]:


sum(ogdata['Price'])


# In[233]:


#Create a summary data frame to hold the results
disbasic={'Unique Items': [183], 'Average Price': ['$3.07'], 'Number of Purchases': [780], 'Total Revenue': ['$2,379.77']}

#Optional: give the displayed data cleaner formatting


#Display the summary data frame
disbas = pd.DataFrame(data=disbasic)
disbas
#Again, probably less shitty ways of doing it, but I did it


# In[234]:


#Percentage and Count of Male Players
onlyboys=nadrop.loc[ogdata['Gender']== "Male"]
onlyboys.describe()


# In[235]:


#Percentage and Count of Female Players
onlywomen=nadrop.loc[ogdata['Gender']== "Female"]
onlywomen.describe()


# In[236]:


#Percentage and Count of Other / Non-Disclosed
onlyb=484
onlyw=81
totalppl=576
otherppl=(totalppl-(onlyb+onlyw))


# In[237]:


playinfo={'Male': [onlyb, (onlyb/totalppl)], 'Female': [onlyw, (onlyw/totalppl)], 'Other/Non-Disclosed': [otherppl, (otherppl/totalppl)]}

#Display the summary data frame
playinfodf = pd.DataFrame(data=playinfo)

#Optional: give the displayed data cleaner formatting
#playinfodf.style.format("{:.2%}")
#playinfodf["Male"]=playinfodf["Male"].map("{:.0}".format)
#playinfodf.apply("{:.2%}".format)
playinfodf


# In[238]:


#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender


#Create a summary data frame to hold the results


#Optional: give the displayed data cleaner formatting


#Display the summary data frame


# In[239]:


#Establish bins for ages


#Categorize the existing players using the age bins. Hint: use pd.cut()


#Calculate the numbers and percentages by age group


#Create a summary data frame to hold the results


#Optional: round the percentage column to two decimal points


#Display Age Demographics Table


# In[240]:


#Bin the purchase_data data frame by age


#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


#Create a summary data frame to hold the results


#Optional: give the displayed data cleaner formatting


#Display the summary data frame


# In[241]:


#Run basic calculations to obtain the results in the table below


#Create a summary data frame to hold the results


#Sort the total purchase value column in descending order


#Optional: give the displayed data cleaner formatting


#Display a preview of the summary data frame


# In[242]:


#Retrieve the Item ID, Item Name, and Item Price columns


#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


#Create a summary data frame to hold the results


#Sort the purchase count column in descending order


#Optional: give the displayed data cleaner formatting


#Display a preview of the summary data frame


# In[243]:


#Sort the above table by total purchase value in descending order


#Optional: give the displayed data cleaner formatting


#Display a preview of the data frame

