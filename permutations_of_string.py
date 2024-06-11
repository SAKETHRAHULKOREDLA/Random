def perms(strg):
    if len(strg)==1:
        return strg
    permut=[]
    for i in range(len(strg)):
        fix=strg[i]
        gen=strg[:i]+strg[i+1:]
        for j in perms(gen):
            permut.append(fix+j)
    print(len(permut))

    return permut
print(set(perms("rahul")))