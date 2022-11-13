# File:             P2_MedianSpeed.py
# Programmer:       Nolverto Urias Obeso
# Creation Date:    10/03/2022
# Description:      Calculate the median speed from a list of speed values

# Libraries
import numpy

# Speed Data in m/s
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculation of Median
medianSpeed = numpy.median(speed)

# NOTE: If there are two numbers in the middle, divide the sum of those numbers by two.

# Printing of Results
print("Median Speed: " + str(medianSpeed) + "m/s")

