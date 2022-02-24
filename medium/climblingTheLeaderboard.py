# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# Example
# ranked=[100,90,90,80]
# player=[70,80,105]
# The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st. Return [4,3,1].

# Function Description
# Complete the climbingLeaderboard function in the editor below.
# climbingLeaderboard has the following parameter(s):
# int ranked[n]: the leaderboard scores
# int player[m]: the player's scores

# ----------------------------------------------SOLUTON (TIMEOUT IN FEW CASES)------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def giveRank(ranked):
    ranks=[1]
    i=0
    while(i<len(ranked)-1):
        if(ranked[i]==ranked[i+1]):
            x=ranks[len(ranks)-1]
            ranks.append(x)
        else:
            x=ranks[len(ranks)-1]+1
            ranks.append(x)
        i+=1
    return ranks
def climbingLeaderboard(ranked, player):
    # Write your code here
    ans=[]
    ranks=giveRank(ranked)
    for i in range(0,len(player)):
        ranked.append(player[i])
        ranked.sort(reverse=True)
        val=giveRank(ranked)
        for j in range(0,len(ranked)):
            if(player[i]==ranked[j]):
                result=val[j]
                ans.append(result)
                break
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
