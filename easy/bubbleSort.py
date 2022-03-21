# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above.
# ------------------------SOLUTION---------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    # print(a)
    swap=0
    swapped=False
    k=len(a)
    while(k!=0):
        for i in range(0,len(a)-1):
            if(a[i]>a[i+1]):
                swap+=1
                t=a[i+1]
                a[i+1]=a[i]
                a[i]=t
        k-=1
    # print(a)
    print('Array is sorted in', swap,'swaps.','\nFirst Element:',a[0],'\nLast Element:',a[len(a)-1])
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
