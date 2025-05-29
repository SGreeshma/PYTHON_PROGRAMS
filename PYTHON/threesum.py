def threeSum(arr, target):
    n = len(arr)
    
    for i in range(n): 
        ele = {}  
        for j in range(i + 1, n):  
            rest = target - (arr[i] + arr[j])  
            if rest in ele:  
                return [ele[rest], i, j]       
            ele[arr[j]] = j  
    return []  
arr=list(map(int,input().split()))
target=int(input())
result = threeSum(arr, target)
print(result)
