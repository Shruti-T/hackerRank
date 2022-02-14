# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a=[2,6]
# b=[24,36]
# There are two numbers between the arrays:  6 and 12 .
# 6%2=0,6%6=0 ,24%6=0  and 36%6=0 for the first value.
# 12%2=0, 12%6=0 and 24%6=0, 36%12=0 for the second value. Return 2.

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
# getTotalX has the following parameter(s):
# int a[n]: an array of integers
# int b[m]: an array of integers

# -----------------SOLUTION------------
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
