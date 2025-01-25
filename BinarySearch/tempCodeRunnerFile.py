def Binary_Search(arr,n,low,high):

    if low <= high :
        midpoint = low+ (high-1) //2

        if arr[midpoint] == n:
             return midpoint
        
        if arr[midpoint] < n:
            Binary_Search(arr,n,low,midpoint-1)
        elif arr[midpoint] > n:
            Binary_Search(arr,n,midpoint+1,high)
    else:
        return 1





arr = [1,2,3,4,5,6,7,8,9,10]
n =9
print(Binary_Search(arr,n,0,len(arr)))

