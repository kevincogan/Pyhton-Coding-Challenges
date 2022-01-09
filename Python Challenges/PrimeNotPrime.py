import sys
import math
n = int(input("Input number: "))
t = 0
if n==1 or n==0 or (n % 2 == 0 and n > 2):
    print("Inpput number squared: " + str(n * n))
else:
    for d in str(n):
        t += int(d)
    print("Sum of each input digit squared: " + str(t * t))
