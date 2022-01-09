import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

RNA = ["A", "C", "G", "U"]
DNA = ["A", "C", "G", "T", "U"]
current_list = []

for letter in s:
    if letter not in current_list:
        current_list.append(letter)

    if letter in RNA and letter in DNA:
        output = "VALID RNA " + "".join(current_list)

    elif not letter in RNA and letter in DNA:
        output = "VALID DNA " + "".join(current_list)

    else:
        output = "INVALID INPUT"

print(output)
