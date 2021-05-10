#pokemon_networkx.py
#https://www.kaggle.com/kingburrito666/pokemon-complete-analysis-networkx
import numpy as np #linear algebra
import pandas as pd #data processing, csv file i.e. pd.read()
import seaborn as sns #STAT graphs 

from subprocess import check_output
#checks output for error https://docs.python.org/3/library/subprocess.html

import matplotlib.pyplot as plt 
import networkx as nx

#import data and view head and tail
data = pd.read_csv('/Users/kcchua/Documents/GitHub/ICANN-Lab/Pokemon.csv')
print(data.head())
print(data.tail())

#check for null values
print(len(data.isnull().any()))
print(data.isnull().any())

#replace the nulls. np = numpy, nan = not a number.  
#inplace = True is used, it performs operation on data and nothing is returned.
data['Type 2'].replace(np.nan,'0',inplace=True)
data['Type 2'].head(10)
print(data['Type 2'].head(10)) #since we see 0's here, instead of nan, we are good

print("Number of pokemon are: "+ str(data['Name'].nunique() )) #800 pokemon
pd.DataFrame(data['Name'].unique().tolist(), columns=['Pokemon']) #returns a list of values
#How to see output of above line:
#yeah=pd.DataFrame(data['Name'].unique().tolist(), columns=['Pokemon']) #returns a list of values
#print(yeah)

##copy the data and plot it
npoke_total = data.copy()
npoke_total.columns
#print(npoke_total.columns) #see the columns

npoke_total = pd.concat([npoke_total['Name'], data['Total']], axis=1)
#print(npoke_total) #see the concatenated list

######
## Big plot
######

sns.set() #initialize a graph set
plt.figure(figsize=(8,20))
#input, output, and sorting for the graph display
ax = sns.barplot(x='Total',y='Name',data=npoke_total.sort_values(by='Total',ascending=False).head(25)) 
ax.set(xlabel='Overall',ylabel='Pokemon') #initialize the graph labels
plt.show()

######
## NetworkX data analysis
######

g=nx.graph #initialize a graph container
#g = nx.from_pandas_dataframe(data,source='Name',target='Type 1')
#In networkx 2.0 from_pandas_dataframe has been removed.
#Instead you can use from_pandas_edgelist.
g = nx.from_pandas_edgelist(data,source='Name',target='Type 1')
print(nx.info(g))