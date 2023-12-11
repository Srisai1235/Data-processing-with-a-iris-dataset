#import the required packages 
import numpy as np
import pandas as pd
from numpy import nan as na

#import the .csv file 
data=pd.read_csv("Data1.csv")
data

#make it as a data  frame
aa=pd.DataFrame(data)
aa

#data description
aa.describe()
aa.describe().astype(int)
aa.describe(include='all')
aa['Salary'].describe()
aa['Age'].describe()

#visualization...
import matplotlib.pyplot as plt
import numpy as np
xline = aa['Salary']
yline = aa["Age"]
plt.plot(xline, yline)
plt.show()

#handling missing data 
aa.isnull()

#droping the null values
aa.dropna()
aa['Salary'].dropna()

#filling the NaN values with our desired value
aa.fillna("15426.0")
aa.fillna({'Age':24.0,'Salary':23453.0})

#fill the NaN values using ffill and bfill
aa.fillna(method='bfill')
aa.fillna(method='ffill')

#filter the duplicates
aa.duplicated()
aa['Age'].duplicated()

#remove duplicates 
aa.drop_duplicates()
