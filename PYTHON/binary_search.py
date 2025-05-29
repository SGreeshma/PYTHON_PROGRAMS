def bs(arr, k):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):    
            return True
        elif(arr[mid]<k):
            low=mid+1
        else:
            high=mid-1
    return False
arr=list(map(int, input().split()))
k=int(input())
print(bs(arr, k))
