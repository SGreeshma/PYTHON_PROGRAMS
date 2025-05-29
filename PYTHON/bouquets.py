# Min days required to make M bouquets
class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        if(m>len(arr)):
            return -1 
        Min=min(arr) 
        Max=max(arr) 
        for bloomday in range(Min,Max+1):
            count=0 
            noOfB=0 
            for flower in arr:
                if(flower<=bloomday):
                    count+=1 
                else:
                    noOfB+=count//k 
                    count=0 
            noOfB+=count//k 
            if(noOfB>=m):
                return bloomday 
        return -1 
#User function Template for python3
'''
class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        if(m>len(arr)):
            return -1 
        low=min(arr) 
        high=max(arr) 
        ans = -1 
        while(low<=high):
            bloomday=(low+high)//2 
            count=0 
            noOfB=0 
            for flower in arr:
                if(flower<=bloomday):
                    count+=1 
                else:
                    noOfB+=count//k 
                    count=0 
            noOfB+=count//k 
            if(noOfB<m):
                low=bloomday+1 
            else:
                ans=bloomday 
                high=bloomday-1 
        return ans
'''