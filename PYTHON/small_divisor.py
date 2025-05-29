# SMALLEST DIVISOR

# METHOD 1: Linear search 
# time complexity : O(N**2)
'''
import math
def smallDiv(arr, k):
    for i in range(1, max(arr)):
        Sum=0
        for num in arr:
            Sum+=math.ceil(num/i)
        if (Sum<=k):
            return i
arr=list(map(int, input().split()))
k=int(input())
print(smallDiv(arr, k))
'''
# METHOD 2: Binary search 
# time complexity : O(log N)
import math
def sd(arr, k):
    low=0
    high=max(arr) 
    while(low<=high):
        div=(low+high)//2 # div=mid; here we divide with the mid pointer 
        Sum=0 
        for num in arr:
            Sum+=math.ceil(num/div) # we have consider ceil value 
        if(Sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int, input().split()))
k=int(input())
print(sd(arr, k))