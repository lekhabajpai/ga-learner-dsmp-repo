# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)

# code starts here
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
#numerical variable
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)
banks = bank.drop(labels='Loan_ID', axis=1)

print(banks.isnull().sum())
bank_mode = banks.mode(axis=1, numeric_only=False)

banks.fillna(banks.mode().iloc[0], inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
#pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')[source]
avg_loan_amount = pd.pivot_table(banks,values='LoanAmount', index=['Gender','Married','Self_Employed'],aggfunc='mean')
# code ends here



# --------------
# code starts here
#DataFrame.count(axis=0, level=None, numeric_only=False)[source]
#Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)[source]
#big_loan_term = len(loan_term[loan_term >= 25]) 
loan_approved_se = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')).value_counts()[1]
loan_approved_nse = ((banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')).value_counts()[1]
Loan_Status = banks['Loan_Status'].count()
print('LA_SE=', loan_approved_se,'LA_NSE=', loan_approved_nse,'Loan Status=',Loan_Status)
#Cal % of loan approval for SE & NSE
se = (banks['Self_Employed'] == 'Yes').value_counts()
nse = (banks['Self_Employed'] == 'No').value_counts()
print(se,nse)
percentage_se = ((loan_approved_se * 100) /Loan_Status)
print(percentage_se)
percentage_nse = ((loan_approved_nse * 100) /Loan_Status)
print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term   = banks['Loan_Amount_Term'].apply(lambda x: x/12)  
#print(loan_term)  

big_loan_term = len(loan_term[loan_term >= 25])   
print(big_loan_term) 

# code ends here


# --------------
# code ends here
#DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, **kwargs)

#print(banks)
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.agg([np.mean])
print(mean_values)

# code ends here


