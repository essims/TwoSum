def twoSum(nums, target):
         for i in range(len(nums)):
            mid = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == mid:
                    return [i,j]
