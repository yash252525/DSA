# Make a function has_duplicates 

def has_duplicates(nums):
    duplicates =[]

    for num in nums:
        if num in duplicates:
            return True
        duplicates.append(num)  

    return False





nums = [1,2,3,4,5,6,6,7,7,8,9,10]
print(has_duplicates(nums))