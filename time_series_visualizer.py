import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

print(df)

def draw_line_plot():
    # Draw line plot
    df.plot()
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    #plt.show()

    #get current figure
    fig = plt.gcf()



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby([df.index.year.rename('year'), df.index.month.rename('month')])['value'].mean().reset_index(name='averages')

    # Draw bar plot
    plot = sns.catplot(x="year", y="averages", data=df_bar, kind="bar", hue="month")
    legend = plot._legend
    legend.set_title("Months")
    plot.set_axis_labels("Years", "Average Page Views")
    
    #trying to get figure
    fig = plot.figure




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2)

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    plot1 = sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    plot2 = sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    #trying to get figure
    #fig = plot.figure


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
