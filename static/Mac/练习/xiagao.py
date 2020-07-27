# class Solution:
# 	def twoSum(self,nums,target):
# 		d = {}
# 		n = len(nums)
# 		for x in range(n):
# 			if target - nums[x] in d:
# 				return d[target-nums[x]],x
# 			else:
# 				d[nums[x]] = x
#
# u=Solution().twoSum(nums = [11,2,15,7],target = 9)
# #a=u.twoSum(nums = [11,2,15,7],target = 9)
# print(u)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target - num],idx]
            else:
                d[num] = idx
u=Solution().twoSum(nums = [11,2,15,7],target = 9)