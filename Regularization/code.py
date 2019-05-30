# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path
df = pd.read_csv(path)
#Code starts here

#display first 5 columns
#print(df.iloc[:, :5])

y = df['Price']
#X = df.iloc[:,:9]
X = df.drop('Price', axis=1)

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=6)

corr = X_train.corr(method='pearson')
print(corr)


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
#mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here
lasso = Lasso()
lasso.fit(X_train, y_train)

lasso_pred = lasso.predict(X_test)

r2_lasso = r2_score(y_test, y_pred)
print(r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here
ridge = Ridge()
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
r2_ridge = r2_score(y_test, y_pred)

# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

#Code starts here
regressor = LinearRegression()
model = regressor
score = cross_val_score(model, X_train, y_train, cv = 10)

mean_score = score.mean()
print(mean_score)



# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here

model = make_pipeline(PolynomialFeatures(2), LinearRegression())

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2_poly = r2_score(y_test, y_pred)
print(r2)


