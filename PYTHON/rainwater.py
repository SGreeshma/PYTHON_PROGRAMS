# TRAPPING RAIN WATER 

def trap(height):
    n=len(height)
    leftMax=[-1]*n # [-1, -1, -1 until length of arr]
    leftMax[0]=height[0] # as starting there will be no building before 1st building
    for i in range(1, n):
        leftMax[i]=max(leftMax[i-1], height[i]) #height of previous and current
    rightMax=[-1]*n
    rightMax[-1]=height[-1]
    for i in range(n-2, -1, -1):
        rightMax[i]=max(rightMax[i+1], height[i]) #height = current value
    Min=[]
    for i in range(0, n):
        Min.append(min(rightMax[i], leftMax[i])) 
    result=0
    for i in range(0, n):
        result+=Min[i]-height[i]
    return result
height=list(map(int, input().split()))
print(trap(height)) 