import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year',y='CSIRO Adjusted Sea Level',data=df)
  
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    x = df['Year']
    line_x1 = np.arange(x.min(), 2051)
    line_y1 = slope*line_x1 + intercept
    plt.plot(line_x1,line_y1,'g--')
  
    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(x=df2['Year'],y=df2['CSIRO Adjusted Sea Level'])
    x = df2['Year']
    line_x2 = np.arange(x.min(), 2051)
    line_y2 = slope*line_x2 + intercept
    plt.plot(line_x2,line_y2,'b--')
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
