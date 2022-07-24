# ABC is a right triangle, 90 at B. Therefore, angle ABC=90.
# Point M is the midpoint of hypotenuse AC. You are given the lengths AB and BC. Your task is to find MBC (angle theta, as shown in the figure) in degrees.


# ----------------------------------------------SOLUTION------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab=int(input())
bc=int(input())

angle=round(math.degrees(math.atan2(ab,bc)))
print(str(angle)+"\u00B0")
