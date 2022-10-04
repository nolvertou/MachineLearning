# File:             P4_Standard_DeviationSpeed.py
# Programmer:       Nolverto Urias Obeso
# Creation Date:    10/03/2022
# Description:      Calculate the standard deviation speed from a list of speed values
# Notes:            * Standard deviation is a number that describes how spread out the values are.
#                   * A low standard deviation means that most of the numbers are close to the mean (average) value.
#                   * A high standard deviation means that the values are spread out over a wider range.
#

# Libraries
import numpy as np

# Speed Data in m/s
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculation of Mode
stdDeviationSpeed = np.std(speed)

# Printing of Results
print(stdDeviationSpeed)
