def bubble_sort(arr):
    for i in range(len(arr)):
        swap=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=True
        if swap==False:
            break
    return arr
print(bubble_sort([10,15,25,3,1,30,6]))

#time complexity=O(n**2)(there is a nested loop)
#space complexity=O(1)(only one temporary variable is used)