# File:             P1_AverageSpeed.py
# Programmer:       Nolverto Urias Obeso
# Creation Date:    10/03/2022
# Description:      Calculate the average speed from a list of speed values

# Libraries
import numpy

# Speed Data in m/s
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculation of Average
averageSpeed = numpy.mean(speed)

# Printing of Results
print("Average Speed: " + str(averageSpeed) + "m/s")

