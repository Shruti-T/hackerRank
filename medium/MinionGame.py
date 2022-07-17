# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.


#-----------------------------------SOLUTION------------------------------------------

def minion_game(string):
    vowels = 'AEIOU'
    kev=0
    stu=0
    for i in range(len(s)):
        if s[i] in vowels:
            kev+= (len(s)-i)
            # print(i,s[i],kev,'kev----')
        else:
            stu+= (len(s)-i)
            # print(i,s[i],stu,'stu----')

    if(kev>stu):
        print("Kevin", kev)
    elif(kev<stu):
        print("Stuart", stu)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)