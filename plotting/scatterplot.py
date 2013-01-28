#scatterplot.py
import numpy as np
import pylab as pl

#Make an array of x values
x = [1, 2, 3, 4, 5]

# Make an array of y values
y = [1, 4, 9, 16, 25]

# Use pylab to plot x and y
pl.plot(x, y, 'ro')

# Show the plot on the screen
pl.show()