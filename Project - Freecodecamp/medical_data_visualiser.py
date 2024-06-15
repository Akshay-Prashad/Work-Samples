import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

df['bmi'] = df['weight'] / (df['height'] / 100) ** 2


df['overweight'] = (df['bmi'] > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)



# Draw Categorical Plot
def draw_cat_plot():
  columns = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight']
  df_selected = df[columns]

  df_cat = pd.melt(df_selected)
  df_cat=df_cat.groupby(['cardio', 'variable']).size().unstack()
  df_cat.columns = ['Cholesterol', 'Glucose', 'Alcohol', 'Active', 'Overweight', 'Smoking']
  df_cat= df_cat.reset_index()
  catplot = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count')
  fig = catplot.fig
  fig.savefig('catplot.png')
  return fig



def draw_heat_map():
  df_filtered = df[df['ap_lo'] <= df['ap_hi']]
  df_filtered=df[df['height'] >= df['height'].quantile(0.025)]
  df_filtered=df[df['height'] <= df['height'].quantile(0.95)]
  df_filtered=df[df['weight'] >= df['weight'].quantile(0.025)]
  df_filtered=df[df['weight'] <= df['weight'].quantile(0.95)]
  
  df_heat = df_filtered

  corr = df_heat.corr()

  mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
   



    
  fig, ax = plt.subplots(figsize=(10, 8))
  sns.heatmap(corr, annot=True, cmap='coolwarm', mask=mask, ax=ax)
  fig.savefig('heatmap.png')
  return fig
