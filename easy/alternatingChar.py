# You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
# Your task is to find the minimum number of required deletions.

# ---------------SOLUTION-----------------------

import os

def alternatingCharacters(s):
    # Write your code here
    t=0
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            t+=1
    return t
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
