pos = -1 

def linear_search(arr,n):
    global pos
    pos = 0
    i=0
    while i < len(arr):
        if arr[i] == n:
            pos = i
            return True
        i+=1
    return False



arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 50

if linear_search(arr,n):
    print(f"The number {n} is found at index ", pos)
else:
    print(f"The number {n} does not exist in array.")


