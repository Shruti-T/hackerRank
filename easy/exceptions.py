# Exceptions
# Errors detected during execution are called exceptions.
# Examples:
# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero.
# ValueError
# This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

# ---------------------------------------------------SOLUTION--------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    a,b=input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer",str(e)[:8]+" or modulo"+str(e)[8:])
    except  ValueError as e:
        print("Error Code:",e)
