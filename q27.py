# def removeElement(nums, val) :
#         k=0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k+=1
#         return nums,k
# print(removeElement([3,2,2,3],3))

def removeElement(nums, val) :
        for i in range(nums.count(val)):
            nums.remove(val)
        return nums,len(nums)
print(removeElement([3,2,2,3],3))