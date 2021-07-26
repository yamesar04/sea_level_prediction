import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    X= df['Year']
    Y= df['CSIRO Adjusted Sea Level']
    plt.scatter( X , Y, c='b', s= 10, alpha= 0.5)

    # Create first line of best fit
    line1 = linregress(df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope, intercept, r_value, p_value, std_err = line1

    years_extended = df['Year'].append(pd.Series(range(2014, 2051)), ignore_index=True)

    plt.plot(years_extended, years_extended*slope + intercept, color="black")



    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    X= df_2000["Year"]
    Y= df_2000['CSIRO Adjusted Sea Level']
    model= linregress(X, Y)
    slope= model.slope
    intercept= model.intercept
    years_x= range(2000, 2051)
    plt.plot(years_x, slope * years_x + intercept, color= 'yellow'  )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()