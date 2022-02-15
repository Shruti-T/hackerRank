#----------------------------------------------- ONGOING----------------------------------
# 
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    arr=[]
    copy=[]
    for i in range(1,n+1):
        arr.append(i)
        copy.append(i)
    print(arr,copy)
    diff=[]
    for i in arr:
        for j in copy:
            if(abs(i-j)==k):
                diff.append(j)
                copy.remove(j)
    if(diff==[] or copy!=[]):
        return [-1]
    else:
        return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
