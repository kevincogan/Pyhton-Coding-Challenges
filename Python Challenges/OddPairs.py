# Goal
# find the distinct number between 3 integers a, b and c
# Note: There always two number are the same
# Input
# Line 1: An integer a
# Line 2: An integer b
# Line 3: An integer c
# Output
# Line 1 : A distinct number
# Constraints
# 0 <= a <= 1000
# 0 <= b <= 1000
# 0 <= c <= 1000
# Example
# Input
# 1
# 0
# 1
# Output
# 0

a = int(input())
b = int(input())
c = int(input())
if  a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)
