# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

# Example
# x1=2
# v1=1
# x2=1
# v2=2
# After one jump, they are both at x=3, (x1+v1=2+1,x2+v2=1+2), so the answer is YES.

# Function Description

# Complete the function kangaroo in the editor below.
# kangaroo has the following parameter(s):
# int x1, int v1: starting position and jump distance for kangaroo 1
# int x2, int v2: starting position and jump distance for kangaroo 2

# ------------SOLUTION--------------
#!/bin/python3
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    d1=x1
    d2=x2
    for i in range(0,10001):
        d1+=v1
        d2+=v2
        if(d1==d2):
            a=1
            break
        else:
            a=0
    if(a==1):
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
