# File:             P3_ModeSpeed.py
# Programmer:       Nolverto Urias Obeso
# Creation Date:    10/03/2022
# Description:      Calculate the standard deviation speed from a list of speed values

# Libraries
import statistics as st
import numpy as np

# Speed Data in m/s
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculation of Mode
modeSpeed = st.mode(np.array(speed))

# Printing of Results
print(modeSpeed)
