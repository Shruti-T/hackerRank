# Your local library needs your help! Given the expected and actual return dates for a library book, 
# create a program that calculates the fine (if any)

# -----------------------------------SOLTUION-------------------------

import os
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    ans=-10
    if(y2<y1):
        ans=10000
    elif(m1>m2 and y1==y2):
        ans=500*(m1-m2)
    elif(d1>d2 and m1==m2 and y1==y2):
        ans=15*(d1-d2)
    else:
        ans=0
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])
    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    fptr.write(str(result) + '\n')
    fptr.close()
