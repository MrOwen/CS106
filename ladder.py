#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 1
# Calculate the required length of a ladder
#####
# The math library is required for this one
import math
# Read user input for house height and put into the house_height variable
house_height = input("What is the height of the house (in feet)?: ")
# Read user input for ladder angle and put into the ladder_angle variable
ladder_angle = input("What is the angle of the ladder?: ")
# Calculate the ladder length using tan = opp/hypot
# Math.tan take a radian arguement, so convert ladder_angle to radians
ladder_length = house_height * math.tan(math.radians(ladder_angle))
print("The length of the ladder is: %.2f" % round(ladder_length, 2))