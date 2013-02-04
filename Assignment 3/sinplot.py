#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 3
# Make a graph from the equation y = sin(1/x)
#####
# Import plotting libraries
import numpy as np
import pylab as pl

# Define x range from -3 to 3
x = np.arange(-3, 3, 0.01)
# Define y values as a sin function based on the x values
y = np.sin(1/x)

# Add some padding to the graph on the y-axis
pl.ylim(-1.25, 1.25)

# Use pylab to plot x and y points
pl.plot(x, y)

# Set the labels and title for the graph
pl.xlabel("Values from [-3, 3]")
pl.ylabel("Values of y = sin(1/x)")
pl.title("Graph of the equation y = sin(1/x)")

# Show the plot on the screen
pl.show()