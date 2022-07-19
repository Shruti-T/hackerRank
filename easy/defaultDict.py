# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

# ---------------------------SOLUTION---------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
ar=input().split()
n=int(ar[0])
m=int(ar[1])

A=[]
B=[]

for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())

indices=[]
for k in range(0,len(B)):
    indices=[i+1 for i,x in enumerate(A) if x==B[k]]
    if(indices==[]):
        indices.append(-1)
    print(*indices)
        
        
        
        