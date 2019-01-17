# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
#value count of Loan_Status
loan_status = data['Loan_Status'].value_counts()
print(loan_status)
#Plot bar graph
plt.figure(figsize=[14,8])
#plt.xlabel("Type 2 Pokemon Variants")
#plt.ylabel("No of Pokemons")
plt.title("Distribution loan approvals")
# display plot
plt.bar(loan_status.index, loan_status)
plt.plot(kind='bar')
plt.show()

#Code starts here


# --------------
#Code starts here
data = pd.read_csv(path)
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
#X axis
plt.xlabel("Property Area")
#y axis
plt.ylabel("Loan Staus")
#Rotae labels of x axis by 45deg
plt.xticks(rotation=45)

# display plot
#plt.bar(property_and_loan.index, property_and_loan)
#plt.plot(kind='bar')
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
#X axis
plt.xlabel("Education Status")
#y axis
plt.ylabel("Loan Staus")
#Rotae labels of x axis by 45deg
plt.xticks(rotation=45)

# display plot
#plt.bar(property_and_loan.index, property_and_loan)
#plt.plot(kind='bar')
plt.show()


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
#plot a density plot
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

# display plot
plt.show()










#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig = plt.figure(figsize=(40,20))
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1)

data.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome', y='LoanAmount', ax=ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)
ax_3.set_title('Total Income')



