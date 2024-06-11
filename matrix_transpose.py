def matrix_transpose(mat):
    x=len(mat)
    for i in range(x):
        for j in range(x):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return mat
print(matrix_transpose([[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]))