def Binary_search(arr,n):
    global midpoint
    i=0
    j = len(arr) -1 
    while i <= j :
        midpoint = (i+j)//2

        if arr[midpoint] == n:
            return midpoint
        elif arr[midpoint] < n:
            i = midpoint + 1 
        else:
            j = midpoint - 1
    return False


arr = [1,2,3,4,5,6,7,8,9,10]
n =9

if Binary_search(arr,n):
    print(f"Value {n} found at ", midpoint)
else:
    print(f"Value {n} not found")


