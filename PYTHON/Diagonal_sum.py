# to find diagonal sum

n=int(input())
m=int(input())
mat=[]
for i in range (n):
    temp=list(map(int,input().split()))
    mat.append(temp)
Sum=0
for i in range (n):
    if(i==i):
        Sum+=mat[i][i]
print(Sum)
