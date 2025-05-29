# ISLANDS

def dfs(i, j, visited, grid, n, m):
    visited[i][j]=1
    for r, c in [[-1, 0], [0, 1], [1, 0], [0, -1]]: #for top, right, bottom, down
        nRow=i+r
        nCol=j+c
        if(nRow>=0 and nRow<n and nCol>=0 and nCol<m and grid[nRow][nCol]==1 and visited[nRow][nCol]==0):
            dfs(nRow, nCol, visited, grid, n, m)
def numIl(grid):
    n=len(grid) #row
    m=len(grid[0]) #column
    visited=[]
    for i in range(n):
        lst=[0]*m
        visited.append(lst)
    c=0
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==1 and visited[i][j]==0):
                dfs(i, j, visited, grid, n, m)
                c+=1
    return c
grid=[[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
print(numIl(grid))