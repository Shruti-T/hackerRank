#!/bin/python3
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    t=0
    status=False
    for i in range(1,101):
        for k in a:
            if(i%k==0):
                status=True
            else:
                status=False
                break
        if(status==True):
            for l in b:
                if(l%i==0):
                    status=True
                else:
                    status=False
                    break
        if(status==True):
            t+=1
    return t
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
