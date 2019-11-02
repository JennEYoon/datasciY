#-------------------------------------------------------------------------------
# Name:        RandomWalk.py
# Purpose:     Simple demo of Random Walk and pyplot.
#
# Author:      Jennifer Yoon
# Created:     07/13/2016
#
#-------------------------------------------------------------------------------
import random  # Python random.py module, NOT NumPy.
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 500
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
##    print "i:", i, "step:", step, "walk:", walk
plt.plot(walk)
plt.xlabel('steps')
plt.ylabel('position')
plt.show()

