# Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , 
# that is  increments from  to , find any integer  
# such that  and keep a history of the values of  in a return array.

# ---------------------------SOLUTION-----------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    s=min(p)
    e=max(p)
    ans=[]
    # print(p,s,e+1)
    for x in range(s,e+1):
        # print(x)
        i=p.index(x)+1
        # print('----',i)
        ipos=p.index(i)+1
        ans.append(ipos)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    