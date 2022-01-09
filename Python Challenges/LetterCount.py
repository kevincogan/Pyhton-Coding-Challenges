# Add the value of the letters
# Value is the same whether capitalized or not.
# Non-letter characters are worth 0.
# Input
# Line 1: An integer n, number of lines
# Following n lines: string l
# Output
# n lines: The computed values, in order of input
# Constraints
# Example
# Input
# 4
# a
# b
# C
# D
# Output
# 1
# 2
# 3
# 4

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
alphabet = "abcdefghijklmnopqrstuvwxyz"


n = int(input())
for i in range(n):
    l = input()

    if l.isalpha():
        i = 0
        for letter in l:
            i += alphabet.index(letter) + 1
        print(i)
    else:
        pass
