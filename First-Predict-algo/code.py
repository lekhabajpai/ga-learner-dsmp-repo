# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
print(df.head(5))
#Store features in X
y = df.iloc[:,1]
X = df.iloc[:,:9]
#X = X.drop('list_price', axis=1)
#print(X.head())
#Split dataframe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

# display first five rows of training features and target
print(X_train.head())
print(y_train.head())

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        

cols = X_train.columns
#print(cols)
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))
for i in range(0,3):
    for j in range(0,3):
        col = cols[i * 3 + j]
        axes[i,j].set_title(col)
        axes[i,j].scatter(X_train[col], y_train)
        axes[i,j].set_xlabel(col)
        axes[i,j].set_ylabel('list_price')
       
plt.show()

# code ends here



# --------------
# Code starts here



# Code ends here
corr = X_train.corr()
print(corr)
#drop columns from X_train
X_train.drop(['play_star_rating', 'val_star_rating'], axis = 1, inplace=True)
#drop columns form X_test
X_test.drop(['play_star_rating', 'val_star_rating'], axis = 1, inplace=True)


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(r2)

# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
print(residual)


# Code ends here


