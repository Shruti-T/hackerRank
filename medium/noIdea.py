# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing  integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i bllongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# ----------------------------SOLUTION-------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
nm=input()
arr = input().split()
a = set(input().split())
b = set(input().split())
print(sum([(i in a) - (i in b) for i in arr]))
