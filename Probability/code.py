# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df)
p_b = len(df[df['purpose']=='debt_consolidation'])/len(df)
df1 = df[df['purpose']=='debt_consolidation']
# Probability of event purpose = debt_consolidation given fico >700
p_a_b = len(df1[df1['fico']>700])/len(df[df['fico']>700])
df2 = df[df['fico']>700]
# Probability of event fico >700 given purpose = debt_consolidation
p_b_a = len(df2[df2['purpose']=='debt_consolidation'])/len(df[df['purpose']=='debt_consolidation'])
print(p_a)
print(p_b)
print(p_a_b)
print(p_b_a)
#Independecy Check
result = p_a_b==p_a
print(result)
# code ends here


# --------------
# code starts here

prob_lp = len(df[df['paid.back.loan']== 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)
print(prob_lp)
print(prob_cs)
new_df = df[df['paid.back.loan'] == 'Yes']
#prob of p(b|a) for event paid.back.loan = yes given credit.policy=yes
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
#Conditional probability
bayes = (prob_pd_cs * prob_lp)/ prob_cs
print(bayes)

# Probability of event purpose = debt_consolidation given fico >700
#p_a_b = len(df1[df1['fico']>700])/len(df[df['fico']>700])
#df2 = df[df['fico']>700]
# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan'] == 'No']
print(df1['purpose'].value_counts())
plt.bar(df1['purpose'], 10)
plt.show()

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
print(inst_median, inst_mean)
plt.hist(df['installment'], bins=10)
plt.show()


# code ends here


