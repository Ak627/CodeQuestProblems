import sys
import math
import string

num = int(input())


legs = []

for i in range(num):
    line = sys.stdin.readline().rstrip()
    t, g, h = (int(val) for val in line.split(" "))
    
    tl = t * 2
    gl = g * 4
    hl = h * 4
    
    totalL = tl + gl + hl
    legs.append(totalL)
    
for i in range(num):
    print(legs[i])
    
