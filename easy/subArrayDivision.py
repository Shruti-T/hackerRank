# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Example
# s=[2,2,1,3,2]
# d=4
# m=2
# Lily wants to find segments summing to Ron's birth day,d=4  with a length equalling his birth month,m=2 . In this case, there are two segments meeting her criteria: [2,2] and [1,3] .

# Function Description

# Complete the birthday function in the editor below
# birthday has the following parameter(s):
# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month

# ---------SOLUTION---------
#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    t=0
    bar=[]
    i=0
    #for i in range(0,len(s)):
    while i<len(s):
        bar.append(s[i])
        if(len(bar)==m):
            sum=0
            for j in bar:
                sum+=j
            if(sum==d):
                t+=1
            bar=[]
            if(m==1):
                i+=1
            else:
                i-=(m-2)
        else:
            i+=1        
    return t
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
