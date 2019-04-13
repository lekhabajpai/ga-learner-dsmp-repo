# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split

#Code starts here
data = pd.read_csv(path)
X = data.iloc[:,:7]
y = data['Rating']
#plot histogram
sns.distplot(y.dropna())
plt.show()
#Cleaning - contains rating <= 5
data = data[(data['Rating'] <= 5)]
y = data['Rating']
#plot histogram
sns.distplot(y.dropna())
plt.show()



#Code ends here


# --------------
# code starts here
X_train, y_train = data.iloc[:,:7], data[['Rating']]
# Exploration
total_null = data.isnull().sum()
percentage_null = (total_null/data.isnull().count())
    
missing_data = pd.concat([total_null, percentage_null], axis=1, keys=['Total','Percent'])
print(missing_data)

#drop null values
data.dropna(inplace = True)

#Explorations 2
total_null_1 = data.isnull().sum()
percentage_null_1 = (total_null_1/data.isnull().count())
    
missing_data_1 = pd.concat([total_null_1, percentage_null_1], axis=1, keys=['Total','Percent'])
print(missing_data_1)

X_train, y_train = data.iloc[:,:7], data[['Rating']]

# code ends here


# --------------
import seaborn as sns

#Code starts here

ax = sns.catplot(x="Category", y="Rating", data=data, kind="box", height=10)
ax.set_xlabels(rotation=90)
#ax.suptitle('Rating vs Category')
plt.show()

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

#Cleaning
data['Installs'] = data['Installs'].str.replace(",", "")
data['Installs'] = data['Installs'].str.replace("+", "")

data['Installs'] = pd.to_numeric(data['Installs'])
print(data['Installs'])

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
print(data['Installs'])

sns.regplot(x="Installs", y="Rating", data=data)
plt.title("Rating vs Installs")
plt.show()

#Code ends here



# --------------
#Code starts here

print(data['Price'].value_counts())

data['Price'] = data['Price'].str.replace("$", "")
data['Price'] = pd.to_numeric(data['Price'])

sns.regplot(x="Price", y="Rating", data=data)
plt.title("Rating vs Price [RegPlot]")
plt.show()

#Code ends here


# --------------

#Code starts here
ser = pd.Series(data['Genres'])
#print(ser.unique())

data['Genres'] = data['Genres'].str.split(pat=";", n=1, expand=True)
#print(data['Genres'])

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
#gr_mean = data[data['Genres'], data['Rating']].groupby(data['Genres'], as_index=False)
print(gr_mean)

gr_mean = gr_mean.sort_values('Rating')
print(gr_mean)

#Code ends here


# --------------

#Code starts here
#print(data['Last Updated'])

Last = data['Last Updated']
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

print(data['Last Updated'])

max_date = data['Last Updated'].max()
print(max_date)

LastUpdatedDays = (max_date - data['Last Updated']).dt.days
print(LastUpdatedDays)

data['Last Updated Days'] = LastUpdatedDays

print(data.head())

sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title("Rating vs Last Updated [RegPlot]")
plt.show()

#Code ends here


