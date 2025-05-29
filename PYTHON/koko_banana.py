# KOKO EATING BANANA
from math import *
def koko(piles, k):
    low=1
    high=max(piles)
    while(low<=high):
        mid=(low+high)//2
        Sum=0
        for num in piles:
            Sum+=ceil(num/mid)
        if(Sum<=k):
            high=mid-1
        else:
            low=mid+1
    return low
piles=list(map(int, input().split()))
k=int(input())
print(koko(piles, k))