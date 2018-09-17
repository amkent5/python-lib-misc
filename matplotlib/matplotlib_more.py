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