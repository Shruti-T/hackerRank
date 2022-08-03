# You are given an integer,N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# --------------------------------SOLUTION-----------------------------

def print_rangoli(size):
    alp=chr(size+96)
    arr=[alp]
    for i in range(1,size):
        n=arr[i-1][0:i]+chr(ord(alp)-(i))+arr[i-1][-i:]
        arr.append(n)
    l=len(arr[len(arr)-1].replace("","-")[1:-1])
    for k in range(0,len(arr)):
        s=arr[k].replace("","-")
        if(k!=len(arr)-1):
            print(s.center(l,"-"))
        else:
            print(s[1:-1])
    
    for k in reversed(range(0,len(arr)-1)):
        s=arr[k].replace("","-")
        if(k!=len(arr)-1):
            print(s.center(l,"-"))
        else:
            print(s[1:-1])
        
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)