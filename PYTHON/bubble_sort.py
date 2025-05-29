# BUBBLE SORT : We consider greater elements and move to end position by adjacency swap

def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1, -1, -1): # as bigger elements should be last position we consider from n-1 
        for j in range(i):
            if (arr[j]>arr[j+1]): 
                arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr
arr=list(map(int, input().split()))
print(bubbleSort(arr))