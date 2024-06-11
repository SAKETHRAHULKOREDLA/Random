def merge_sort(arr,left,mid,right):
    sub_arr_one=mid-left+1
    sub_arr_two=right-mid

    left_arr=[0]*sub_arr_one
    right_arr=[0]*sub_arr_two

    for a in range(sub_arr_one):
        left_arr[a]=arr[a+left]
    for b in range(sub_arr_two):
        right_arr[b]=arr[mid+b+1]

    i=0
    j=0
    k=left
    while i<sub_arr_one and j<sub_arr_two:
        if left_arr[i]<=right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
        k+=1
    

    while i<sub_arr_one:
        arr[k]=left_arr[i]
        i+=1
        k+=1
    while j<sub_arr_two:
        arr[k]=right_arr[j]
        j+=1
        k+=1
    
def merge_sort_2(arr,begin,end):
    if begin>=end:
        return

    mid=begin+(end-begin)//2
    merge_sort_2(arr,begin,mid)
    merge_sort_2(arr,mid+1,end)
    merge_sort(arr,begin,mid,end)

    return arr



print(merge_sort_2([10,15,25,3,1,30],0,len([10,15,25,3,1,30])-1))
