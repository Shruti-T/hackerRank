# Consider the following: 
# A string, s , of length n.
# An integer, k , where kis a factor of n.
# We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui.

# ----------------------------------------SOLUTION--------------------------------------------------
def merge_the_tools(string, k):
    # your code goes here
    # print(string,k)
    arr=[]
    num=int(len(string)/k)
    for i in range(0,len(string),k):
        s=string[i:i+k]
        arr.append(s)
    
    # print(arr)
    
    for k in range(0,len(arr)):
        charSeen=[]
        for c in arr[k]:
            if(c not in charSeen):
                charSeen.append(c)
        print("".join(charSeen))
        
        
if __name__ == '__main__':