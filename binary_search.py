def bin_search(arr,x):
    i=0
    j=len(arr)-1
    m=(i+j)//2
    print(m)
    while i<j:
        m=(i+j)//2

        if arr[m]<x:
            i=m+1
        elif arr[m]>x:
            j=m-1

        else:
            return m
            
    return -1

print(bin_search([1,2,3,4,5,6,7,8,9,10,11],10))