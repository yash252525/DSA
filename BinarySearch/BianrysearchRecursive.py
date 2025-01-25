def Binary_Search(arr,n,low,high):

    if low <= high :
        midpoint = low+ (high-low) // 2

        if arr[midpoint] == n:
             return midpoint
        
        if arr[midpoint] < n:
           return Binary_Search(arr,n,midpoint+1,high)
        elif arr[midpoint] > n:
           return Binary_Search(arr,n,low, midpoint-1)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
n =9 
answer = Binary_Search(arr,n,0,len(arr)-1)
if answer !=  -1:
    print("Element found")
else:
    print('Element not found')

