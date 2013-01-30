#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 3
# Make a multi line graph from 2 equations
#####
# Import plotting libraries
import numpy as np
import pylab as pl

# Define x range from -5 to 5
x = np.arange(-5, 5, 0.01)
# Define y values as linear functions of x
y1 = 3*x - 4
y2 = (-1/2.0)*x + 3

# Define a [-5, 5] range on each axis
pl.ylim(-5, 5)
pl.xlim(-5, 5)

# Use pylab to plot x and both y points
pl.plot(x, y1, ':')
pl.plot(x, y2, 'r')

# Set the labels and title for the graph
pl.xlabel("Values from [-5, 5]")
pl.ylabel("Values from [-5, 5]")
pl.title("Graph of the equation y = 3x - 4 (blue) and y = (-1/2)x + 3 (red)")

# Show the plot on the screen
pl.show()