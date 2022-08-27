# Given a sequence of n integers, p(1), p(2),...,p(n) where each element is distinct and satisfies 1 <=p(x) <=n. 
# For each x where 1 <= x <=n, that is x increments from 1 to n, find any integer y such that p(p(y)) = x and 
# keep a history of the values of y in a return array.

# ------------------------------------------SOLUTION-----------------------------

def permutationEquation(p):
    # Write your code here
    s=min(p)
    e=max(p)
    ans=[]
    # print(p,s,e+1)
    for x in range(s,e+1):
        # print(x)
        i=p.index(x)+1
        # print('----',i)
        ipos=p.index(i)+1
        ans.append(ipos)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    