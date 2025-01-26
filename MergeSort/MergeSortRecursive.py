def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # MergeSort (Recursion)  // Splitting 
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i=0 # index for left arrary
        j=0 # index for right arrary
        k=0 # index for sorted array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        
    return arr


arr=[38,27,43,3,9,82,10]
merge_sort(arr)
print(arr)
