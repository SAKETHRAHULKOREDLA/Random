def armstrong_number(x):
    val=0
    for i in str(x):
        val+=int(i)**3
    print(val)
    if val==x:
        return "Armstrong number"
    else:
        return "Not a Armstrong number"
print(armstrong_number(372))