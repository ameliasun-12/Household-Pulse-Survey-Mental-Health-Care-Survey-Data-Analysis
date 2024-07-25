# Intro to Python Project: Data Analysis of “Mental Health Care in the Last 4 Weeks” Data Set
By Amelia Sun

## Background
The data was taken from the Household Pulse Survey run by the U.S. Census Bureau in collaboration with five federal agencies in order to produce data on the social and economic impacts of Covid-19 on American households.
The data focuses on the questions:
1. At any time in the last 4 weeks, did you take prescription medication to help you with any emotions or with your concentration, behavior or mental health?
2. At any time in the last 4 weeks, did you receive counseling or therapy from a mental health professional such as a psychiatrist, psychologist, psychiatric nurse, or clinical social worker? Include counseling or therapy online or by phone.
3. At any time in the last 4 weeks, did you need counseling or therapy from a mental health professional, but did not get it for any reason?

- The time period that data was taken was from October 28th, 2020 to May 9th, 2022.
- More than 50,000 people were surveyed.
- The data values represent the percent of people who answered yes, in other words, people who needed mental healthcare.

[Link to the dataset](https://catalog.data.gov/dataset/mental-health-care-in-the-last-4-weeks) & [Link to the landing page](https://www.cdc.gov/nchs/covid19/pulse/mental-health-care.htm)

## Data Overview

The dataset "Mental_Health_Care_in_the_Last_4_Weeks.csv" contains information on mental health care statistics over various time periods. The key columns in the dataset are:

- Group: The demographic group the data pertains to (e.g., Age group, Gender, etc.)
- Subgroup: Specific subgroup within the main group (e.g., "18 - 29 years" within Age group)
- Indicator: The type of mental health care metric being measured (e.g., "Took Prescription Medication for Mental Health, Last 4 Weeks")
- Time Period: The time period over which the data was collected
- Value: The measured percentage who said yes for the given indicator within the subgroup.

Before analysis, the following cleaning steps were performed:

1. Converted columns to appropriate data types.
2. Standardized missing values to NaN.
3. Checked for duplicates and dropped any redundant rows.
4. Removed unnecessary whitespace from string columns.

```
missing_values = data.isnull().sum()
descriptive_stats = data.describe()

cleaned_data = data.dropna(subset=['Value'])
cleaned_descriptive_stats = cleaned_data.describe()
```
## Data Analysis

### All Indicators

#### Frequency of Mental Health Need
![](https://media.discordapp.net/attachments/805438507987632190/1266059082737913886/image.png?ex=66a3c4e7&is=66a27367&hm=5db7cd6849fb0cb42c461663cf8fb024b7e488cf5a452c515233a4ea5f54b9a0&=&format=webp&quality=lossless&width=1572&height=1012)

#### Average Mental Health Needs by Subgroup
![image](https://github.com/user-attachments/assets/c74ed7a8-ffd8-437b-ad9c-323e11cd605b)

