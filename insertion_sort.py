def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
#Time Complexity: O(N^2) 
#Auxiliary Space: O(1)

print(insertion_sort([10,15,25,3,1,30]))