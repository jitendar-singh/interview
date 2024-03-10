def binary_search(nums, key):
    low = 0
    high = len(nums) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == nums[mid]:
            found = True
        elif key > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return found
        

numbers = [1,2,5,6,10,12,55,75,78,79,89,93,95,99]
key = int(input("Enter key:"))
result = binary_search(numbers, key)
print(result)