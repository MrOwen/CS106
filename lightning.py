#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 1
# Calculate the distance to a lightning strike based on time
#####
# Read user input and put into the time variable
time = input("What was the time between the lightning flash and sound (in seconds)?: ")
distance = 1100 * time
# Convert the distance to miles (it is currently in feet)
distance_in_miles = distance/5280.0 # force a floating point answer
# Print out the distance correctly rounded and formatted to 2 decimal places
print("The distance to the lightning in miles is: %.2f" % round(distance_in_miles, 2))