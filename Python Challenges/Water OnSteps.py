# Water pours down steps, You can watch it pour. For each step, the water travels down 1 more step.
# Input
# A number of steps n for which the water(symbol for water) will pour down.
# NEXT LINE will be the water pouring down the next step.
# Output
# water pouring down the steps.
#
# Constraints
# 0<n<8
# Example
# Input
# 5
# _
# Output
# _
#  _
#   _
#    _
#     _

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
water = input()

for i in range(n):
    print((i * " ") + water)
