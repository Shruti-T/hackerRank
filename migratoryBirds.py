#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    mySet=set(arr)
    myList = list(mySet)
    maxi=0
    ele=0
    for i in myList:
        t=arr.count(i)
        if(maxi<t):
            maxi=t
            ele=i
        elif(maxi==t):
            if(ele>i):
                maxi=t
                ele=i
    return ele

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
