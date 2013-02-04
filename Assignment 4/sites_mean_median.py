#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Means and medians of the water pollution data points
#####
# Import the libraries needed for plotting
import numpy as np

# Data points for Sandusky
sandusky = [100, 700, 800, 600, 300, 200, 500, 600,
			1900, 1700, 200, 500, 100, 400, 100, 200]

# Data points for Farm Basket
farm_basket = [400, 100, 400, 200, 400, 400,
			   100, 300, 0, 100, 300, 300, 400, 400]

# Data points for Hollin's Mill
hollins_mill = [800, 200, 500, 200, 1600, 900, 6600, 5800,
				200, 200, 600, 500, 6100, 6400, 1800, 1200]

# Compute the statistics
sandusky_mean = np.mean(sandusky)
sandusky_median = np.median(sandusky)

farm_basket_mean = np.mean(farm_basket)
farm_basket_median = np.median(farm_basket)

hollins_mill_mean = np.mean(hollins_mill)
hollins_mill_median = np.median(hollins_mill)

print "Sandusky mean: %.2f" % round(sandusky_mean, 2)
print "Sandusky median: %.2f" % round(sandusky_median, 2)

print "Farm Basket mean: %.2f" % round(farm_basket_mean, 2)
print "Farm Basket median: %.2f" % round(farm_basket_median, 2)

print "Hollin's Mill mean: %.2f" % round(hollins_mill_mean, 2)
print "Hollin's Mill median: %.2f" % round(hollins_mill_median, 2)
