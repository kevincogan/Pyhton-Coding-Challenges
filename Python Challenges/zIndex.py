# The program:
# You have intercepted an enemy communication, but the signal is encrypted. However, you know that the message was encrypted using the following algorithm:
#
# For every letter in the message, write an integer E representing the distance of that letter from the letter z in the English alphabet. For spaces, write a value of -1.
#
# You must decrypt this communication, or risk losing the war!
#
# INPUT:
# Line 1: An integer N for the number of letters to decrypt.
# Next N lines: An integer E representing a single letter of the message.
#
# OUTPUT:
# Line 1: A lowercase string representing the decrypted message.
#
# CONSTRAINTS:
# 1 ≤ N ≤ 100
#
# EXAMPLE:
# Input
# 5
# 18
# 21
# 14
# 14
# 11
# Output
# hello



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
alphabet = "abcdefghijklmnopqrstuvwxyz"

list = []
n = int(input())
for i in range(n):
    e = int(input())

    if e == -1:
        list.append(" ")
    else:
        list.append(alphabet[25 - e])


print("".join(list))
