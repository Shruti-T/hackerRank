# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# -------------------------------------SOLUTION--------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    new=list(set(a))
    new.sort()
    allArr=[]
    maxList=[]
    
    print(a,new)
    
    if(len(new)<=1):
        return len(a)
    else:
        for i in range(0,len(new)-1):
            if(new[i+1]-new[i]<=1):
                allArr.append([new[i],new[i+1]])
            else:
                allArr.append([new[i]])
                allArr.append([new[i+1]])
        for j in range(0,len(allArr)):
            s=0
            for k in range(0,len(allArr[j])):
                s+=a.count(allArr[j][k])
            maxList.append(s)
        return max(maxList)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
