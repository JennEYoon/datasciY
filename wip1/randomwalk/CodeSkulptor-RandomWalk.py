# Author:      Jennifer Yoon
# Created:     07/13/2016
# Purpose:     Ramdon Walk simple demo in Python 2.7.
#              The pyplot library was subed by simpleplot to run on CodeSkulptor.
#-------------------------------------------------------------------------------
import random  # Uses built-in Python's random.py module, NOT NumPy's. #
#import matplotlib.pyplot as plt
import simpleplot

### Test code for random walk, steps=30. CodeSkulptor print max, steps=500.###
print "Test of random walk function."
position = 0
walk = [position]
steps = 30
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
    print "i:", i, ", step:",  step, ",  walk:", walk

### Main random walk function. Steps = 1000, omits print.###
#position = 0
#walk = [position]
#steps = 1000
#for i in xrange(steps):
#    step = 1 if random.randint(0, 1) else -1
#    position += step
#    walk.append(position)

## The simpleplot library replace pyplot to run on CodeSkulptor. ##

### Simpleplot test code. ###
#simpleplot.plot_lines(framename, width, height, xlabel, ylabel, datasets, points, legends)
dataset1 = {3: 5, 8: 2, 1: 3}
dataset2 = [(1, 2), (4, 7), (2, 5), (7, 6)]
simpleplot.plot_lines('Sample', 400, 300, 'x', 'y', [dataset1, dataset2], True, ['dataset1', 'dataset2'])

### original pyplot test code. ###
#import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

### original pyplot code. ###
#plt.plot(walk)
#plt.xlabel('steps, first 1000')
#plt.ylabel('position')
#plt.show()