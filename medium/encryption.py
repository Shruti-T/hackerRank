# An English text needs to be encrypted using the following encryption scheme. First, the spaces are removed from the text. Let L be the length of this text.

# ----------------------------------------------SOLUTION--------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    l=len(s)
    row=int(math.sqrt(l))
    col=row+1
    a=row*col
    b=row*(col-1)
    if(a<l):
        row+=1
    if(a>l and b>=l):
        col-=1
        
    arr=[]
    j=0
    for i in range(0,row):
        temp=""
        temp=s[j:j+col]
        j+=col
        arr.append(temp)

    final=[]
    for p in range(0, col):
        t=""
        for k in range(0, len(arr)):
            try:
                t+=arr[k][p]
            except IndexError:
                break
        final.append(t)
        
    mytuple=tuple(final)
    ans=" ".join(mytuple)
    
    return ans
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
