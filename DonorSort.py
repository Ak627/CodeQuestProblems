import sys
import string

cases = int(sys.stdin.readline().rstrip())

for testCases in range(cases):
    list1 = sys.stdin.readline().rstrip().split(",")
    list2 =sys.stdin.readline().rstrip().split(",")
    both = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                both.append(list1[i])
  
    for i in both:
        list1.remove(i)
        list2.remove(i)
                
    list1.sort()
    list2.sort()
    both.sort()

    print(f"{','.join(list1)}")
    print(f"{','.join(both)}")
    print(f"{','.join(list2)}")
    
