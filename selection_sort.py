def select_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr


print(select_sort([10,15,25,3,1,30]))

#time complexity=O(n**2)(there is a nested loop)
#space complexity=O(1)(only one temporary variable is used)