# You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.



# -------------SOLUTION (few test cases timeOut)------------------
# SELECTION SORT!

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    total=0
    for i in range(0,len(arr)):
        num=min(arr[i:len(arr)])
        k=len(arr)-(arr[::-1].index(num)+1)
        if(i!=k):
            arr[k]=arr[i]
            total+=1
    return total
            
        
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
