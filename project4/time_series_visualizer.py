import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.loc[(df['value'] < df['value'].quantile(0.975)) & (df['value'] > df['value'].quantile(0.025))]

def draw_line_plot():
    fig = plt.figure(figsize=[20,4])
    ax = fig.add_subplot(111)
    ax.plot(df['date'],df['value'])
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=None
    df2 = pd.DataFrame(columns=['year','month','day'])
    df2[['year','month','day']] = df['date'].str.split('-',expand=True) 
    df2['value'] = df['value']
    df_bar = pd.DataFrame( df2.groupby(['year','month'])['value'].agg(['count','mean'])).reset_index()
    df_bar['month'] = pd.to_datetime(df_bar['month'],format='%m').dt.month_name() 

    # Draw bar plot
    fig, ax = plt.subplots()
    ax = sns.barplot(data=df_bar,x='year',y='mean',hue='month',ci=None,palette='dark')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    # re ordering legend labels
    handles, labels = ax.get_legend_handles_labels()
    order = [8,9,10,11,0,1,2,3,4,5,6,7]
    plt.legend([handles[i] for i in order], [labels[i] for i in order],loc='upper left', title='Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots 
    df2 = pd.DataFrame(columns=['year','month','day'])
    df2[['year','month','day']] = df['date'].str.split('-',expand=True)
    df2['value'] = df['value']
    df_box = pd.DataFrame(df2.groupby(['year','month'])['value'].mean()).reset_index().sort_values(by=['year','month'])
    df_box['month'] = pd.to_datetime(df_box['month'],format='%m').dt.month_name().str[:3]
    
    # Draw box plots (using Seaborn)
    fig, (ax1,ax2)= plt.subplots(1,2,figsize=(12,5))
    sns.boxplot(x='year',y='value',data=df_box,orient='v',ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_yticks(np.arange(0,220000,20000))
    sns.boxplot(x='month',y='value',data=df_box,order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],orient='v',ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_yticks(np.arange(0,220000,20000))

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
