# MERGE SORT : Divide and conquer method is used (2 pointer technique is used)

def merge(nums, low, high): #time complexity = O(n log n)
    if (low>=high): # BASE CONDITION : as 1 element cannot be divided further, ex: [5] cant be divided further has only element i.e 5
        return 
    mid=(low+high)//2
    merge(nums, low, mid) # 1st part
    merge(nums, mid+1, high) #  2nd part
    sort(nums, low, mid, high)

def sort(nums, low, mid, high):
    i=low # in the arr i is taken as low
    j=mid+1 # j starts from mid+1
    k=[]   #space complexity= O(n)
    while(i<=mid and j<=high):
        if(nums[i]<=nums[j]):  # if nums[i]==nums[j] then we consider i as smallest value 
            k.append(nums[i])
            i+=1
        else:
            k.append(nums[j])
            j+=1
    while(i<=mid): # i at max it can go till mid value
        k.append(nums[i]) 
        i+=1
    while(j<=high): # j at max it can go till high value
        k.append(nums[j])
        j+=1
    for ind, val in enumerate(k): 
        nums[ind+low]=val
nums=list(map(int, input().split()))
merge(nums, 0, len(nums)-1)
print(nums)  