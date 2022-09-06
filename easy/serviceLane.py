# You will be given an array of widths at points along the road (indices), then a list of the indices of entry 
# and exit points. Considering each entry and exit point pair, 
# calculate the maximum size vehicle that can travel that segment of the service lane safely.

# --------------------------------------------SOLUTION------------------------------------

import os

def serviceLane(n, cases,wd):
    # Write your code here
    # print(n,cases)
    ans=[]
    for r in cases:
        entry=r[0]
        exit=r[1]
        # print(entry,exit)
        wt=wd[entry:exit+1]
        ans.append(min(wt))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases,width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
