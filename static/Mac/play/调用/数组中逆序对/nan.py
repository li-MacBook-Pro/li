from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        res = 0
        for i in range(0, size - 1):
            for j in range(i + 1, size):
                if nums[i] > nums[j]:
                    res += 1
        return res

# 后有序数组中元素出列的时候，计算逆序个数
from typing import List
# class Solution:
#
#     def reversePairs(self, nums: List[int]) -> int:
#         size = len(nums)
#         if size < 2:
#             return 0
#
#         # 用于归并的辅助数组
#         temp = [0 for _ in range(size)]
#         return self.count_reverse_pairs(nums, 0, size - 1, temp)
#
#     def count_reverse_pairs(self, nums, left, right, temp):
#         # 在数组 nums 的区间 [left, right] 统计逆序对
#         if left == right:
#             return 0
#         mid = (left + right) >> 1
#         left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
#         right_pairs = self.count_reverse_pairs(nums, mid + 1, right, temp)
#
#         reverse_pairs = left_pairs + right_pairs
#         # 代码走到这里的时候，[left, mid] 和 [mid + 1, right] 已经完成了排序并且计算好逆序对
#
#         if nums[mid] <= nums[mid + 1]:
#             # 此时不用计算横跨两个区间的逆序对，直接返回 reverse_pairs
#             return reverse_pairs
#
#         reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
#         return reverse_pairs + reverse_cross_pairs
#
#     def merge_and_count(self, nums, left, mid, right, temp):
#         """
#         [left, mid] 有序，[mid + 1, right] 有序
#
#         前：[2, 3, 5, 8]，后：[4, 6, 7, 12]
#         只在后面数组元素出列的时候，数一数前面这个数组还剩下多少个数字，
#         由于"前"数组和"后"数组都有序，
#         此时"前"数组剩下的元素个数 mid - i + 1 就是与"后"数组元素出列的这个元素构成的逆序对个数
#
#         """
#         for i in range(left, right + 1):
#             temp[i] = nums[i]
#
#         i = left
#         j = mid + 1
#         res = 0
#         for k in range(left, right + 1):
#             if i > mid:
#                 nums[k] = temp[j]
#                 j += 1
#             elif j > right:
#                 nums[k] = temp[i]
#                 i += 1
#             elif temp[i] <= temp[j]:
#                 # 此时前数组元素出列，不统计逆序对
#                 nums[k] = temp[i]
#                 i += 1
#             else:
#                 # assert temp[i] > temp[j]
#                 # 此时后数组元素出列，统计逆序对，快就快在这里，一次可以统计出一个区间的个数的逆序对
#                 nums[k] = temp[j]
#                 j += 1
#                 # 例：[7, 8, 9][4, 6, 9]，4 与 7 以及 7 后面所有的数都构成逆序对
#                 res += (mid - i + 1)
#         return res


# 前有序数组中元素出列的时候，计算逆序个数
from typing import List
# class Solution:
#
#     def reversePairs(self, nums: List[int]) -> int:
#         size = len(nums)
#         if size < 2:
#             return 0
#
#         temp = [0 for _ in range(size)]
#         return self.reverse_pairs(nums, 0, size - 1, temp)
#
#     def reverse_pairs(self, nums, left, right, temp):
#         """
#         在数组 nums 的区间 [l,r] 统计逆序对
#         :param nums:
#         :param left: 待统计数组的左边界，可以取到
#         :param right: 待统计数组的右边界，可以取到
#         :param temp:
#         :return:
#         """
#         if left == right:
#             return 0
#         mid = (left + right) >> 1
#         left_pairs = self.reverse_pairs(nums, left, mid, temp)
#         right_pairs = self.reverse_pairs(nums, mid + 1, right, temp)
#
#         reverse_pairs = left_pairs + right_pairs
#         if nums[mid] <= nums[mid + 1]:
#             return reverse_pairs
#
#         reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
#         return reverse_pairs + reverse_cross_pairs
#
#     def merge_and_count(self, nums, left, mid, right, temp):
#         """
#         [left, mid] 有序，[mid + 1, right] 有序
#
#         前：[2, 3, 5, 8]，后：[4, 6, 7, 12]
#         我们只需要在后面数组元素出列的时候，数一数前面这个数组还剩下多少个数字，
#         因为"前"数组和"后"数组都有序，
#         因此，"前"数组剩下的元素个数 mid - i + 1 就是与"后"数组元素出列的这个元素构成的逆序对个数
#
#         """
#         for i in range(left, right + 1):
#             temp[i] = nums[i]
#
#         i = left
#         j = mid + 1
#
#         res = 0
#         for k in range(left, right + 1):
#             if i > mid:
#                 nums[k] = temp[j]
#                 j += 1
#             elif j > right:
#                 nums[k] = temp[i]
#                 i += 1
#
#                 res += (right - mid)
#             elif temp[i] <= temp[j]:
#                 nums[k] = temp[i]
#                 i += 1
#
#                 res += (j - mid - 1)
#             else:
#                 assert temp[i] > temp[j]
#                 nums[k] = temp[j]
#                 j += 1
#         return res


from typing import List
# class Solution:
#
#     def reversePairs(self, nums: List[int]) -> int:
#
#         class FenwickTree:
#             def __init__(self, n):
#                 self.size = n
#                 self.tree = [0 for _ in range(n + 1)]
#
#             def __lowbit(self, index):
#                 return index & (-index)
#
#             # 单点更新：从下到上，最多到 len，可以取等
#             def update(self, index, delta):
#                 while index <= self.size:
#                     self.tree[index] += delta
#                     index += self.__lowbit(index)
#
#             # 区间查询：从上到下，最少到 1，可以取等
#             def query(self, index):
#                 res = 0
#                 while index > 0:
#                     res += self.tree[index]
#                     index -= self.__lowbit(index)
#                 return res
#
#         # 特判
#         size = len(nums)
#         if size < 2:
#             return 0
#
#         # 原始数组去除重复以后从小到大排序，这一步叫做离散化
#         s = list(set(nums))
#
#         # 构建最小堆，因为从小到大一个一个拿出来，用堆比较合适
#         import heapq
#         heapq.heapify(s)
#
#         # 由数字查排名
#         rank_map = dict()
#         rank = 1
#         # 不重复数字的个数
#         rank_map_size = len(s)
#         for _ in range(rank_map_size):
#             num = heapq.heappop(s)
#             rank_map[num] = rank
#             rank += 1
#
#         res = 0
#         # 树状数组只要不重复数字个数这么多空间就够了
#         ft = FenwickTree(rank_map_size)
#
#         # 从后向前看，拿出一个数字来，就更新一下，然后向前查询比它小的个数
#         for i in range(size - 1, -1, -1):
#             rank = rank_map[nums[i]]
#             ft.update(rank, 1)
#             res += ft.query(rank - 1)
#         return res