# Intro to Python Project: Data Analysis of “Mental Health Care in the Last 4 Weeks” Data Set
By Amelia Sun

## Conclusions

#### Prevalance
The most common percentage was 10% with another spike around the low 20%s. While not the majority, this showcases a significant amount of people who indicated that they needed assistance with their mental health. 

#### General Trends Across Indicators

1. **Prescription Medication Usage:**
   - A significant portion of the population reported taking prescription medication for mental health in the last 4 weeks. This indicator is critical as it shows the extent to which mental health issues are being managed through medication.

2. **Counseling and Therapy:**
   - The percentage of people receiving counseling or therapy was also substantial but varied more widely across different subgroups. This suggests variability in access to or acceptance of therapy across different demographics.

3. **Combined Treatment:**
   - Many individuals reported receiving both medication and therapy, indicating a holistic approach to mental health care that combines pharmacological and psychotherapeutic interventions.

4. **Unmet Needs:**
   - A notable portion of respondents indicated needing counseling or therapy but not receiving it. This is a significant gap in mental health care that needs addressing.

**Took Prescription Medication for Mental Health:**
- **Stable Increase:** This indicator showed a stable increase over time, reflecting broader acceptance and use of pharmacological interventions for mental health issues.

**Received Counseling or Therapy:**
- **Fluctuations:** There were fluctuations in this indicator, with some periods showing significant increases. This could be influenced by external campaigns promoting therapy or changes in healthcare policies.

**Combined Treatment:**
- **Holistic Approach:** A substantial number of respondents reported using both medication and therapy, indicating a trend towards holistic treatment approaches.

**Unmet Needs for Counseling or Therapy:**
- **Persistent Gap:** This indicator consistently showed a significant percentage of the population needing but not receiving therapy. This highlights ongoing issues in mental health service provision.

### Distribution of Mental Health Care Values

Using histograms, we observed:
- **Central Tendency:** The median value provided a sense of the typical level of mental health care usage.
- **Spread:** The range and interquartile range (IQR) indicated the variability in responses.
- **Skewness:** Some indicators showed skewness, suggesting that for some metrics, most values were clustered around lower or higher ends.

### Boxplot Analysis by Subgroup

The boxplot analysis revealed:
- **Variation Across Subgroups:** Different subgroups showed different levels of mental health care usage. For example, younger age groups (18-29 years) might have different utilization patterns compared to older age groups.
- **Outliers:** Presence of outliers in some subgroups pointed to atypical responses or potentially different experiences within these subgroups.

### Correlation Analysis

To understand relationships within the data, we conducted correlation analyses:

#### Correlation Matrix for Subgroups within Specific Indicators

For example, within the indicator "Took Prescription Medication for Mental Health, Last 4 Weeks":
- **Strong Correlations:** Some subgroups showed strong positive correlations, indicating similar patterns of medication usage.
- **Weak Correlations:** Other subgroups had weak or negative correlations, suggesting different or opposite trends in medication usage.

#### Correlation Matrix Based on Subgroups Over Time

This analysis highlighted:
- **Temporal Trends:** Subgroups that maintained consistent levels of mental health care usage over different time periods.
- **Variability:** Subgroups with high variability over time, possibly influenced by external factors (e.g., policy changes, societal events).

#### Correlation Matrix for "18-29 years" Subgroup Across Different Indicators

Focusing on the "18-29 years" subgroup:
- **Inter-Indicator Relationships:** Strong correlations between indicators like medication usage and therapy indicated that individuals receiving one form of care often received the other as well.
- **Unique Trends:** Some indicators, such as unmet needs for therapy, showed unique trends that did not correlate strongly with other indicators, highlighting specific areas of concern.

### Detailed Trends and Insights

#### Age Group Trends

**18-29 Years:**
- **High Engagement:** This age group showed high levels of engagement with mental health services, both in terms of medication and therapy.
- **Unmet Needs:** Despite high engagement, there was also a significant percentage reporting unmet needs for counseling and therapy, suggesting barriers to access or utilization.

**30-39 Years:**
- **Moderate Usage:** This group showed moderate levels of both medication and therapy usage. Trends indicated a stable but less intensive engagement compared to the younger group.

**40-49 Years and Older:**
- **Lower Usage:** Older age groups generally reported lower levels of engagement with mental health services. This could be due to a variety of factors including stigma, accessibility, or different coping mechanisms.

#### Gender Trends

**Females:**
- **Higher Reporting:** Females generally reported higher usage of both medication and therapy compared to males. This aligns with broader trends in healthcare utilization where women are more likely to seek medical help.
- **Unmet Needs:** Despite higher engagement, females also reported higher levels of unmet needs for therapy, suggesting a gap in service provision.

**Males:**
- **Lower Engagement:** Males reported lower engagement with mental health services. This might reflect societal norms around masculinity and mental health, which discourage help-seeking behavior.

#### Trends Over Time

**Increased Awareness and Usage:**
- **Rising Trends:** Over recent time periods, there has been a noticeable increase in the reporting of mental health care usage. This could be attributed to increased awareness, reduced stigma, and better availability of services.

**Impact of External Events:**
- **COVID-19 Pandemic:** Although not explicitly labeled in the dataset, external events like the COVID-19 pandemic likely influenced the trends. There was a spike in mental health care usage and unmet needs during the periods corresponding to the pandemic.

### Further Research

- **Longitudinal Studies:** Conduct longitudinal studies to track the long-term trends and impacts of mental health interventions.
- **Qualitative Insights:** Incorporate qualitative research to understand the barriers to accessing mental health care from the perspective of the affected populations.
- **External Factors:** Investigate the impact of external factors like the COVID-19 pandemic on mental health trends in more detail.

### Important
While this survey was done during the COVID-19 pandemic, it is important not to jump to conclusions and assume that certain subgroups of people have more mental health needs due to the pandemic. Many groups, such as the disabled and transgender (two groups with notably higher percentages seeking therapy and medication in the survey), are more predisposed to stress and mental health issues than others. However, while this dataset cannot be used to say that these levels were caused by the pandemic, it can be used to observe the mental health of people during it without assigning any sort of specific reason.  

## Issues with My Analysis

My graphs are very limited with what they expressed and are not the most clear. For example, the correlation matrix for each indicator was very hard to read and provides an unclear reading as to what the data says. While it is readable, it is very hard to parse through the visualization. The indicator graphs over time also do not provide a clear depcition of the dates. 

My unfamiliarity with python and coding in general has limited my analysis greatly, and I'd like to come back when I have a better understanding.

