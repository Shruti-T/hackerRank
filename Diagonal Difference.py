#!/bin/python3
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    sumLeft=0
    sumRight=0
    for i in range(0,n):
        sumLeft+=arr[i][i]
    m=n-1
    for i in range(0,n):
        sumRight+=arr[i][m-i]
    return abs(sumLeft-sumRight)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr,n)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
