# There is a string,s , of lowercase English letters that is repeated infinitely many times. Given an integer,n , find and print the number of letter a's in the first n letters of the infinite string.

# --------SOLUTION--------

import os
import re
def repeatedString(s, n):
    # Write your code here
    x=len(re.findall('a',s))
    slen=len(s)
    j=n%slen
    y=len(re.findall('a',s[0:j]))
    final=x*(n//slen)+y
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
