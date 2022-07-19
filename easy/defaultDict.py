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
    
print(A,B)

# for k in range(0,len(B)):
#     # indices=[i for i,x in enumerate(A) if x=='a']
#     indices='s'
#     print(indices)
