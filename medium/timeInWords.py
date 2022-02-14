# Given the time in numerals we may convert it into words, as shown below:
# 5:00-"five o' clock"
# 5:01-"one minute past five"
# 5:15-"quarter past five"
# 5:30-"half past five"
# 5:40-"twenty minutes to six"
# 5:45-"quarter to six"
# 5:28-"twenty eight minutes past five"


# At minutes=0, use o' clock. For 1<=minutes<=30 , use past, and for 30<minutes  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

# Function Description

# Complete the timeInWords function in the editor below.
# timeInWords has the following parameter(s):
# int h: the hour of the day
# int m: the minutes after the hour

# ---------SOLUTION----------
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
def number(clock):
    switcher = {
        1: "one",2: "two",3: "three",4: "four", 5: "five",6: "six",7: "seven",8: "eight",9: "nine",10: "ten",11: "eleven",12: "twelve",13 : 'thirteen', 14 : 'fourteen',15 : 'fifteen',16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',19 : 'nineteen', 20 : 'twenty',30:'thirty'
    }
    if(clock>20 and clock!=30):
        x=switcher.get(clock%10)
        y=switcher.get(int(clock)-(clock%10))
        return y+" "+x
    else:
        return switcher.get(clock)
def timeInWords(h, m):
    # Write your code here
    if(m==00):
        txt=number(h)
        return txt+" o' clock"
    elif(1<=m and m<=30):
        mi=number(m)
        sec=number(h)
        if(m==15):
            x="quarter past "+sec
        elif(m==30):
            x="half past "+sec
        elif(m==1):
            x=mi+" minute past "+sec
        else:
            x=mi+" minutes past "+sec
        return x
    elif(m>30):
        if(h==12):
            h=1
        else:
            h+=1
        if(m==45):
            m=60-m
            mi=number(m)
            sec=number(h)
            return "quarter to "+sec
        else:
            m=60-m
            mi=number(m)
            sec=number(h)
            return mi+" minutes to "+sec    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
