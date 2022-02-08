#!/bin/python3

# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        space=n-i
        string=""
        string=string.zfill(space)
        string=string.replace("0", " ")
        
        hashS=""
        hashS=hashS.zfill(i)
        hashS=hashS.replace("0", "#")
        line=string+hashS
        print(line)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
