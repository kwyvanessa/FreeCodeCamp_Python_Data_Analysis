import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None
    df = pd.read_csv('adult.data.csv')
    # Get column names
    list(df.columns)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None
    race_count = df.race.value_counts()
    # What is the average age of men?
    average_age_men = None
    average_age_men = df.age.loc[df['sex']=='Male'].mean().round(decimals=1)
  
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None
    percentage_bachelors = df.education.loc[df['education']=='Bachelors'].count()/df.education.count()*100
    percentage_bachelors = percentage_bachelors.round(decimals=1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    high_education=df.education.loc[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    higher_education = len(df.education.loc[df['education'].isin(['Bachelors','Masters','Doctorate'])])
    lower_education = None
    low_education=df.education.loc[~df['education'].isin(high_education)]
    lower_education = len(df.education.loc[~df['education'].isin(high_education)])
    # percentage with salary >50K
    higher_education_rich = df.salary.loc[(df['salary']=='>50K') & (df['education'].isin(high_education))].count()/higher_education*100
    higher_education_rich = higher_education_rich.round(decimals=1)

    lower_education_rich = df.salary.loc[(df['salary']=='>50K') & (df['education'].isin(low_education))].count()/lower_education*100
    lower_education_rich = lower_education_rich.round(decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None
    num_min_workers = len(df[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')])
    rich_percentage = None
    rich_percentage = num_min_workers/len(df[df['hours-per-week']==min_work_hours])*100
   
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    country_salary=pd.DataFrame()
    country_salary[['country','salary']]=df[['native-country','salary']]
    high_salary=len(country_salary[country_salary['salary']=='>50K'])

    all_salary=country_salary[country_salary['salary']!='>50K'].groupby(country_salary['country']).size()

    salary_percent = country_salary[country_salary['salary']=='>50K'].groupby(country_salary['country']).size()/df.groupby('native-country').size()*100
    salary_percent=salary_percent.sort_values(ascending=False).round(decimals=1)

    highest_num_salary=salary_percent[0]
    highest_earning_country=salary_percent.idxmax()

    highest_earning_country_percentage = None
    highest_earning_country_percentage = highest_num_salary

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    top_IN_occupation = df.loc[(df['salary']=='>50K') & (df['native-country']=='India')].groupby(['occupation']).size().idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
