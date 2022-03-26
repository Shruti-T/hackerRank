# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candels=[4,4,1,3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.

# Function Description

# Complete the function birthdayCakeCandles in the editor below.
# birthdayCakeCandles has the following parameter(s):
# int candles[n]: the candle heights

# ---------SOLTUION-------------
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # Write your code here
    high=0
    for i in candles:
        if(high<i):
            high=i
    x=candles.count(high)
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
