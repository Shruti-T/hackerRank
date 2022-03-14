# There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.

# ------------SOLUTION----------
#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # Write your code here
    high=-100
    # print(len(arr))
    for c in range(0,4):
        for r in range(0,4):
            sum1=arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
            if(sum1>high):
                high=sum1
    return high
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
