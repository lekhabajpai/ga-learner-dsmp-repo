# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#print(data)
#Code starts here 
data['Gender'].replace('-', 'Agender',inplace=True)
#print(data)
gender_count = data['Gender'].value_counts()
print(gender_count)
plt.bar(gender_count.index, gender_count)
plt.plot(kind='bar')
plt.show()



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
explode=(0.1,0.1,0.1)
labels=alignment.iloc[0:]
print('Label=',labels)
plt.pie(alignment, explode, labels=labels)
plt.title('Character  Alignment')


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
# Find covariance
sc_covariance = round(sc_df.cov().loc['Strength','Combat'], 2)
print('sc_covariance= ', sc_covariance)
#Find Standard Deviation
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
print('sc_strength', sc_strength, 'sc_combat', sc_combat)
#Find Pearson corelation
sc_pearson = round((sc_covariance / (sc_strength*sc_combat)), 2)
print('sc_pearson= ', sc_pearson)

#Same for Intelligence & Combat
ic_df = data[['Intelligence', 'Combat']].copy()
# Find covariance
ic_covariance = ic_df.cov().loc['Intelligence','Combat']
print('ic_covarinace = ', ic_covariance)
#Find Standard Deviation
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
print('ic_intelligence', ic_intelligence, 'ic_combat', ic_combat)
#Find Pearson corelation
ic_pearson = (ic_covariance / (ic_intelligence*ic_combat))
print('ic_pearson = ', ic_pearson)




# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
print(total_high)
super_best = data[data['Total'] > total_high]
print(super_best)
super_best_names=list();
super_best_name = super_best['Name'].tolist()
print(super_best_name)




# --------------
#Code starts here
fig = plt.figure(figsize=(60,20))
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1)
#res = data['Intelligence', 'Speed', 'Power'])
res1 = data.groupby(['Intelligence'])
res1.plot(kind='bar', stacked=True, ax=ax_1)
ax_1.set_title('Intelligence')
#res.plot(kind='bar', stacked=True, ax=ax_2)
#ax_2.set_title('Speed')
#res.plot(kind='bar', stacked=True, ax=ax_3)
#ax_3.set_title('Power')


