nums = [5,7,1,72,0,25,0,5,4,65,1,3]

for num in range(len(nums)):
    min_val = min(nums[num:])
    min_index = nums.index(min_val, num)
    nums[num], nums[min_index] = nums[min_index], nums[num]

print(nums)