import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b, c = [int(i) for i in input().split()]

distanceToGoal = a

i = 0
if b <= c:
    print("Impossible")

else:
    while distanceToGoal > 0:
        distanceToGoal = distanceToGoal - b

        if distanceToGoal > 0:
            distanceToGoal = distanceToGoal + c
        i += 1

    print(i)
