def twoSum(nums,target):
    dict={}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in dict:
            return [dict[complement],i]
        dict[num] = i
    return []


nums=[3,3]
target=6
print(twoSum(nums,target))
    



