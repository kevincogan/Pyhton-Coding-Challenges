# In this exercise, you have to analyze records of temperature to find the closest to zero.
#
#
# Sample temperatures
# Here, -1 is the closest to 0.
#  	Rules
# Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
#  	Game Input
# Your program must read the data from the standard input and write the result on the standard output.
# Input
# Line 1: N, the number of temperatures to analyze
# 
# Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526
#
# Output
# Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
# Constraints
# 0 ≤ N < 10000
# Example
# Input
# 5
# 1 -2 -8 4 5
# Output
# 1


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
BelowZeroTemp = [-9999999]
AboveZeroTemp = [9999999]
if n != 0:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)

        if t < 0:
            BelowZeroTemp.append(t)
        else:
            AboveZeroTemp.append(t)


    BelowZero = max(BelowZeroTemp)
    AboveZero = min(AboveZeroTemp)

    if (BelowZero * -1) < AboveZero:
        print(BelowZero)
    else:
        print(AboveZero)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
else:
    print(0)
