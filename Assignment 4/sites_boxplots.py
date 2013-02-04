#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Box plots of three water pollution collection sites
#####
# Import the libraries needed for plotting
import pylab as pl

# Data points for Sandusky
sandusky = [100, 700, 800, 600, 300, 200, 500, 600,
			1900, 1700, 200, 500, 100, 400, 100, 200]

# Data points for Farm Basket
farm_basket = [400, 100, 400, 200, 400, 400,
			   100, 300, 0, 100, 300, 300, 400, 400]

# Data points for Hollin's Mill
hollins_mill = [800, 200, 500, 200, 1600, 900, 6600, 5800,
				200, 200, 600, 500, 6100, 6400, 1800, 1200]

# Combine the data sets
data = [sandusky, farm_basket, hollins_mill]

# Plot to combined data sets. Use horizontal graphs
pl.boxplot(data, vert=False)

# Label the x-axis
pl.yticks([1, 2, 3], ["Sandusky", "Farm Basket", "Hollin's Mill"])
pl.show()