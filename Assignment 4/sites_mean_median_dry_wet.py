#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Box plots of three water pollution collection sites
# This compares wet and dry collection days
#####
# Import the libraries needed for plotting
import numpy as np

# Data points for Sandusky
sandusky_dry = [100, 700, 800, 600, 300, 200, 500, 600]
sandusky_wet = [1900, 1700, 200, 500, 100, 400, 100, 200]

# Data points for Farm Basket
farm_basket_dry = [400, 100, 400, 200, 400, 400]
farm_basket_wet = [100, 300, 0, 100, 300, 300, 400, 400]

# Data points for Hollin's Mill
hollins_mill_dry = [800, 200, 500, 200, 1600, 900, 6600, 5800]
hollins_mill_wet = [200, 200, 600, 500, 6100, 6400, 1800, 1200]

# Compute the statistics
sandusky_mean_dry = np.mean(sandusky_dry)
sandusky_mean_wet = np.mean(sandusky_wet)
sandusky_median_dry = np.median(sandusky_dry)
sandusky_median_wet = np.median(sandusky_wet)

farm_basket_mean_dry = np.mean(farm_basket_dry)
farm_basket_mean_wet = np.mean(farm_basket_wet)
farm_basket_median_dry = np.median(farm_basket_dry)
farm_basket_median_wet = np.median(farm_basket_wet)

hollins_mill_mean_dry = np.mean(hollins_mill_dry)
hollins_mill_mean_wet = np.mean(hollins_mill_wet)
hollins_mill_median_dry = np.median(hollins_mill_dry)
hollins_mill_median_wet = np.median(hollins_mill_wet)

print "Sandusky mean (dry): %.2f" % round(sandusky_mean_dry, 2)
print "Sandusky mean (wet): %.2f" % round(sandusky_mean_wet, 2)
print "Sandusky median (dry): %.2f" % round(sandusky_median_dry, 2)
print "Sandusky median (wet): %.2f" % round(sandusky_median_wet, 2)

print "Farm Basket mean (dry): %.2f" % round(farm_basket_mean_dry, 2)
print "Farm Basket mean (wet): %.2f" % round(farm_basket_mean_wet, 2)
print "Farm Basket median (dry): %.2f" % round(farm_basket_median_dry, 2)
print "Farm Basket median (wet): %.2f" % round(farm_basket_median_wet, 2)

print "Hollin's Mill mean (dry): %.2f" % round(hollins_mill_mean_dry, 2)
print "Hollin's Mill mean (wet): %.2f" % round(hollins_mill_mean_wet, 2)
print "Hollin's Mill median (dry): %.2f" % round(hollins_mill_median_dry, 2)
print "Hollin's Mill median (wet): %.2f" % round(hollins_mill_median_wet, 2)
