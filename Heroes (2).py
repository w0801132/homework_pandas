
# coding: utf-8

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
ogfile = "C:/Users/ginaf/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
ogdata = pd.read_csv(ogfile)
ogdata.head()


# In[3]:


#list(ogdata)


# In[4]:


#Display the total number of players
ddupdata=ogdata.SN.drop_duplicates()
#ddupdata.describe()


# In[5]:


#ddupdata.head()


# In[6]:


nadrop=ogdata.drop_duplicates(['SN'], 'first')
#nadrop.head()


# In[7]:


#nadrop.describe()


# In[8]:


totalpl={'Total Players': [576]}
distotal = pd.DataFrame(data=totalpl)
distotal
#there's probably a way better way of doing this, but I'm just thrilled I got it to work this way


# In[9]:


#Run basic calculations to obtain number of unique items, average price, etc.
uitems=ogdata.drop_duplicates(['Item ID'], 'first')
#uitems.head()


# In[10]:


#uitems.describe()


# In[11]:


#ogdata.describe()


# In[12]:


#len(ogdata['Purchase ID'])


# In[13]:


#sum(ogdata['Price'])


# In[14]:


#Create a summary data frame to hold the results
disbasic={'Unique Items': [183], 'Average Price': ['$3.07'], 'Number of Purchases': [780], 'Total Revenue': ['$2,379.77']}

#Optional: give the displayed data cleaner formatting


#Display the summary data frame
disbas = pd.DataFrame(data=disbasic)
disbas
#Again, probably less shitty ways of doing it, but I did it


# In[15]:


#Percentage and Count of Male Players
onlyboys=nadrop.loc[ogdata['Gender']== "Male"]
#onlyboys.describe()


# In[16]:


#Percentage and Count of Female Players
onlywomen=nadrop.loc[ogdata['Gender']== "Female"]
#onlywomen.describe()


# In[17]:


#Percentage and Count of Other / Non-Disclosed
onlyb=484
onlyw=81
totalppl=576
otherppl=(totalppl-(onlyb+onlyw))


# In[18]:


others=nadrop.loc[ogdata['Gender']== "Other / Non-Disclosed"]
#others.describe()


# In[19]:


playinfo={' ': ['Male', 'Female', 'Other/Non-Disclosed'],
          'Total Count': [onlyb, onlyw, otherppl],
          'Percentage of Players': [((onlyb/totalppl)*100), ((onlyw/totalppl)*100), ((otherppl/totalppl)*100)]}

#Display the summary data frame
playinfodf = pd.DataFrame(data=playinfo)

#Optional: give the displayed data cleaner formatting
playinfodf['Percentage of Players']=playinfodf["Percentage of Players"].map("{0:.2f}%".format)


playinfodf


# In[20]:


#ogdata.describe()


# In[21]:


#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
purch=ogdata.loc[:, ['Purchase ID', 'Gender']]
#purch.head()


# In[22]:


boybuy=purch.loc[ogdata['Gender']== "Male"]
boybuy.describe()
bbuy=652


# In[23]:


wobuy=purch.loc[ogdata['Gender']== "Female"]
wobuy.describe()
wbuy=113


# In[24]:


pplbuy=purch.loc[ogdata['Gender']== "Other / Non-Disclosed"]
pplbuy.describe()
pbuy=15


# In[25]:


avgprice=ogdata.loc[:, ['Price', 'Gender']]
#avgprice.head()


# In[26]:


boyprice=avgprice.loc[ogdata['Gender']== "Male"]
boyprice.describe()
bavg=3.02


# In[27]:


woprice=avgprice.loc[ogdata['Gender']== "Female"]
woprice.describe()
wavg=3.20


# In[28]:


plprice=avgprice.loc[ogdata['Gender']== "Other / Non-Disclosed"]
plprice.describe()
plavg=3.35


# In[29]:


pltotal=sum(plprice['Price'])
#pltotal


# In[30]:


#plmean=plprice['Price'].mean()
#plmean


# In[31]:


perpl=pltotal/otherppl
#perpl


# In[32]:


#Create a summary data frame to hold the results
purchinfo={'Gender': ['Male', 'Female', 'Other/Non-Disclosed'], 
           'Purchase Count': [bbuy, wbuy, pbuy], 
           'Average Purchase Price': [bavg, wavg, plavg], 
           'Total Purchase Value': [ (sum(boyprice['Price'])), (sum(woprice['Price'])), (sum(plprice['Price'])) ], 
           'Avg Total Purchase Per Player': [(sum(boyprice['Price'])/onlyb), (sum(woprice['Price'])/onlyw), (sum(plprice['Price'])/otherppl)]}

purchinfodf = pd.DataFrame(data=purchinfo)

#Optional: give the displayed data cleaner formatting
#hosted_in_us["average_donation"] = hosted_in_us["average_donation"].astype(float).map("${:,.2f}".format)
purchinfodf["Average Purchase Price"]=purchinfodf["Average Purchase Price"].map("${: ,.2f}".format)
purchinfodf["Total Purchase Value"]=purchinfodf["Total Purchase Value"].map("${: ,.2f}".format)
purchinfodf["Avg Total Purchase Per Player"]=purchinfodf["Avg Total Purchase Per Player"].map("${: ,.2f}".format)

purchinfodf


# In[33]:


#Establish bins for ages
bins = [0, 10, 15, 20, 25, 30, 35, 40, 50]
group_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


#Categorize the existing players using the age bins. Hint: use pd.cut()
binned_data=pd.cut(nadrop['Age'], bins, labels=group_labels, right=False)
#binned_data.head()


# In[34]:


nadrop['Age Group']=binned_data
#nadrop.head()


# In[35]:


grouped_age=nadrop.groupby(['Age Group'])
#grouped_age.head()


# In[36]:


#Calculate the numbers and percentages by age group
#grouped_age.count()


# In[37]:


#Create a summary data frame to hold the results
agestuff={' ': ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"],
          'Total Count': ["17", "22", "107", "258", "77", "52", "31", "12"],
          'Percentage of Players': [((17/576)*100), ((22/576)*100), ((107/576)*100), ((258/576)*100), ((77/576)*100), ((52/576)*100), ((31/576)*100), ((12/576)*100)]}

#Optional: round the percentage column to two decimal points
#agestuff['Percentage of Players']=agestuff['Percentage of Players'].map("{0:.2f}%".format)

#Display Age Demographics Table
agestuffdf = pd.DataFrame(data=agestuff)
agestuffdf


# In[38]:


#Bin the purchase_data data frame by age
bins = [0, 10, 15, 20, 25, 30, 35, 40, 50]
group_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


#Categorize the existing players using the age bins. Hint: use pd.cut()
binned_dataog=pd.cut(ogdata['Age'], bins, labels=group_labels, right=False)
ogdata['Age Group']=binned_dataog
ogdata.head()
#nadrop.describe()
#ogdata.describe()


# In[39]:


#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
purchage=ogdata.loc[:, ['Price', 'Age Group']]
#purchage.head()
#purchage.describe()


# In[40]:


price1=purchage.loc[ogdata['Age Group']== "<10"]
#price1.describe()
count1=23
pr1=3.35


# In[41]:


price2=purchage.loc[ogdata['Age Group']== "10-14"]
#price2.describe()
count2=28
pr2=2.95


# In[42]:


price3=purchage.loc[ogdata['Age Group']== "15-19"]
#price3.describe()
count3=136
pr3=3.03


# In[43]:


price4=purchage.loc[ogdata['Age Group']== "20-24"]
#price4.describe()
count4=365
pr4=3.05


# In[44]:


price5=purchage.loc[ogdata['Age Group']== "25-29"]
#price5.describe()
count5=101
pr5=2.90


# In[45]:


price6=purchage.loc[ogdata['Age Group']== "30-34"]
#price6.describe()
count6=73
pr6=2.93


# In[46]:


price7=purchage.loc[ogdata['Age Group']== "35-39"]
#price7.describe()
count7=41
pr7=3.60


# In[47]:


price8=purchage.loc[ogdata['Age Group']== "40+"]
#price8.describe()
count8=13
pr8=2.94


# In[50]:


#purchase_group=ogdata.groupby(['Age Group'])
#purchase_group.head()

#for group in purchase_group:
    #sum(ogdata['Price'])

# purch_group=ogdata.loc[:, ['Age Group', 'Price']]
# purch_grouped = pd.DataFrame(data=purch_group)
#purch_grouped


ogdata.groupby('Age Group').agg(lambda x:  {'sum': x.sum(), 'mean':x.mean()})


# purch_groupdf.head()


# In[48]:


#Create a summary data frame to hold the results
purchagedf={' ': ['>10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+'], 
           'Purchase Count': [count1,count2, count3, count4, count5, count6, count7, count8 ], 
           'Average Purchase Price': [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8]} 
           #'Total Purchase Value': [  ], 
           #'Avg Total Purchase Per Player': [ ]}

purchagedf = pd.DataFrame(data=purchage)

#Optional: give the displayed data cleaner formatting
#purchagedf["Average Purchase Price"]=purchagedf["Average Purchase Price"].map("${: ,.2f}".format)
#purchagedf["Total Purchase Value"]=purchagedf["Total Purchase Value"].map("${: ,.2f}".format)
#purchagedf["Avg Total Purchase Per Player"]=purchagedf["Avg Total Purchase Per Player"].map("${: ,.2f}".format)

#Display the summary data frame
purchagedf.head()


# In[49]:


#Run basic calculations to obtain the results in the table below
spend=nadrop.loc[:, ['SN', 'Price']]
spend.head()


# In[50]:


user=spend.loc[ogdata['SN']== "Lisosia93"].sum()
user.describe()


# In[51]:


#SN=spend(1)

#for SN in spend:
    #if SN=(SN+1)
        #return sum(nadrop['Price'])    


# In[52]:


#Create a summary data frame to hold the results
#SN_d = dict(zip(nadrop['SN']))

#spenddf={'SN': [SN_d], 
           #'Purchase Count': [ ], 
           #'Average Purchase Price': [ ]} 
           #'Total Purchase Value': [ (sum(boyprice['Price'])), (sum(woprice['Price'])), (sum(plprice['Price'])) ], 
           #'Avg Total Purchase Per Player': [(sum(boyprice['Price'])/17), (sum(woprice['Price'])/22), (sum(plprice['Price'])/107),
                                            #(sum(boyprice['Price'])/258), (sum(woprice['Price'])/77), (sum(plprice['Price'])/52),
                                            #(sum(boyprice['Price'])/31), (sum(woprice['Price'])/12)]}

#spenddf = pd.DataFrame(data=spend)

#Sort the total purchase value column in descending order


#Optional: give the displayed data cleaner formatting
#spenddf["Average Purchase Price"]=spenddf["Average Purchase Price"].map("${: ,.2f}".format)
#spenddf["Total Purchase Value"]=spenddf["Total Purchase Value"].map("${: ,.2f}".format)

#Display a preview of the summary data frame


# In[55]:


#Retrieve the Item ID, Item Name, and Item Price columns
popitem=ogdata.loc[:, ['Item ID', 'Item Name', 'Price']]
popitem.head()


# In[58]:


#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
popgroup=popitem.groupby(['Item ID', 'Item Name'])
popgroup.head()


# In[59]:


popgroup.describe()


# In[ ]:


#Create a summary data frame to hold the results
popits={'Item ID': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
                    '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', 
                    '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76',
                    '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', 
                    '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', 
                    '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129',
                    '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146',
                    '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', 
                    '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181',],
          'Item Name': [onlyb, onlyw, otherppl],
          'Purchase Count': [((onlyb/totalppl)*100), ((onlyw/totalppl)*100), ((otherppl/totalppl)*100)]
          'Item Price': [onlyb, onlyw, otherppl],
          'Total Purchase Value': [ ]}

#Display the summary data frame
playinfodf = pd.DataFrame(data=playinfo)

#Optional: give the displayed data cleaner formatting
playinfodf['Percentage of Players']=playinfodf["Percentage of Players"].map("{0:.2f}%".format)


playinfodf

#Sort the purchase count column in descending order


#Optional: give the displayed data cleaner formatting


#Display a preview of the summary data frame


# In[54]:


#Sort the above table by total purchase value in descending order


#Optional: give the displayed data cleaner formatting


#Display a preview of the data frame

