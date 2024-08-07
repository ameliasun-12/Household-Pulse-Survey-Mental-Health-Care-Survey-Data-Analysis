#%% 
#look at https://www.cdc.gov/nchs/covid19/pulse/mental-health-care.htm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Mental_Health_Care_in_the_Last_4_Weeks.csv')

#%%
data.head()

# %%
missing_values = data.isnull().sum()
descriptive_stats = data.describe()

cleaned_data = data.dropna(subset=['Value'])
cleaned_descriptive_stats = cleaned_data.describe()

missing_values, descriptive_stats, cleaned_data.head(), cleaned_descriptive_stats

indicators = [
    "Took Prescription Medication for Mental Health, Last 4 Weeks",
    "Received Counseling or Therapy, Last 4 Weeks",
    "Took Prescription Medication for Mental Health And/Or Received Counseling or Therapy, Last 4 Weeks",
    "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
]

filtered_data_indicators = cleaned_data[cleaned_data['Indicator'].isin(indicators)]

#%%
age_subgroups = ['18 - 29 years', '30 - 39 years', '40 - 49 years', '50 - 59 years','60 - 69 years', '70-79 years','80 years and above']
sex_subgroups = ['Male','Female']
gender_subgroups = ['Cis-gender male','Cis-gender female','Transgender']
orienta_subgroups = ['Gay or lesbian','Straight','Bisexual']
sympt_subgroups = ['Did not experience symptoms of anxiety/depression in the past 4 weeks', 'Experienced symptoms of anxiety/depression in past 4 weeks']
race_subgroups = ['Hispanic or Latino', 'Non-Hispanic Asian, single race','Non-Hispanic White, single race','Non-Hispanic Black, single race','Non-Hispanic, other races and multiple races']
edu_subgroups = ['Less than a high school diploma', 'High school diploma or GED',"Some college/Associate's degree","Bachelor's degree or higher"]
disab_subgroups = ['With disability', 'Without disability']
state_subgroups = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#%%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(age_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Age')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(sex_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Sex')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(gender_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Gender')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(orienta_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Sexual Orientation')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(sympt_subgroups)] 

plt.figure(figsize=(18, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Presence of Anxiety/Depression Symptoms')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(race_subgroups)] 

plt.figure(figsize=(20, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Race')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(edu_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Education')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(disab_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by Disability')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
# %%
filtered_data_subgroups = filtered_data_indicators[filtered_data_indicators['Subgroup'].isin(state_subgroups)] 

plt.figure(figsize=(29, 16))
sns.boxplot(data=filtered_data_subgroups, x='Subgroup', y='Value')
plt.title('Mental Health Care Values by State')
plt.xlabel('Subgroup')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.show()
#%%