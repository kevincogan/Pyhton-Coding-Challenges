import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input().split()
n = int(input())
for i in range(n):
    word = input()

    i = 0
    for m in message:
        if m == (len(word) * "_"):
            message[i] = word
        i += 1

print(" ".join(message))
