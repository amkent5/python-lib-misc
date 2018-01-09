# Pandas Library
# https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question5
# http://nbviewer.jupyter.org/gist/manujeevanprakash/996d18985be612072ee0

import pandas as pd


### Series
"""
A little bit like a dict (has an index and a value)
A 1-dimensional array like object containing an array of data and an index
"""


# Form Series from array
s = pd.Series( [1,2,3,4,5] )
print s 					# print index and values
print s.index				# print index (auto increments from 0 by default)
print s.values				# print values
print s[0]					# print value associated to index
print '\n'


# Form Series from array and specify the index
s = pd.Series( [1,2,3,4,5], index=['a','b','c','d','e'] )
print s
print s['c']				# print value assocaited to 'c' index
print s[['a','c','e']]		# print group of values
print s[s>2]				# print subset of series where values >2
print s *2					# multiply all values by 2
print '\n'


# Apply numpy operations to pandas Series
import numpy as np
print np.mean(s)
print '\n'

# Form Series from dict
d = {'ash': 0, 'emma': 50, 'anakin': 100, 'dicky': None}
s = pd.Series(d)
print s
'''
anakin    100.0
ash         0.0
dicky       NaN
emma       50.0
dtype: float64	'''
print pd.isnull(s)			# check whether values are null (dicky is)

# name our series and our index
s.name = 'The Family'
s.index.name = 'Names'
print s
'''
Names
anakin    100.0
ash         0.0
dicky       NaN
emma       50.0
Name: The Family, dtype: float64	'''

# you can change the index
s.index = ['emma', 'emma2', 'emma3', 'emma4']
print s
'''
emma     100.0
emma2      0.0
emma3      NaN
emma4     50.0
Name: The Family, dtype: float64	'''


# ------------------------------------------------------------------------

### DataFrames
"""
A spread sheet like structure, containing ordered collection of columns.
Each column can have different value type. A Dataframe has both a row index
*and* a column index.
"""

# form from multi-dimensional array
arr = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(arr)
print df
'''
    0   1   2   3   4   5   6   7   8
0   0   1   2   3   4   5   6   7   8
1   9  10  11  12  13  14  15  16  17
2  18  19  20  21  22  23  24  25  26
3  27  28  29  30  31  32  33  34  35
4  36  37  38  39  40  41  42  43  44
5  45  46  47  48  49  50  51  52  53
6  54  55  56  57  58  59  60  61  62
7  63  64  65  66  67  68  69  70  71
8  72  73  74  75  76  77  78  79  80	'''

# form from numpy array
narr = np.arange(30).reshape(10,3)
df = pd.DataFrame(data=narr, columns=['X', 'Y', 'Z'])
print df
'''
    X   Y   Z
0   0   1   2
1   3   4   5
2   6   7   8
3   9  10  11
4  12  13  14
5  15  16  17
6  18  19  20
7  21  22  23
8  24  25  26
9  27  28  29	'''

# form from csv
#df = pd.read_csv('some_filename')

# form from dict
d = {
	'name': ['ash', 'emma', 'anakin'],
	'wealth': [100, 200, 500],
	'location': ['cranbrook', 'mars', 'pluto']
}

df = pd.DataFrame(d)
print df 							# by default the columns are in alph order
'''
    location    name  wealth
0  cranbrook     ash     100
1       mars    emma     200
2      pluto  anakin     500	'''

# change the column order
df = pd.DataFrame(df, columns=['name', 'wealth', 'location'])
print df
'''
     name  wealth   location
0     ash     100  cranbrook
1    emma     200       mars
2  anakin     500      pluto	'''

# Add column and rename it
# columns are just series
new_col = pd.Series( ['EX5', 'MARS1', ''], index=df.index )
print new_col
'''
0      EX5
1    MARS1
2
'''

"""
Before you can get to the solution, it's first a good idea to grasp the concept of loc and how it differs
from other indexing attributes such as .iloc and .ix:

- 	loc works on labels of your index. This means that if you give in loc[2], you look for the values of your
	DataFrame that have an index labeled 2.
- 	iloc works on the positions in your index. This means that if you give in iloc[2], you look for the values
	of your DataFrame that are at index '2'.
- 	ix is a more complex case: when the index is integer-based, you pass a label to ix. ix[2] then means that 
	you're looking in your DataFrame for values that have an index labeled 2. This is just like loc! However, 
	if your index is not solely integer-based, ix will work with positions, just like iloc.
"""

# remember DataFrames have a horizontal and vertical index
# so we can access a new vertical index by doing loc[:, new_verical_ix]
df.loc[:, 4] = new_col
print df
'''
     name  wealth   location      4
0     ash     100  cranbrook    EX5
1    emma     200       mars  MARS1
2  anakin     500      pluto
'''

df.rename(columns={4: 'Postcode'}, inplace=True)		# {old_col_name: new_col_name}
print df
'''
     name  wealth   location Postcode
0     ash     100  cranbrook      EX5
1    emma     200       mars    MARS1
2  anakin     500      pluto
'''


# note as loc accesses the labels of the index I could have sped up this process
# and passed in a new label as the index! i.e.:
new_col2 = pd.Series( [9.7, 9.8, 9.9], index=df.index )
df.loc[:, 'Looks'] = new_col2
print df
'''
     name  wealth   location Postcode  Looks
0     ash     100  cranbrook      EX5    9.7
1    emma     200       mars    MARS1    9.8
2  anakin     500      pluto             9.9
'''

# let's add a few more rows to our dataframe
df.loc[3, :] = ['Bowler', -60, 'Exeter', 'EX2', 10]
df.loc[4, :] = ['Bowler123', 60, 'Sweden', 'EX2', 2.5]
print df

# we use loc (or iloc) to access rows, columns, elements of our dataframe
# access a column
print df.loc[:, 'location']

# access a row
print df.loc[2, :]

# access a cell
print df.loc[1, 'Postcode']




# Set the index on a dataframe as something else, but then swap it back out
print df
'''
       A     B     C  new_col
0    0.0   1.0   2.0      9.0
1    3.0   4.0   5.0      8.0
2    6.0   7.0   8.0      7.0
3    9.0  10.0  11.0      6.0
4   12.0  13.0  14.0      5.0
5   15.0  16.0  17.0      4.0
6   18.0  19.0  20.0      3.0
7   21.0  22.0  23.0      2.0
8   24.0  25.0  26.0      1.0
9   27.0  28.0  29.0      0.0
10   1.0   1.0   1.0      1.0
e    1.0   1.0   1.0      1.0
'''

df = df.set_index('C')
print df
'''
         A     B  new_col
C
2.0    0.0   1.0      9.0
5.0    3.0   4.0      8.0
8.0    6.0   7.0      7.0
11.0   9.0  10.0      6.0
14.0  12.0  13.0      5.0
17.0  15.0  16.0      4.0
20.0  18.0  19.0      3.0
23.0  21.0  22.0      2.0
26.0  24.0  25.0      1.0
29.0  27.0  28.0      0.0
1.0    1.0   1.0      1.0
1.0    1.0   1.0      1.0
'''

print df.index
'''
Float64Index([2.0, 5.0, 8.0, 11.0, 14.0, 17.0, 20.0, 23.0, 26.0, 29.0, 1.0,
              1.0],
             dtype='float64', name=u'C')
'''

# now put the index back in
# let's re-create it
my_series = pd.Series( [i for i in range(len(df))] )

# put the 'C' column back in the dataframe
df.loc[:, 'C'] = df.index

# then set the index based on my series
df.set_index(my_series)
print df
'''
       A     B  new_col     C
0    0.0   1.0      9.0   2.0
1    3.0   4.0      8.0   5.0
2    6.0   7.0      7.0   8.0
3    9.0  10.0      6.0  11.0
4   12.0  13.0      5.0  14.0
5   15.0  16.0      4.0  17.0
6   18.0  19.0      3.0  20.0
7   21.0  22.0      2.0  23.0
8   24.0  25.0      1.0  26.0
9   27.0  28.0      0.0  29.0
10   1.0   1.0      1.0   1.0
11   1.0   1.0      1.0   1.0
'''




# Remove rows, and remove cols, and set cells as None
# remove rows
print df
'''
       A     B     C  new_col
0    0.0   1.0   2.0      9.0
1    3.0   4.0   5.0      8.0
2    6.0   7.0   8.0      7.0
3    9.0   NaN  11.0      6.0
4   12.0  13.0  14.0      5.0
5   15.0  16.0  17.0      4.0
6   18.0  19.0  20.0      3.0
7   21.0  22.0  23.0      2.0
8   24.0  25.0  26.0      1.0
9   27.0  28.0  29.0      0.0
10   1.0   1.0   1.0      1.0
e    1.0   1.0   1.0      1.0
'''
df = df.drop(5, axis=0)		# axis 0 is the horizontal axis, axis 1 is the vertical
print df
'''
       A     B     C  new_col
0    0.0   1.0   2.0      9.0
1    3.0   4.0   5.0      8.0
2    6.0   7.0   8.0      7.0
3    9.0   NaN  11.0      6.0
4   12.0  13.0  14.0      5.0
6   18.0  19.0  20.0      3.0
7   21.0  22.0  23.0      2.0
8   24.0  25.0  26.0      1.0
9   27.0  28.0  29.0      0.0
10   1.0   1.0   1.0      1.0
e    1.0   1.0   1.0      1.0
'''

# remove column
df = df.drop('C', axis=1)
print df
'''
       A     B  new_col
0    0.0   1.0      9.0
1    3.0   4.0      8.0
2    6.0   7.0      7.0
3    9.0   NaN      6.0
4   12.0  13.0      5.0
6   18.0  19.0      3.0
7   21.0  22.0      2.0
8   24.0  25.0      1.0
9   27.0  28.0      0.0
10   1.0   1.0      1.0
e    1.0   1.0      1.0
'''

# set a value to None
df.loc[2, 'A'] = None
print df
'''
       A     B  new_col
0    0.0   1.0      9.0
1    3.0   4.0      8.0
2    NaN   7.0      7.0
3    9.0   NaN      6.0
4   12.0  13.0      5.0
6   18.0  19.0      3.0
7   21.0  22.0      2.0
8   24.0  25.0      1.0
9   27.0  28.0      0.0
10   1.0   1.0      1.0
e    1.0   1.0      1.0
'''
