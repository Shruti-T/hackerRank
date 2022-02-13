# Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

# From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

# In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

# Divisible by 400.
# Divisible by 4 and not divisible by 100.
# Given a year, Y, find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is Y.

# For example, the given  year= 1984. 1984 is divisible by 4, so it is a leap year. The 256th day of a leap year after 1918 is September 12, so the answer is 12.09.1984.
#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#Function Description

# Complete the dayOfProgrammer function in the editor below. It should return a string representing the date of the 256th day of the year given.
# dayOfProgrammer has the following parameter(s):
# year: an integer

# -----------------SOLUTION---------
def julian(leap):
    sum=0
    month=0
    day=0
    for i in range(1,12):
                if(i==4 or i==6 or i==9 or i==11):
                    sum+=30
                    x=30
                elif(i==2):
                    sum+=leap
                    x=leap
                else:
                    sum+=31
                    x=31
                month+=1
                if(sum>256):
                    last=sum-x
                    day=256-last
                    break
    if(len(str(month))==1):
        month="0"+str(month)
    return [month,str(day)]
def dayOfProgrammer(year):
    # Write your code here0
    if(year<1918):
        if(year%4==0):
            [month,day]=julian(29)
        else:
            [month,day]=julian(28)
    elif(year>1918):
        if(year%400==0 or (year%4==0 and year%100!=0)):
            [month,day]=julian(29)
        else:
            [month,day]=julian(28)
    else:
        [month,day]=julian(15)
    return day+"."+month+"."+str(year)
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
