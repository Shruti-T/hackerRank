# HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  5 people on social media.

# --------------------------------------------SOLUTION---------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    liked=0
    share=5
    for i in range(0,n):
        x=int(share/2)
        liked+=x
        share=x*3
    return liked

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
