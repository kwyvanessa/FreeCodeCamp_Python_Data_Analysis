import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = None
df = pd.read_csv('medical_examination.csv')
# Add 'overweight' column
df['overweight'] = None
#BMI: weight (kg) / square of height (m**2)
BMI = df.weight / ((df.height/100)**2)
df['overweight'] = BMI
df.loc[df['overweight'] > 25, 'overweight'] = 1
df.loc[df['overweight'] <= 25, 'overweight'] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    df2 = pd.melt(df, id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight']).reset_index(drop=True)
    df_cat = pd.DataFrame({'count':df2.groupby(['cardio','value','variable'],)['value'].count()}).reset_index()
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat,x='variable',y='count',hue='value',col='cardio',kind='bar',legend=True,ci=None)
    fig.set(xlabel ='variable', ylabel ='total')
    plt.show()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = None
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = None
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(7,5))
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,vmin=-0.15,vmax=0.3,center=0.08,mask=mask, square = True,annot=True,fmt=".1f",annot_kws={"size": 5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
