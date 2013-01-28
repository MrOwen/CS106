#multilineplot.py
import numpy as np
import pylab as pl

#Make an array of x values
x = [1, 2, 3, 4, 5]
#Define another set of x values
x2 = [1, 2, 4, 6, 8]

# Make an array of y values
y = [1, 4, 9, 16, 25]
#Define another set of x values
y2 = [2, 4, 8, 12, 16]

# Use pylab to plot x and y points
p1 = pl.plot(x, y, 'ro')
# Secondary plot
p2 = pl.plot(x2, y2, '*')

# Add a plot legend
plots = (p1, p2)
# Lables for legend
labels = ('Results of y=x^2', 'Results of y=2x')
pl.legend(plots, labels, 'best', numpoints=1)

# Set the labels and title for the graph
pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.title("An interesting graph")

# Set axis limits for the graph
pl.xlim(0, 9)
pl.ylim(0, 30)

# Show the plot on the screen
pl.show()