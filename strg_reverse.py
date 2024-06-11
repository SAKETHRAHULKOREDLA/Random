def reversing_string(s):
    x=len(s)
    rev_strg=""
    for i in range(x-1,-1,-1):
        rev_strg+=s[i]
    return rev_strg
print(reversing_string("Rahul"))

