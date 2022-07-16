# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

#----------------------------------------------SOLUTION---------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
d={}
uni=0
for i in range(0,n):
    a=input()
    if(d.get(a)!=None):
        d[a]=(d.get(a)+1)
    else:
        d[a]=1
        uni+=1
        
print(uni)
for value in d.values():
    print(value,end=" ")
    