# You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

# ------------------------------------SOLUTION---------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT

# sep=we can change the default spacing in print python!


from itertools import groupby
for i, n in groupby(input()):
        a = list(n) 
        print("(",len(a),", ",a[0],")",sep="",end=" ")
        
