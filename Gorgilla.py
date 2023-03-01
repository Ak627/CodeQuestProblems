import sys
import string

num = int(input())

for i in range(num):
    line = sys.stdin.readline().rstrip()
    g1, g2 = (str(val) for val in line.split(" "))

    if g1 == "true" and g2 == "true":
        print("true")
    elif g1== "false" and g2 == "false":
        print("true")
    else:
        print("false")
