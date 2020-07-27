class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return list(filter(lambda x: cnt[x] == 1, cnt))