# load the legos dataset into df and try these out one at a time
df.plot()  # plot your dataframe, plots key vs all values
df.columns # what are my columns?
df.plot(y='list_price', x='piece_count')  # okay, but a line
df.plot(y='list_price', x='piece_count', kind='scatter')  # cool, scatterplot
pd.plotting.scatter_matrix(df)  # great for exploring dataset!!
df.plot.scatter(x='piece_count', y='list_price', c='star_rating')  # add a 3rd dimension using color
df['list_price'].plot.hist()  # create a histogram
df['list_price'].plot.hist(bins=40)  # specify the number of bins
df['list_price'].plot.kde()  # kernel density plot
ax = df['list_price'].plot.kde()
ax.set_title("KDE Plot")
ax.set(ylabel='frequency', xlabel='list_price')
ax.set(ylabel='frequency', xlabel='list_price', title='KDE')