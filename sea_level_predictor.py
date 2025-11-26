import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,10))
    plt.scatter(df['Year'],
                df['CSIRO Adjusted Sea Level'],
                color='aqua',
                label='Actual Sea Level Measurements')


    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    lineXVals = pd.Series(range(1880, 2051))
    lineYVals = line.slope * lineXVals + line.intercept

    plt.plot(lineXVals,
             lineYVals,
             color='black',
             linestyle='dashed',
             label='Predicted CSIRO Adjusted Sea Level (from 1880)')

    # Create second line of best fit
    df_recent = df.copy()
    df_recent = df_recent[df_recent['Year'] >= 2000]

    secondLine = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    secondLineXVals = pd.Series(range(2000, 2051))
    secondLineYVals = secondLine.slope * secondLineXVals + secondLine.intercept

    plt.plot(secondLineXVals,
             secondLineYVals,
             color='red',
             linestyle='dotted',
             label='Predicted CSIRO Adjusted Sea Level (from 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# REMOVE BEFORE TESTING WITH MAIN.PY
# draw_plot()