# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here
df = pd.read_csv(path)
print(df.head())

X = df.iloc[:,:7]
y = df['insuranceclaim']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)



# Code ends here


# --------------
import matplotlib.pyplot as plt


# Code starts here
fig, ax = plt.subplots()
ax.boxplot(X_train['bmi'])
plt.show()

#set quantile
q_value = X_train['bmi'].quantile(0.95)

#Check calue counts
print(y_train.value_counts(normalize=True))

# Code ends here


# --------------
# Code starts here
relation = X_train.corr()
print(relation)

sns.pairplot(X_train)
plt.show()

# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here

#store categorical variable
cols = ['children', 'sex', 'region', 'smoker']
print(cols)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,20))

for i in range(0,2):
    for j in range(0,2): 
        col = cols[i * 2 +j]
        sns.countplot(x=X_train[col], hue=y_train, ax=axes[i,j])


# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here

lr = LogisticRegression()

#GridSearchCV
grid = GridSearchCV(estimator=lr, param_grid=parameters)
#fit model
grid.fit(X_train, y_train)

#Predict
y_pred = grid.predict(X_test)
print(y_pred)

accuracy = grid.score(X_test, y_test)
print(accuracy)


# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix

# Code starts here
score = roc_auc_score(y_test, y_pred)

y_pred_proba = grid.predict_proba(X_test)[:,1]
#print(y_pred_proba)

fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_proba)
print(fpr, tpr)

roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label='Logistic model')
plt.show()



# Code ends here


