# SQUARE ROOT 

# METHOD 1 : linear search 
# time complexity : O(N)
'''
def mySqrt(x):
    ans=0
    for i in range(1, x):
        if(i*i<=x): 
            ans=i
            break
        else:
            break
    return ans
x=int(input())
print(mySqrt(x))
'''
# METHOD 2 : Binary search technique
# time complexity : O(log N)
# here we consider nearest value that doesn't excced given value, if the value is not the perfect square
def mySqrt(x):
        low=1
        high=x 
        while(low<=high):
            mid=(low+high)//2
            if(mid*mid<=x): 
                low=mid+1
            else:
                high=mid-1
        return high
x=int(input())
print(mySqrt(x))
