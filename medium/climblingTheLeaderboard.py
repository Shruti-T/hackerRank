

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
