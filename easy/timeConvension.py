# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# ---------------SOLUTION--------------------

import math
import os
import random
import re
import sys
def timeConversion(s):
    # Write your code here
    first=s[0:2]
    time=s[-2:]
    if time=="PM":
        if(first!="12"):
            newTime=str(int(first)+12)
        else:
            newTime="12"
    else:
        if(first=="12"):
            newTime="00"
        else:
            newTime=first
    
    final=newTime+s[2:8]
    return final
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
