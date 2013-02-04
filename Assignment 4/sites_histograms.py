#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Histogram plots of three water pollution collection sites
#####
# Import the libraries needed for plotting
import numpy as np
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

pl.hist(sandusky, bins=np.arange(0.0,2000.0,100.0),
	normed=True, color='b', label="Sandusky")
pl.hist(farm_basket, bins=np.arange(0.0,500.0,50.0),
	normed=True, color='g', alpha=0.75, label="Farm Basket")
pl.hist(hollins_mill, bins=np.arange(100.0,7000.0,500.0),
	normed=True, color='r', alpha=0.5, label="Hollin's Mill")
pl.title("Water Pollution Data Collection Histogram")
pl.legend()
pl.show()