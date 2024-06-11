def add_matrix(a,b):
    x=len(a)
    fin_mat=[]
    for i in range(x):
        mat=[]
        for j in range(x):
            mat.append(a[i][j]+b[i][j])
        fin_mat.append(mat)
    return fin_mat



print(add_matrix([[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]))