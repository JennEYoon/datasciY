# Quick matplotlib test  
# 3/8/2022  to run, understand plt and ax method really well.  
# all runs.  Produce many graphs in windows.  
# Test on VS Code, with # %% magic command.  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import matplotlib as mpl

# sine wave data
X = np.linspace(0, 6.283, 30)
Y = np.sin(X)
print("X: ", X, "\nY: ", Y)

X1 = np.zeros([1, 30])
np.around(X, decimals=3, out=X1)  
# 'a'round for full array.  Slightly inaccurate but fast. 
#  output to new array, so original significant digits are kept.  
print(X1)
print(X)  # unchanged digits? Yes.  

# For single number, np.format_float_positional(x, precision=n).
# np.round(array)  same as np.around(array) 
X2 = np.zeros([1, 30])
np.round(X, decimals=3, out=X2)
print(X2, X)

# Pandas quick plot
s1 = pd.Series(data=Y)  
# Don't need X index.  auto-index X axis.  
s1.plot()
plt.show()  # worked.  
plt.close()

# matplotlib without setup
plt.plot(X, Y, 'ro')
plt.show()
plt.close()

# matplotlib with fig, ax setup
fig = plt.figure(2)
ax = plt.axes()
ax.set_title("Axis title, blue dash plot")
plt.plot(X, Y, 'b--')
plt.show()
plt.close()

# subplots method.  
fig, ax = plt.subplots()
ax.plot(X, Y, 'go')
ax.set_title('fig, ax defined, suplots method')
plt.show()
plt.close()

# fig, ax method, multiple plots.    
fig = plt.figure(3)
ax = plt.axes()
ax.plot(X, Y, 'ko-')
ax.plot(X, np.cos(X), 'r--')
ax.plot(X, -1.25*Y, 'go')
ax.set_title('add plots to 1 axis method')
plt.show()
plt.close()

# add_axes method  
# Creating two axes
# add_axes([xmin,ymin,dx,dy])
fig = plt.figure(5)
ax=fig.add_axes([0, .5,1, .4]) # left%, bottom%, width%, height% 
plt.plot(X, Y, 'ko--')
ax1=fig.add_axes([0, 0, 1, .4])
plt.plot(X, np.cos(X), 'r--')
ax.set_title('ax0')
ax1.set_title('ax1')
fig.suptitle('add_axes method, to single figure')
plt.show() # Yeah! Works!  
plt.close()



"""  
### Simple Plot, 
# https://matplotlib.org/3.5.1/gallery/lines_bars_and_markers/simple_plot.html  

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
"""   
