# QUICK SORT 
# we consider pivot element and compare with the low and high elements

def qs(arr, low, high):
    if(low<high): # BASE CONDITION : low pointer should not exceed the high pointer, it should always be less
        pIndex=partition(arr, low, high) # the perfect position of pivot is considered as partition point and its index is called partition index
        qs(arr, low, pIndex-1) # 1st part after the we get partition point where pivot element as fixed its position
        qs(arr, pIndex+1, high) # 2nd part 
def partition(arr, low, high):
    i=low 
    j=high
    pivot=arr[low] # initially we consider pivot at low, pivot can be consider anywhere either low, high or mid can be any element  but in simple we can consider low element
    while(i<j): # i pointer shouldn't exceed j pointer
        while(arr[i]<=pivot and i<high): # the i pointer elements should be greater than pivot, if they are less skip those elements and i should not go out of bound
            i+=1 # when i pointer is less than pivot we skip
        while(arr[j]>=pivot and j>low): # j pointer elements should be less than pivot, if they are big skip those elements andj should not go out bound
            j-=1 # when j pointer is big than pivot we skip, we took j-=1 coz j is at last position we have to move last to first 
        if(i<j):
            arr[i], arr[j]=arr[j], arr[i] # swap the i,j if i>pivot and j<pivot 
    arr[low], arr[j]=arr[j], arr[low] # else swap swap j, pivot if j exceeds i                 
    return j
arr=list(map(int, input().split()))
qs(arr, 0, len(arr)-1)
print(arr)