# MATRIX DIAGONAL SUM (PRIMARY AND SECONDARY DIAGONAL SUM)
def diagonalSum(mat):
    n = len(mat)
    Sum = 0
    for i in range(n):
        Sum += mat[i][i]   # Primary diagonal
        if i != n - 1 - i:
            Sum += mat[i][n - 1 - i]  # Subtract center element once (if counted twice)
    return Sum
