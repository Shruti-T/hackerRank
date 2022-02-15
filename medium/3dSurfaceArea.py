# Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board A  of size H x W  with H rows and W columns. The board is divided into cells of size 1x1 with each cell indicated by its coordinate (i,j) . The cell (i,j) has an integer Aij written on it. To create the toy Mason stacks Aij number of cubes of size 1x1x1 on the cell (i,j).

# Given the description of the board showing the values of Aij and that the price of the toy is equal to the 3d surface area find the price of the toy.

# Input Format
# The first line contains two space-separated integers H and W the height and the width of the board respectively.
# The next H lines contains W space separated integers. The jth integer in ith line denotes Aij.


# ----------------------SOLUTION------------------------------------
#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#
def sides(arr,t):
    firstSum=0
    for i in range(0,len(arr[0])):
        diff=0
        for j in range(0,len(arr)):
            if(j==len(arr)-1):
                break
            elif(arr[j][i]<arr[j+1][i]):
                diff+=arr[j+1][i]-arr[j][i]
        firstSum+=diff 
    sum=0
    for i in range(0,len(arr[0])):
        sum+=arr[0][i]
    finalSum=sum+firstSum
    return finalSum

def surfaceArea(A):
    # Write your code here
    top=len(A)*len(A[0])
    top=top*2
    K=[]
    B=[]
    L=[]
    R=[]
    # print(len(A),len(A[0]))
    for i in range(0,len(A[0])):
        x=[]
        for j in range(0,len(A)):
            x.append(A[j][i])
        K.append(x)
    for i in reversed(range(0,len(A[0]))):
        x=[]
        for j in range(0,len(A)):
            x.append(A[j][i])
        B.append(x)
    for i in range(0,len(A)):
        x=[]
        for j in range(0,len(A[0])):
            x.append(A[i][j])
        L.append(x)
    for i in reversed(range(0,len(A))):
        x=[]
        for j in range(0,len(A[0])):
            x.append(A[i][j])
        R.append(x)
    
    front=sides(K,0)
    back=sides(B,1)
    left=sides(L,2)
    right=sides(R,3)
    return front+back+left+right+top

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
