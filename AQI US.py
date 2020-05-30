#importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

#reading dataset
df=pd.read_csv("US air.csv")
print(df)

value1=df['StateFips'].value_counts()
print(value1)

value2=df['Value'].value_counts()
print(value2)

#filling the missing values
grp_location=df.groupby(['CountyName','Value'])
dict_grp_location=dict(list(grp_location))

#print(df['StateFips'].isnull().sum())
#print(df['CountyFips'].isnull().sum())
#print(df['Value'].isnull().sum())

#adding new year & column
df['ReportYear']=df['ReportYear'].fillna(method='ffill')
print(df['ReportYear'].isnull().sum())
df['ReportYear']=df['ReportYear'].astype(int)
print(df)

#grouped state table
state=df.groupby('StateName').median()
state=state[['StateFips','Value']]

#plotting graph in descending order as per Value
state=state.sort_values(by='Value',ascending=False)
print(state.plot(kind='bar',figsize=(15,10)))
plt.show()

#plotting graph in descending order as per StateFips
state.sort_values(by='StateFips',ascending=False).plot(kind='bar',figsize=(15,10))
plt.show()

#top 5 states polluted
states=state.reset_index().head(5)
top_five_states=states['StateName']
for i in top_five_states:
    print(i)

#top 5 states with info
group_by_state=dict(list(df.groupby('StateName')))
plot_five_states=pd.DataFrame()
for i in top_five_states:
    df1=group_by_state[i][['StateName','CountyName','Value','StateFips','CountyFips']]
    plot_five_states=pd.concat([plot_five_states,df1])
print(plot_five_states)

#AQI levels in california
df=df.groupby('CountyName').median()
df=df.reset_index()
print(df)
plt.figure(figsize=(15,5))
plt.xticks(np.arange(1,20000))
plt.yticks(np.arange(5,1000))
sns.pointplot(df['CountyName'],df['Value'],color='r')
sns.pointplot(df['CountyName'],df['StateFips'],color='g')
plt.show()




