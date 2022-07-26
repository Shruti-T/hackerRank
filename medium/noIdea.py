# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing  integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i bllongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# ----------------------------SOLUTION (not working with 10^5 values of input)-------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
nm=input()
arr=list(map(int,input().split(" ")))
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))

# happy=0
# arr2=list(set(arr))
# for i in arr2:
#     if(i in a):
#         x=arr.count(i)
#         happy+=x
#     elif(i in b):
#         x=arr.count(i)
#         happy-=x
# print(happy)

# ==============
# print(sum([(i in a) - (i in b) for i in arr]))
# ==============
# array = input().split()
# like = set(input().split())
# dislike = set(input().split())
print(sum((i in a) - (i in b) for i in arr))
