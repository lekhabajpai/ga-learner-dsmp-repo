# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
path
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate([data, new_record])
print(census)
#Code starts here



# --------------
#Code starts here
path
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate([data, new_record])
#print(census)
#array age
age=census[:,0]
#print(age)
max_age, min_age = max(age), min(age)
age_mean = np.mean(age)
#(max_age - min_age)/(len(age))
age_std = np.std(age)
#print(max_age, min_age, age_mean, age_std)


# --------------
#Code starts here
path
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate([data, new_record])

#Race all
len_0, len_1, len_2, len_3, len_4 = 0, 0, 0, 0, 0
race = census[:,2]


#print(race)
for x in range(0,len(race)):
    race = census[x,2]
    #print(race)
    if race == 0:
        race_0 = census[census[:,2] == 0]
        #race_0 = np.append(race,x)
        #len_0 += 1
    elif race == 1:
        race_1 = census[census[:,2] == 1]
        len_1 += 1
    elif race == 2:
        race_2 = census[census[:,2] == 2]
        len_2 += 1
    elif race == 3:
        race_3 = census[census[:,2] == 3]
        len_3 += 1
    elif race == 4:
        race_4 = census[census[:,2] == 4]
        len_4 += 1
len_0, len_1, len_2, len_3, len_4 = len(race_0), len(race_1), len(race_2), len(race_3), len(race_4)   
#print(len_0, len_1, len_2, len_3, len_4)
min_race = min(len_0, len_1, len_2, len_3, len_4)
for x in range(0,4):
    if len_0 == min_race:
        minority_race = 0
    elif len_1 == min_race:
        minority_race = 1
    elif len_2 == min_race:
        minority_race = 2
    elif len_3 == min_race:
        minority_race = 3
    elif len_4 == min_race:
        minority_race = 4
print(minority_race)







# --------------
#Code starts here

senior_citizens = census[census[:,0] > 60]
#print(senior_citizens)
#print(age)

working_hours_sum = senior_citizens.sum(axis=0)[6]
print('working sum', working_hours_sum)
senior_citizens_len = len(senior_citizens)
print('len', senior_citizens_len)
avg_working_hours = (working_hours_sum / senior_citizens_len)
print('avg', avg_working_hours)
#code end


# --------------
#Code starts here

#filter high & low
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

avg_pay_high = (high[:,7]).mean()
avg_pay_low = (low[:,7]).mean()

print(avg_pay_high, avg_pay_low)




