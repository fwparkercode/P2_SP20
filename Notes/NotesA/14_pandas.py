# Pandas!

import random
import pandas as pd
pd.set_option('display.max_columns', None)
# lists > dicts > dataframes(series)

# Series are pandas arrays (1d arrays)
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(my_series)
print(type(my_series))  # pd.Series type
print(list(my_series))  # conversion to list is simple

# make a df (DataFrame) from a dictionary
d = {'col1': [1,2,3],
     'col2': [4,5,6]}
df = pd.DataFrame(data=d)
print(df)

# from an array/list
d2 = [[1,2,3],
      [4,5,6],
      [7,8,9]]  # each item is a row
cols = ["A", "B", "C"]
df2 = pd.DataFrame(data=d2, columns=cols)
print(df2)

# read from a csv (or other datafile)
df3 = pd.read_csv('World firearms murders and ownership - Sheet 1.tsv', sep='\t')
print(df3)

# useful methods
print(df3.head())  # first 5 rows/items
print(df3.tail())  # last 5
print(df3.info())  # datatypes (null values)
print(df3.describe())  # basic stats

# useful attributes
print(df3.index)  # index numbers
print(df3.columns)
print(df3.dtypes)
print(df3.shape)  # rows/indexes and columns

# simple column selection
rank_ownership = df3['Rank by rate of ownership']
print(type(rank_ownership))
print(rank_ownership)

# slicing dataframe using iloc[]   (index location)
print(df3.iloc[:5, 2])  # slice by row column
print(df3.iloc[:, [1, 6]])  # select by sending in a list of columns or rows

# slicing dataframe using loc[]
print(df3.loc[:, ['ISO code', 'Rank by rate of ownership']])
iso_and_rank = df3.loc[:, ['ISO code', 'Rank by rate of ownership']]
print(type(iso_and_rank))



# World cup matches


