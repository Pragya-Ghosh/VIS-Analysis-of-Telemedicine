# Analysis of the Impact of Telemedicine Programs on Mortality Rates

## Overview
This project analyzes the effectiveness of telemedicine programs in reducing mortality rates across different medical conditions. It compares mortality rates before and after the implementation of telemedicine interventions using São Paulo hospitals' data.

## Introduction
**Telemedicine** is the use of electronic information to communicate technologies to provide and support healthcare when distance separates the participants. Although initially considered *futuristic* and *experimental*, telemedicine became a necessary reality during the COVID-19 pandemic. Worldwide, people living in rural and remote areas struggle to access timely, good-quality specialty medical care. Residents of these areas often have substandard access to specialty healthcare, primarily because specialist physicians are more likely to be located in areas of concentrated urban population. Telemedicine has the potential to bridge this distance and facilitate healthcare in these remote areas.

Evaluating the impact of telemedicine is essential for determining its role in enhancing healthcare accessibility and patient care.

## Data Source
The dataset used in this project is titled **“Impact of Telemedicine in Hospital Culture and its Consequences on Quality of Care and Safety”**, obtained from 257 teleconsultations records over a 12-month period. The data is sourced from [SciELO Journals](https://scielo.figshare.com/articles/dataset/Impact_of_telemedicine_in_hospital_culture_and_its_consequences_on_quality_of_care_and_safety/20029458/1?file=35773332).

## Tools and Libraries
**Programming Language:** Python
- Pandas: Utilized for data manipulation and preparation.
- Matplotlib: Employed for creating the bar chart visualization.
- NumPy: Used for numerical computation.

## Program Code
The program was written in PyCharm. You can access the [Program](Program) file here on GitHub or run the code on Google Colab by clicking on the colab badge below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ngtyjvaxjVPGCdPp1-BmUKRg6b4Lrhzp)

## Program Output


## Methodology
A line plot is created to represent the weekly reported cases of Influenza Type A and Type B in the US from 2023 to 2024. This plot serves as the foundational visualization, allowing for the observation of both short-term variations and long-term trends.

Following the line plot, we apply rolling statistical techniques to further analyze the data. The rolling mean is computed to smooth out short-term fluctuations and to highlight underlying trends in the case counts. By using a rolling window, the mean provides a clearer view of the general trend in influenza cases over time.

The rolling standard deviation is calculated to measure the variability of the influenza case counts. This statistic helps to identify periods of increased fluctuation and potential outliers, providing insights into the stability of the case counts and the presence of significant deviations from the trend.

## Observation
For the purpose of this analysis, we will focus exclusively on Graph 2 to have a more detailed understanding of the trends and variability over time.

### Graph 2: Rolling Mean and Standard Deviation

- **Influenza Type A:**
  - The rolling mean and standard deviation indicate a clear peak around Week 50, with a higher level of variability around the peak.
  - Variability decreases significantly after the peak, indicating a more consistent decline.
  - Influenza Type A cases peak earlier (Week 50) and are more numerous compared to Type B.
    
- **Influenza Type B:**
  - The rolling mean shows a gradual increase until the peak around Week 4, with variability increasing towards the peak.
  - After the peak, the number of cases declines steadily, with less variability compared to the rising phase.
  - Influenza Type B cases peak later (Week 4) and have fewer cases overall.

## Inference
- Influenza Type A spreads more rapidly and affects more individuals compared to Type B, possibly due to differences in virulence or transmissibility.
- Influenza Type B, although less virulent, has a longer duration of spread.

## Conclusion
- The data suggests the need for early interventions for Type A to mitigate its rapid spread.
- For Type B, prolonged surveillance and continuous intervention may be necessary due to its extended spread period.

### Implications for Health Care Professionals
Health care professionals can use this data to predict and prepare for peak influenza seasons.

- **Intervention:**
  - Vaccination campaigns should start before Week 40 to ensure immunity before the peak periods.
  - Public health advisories should be issued earlier for Type A, considering its rapid rise.
    
- **Resource Allocation:**
  - Hospitals and clinics should prepare for higher patient volumes around Week 50 for Type A and Week 4 for Type B.
  - Stockpiling antivirals and other necessary medical supplies ahead of the peak periods can help manage the surge in cases.

## Author
Pragya Ghosh
