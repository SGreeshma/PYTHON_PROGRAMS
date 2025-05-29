# SINGLE ELEMENT IN A SORTED ARRAY

# METHOD 1: time complexity - O(n**2)
'''
def find(arr):
    for i in arr:
        if(arr.count(i)==1):
            return i
arr=list(map(int, input().split()))
print(find(arr))
'''

# METHOD 2: Binary search technique 
# time complexity - O(log N)
def find(nums):
    n=len(nums)
    if(n==1): # if arr has 1 ele
        return nums[0]
    if(nums[0]!=nums[1]): # if 0th index is single ele
        return nums[0]
    if(nums[n-1]!=nums[n-2]): # if single ele is at n-1 
        return nums[n-1]
    low=1 # as we already checked 0th pos
    high=n-2 # as we already checked n-1 pos
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]): 
            return nums[mid]
        # left half (even, odd)
        elif((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):
            low=mid+1
        # right half (odd, even)
        elif((mid%2==1 and nums[mid]==nums[mid+1]) or (mid%2==0 and nums[mid]==nums[mid-1])):
            high=mid-1
    return nums[mid]
nums=list(map(int, input().split()))
print(find(nums))
