#made on Jupyter, from anaconda
#Extra: Data Visualization (Scatter Plot)

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import seaborn as sns


#Finds the average release date for each camera
process = pd.read_csv('cam_data.csv')

avgstor=process['Release date'].mean()
print("The Average Release Date for each Camera")
print(int(avgstor))


dfile1 = pd.read_csv('cam_data.csv', usecols = ['Release date'])

dfile=pd.read_csv('cam_data.csv')
data= dfile

#scatter plot comparing the type of camera and its release date
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.figure(figsize=(15,5)) #There are a lot of camera which is why the
plt.scatter(X,Y,color='red')
plt.title('Camera Release Dates')
plt.ylabel('Release Date')
plt.xlabel('Type of Camera')
plt.show()

#Makes coloumns in the dataset
#Correlation between graph and dataset
dfile=pd.read_csv('cam_data.csv')
dfile2= dfile.head()

print(dfile2)

