# An integer d is a divisor of an integer n if the remainder of n/d=0. Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.


# -----------------SOLUTION-------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    num=n
    digit=-10
    t=0
    for k in range(0,len(str(n))):
        digit=n%10
        n=n//10
        if(digit!=0):
            if(num%digit==0):
                t+=1
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
