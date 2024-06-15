import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv(url, parse_dates=['date'], index_col='date')
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) or (df['value'] <= upper_bound)]



def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

   
    plt.show()
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month_name()
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    
  fig, ax = plt.subplots(figsize=(10, 6))
  df_bar.plot(kind='bar', ax=ax)
  ax.set_title('Average Daily freeCodeCamp Forum Page Views\n(Yearly-Monthly)')
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  ax.legend(title='Months', loc='upper left')
  plt.show()
   # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

  
    
   

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    sns.boxplot(data=df_box, x='year', y='value', palette='Set3')
    plt.title('Distribution of freeCodeCamp Forum Page Views by Year')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.show()
    fig.savefig('box_plot.png')
    return fig
