import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


"""
Best plotting options for visualisation
"""

# create random dataframe of 10 sensors
df = pd.DataFrame(np.random.uniform(low=0, high=300, size=(100, 10)), columns=[ 'sensor_%i'% i for i in range(10) ])
print (df.head())
print (df.shape)

# plot with best looking plot options
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (15, 12)

plt.plot(df, linewidth=1);
#plt.axvline(500, ls='--', c='black')
plt.title('Local Behaviour')
plt.show()




"""
Using Gridspec for multiple subplots and huge control
"""
# assumes we have a dataframe called df_data and running
gs = gridspec.GridSpec(8, 8)
ax1 = plt.subplot(gs[:5, :])
ax2 = plt.subplot(gs[5, :])
ax3 = plt.subplot(gs[6, :])
ax4 = plt.subplot(gs[7, :])
df_data[tag_list]['2014-06-01':'2014-06-15'].plot(ax=ax1)
running[['50']]['2014-06-01':'2014-06-15'].plot(ax=ax2)
running[['51']]['2014-06-01':'2014-06-15'].plot(ax=ax3)
running[['52']]['2014-06-01':'2014-06-15'].plot(ax=ax4)
ax1.legend_.remove()


"""
Another Gridspec example
"""
import matplotlib.gridspec as gridspec

plt.rcParams['figure.figsize'] = (15, 12)

gs = gridspec.GridSpec(16, 1)
ax1 = plt.subplot( gs[:4, 0] )
ax2 = plt.subplot( gs[5:9, 0] )
ax3 = plt.subplot( gs[10:14, 0] )
ax4 = plt.subplot( gs[15:, 0] )

s='2016-09-20'
e='2016-10-02'

df_data[s:e][ df_data.columns[:-1] ].plot(ax=ax1, legend=False, ylim=[565, 625], title='Blade/Bearing Temperatures')
df_data[s:e][ df_data.columns[:-1] ].plot(ax=ax2, legend=False, ylim=[9, 125], title='Generator Vibrations')
df_data[s:e][ df_data.columns[:-1] ].plot(ax=ax3, legend=False, ylim=[0, 10], title='Generator Currents')
df_data[s:e][ df_data.columns[-1] ].plot(ax=ax4, legend=True, title='Running tag')


def remove_axis_label(axis):
    x_axis = axis.axes.get_xaxis()
    x_label = x_axis.get_label()
    x_label.set_visible(False)

remove_axis_label(ax1)
remove_axis_label(ax2)
remove_axis_label(ax3)
remove_axis_label(ax4)




