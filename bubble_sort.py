nums = [5,7,1,72,0,25,0,5,4,65,1,3]

for j in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1],  nums[i]
print(nums)
