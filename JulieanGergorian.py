#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def julian(leap):
    sum=0
    month=0
    day=0
    for i in range(1,12):
                if(i==4 or i==6 or i==9 or i==11):
                    sum+=30
                    x=30
                elif(i==2):
                    sum+=leap
                    x=leap
                else:
                    sum+=31
                    x=31
                month+=1
                if(sum>256):
                    last=sum-x
                    day=256-last
                    break
    if(len(str(month))==1):
        month="0"+str(month)
    return [month,str(day)]
def dayOfProgrammer(year):
    # Write your code here0
    if(year<1918):
        if(year%4==0):
            [month,day]=julian(29)
        else:
            [month,day]=julian(28)
    elif(year>1918):
        if(year%400==0 or (year%4==0 and year%100!=0)):
            [month,day]=julian(29)
        else:
            [month,day]=julian(28)
    else:
        [month,day]=julian(15)
    return day+"."+month+"."+str(year)
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
