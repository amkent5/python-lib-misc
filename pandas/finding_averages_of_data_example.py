import pandas as pd

# read file into pd
df = pd.read_csv('ai_data.csv', delimiter=',', names=['model', 'date', 'year', 'month', 'day', 'avg_day'])

# only want data from 05/12/2017 onwards
df = df[df.date > '2017-12-04' ]

# also exclude dates between 25/12/2017 - 01/01/2018 (inclusively)
l_exclude = ['2017-12-25',
        '2017-12-26',
        '2017-12-27',
        '2017-12-28',
        '2017-12-29',
        '2017-12-30',
        '2017-12-31',
        '2018-01-01']
df = df[ ~df.date.isin(l_exclude) ]

# calculate averages
misdiag_avg = df[ df.model == 'Misdiagnosis' ].avg_day.mean()
noaccess_avg = df[ df.model == 'No access' ].avg_day.mean()
parts_avg = df[ df.model == 'Parts' ].avg_day.mean()

print misdiag_avg
print noaccess_avg
print parts_avg
