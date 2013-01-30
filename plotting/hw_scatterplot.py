#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 3
# Make a scatter plot from highway sign visibility data
#####
# Import plotting libraries
import numpy as np
import pylab as pl

# Array of age values (x)
age = [18, 20, 22, 23, 23, 25, 27, 28, 29, 32,
	   37, 41, 46, 49, 53, 55, 63, 65, 66, 67,
	   68, 70, 71, 72, 73, 74, 75, 77, 79, 82]

# Array of distance values (y)
distance = [510, 590, 560, 510, 460, 490, 560, 510, 460, 410,
			420, 460, 450, 380, 460, 420, 350, 420, 300, 410,
			300, 290, 320, 370, 280, 420, 460, 360, 310, 360]

# Use pylab to plot x and y points
pl.plot(age, distance, 'ro')

# Set the labels and title for the graph
pl.xlabel("Age of driver (in years)")
pl.ylabel("Sign legibility distance (in feet)")
pl.title("Legibility and visibility of highway signs")

# Show the plot on the screen
pl.show()