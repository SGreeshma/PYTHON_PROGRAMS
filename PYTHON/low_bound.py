# LOWER BOUND : smallest element such that arr[ind]>=target

def lowBound(arr, k):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=k): # for lower bound the elements must be greater or equal than the target but we consider smallest index among all the greater elements
            ans=mid
            high=mid-1 # eliminating the right search space
        else:
            low=mid+1 # eliminating the left search space
    return ans
arr=list(map(int, input().split()))
k=int(input())
print(lowBound(arr, k))