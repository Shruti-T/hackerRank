# ------------------ FEW TEST CASES FAILED(RUNTIME)----------------------------


# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Example
# a=[1,1,2,2,4,4,5,5,5]
# There are two subarrays meeting the criterion: [1,1,2,2] and[4,4,5,5,5] . The maximum length subarray has 5 elements.

# Function Description
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers


# -----------------SOLUTION-----------------
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    myans=[]
    lenth=len(myans)
    for i in range(0,len(a)):
        ans=[]
        ans.append(a[i])
        for j in range(0,len(a)):
            # print(a[i],a[j])
            if(i!=j):
                if(abs(a[i]-a[j])<=1):
                    ans.append(a[j])
        myans.append(ans)
    lenarr=[]
    
    for k in range(len(myans)):
        print(len(myans[k]))
        perm = combinations(myans[k], 2)
        for i in list(perm):
            if(abs(i[0]-i[1])>1):
                status=0
                break
            else:
                status=1
        if(status==1):
            lenarr.append(len(myans[k]))
    print(lenarr)
    return max(lenarr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
