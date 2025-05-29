# METHOD-1: iterative model (Brute force)
def twosum(num, target):
    n=len(num)
    for i in range(0, n): #time complexity=O(N**2)
        for j in range(i+1, n): #space complexity=O(1)
            if(num[i]+num[j]==target):
                return [i, j] #returns index's
    return []
num=list(map(int,input().split()))
target=int(input())
result=twosum(num, target)
print(result)

# METHOD-2: Hashing
def twosum(nums, target):
    d={}
    n=len(nums)
    for a in range(0, n):# time, space complexity = O(N)
        b=target-nums[a] #if b = 6-5 = 1(value of b, its not index)
        if(b in d):
            return [a, d[b]] #a=index , d[b]= index of b (checks in dict & returns index of value b)
        else:
            d[nums[a]]=a
nums=list(map(int,input().split()))
target=int(input())
result=twosum(nums, target)
print(result)

# METHOD-3: Optimal method
# make sure array should be in sorted array
# here we 2 pointer technique
# if target is greater, then move high pointer(decrease) & if target is greater, then move low pointer(increase)
#low should be always less than high (low<high) 
#this doesnt work in leet code coz if sorted the index's will be disturbed
def twosum(nums, target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high): #time complexity: O(log N)
        Sum=nums[low]+nums[high] #space complexity: O(1)
        if(Sum==target):
            return "Yes"
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
    return "No"
nums=list(map(int,input().split()))
target=int(input())
result=twosum(nums, target)
print(result)