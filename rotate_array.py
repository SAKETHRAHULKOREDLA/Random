def rotate_arr(arr,x):
    y=len(arr)
    arr=arr[::-1]
    return arr[(y-x)-1::-1]+arr[:(y-x)-1:-1]
print(rotate_arr([1,2,3,4,5,6,7,8],4))