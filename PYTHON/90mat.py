# 22/05/25 : 90 DEGREES MATRIX
'''
# METHOD 1 
# space complexity : O(N**2)
mat=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(mat)
m=len(mat[0])
dupMat=[]
for i in range(n):
    temp=[0]*n # creating duplicate matrix with all 0's
    dupMat.append(temp)
for i in range(0, n):
    for j in range(0, n):
        dupMat[j][n-i-1]=mat[i][j] 
for i in range(0, n):
    for j in range(0, n):
        mat[i][j]=dupMat[i][j] # changing to original matrix
for row in mat: # to print in matrix format
    print(row)
'''

# METHOD 2 - Transpose and reverse 
# space complexity : O(1)
matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(matrix)
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j] 
for i in range(n):
    matrix[i]=matrix[i][::-1]
for row in matrix: # to print in matrix format
    print(row)  