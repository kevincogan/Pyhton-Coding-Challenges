# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:

# 01 Test 1
# Input
# Expected output
# upper
# 3
# A B C

# 02 Test 2
# Input
# Expected output
# lower
# 3
# a b c

# 03 Test 3
# Input
# Expected output
# uPpeR
# 26
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# 04 Test 4
# Input
# Expected output
# lowER
# 26
# a b c d e f g h i j k l m n o p q r s t u v w x y z

# 05 Test 5
# Input
# Expected output
# upper
# 27
# ERROR



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

case_or_trick = input().lower()
n = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

i = 0
output = ""
if n > 26:
    output = "ERROR"

elif case_or_trick == "upper":
    while i < n:
        output = output + alphabet[i].upper() + " "
        i += 1


elif case_or_trick == "lower":
    while i < n:
        output = output + alphabet[i].lower() + " "
        i += 1

print(output.strip())
