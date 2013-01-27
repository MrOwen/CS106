#####
# Owen Kuemerle
# CS 106 - Introduction to Programming
# Programming assignment 1
# Calculate the distance to a lightning strike based on time
#####
# Read user input and put into the c_temp variable
c_temp = input("What is the temperature in celcius?: ")
# Convert celcius to fahrenheit according to the formula
f_temp = c_temp * (9/5.0) + 32.0# force a floating point result
# Print out the temp correctly rounded and formatted to 2 decimal places
print("The temperature in fahrenheit is: %.2f" % round(f_temp, 2))