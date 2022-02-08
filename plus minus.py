#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    z=0
    p=0
    n=0
    for i in range(0,len(arr)):
        if(arr[i]==0):
            z+=1
        elif(arr[i]<0):
            n+=1
        else:
            p+=1    
    x="{:.6f}".format(p/len(arr))  
    y="{:.6f}".format(n/len(arr))
    l="{:.6f}".format(z/len(arr))
    print(x)
    print(y)
    print(l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

