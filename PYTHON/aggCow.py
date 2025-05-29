# AGGRESSIVE COWS

def aggressiveCows(stalls, k):
    def canweplace(stalls, mindist, k):
        placedCows=1 # initially we'll allocate the 1st cow
        cows=stalls[0] # the starting cow will be allocated to the 1st place
        for stall in range(1, len(stalls)): # in the arr len we'll place the cows
            if(stalls[stall]-cows<=mindist): 
                ''' ex: [0 3 4 7 9 10],k=4 
                    stalls[0]=0, stalls[1]=3 
                    we'll take min dist from 1 upto max(stalls)
                    if mindist=1 then stalls[1]-cows<=1         {cows=stalls[0]}
                '''
                cows+=stalls[stall] # we'll present stalls to the previous stalls
                placedCows+=1 # increase placed cow 
            if(placedCows==k): 
                return True
        return False
    stalls.sort()
    low=1
    high=max(stalls)
    while(low<=high):
        mindist=(low+high)//2
        if(canweplace(stalls, mindist, k)):
            low=mindist+1
        else:
            high=mindist-1
    return mindist-1
stalls=list(map(int, input().split()))
k=int(input())
print(aggressiveCows(stalls, k))