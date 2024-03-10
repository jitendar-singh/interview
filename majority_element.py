def findmajorityelement(nums):
    frequency = {}
    print(len(nums))
    for num in nums:
        if num not in frequency.keys():
            frequency[num] = 1
        else:
            frequency[num]+=1
    print(frequency)

    for key, values in frequency.items():
        # print(key,'->',values)
        if values >= (len(nums)//2):
            # print(key)
            return key

nums = [2, 2, 1, 1, 3, 3, 3, 2, 2,3,3,1,1,1,1,1]
print('majority elemenmt is:',findmajorityelement(nums))