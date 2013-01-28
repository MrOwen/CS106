#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 2
# Calculate the volume and surface area of a sphere given the radius
#####
# Inport the Python math library
import math
# Read user input and put into the radius variable
radius = input("What is the radius of the sphere?: ")
# Calculate and store the value of volume
volume = (4*math.pi*(radius**3))/3.0  #force a floating point answer
sarea = 4*math.pi*(radius**2.0)  #force a flotaing point answer
# Print out the volume and surface area of the sphere
# Round the answers to two decimal places then format them to print out
# only two decimal places
print("Volume of sphere is: %.2f" % round(volume, 2))
print("Surface area of sphere is: %.2f" % round(sarea, 2))