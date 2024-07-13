import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Extract the data from the CSV file
data = pd.read_csv("telemedicine_data.csv")

diagnoses = data['Diagnosis']
without_program = data['Without telemedicine program (%)']
with_program = data['With telemedicine program (%)']

x = np.arange(len(diagnoses))  # the label locations
width = 0.35  # the width of the bars

# Set up the bar chart
fig, ax = plt.subplots()
bars1 = ax.bar(x - width / 2, without_program, width, color="#FF5F00", label='Without Telemedicine')
bars2 = ax.bar(x + width / 2, with_program, width, color="#002379", label='With Telemedicine')

ax.set_xlabel('Diagnoses')
ax.set_ylabel('Mortality Rate (%)')
ax.set_title('Mortality Rates With and Without Telemedicine Program')
ax.set_xticks(x)  # configure the x-tick positions
ax.set_xticklabels(diagnoses)
ax.legend()


# Add text labels above the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'{height:.1f}%',  # Format the label to one decimal place
                ha='center', va='bottom',  # Center the text and align it to the top of the bar
                fontsize=10, color='black')


# Apply the add_labels function to both sets of bars
add_labels(bars1)
add_labels(bars2)

# Automated Layout Adjustment
fig.tight_layout()

plt.show()
