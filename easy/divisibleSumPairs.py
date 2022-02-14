# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

# Example:
# ar=[1,2,3,4,5,6]
# k=5
# Three pairs meet the criteria:[1,4],[2,3] and [4,6].

# Function Description

# Complete the divisibleSumPairs function in the editor below.
# divisibleSumPairs has the following parameter(s):
# int n: the length of array ar
# int ar[n]: an array of integers
# int k: the integer divisor

# ----------SOLUTION---------
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    t=0
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if((ar[i]+ar[j])%k == 0):
                t+=1
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
