# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# Example:
# arr=[1,1,2,2,3]
# There are two each of types  1 and 2 , and one sighting of type 3 . Pick the lower of the two types seen twice: type 1.

# Function Description

# Complete the migratoryBirds function in the editor below.
# migratoryBirds has the following parameter(s):
# int arr[n]: the types of birds sighted



# ----------SOLUTION----------
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    mySet=set(arr)
    myList = list(mySet)
    maxi=0
    ele=0
    for i in myList:
        t=arr.count(i)
        if(maxi<t):
            maxi=t
            ele=i
        elif(maxi==t):
            if(ele>i):
                maxi=t
                ele=i
    return ele

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
