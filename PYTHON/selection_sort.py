# SELECTION SORT : select minimum element and swap by placing at start position 

def selectionSort(arr):
    n=len(arr)
    for i in range(0, n): 
        Min=i # min = minimum index
        for j in range(i+1, n): 
            if(arr[j]<arr[Min]): # checking the min elements
                Min=j # if condition true then update min with j
        arr[i], arr[Min]=arr[Min], arr[i] # swap the elements 
    return arr 
arr=list(map(int, input().split()))
print(selectionSort(arr))