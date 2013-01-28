#lineplot.py
import numpy as np
import pylab as pl

#Make an array of x values
x = [1, 2, 3, 4, 5]

# Make an array of y values
y = [1, 4, 9, 16, 25]

# Use pylab to plot x and y points
pl.plot(x, y, 'ro')

# Set the labels and title for the graph
pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.title("An interesting graph")

# Set axis limits for the graph
pl.xlim(0, 10)
pl.ylim(0, 30)

# Show the plot on the screen
pl.show()