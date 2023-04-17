import sys
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = str(sys.stdin.readline().rstrip())
    
    print(len(line)+1)
