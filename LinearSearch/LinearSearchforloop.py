pos = -1

def linear_search(arr,n):
    global pos
    pos = 0

    for i in range(len(arr)-1):
        if arr[i] == n:
            pos = i
            return True
    return False


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 50


if linear_search(arr,n):
    print(f"The value {n} is found at position", pos)
else:
    print(f"Value {n} not it array.")