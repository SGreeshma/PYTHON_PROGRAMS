# INSERTION SORT : Takes an element, places in a perfect position

def insertionSort(arr):
    n=len(arr)
    for i in range(0, n):
        while(i>0 and arr[i-1]>arr[i]): # i>0 coz in order to compare elements there must be atleast 2 elements
            arr[i-1], arr[i]=arr[i], arr[i-1] # swap if they are not in correct order
            i-=1 
            ''' EX: arr = [5, 3, 4]
                Start from i = 0 → nothing to do.
                i = 1 → compare arr[1]=3 with arr[0]=5, since 5 > 3 → swap.
                Now arr = [3, 5, 4], and i becomes 0 due to i -= 1 — so while ends.
                i = 2 → compare arr[2]=4 with arr[1]=5, swap → [3, 4, 5], 
                now i = 1, again compare arr[1]=4 with arr[0]=3, no swap, done '''
    return arr
arr=list(map(int, input().split()))
print(insertionSort(arr))