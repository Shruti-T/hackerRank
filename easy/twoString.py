# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# ---------------------SOLUTION---------------------
import os
#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    if(len(s1)>len(s2)):
        tos=s1
        fs=s2
    else:
        tos=s2
        fs=s1
        
    for i in tos:
        if i in fs:
            return "YES"
        else:
            status=0
    if(status==0):
        return "NO"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
