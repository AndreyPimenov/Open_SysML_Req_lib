#import math
#import itertools
#import numpy as np

# Productivity = 4 - 5 ton / 8 hours
# input = 4 -  5 ton / 8 hours
# output = how many flakes per second to estimate in case of 1D conveyor belt
# In case of width conveyour belt = it should be more than 10

# 1. Minimum produictivity of the recyaling line for achievemnt 4-5 t/day of the line [2] is 500 - 625 kg/ hour or 8-10 kg/min or 139-174g/ sec
#
# 1a) Estimation of flakes inside 1g and its number per second: 1 PET bottle 1.5L = 40 g and around 200 piecies. Therefore 1 piece of plastic flakes is 0.2g and 695 - 865 samples / sec
#
# 1b) Estimation of samples number in one
# 1m coneyour belt:
# Its area around 2cm^2 and size sqrt(2) = 1.4 cm
# 100cm / 1.4 cm = 71 samples let takes filling of the line around 80%, therefore: 57 samples simultenusoly in one line.
#
# 1d) Productivity for soritng system:
# analysis of 12 - 16 flakes per second
#
# 2. Working in real-time conditions
# ____
# [2] - Numbers from TZVP

# Scalability = 2 * Productivity

# Accuracy = 0.95

# Reliability + read this: https://habr.com/ru/post/122529/
MTBF = 1000000 # mean time between failures
AFR = 1 - math.exp(-8760 / MTBF) # annual failure rate

# Integrability
# Mechamical Integrability - metric system or
# Cyber Inegrability - TCP/IP and logging

#----------------------

print ("MTBF = ", MTBF)
print ("AFR = ", AFR)
