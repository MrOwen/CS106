#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 4
# Box plots of three water pollution collection sites
# This compares wet and dry collection days
#####
# Import the libraries needed for plotting
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

# Combine the data sets
data = [sandusky_dry, sandusky_wet, farm_basket_dry,
        farm_basket_wet, hollins_mill_dry, hollins_mill_wet]

# Plot to combined data sets. Use horizontal graphs
pl.boxplot(data, vert=False)

# Label the x-axis
pl.yticks([1, 2, 3, 4, 5, 6], ["Sandusky Dry", "Sandusky Wet",
    "Farm Basket Dry", "Farm Basket Wet", "Hollin's Mill Dry",
    "Hollin's Mill Wet"])
pl.show()
