# -------------------------------------------- Only some test case passed------------------------------------------------

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#
def sides(arr,t):
    # print(arr)
    firstSum=0
    # if(t==0):
    for i in range(0,len(arr)):
        diff=0
        for j in range(0,len(arr)):
            if(j==len(arr)-1):
                break
            elif(arr[j][i]<arr[j+1][i]):
                diff+=arr[j+1][i]-arr[j][i]
                # print(diff,'-',arr[j][i],arr[j+1][i])
        firstSum+=diff 
    # elif(t==1):
    #     for i in range(0,len(arr)):
    #         diff=0
    #         for j in range(0,len(arr)):
    #             if(j==len(arr)-1 or i==len(arr)-1):
    #                 break
    #             elif(arr[j][i]<arr[j+1][i+1]):
    #                 diff+=arr[j][i]-arr[j+1][i+1]
    #                 print(diff,'sss',arr[i][j],arr[i+1][j+1])
    #         firstSum+=diff
    sum=0
    for i in range(0,len(arr)):
        sum+=arr[0][i]
    finalSum=sum+firstSum
    return finalSum

def surfaceArea(A):
    # Write your code here
    # print(A,len(A),len(A[0]),A[0][1])
    top=len(A)*len(A[0])
    top=top*2
    K=[]
    B=[]
    L=[]
    R=[]
    for i in range(0,len(A)):
        x=[]
        for j in range(0,len(A)):
            x.append(A[j][i])
        K.append(x)
    for i in reversed(range(0,len(A))):
        x=[]
        for j in range(0,len(A)):
            x.append(A[j][i])
        B.append(x)
    for i in range(0,len(A)):
        x=[]
        for j in reversed(range(0,len(A))):
            x.append(A[i][j])
        L.append(x)
    for i in reversed(range(0,len(A))):
        x=[]
        for j in range(0,len(A)):
            x.append(A[i][j])
        R.append(x)
    
    front=sides(K,0)
    back=sides(B,1)
    left=sides(L,2)
    right=sides(R,3)
    # print(front,back,left,right)
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
