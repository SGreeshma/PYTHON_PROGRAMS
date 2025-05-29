# UPPER BOUND : smallest element such that arr[ind]>target

def lowBound(arr, k):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>k):  # for upper bound the elements should be greater than the target but we consider the smallest index among the greater elements
            ans=mid 
            high=mid-1 # eliminating the right search space
        else:
            low=mid+1 # eliminating the left search space
    return ans
arr=list(map(int, input().split()))
k=int(input())
print(lowBound(arr, k))