# NTH ROOT 

# METHOD 1: Linear search 
# time complexity : O(N)
'''
def nthroot(n, m):
    ans=-1
    for i in range(0, m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(nthroot(n, m))
'''
# METHOD 2 : Binary search 
# time complexity : O(log N)
def nthroot(n, m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m): # if mid pointer is equal to the given value
            return mid
        elif(mid**n>m): # if mid pointer is greater then given value
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input())
m=int(input())
print(nthroot(n, m))
