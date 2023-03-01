import sys
import math
import string

def get_key(val):
    for key, value in astlis.items():
        if val == value:
            return key

num = int(input())
SEPERATOR = " "

for i in range(num):
    
    
    astlis = {}
    DISTANCES = []
    aste = int(input())
    
   
    for i in range(aste):
        line = sys.stdin.readline().rstrip()
        ex, wai = (int(val) for val in line.split(SEPERATOR))
        distance = math.sqrt(pow(ex, 2) + pow(wai, 2))
        DISTANCES.append(distance)
        astlis.update({line:distance})
    DISTANCES.sort()
    for distance in DISTANCES:
        print(get_key(distance))
     
