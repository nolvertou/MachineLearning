# File:             P5_Variance.py
# Programmer:       Nolverto Urias Obeso
# Creation Date:    10/03/2022
# Description:      Calculate the variance speed from a list of speed values
# Notes:            * Variance is another number that indicates how spread out the values are.
#                   * If you take the square root of the variance, you get the standard deviation!
#                   * The variance is the average number of these squared differences:

# Libraries
import numpy as np

# Speed Data in m/s
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculation of Mode
varianceSpeed = np.var(speed)

# Printing of Results
print(varianceSpeed)
