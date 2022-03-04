# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

# -------SOLUTION-------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps=0
    ones=[]
    i=0
    k=0
    while (i+2<len(c)-1):
        if(i==len(c)-1 or i==len(c)-2):
            jumps+=1
            k=1
            break
        if(c[i+2]==0):
            jumps+=1
            i+=1
        elif(c[i+1]==0):
            jumps+=1
        i+=1
    if(k==0):
        jumps+=1
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
