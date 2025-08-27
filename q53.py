def maxSubArray(nums):
        summ=0
        maxx=nums[0]
        for i in nums:
            if summ < 0:
                summ = 0
            summ+=i
            maxx=max(summ,maxx)
        return maxx

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
        

