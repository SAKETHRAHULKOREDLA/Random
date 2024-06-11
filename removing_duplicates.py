def removing_duplicates(strg):
    count={}
    for i in strg:
        if i not in count:
            count[i]=0
        else:
            count[i]+=1

    final_strg=""
    for i in count:
        if count[i]>1:
            continue
        else:
            final_strg+=i
    return final_strg

print(removing_duplicates("geeksforgeeksG"))