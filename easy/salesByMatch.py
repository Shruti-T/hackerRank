# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# n=7
# ar=[1,2,1,2,13,2]

# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

# Function Description
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock

# ------------------SOLUTION---------------------------------
import os
def sockMerchant(n, ar):
    # Write your code here
    # print(ar)
    ar.sort()
    pairs=0
    i=0
    while i<n-1:
        if(ar[i]==ar[i+1]):
            pairs+=1
            i+=1
        i+=1
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
