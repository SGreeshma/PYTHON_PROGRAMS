# SEARCH A 2D MATRIX
def searchMatrix(mat, t):
    n=len(mat)
    m=len(mat[0])
    row=0
    col=m-1
    while(row<n and col>=0):
        if(mat[row][col]==t):
            return True
        elif(mat[row][col]<t): 
            row+=1
        elif(mat[row][col]>t):
            col-=1
    return False