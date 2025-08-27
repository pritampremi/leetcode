#Number of good pairs

nums=[1,2,3,1,1,3]
goodpairs=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            goodpairs+=1
print(goodpairs)





