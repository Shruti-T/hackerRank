# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
# 1. Append a lowercase English letter to the end of the string.
# 2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.

# --------------------------------------------------SOLUTION----------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    slt=len(s)
    tlt=len(t)
    if(slt==tlt and k==(slt*2)):
        return "Yes"
    
    start=s.find(t)
    if(start!=-1):
        index=start+tlt
        steps=k-(slt-index)
        if(steps<0):
            return "No"
        else:
            return "Yes"
    else:
        if(slt>=tlt):
            for i in reversed(range(0,tlt)):
                if(s[0:i]==t[0:i]):
                    index=i
                    break
            left=k-((slt-index)+(tlt-index))
        else:
            index=tlt-(tlt-slt)
            for i in range(1,index+1):
                index-=1
                left=k-((slt-index)+(tlt-index))
                if(left==0):
                    break
    if(left<0):
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
