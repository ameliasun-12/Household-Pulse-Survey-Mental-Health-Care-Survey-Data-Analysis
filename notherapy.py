#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Mental_Health_Care_in_the_Last_4_Weeks.csv')

missing_values = data.isnull().sum()
descriptive_stats = data.describe()

cleaned_data = data.dropna(subset=['Value'])
cleaned_descriptive_stats = cleaned_data.describe()

indicators = [
    "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks",
    "Received Counseling or Therapy, Last 4 Weeks",
    "Needed Counseling or Therapy But Did Not Get It And/Or Received Counseling or Therapy, Last 4 Weeks",
    "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
]

filtered_data_indicators = cleaned_data[cleaned_data['Indicator'].isin(indicators)]

age_subgroups = ['18 - 29 years', '30 - 39 years', '40 - 49 years', '50 - 59 years','60 - 69 years', '70-79 years','80 years and above']
sex_subgroups = ['Male','Female']
gender_subgroups = ['Cis-gender male','Cis-gender female','Transgender']
orienta_subgroups = ['Gay or lesbian','Straight','Bisexual']
sympt_subgroups = ['Did not experience symptoms of anxiety/depression in the past 4 weeks', 'Experienced symptoms of anxiety/depression in past 4 weeks']
race_subgroups = ['Hispanic or Latino', 'Non-Hispanic Asian, single race','Non-Hispanic White, single race','Non-Hispanic Black, single race','Non-Hispanic, other races and multiple races']
edu_subgroups = ['Less than a high school diploma', 'High school diploma or GED',"Some college/Associate's degree","Bachelor's degree or higher"]
disab_subgroups = ['With disability', 'Without disability']
state_subgroups = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# %%
indicator_filter = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data_by_indicator = data[data['Indicator'] == indicator_filter]

pivot_data_by_subgroup_within_indicator = filtered_data_by_indicator.pivot_table(index='Time Period', columns='Subgroup', values='Value')

correlation_matrix_subgroup_within_indicator = pivot_data_by_subgroup_within_indicator.corr()

plt.figure(figsize=(64, 48))
sns.heatmap(correlation_matrix_subgroup_within_indicator, annot=True, fmt=".2f", cmap='coolwarm', center=0,
            annot_kws={"size": 10}, linewidths=.5, cbar_kws={"shrink": 0.75})
plt.title(f'Correlation Matrix of Subgroups within "{indicator_filter}" Indicator', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
#%%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(age_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Differing Age Groups by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()
# %%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(sex_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Sexes by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()
# %%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(gender_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Gender Identity by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

#%%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(orienta_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Sexual Orientations by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

#%%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(sympt_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Presence of Anxiety/Depression Symptoms by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

#%%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(race_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Races by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(edu_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of Education Level by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

#%%
indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(disab_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison Between Abled and Disabled by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.grid(True)
plt.show()

indicator = "Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks"
filtered_data = data[(data['Subgroup'].isin(state_subgroups)) & (data['Indicator'] == indicator)]

# Create the scatter plot
plt.figure(figsize=(14, 8))
sns.scatterplot(data=filtered_data, x='Time Period', y='Value', hue='Subgroup', palette='viridis')
plt.title(f'Comparison of States by Amount Who Needed Counseling or Therapy But Did Not Get It Over the Last 4 Weeks Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.legend(title='Subgroup')
plt.legend(bbox_to_anchor:=(1.05, 1.0), loc='upper left')
plt.grid(True)
plt.show()
#%%