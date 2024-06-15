import pandas as pd


def calculate_demographic_data(print_data=True):
  df = pd.read_csv("adult.data.csv")
  columns=["age " ,"workclass" ,  "fnlwgt", "education"   ,"education-num"," marital-status" ,"occupation" ," relationship "  ,"race","sex","capital-gain"  , "capital-loss " ,"hours-per-week" , "native-country"   , "salary"] 
  
  df.columns=columns
  
  race_count = df['race'].value_counts()
 
  df_1=df[df["sex"]=="Male"]
  
  average_age_men = df_1["age"].mean()
  
  total_people = df.shape[0]
  
  bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
  
  percentage_bachelors = (bachelors_count / total_people) * 100
  
  advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  
  total_advanced_education = advanced_education.shape[0]
 
  above_50k_count = advanced_education[advanced_education['income'] == '>50K'].shape[0]
  
  percentage_above50k = (above_50k_count / total_advanced_education) * 100
  
  higher_education = percentage_above50k
  
  non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  
  total_non_advanced_education = non_advanced_education.shape[0]
  
  above_50k_count = non_advanced_education[non_advanced_education['income'] == '>50K'].shape[0]
  
  percentage_above_50k = (above_50k_count / total_non_advanced_education) * 100
  
  lower_education = percentage_above_50k


  higher_education_rich = percentage_above50k
  lower_education_rich =  percentage_above_50k
 
  min_work_hours =  df['hours_per_week'].min()
  min_hours_workers = df[df['hours_per_week'] == min_hours_per_week]
  total_fewest_hours_workers = fewest_hours_workers.shape[0]
  rich_count = fewest_hours_workers[fewest_hours_workers['income'] == 
  '>50K'].shape[0]
  percentage_rich = (rich_count / total_fewest_hours_workers) * 100







  rich_percentage = percentage_rich
  rich_by_country = df[df['income'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
  highest_percentage_country = rich_by_country.idxmax()
  percentage_highest_country = rich_by_country.max()

  highest_earning_country = highest_percentage_country
  highest_earning_country_percentage = percentage_highest_country
  india_data = df[df['native-country'] == 'India']


  occupation_counts = india_data['occupation'].value_counts()

  top_IN_occupation = occupation_counts.head(5)



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
