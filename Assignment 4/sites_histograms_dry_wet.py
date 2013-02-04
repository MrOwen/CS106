#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Histogram plots of three water pollution collection sites
# This compares wet and dry collection days
#####
# Import the libraries needed for plotting
import numpy as np
import pylab as pl

# Data points for Sandusky
sandusky_dry = [100, 700, 800, 600, 300, 200, 500, 600]
sandusky_wet = [1900, 1700, 200, 500, 100, 400, 100, 200]

# Data points for Farm Basket
farm_basket_dry = [400, 100, 400, 200, 400, 400]
farm_basket_wet = [100, 300, 0, 100, 300, 300, 400, 400]

# Data points for Hollin's Mill
hollins_mill_dry = [800, 200, 500, 200, 1600, 900, 6600, 5800]
hollins_mill_wet = [200, 200, 600, 500, 6100, 6400, 1800, 1200]

pl.hist(sandusky_dry, bins=np.arange(0.0,900.0,100.0),
	normed=True, color='#990000', label="Sandusky Dry")
pl.hist(sandusky_wet, bins=np.arange(0.0,2000.0,100.0),
	normed=True, color='#FF0000', label="Sandusky Wet")
pl.hist(farm_basket_dry, bins=np.arange(0.0,500.0,50.0),
	normed=True, color='#006600', alpha=0.75, label="Farm Basket Dry")
pl.hist(farm_basket_wet, bins=np.arange(0.0,500.0,50.0),
	normed=True, color='#00FF00', alpha=0.75, label="Farm Basket Wet")
pl.hist(hollins_mill_dry, bins=np.arange(100.0,7000.0,500.0),
	normed=True, color='#0000FF', alpha=0.5, label="Hollin's Mill Dry")
pl.hist(hollins_mill_wet, bins=np.arange(100.0,7000.0,500.0),
	normed=True, color='#0066FF', alpha=0.5, label="Hollin's Mill Wet")
pl.title("Water Pollution Data Collection Histogram on Wet and Dry Days")
pl.legend()
pl.show()