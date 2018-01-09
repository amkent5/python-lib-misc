# Matplotlib library
# https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')
plt.show()



# In MPL often the behind-the-scenes functions are hidden with convenient methods.
# For example, the following code:

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0.5, 4.5)
plt.show()

# Is actually executing (far better to be explicit like this):

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
plt.show()

# In all MPL charts you have a
"""
Figure 	- window that everything is drawn on
Axes	- added onto the figre. Axes contain functions plot() and scatter etc. 
		  axes have ticks labels etc. associated to them
"""

# pyplot - allows you to implicitly create charts without specifying explictly
#		   which API calls (i.e. in the first example)

# pylab	 - bulk imports both pyplot and numpy (recommend)



# so figure is the first step
# then add the axes:
import matplotlib.pyplot as plt
fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
ax = fig.add_subplot(111)
ax.plot([1,2,3,4], [1,5,2,7])
plt.show()

'''
ax = fig.add_axes()

add_axes(rect), where rect = [x0, y0, width, height]
used for explicity setting the coordinates of the axis
don't usually use this, instead use:

ax = fig.add_subplot()

add_subplot(111) - 1 row, 1 column and plot number 1
Subplot gives you tick marks for free.

'''


# a numpy example with everything we've learnt so far
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(np.random.rand(100,1), np.linspace(0, 10, 100))
plt.show()


# multiple axes example
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

l_cos = [ np.cos(i) for i in np.linspace(1,10,100) ]
l_sin = [ np.sin(i) for i in np.linspace(1,10,100) ]

ax1.plot(np.linspace(1,10,100), l_cos)
ax2.plot(np.linspace(1,10,100), l_sin)

ax1.set(title='cosine', xlabel='x', ylabel='y')
ax2.set(title='sine', xlabel='x', ylabel='y')

plt.show()


'''
We can access the type of plot through the ax.X class.
If you do ax.plot() it defaults to line.
But we can also do:

ax.scatter(x, y)
ax.bar()
ax.hist()
ax.boxplot()

and many more
'''

# eg:
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

x_range = np.linspace(1,10,100)
ax1.plot(x_range, l_sin)
ax2.bar(x_range, l_sin)
ax3.barh(x_range, l_sin)
ax4.boxplot(x_range, l_sin)

plt.show()
