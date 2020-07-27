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



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for idx, num in enumerate(nums):
#             if target - num in d:
#                 return [d[target - num],idx]
#             else:
#                 d[num] = idx
# u=Solution().twoSum(nums = [11,2,15,7],target = 9)


def twoSum(nums, target):
    hashmap = {}
    for i, value in enumerate(nums):
        diff = target - value
        if diff in hashmap:
            return [hashmap.get(diff), i] # i应该放在后面的位置
        hashmap[value] = i
u=twoSum(nums = [11,2,15,7],target = 9)
print(u)
# 如果hashmap中没有diff值, 则把value作为键/位置索引作为值赋给hashmap(注意位置别颠倒)



#三数之和
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         res = []
#         lennums = len(nums)
#
#         for i in range(lennums):
#             left = i + 1
#             right = lennums - 1
#
#             if i > 0 and nums[i - 1] == nums[i]:
#                 left += 1
#                 continue
#
#             while left < right:
#                 sumthree = nums[i] + nums[left] + nums[right]
#                 if sumthree == 0:
#                     res_col = [nums[i], nums[left], nums[right]]
#                     res.append(res_col)
#                     left += 1
#                     right -= 1
#
#                     while nums[left] == nums[left - 1] and left < right:
#                         left += 1
#                     while nums[right] == nums[right + 1] and left < right:
#                         right -= 1
#
#                 if sumthree < 0:
#                     left += 1
#                 if sumthree > 0:
#                     right -= 1
#         return res