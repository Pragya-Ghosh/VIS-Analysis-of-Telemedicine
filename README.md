# Analysis of the Impact of Telemedicine Programs on Mortality Rates

## Overview
This project analyzes the effectiveness of telemedicine programs in reducing mortality rates across different medical conditions. It compares mortality rates before and after the implementation of telemedicine interventions using São Paulo hospitals' data.

## Introduction
**Telemedicine** is the use of electronic information to communicate technologies to provide and support healthcare when distance separates the participants. Although initially considered *futuristic* and *experimental*, telemedicine became a necessary reality during the COVID-19 pandemic. Worldwide, people living in rural and remote areas struggle to access timely, good-quality specialty medical care. Residents of these areas often have substandard access to specialty healthcare, primarily because specialist physicians are more likely to be located in areas of concentrated urban population. Telemedicine has the potential to bridge this distance and facilitate healthcare in these remote areas.

Evaluating the impact of telemedicine is essential for determining its role in enhancing healthcare accessibility and patient care.

## Data Source
The dataset used in this project is titled **“Impact of Telemedicine in Hospital Culture and its Consequences on Quality of Care and Safety”**, obtained from 257 teleconsultations records over a 12-month period. This is sourced from [SciELO Journals](https://scielo.figshare.com/articles/dataset/Impact_of_telemedicine_in_hospital_culture_and_its_consequences_on_quality_of_care_and_safety/20029458/1?file=35773332).

## Tools and Libraries
**Programming Language:** Python
- Pandas: Utilized for data manipulation and preparation.
- Matplotlib: Employed for creating the bar chart visualization.
- NumPy: Used for numerical computation.

## Program Code
The program was written in PyCharm. You can access the [Program](Program) file here on GitHub or run the code on Google Colab by clicking on the colab badge below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ggGqNibgKQZT--O2zrj_yqlpQfhImVpS)

## Program Output
![Bar Chart](https://github.com/user-attachments/assets/340d3af3-ae70-4da6-82df-36e68765195c)

## Methodology
A grouped bar chart is plotted to compare the "before" and "after" mortality rates for the telemedicine program for each diagnosis group-- namely [AMI (Acute Myocardial Infarction)](https://en.wikipedia.org/wiki/Myocardial_infarction), [Septic Shock](https://en.wikipedia.org/wiki/Septic_shock), [Ischemic Stroke](https://en.wikipedia.org/wiki/Stroke#Classification) and [Hemorrhagic Stroke](https://en.wikipedia.org/wiki/Stroke#Classification).

A legend is added to distinguish between the two sets of bars, and data labels are placed above each bar to display the exact mortality rates.

## Observation
There is a notable change in mortality rates across all diagnoses:
  - AMI: 47.2% reduction
  - Septic Shock: 43.0% reduction
  - Ischemic Stroke: 57.5% reduction
  - Hemorrhagic Stroke: 57.7% reduction

## Inference
- There is a significant reduction in mortality rates across all diagnoses when telemedicine is implemented.
- The most substantial reductions are observed in ischemic stroke and hemorrhagic stroke.

## Conclusion
The chart demonstrates the positive impact of telemedicine on reducing mortality rates for several critical diagnoses. This could be one small step for IT, but one giant leap for Healthcare.

### Implications for Health Care Professionals
Healthcare professionals should advocate for and integrate telemedicine services into routine care, especially for managing critical conditions.

- **Policy and Implementation:**
  Health policies should encourage the adoption of telemedicine services, particularly in areas where access to immediate medical care is limited.
    
- **Future Research:**
  Further studies could explore the specific factors within telemedicine that contribute to these improved outcomes, aiming to optimize telemedicine practices.

## Author
Pragya Ghosh
