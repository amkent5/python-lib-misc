#import matplotlib.pyplot as plt

import matplotlib
matplotlib.use
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# we can style matplotlib using the inbuilt css
plt.style.use('bmh')
#plt.style.use('seaborn-white')
#plt.style.use('ggplot')

print plt.style.available

import pandas as pd

df = pd.read_csv('mycsv.csv')
df.columns = ['date', 'val']

# format date properly
df.date = pd.to_datetime(df['date'], format='%d/%m/%Y')

# reset index
df = df.set_index('date')

#df.plot()

# grab control in matplotlib
ax = df.plot(kind='line', style='--', marker='8')

ax.set_title('Misdiagnosis Prediction Volumes')
ax.xaxis.label.set_visible(False)
ax.set_ylabel('volume jobs gone through model')

# average all days
ax.axhline(y=147,xmin=0,xmax=3,c="red",linewidth=0.5,zorder=0, linestyle='dashdot')

# average excluding weekends
ax.axhline(y=200.9,xmin=0,xmax=3,c="green",linewidth=0.75,zorder=0, linestyle='dashdot')

plt.show()
