# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         #dp[i][j] = true,if s[i] = s[j]
#         #dp[0][len(s)-1]
#         length = len(s)
#         dp = [[0] * length for _ in range(len(s))]
#         res = 0, 0 #长度为1时
#         for i in range(1, length):
#              for j in range(length-i):
#                 if s[j] == s[j+i] and (j+1 >= j+i-1 or dp[j+1][j+i-1]):
#                     dp[j][j+i] = 1
#                     res = j, j+i
#         left, right = res
#         return s[left: right+1]


# class Solution:
#     def extend(self, i, index, n, s):
#         while i >= 1 and index < n - 1:
#             if s[i - 1] == s[index + 1]:
#                 i -= 1
#                 index += 1
#             else:
#                 break
#         return i, index
#
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         i = 0
#         max = 0
#         start = 0
#         end = 0
#         while i < n:
#             index = i
#             while index < n - 1 and s[index] == s[index + 1]:
#                 index += 1
#             a, b = self.extend(i, index, n, s)
#             if b - a + 1 > max:
#                 max = b - a + 1
#                 start = a
#                 end = b
#             i = index + 1
#         return s[start:end + 1]




# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         max_len = 1
#         start = 0
#
#         for i in range(size):
#             dp[i][i] = True
#
#         for j in range(1, size):
#             for i in range(0, j):
#                 if s[i] == s[j]:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = False
#
#                 if dp[i][j]:
#                     cur_len = j - i + 1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start + max_len]
#
#
#
#暴力匹配 （Brute Force）
# class Solution:
#     # 暴力匹配（超时）
#     def longestPalindrome(self, s: str) -> str:
#         # 特判
#         size = len(s)
#         if size < 2:
#             return s
#
#         max_len = 1
#         res = s[0]
#
#         # 枚举所有长度大于等于 2 的子串
#         for i in range(size - 1):
#             for j in range(i + 1, size):
#                 if j - i + 1 > max_len and self.__valid(s, i, j):
#                     max_len = j - i + 1
#                     res = s[i:j + 1]
#         return res
#
#     def __valid(self, s, left, right):
#         # 验证子串 s[left, right] 是否为回文串
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#
#动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

#
# #
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         max_len = 1
#         start = 0
#
#         for i in range(size):
#             dp[i][i] = True
#
#         for j in range(1, size):
#             # 只有下面这一行代码不一样
#             for i in range(j - 1, -1, -1):
#                 if s[i] == s[j]:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = False
#
#                 if dp[i][j]:
#                     cur_len = j - i + 1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start + max_len]
#
# #
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         max_len = 1
#         start = 0
#
#         for j in range(1, size):
#             for i in range(0, j):
#
#                 dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
#
#                 if dp[i][j]:
#                     cur_len = j - i + 1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start + max_len]
#
#
#
#
# #中心扩散法
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         # 至少是 1
#         max_len = 1
#         res = s[0]
#
#         for i in range(size):
#             palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
#             palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
#
#             # 当前找到的最长回文子串
#             cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
#             if len(cur_max_sub) > max_len:
#                 max_len = len(cur_max_sub)
#                 res = cur_max_sub
#
#         return res
#
#     def __center_spread(self, s, size, left, right):
#         """
#         left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
#         right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
#         """
#         i = left
#         j = right
#
#         while i >= 0 and j < size and s[i] == s[j]:
#             i -= 1
#             j += 1
#         return s[i + 1:j], j - i - 1
#
#
#
#
# #Manacher 算法（不用掌握，面试的时候绝大多数情况下不会要求写这个算法，了解思想即可）
# class Solution:
#     # Manacher 算法
#     def longestPalindrome(self, s: str) -> str:
#         # 特判
#         size = len(s)
#         if size < 2:
#             return s
#
#         # 得到预处理字符串
#         t = "#"
#         for i in range(size):
#             t += s[i]
#             t += "#"
#         # 新字符串的长度
#         t_len = 2 * size + 1
#         # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
#         max_len = 1
#         # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
#         start = 0
#
#         for i in range(t_len):
#             cur_len = self.__center_spread(t, i)
#             if cur_len > max_len:
#                 max_len = cur_len
#                 start = (i - max_len) // 2
#         return s[start: start + max_len]
#
#     def __center_spread(self, s, center):
#         size = len(s)
#         i = center - 1
#         j = center + 1
#         step = 0
#         while i >= 0 and j < size and s[i] == s[j]:
#             i -= 1
#             j += 1
#             step += 1
#         return step
#
#
# #
# class Solution:
#     # Manacher 算法
#     def longestPalindrome(self, s: str) -> str:
#         # 特判
#         size = len(s)
#         if size < 2:
#             return s
#
#         # 得到预处理字符串
#         t = "#"
#         for i in range(size):
#             t += s[i]
#             t += "#"
#         # 新字符串的长度
#         t_len = 2 * size + 1
#
#         # 数组 p 记录了扫描过的回文子串的信息
#         p = [0 for _ in range(t_len)]
#
#         # 双指针，它们是一一对应的，须同时更新
#         max_right = 0
#         center = 0
#
#         # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
#         max_len = 1
#         # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
#         start = 1
#
#         for i in range(t_len):
#             if i < max_right:
#                 mirror = 2 * center - i
#                 # 这一行代码是 Manacher 算法的关键所在，要结合图形来理解
#                 p[i] = min(max_right - i, p[mirror])
#
#             # 下一次尝试扩散的左右起点，能扩散的步数直接加到 p[i] 中
#             left = i - (1 + p[i])
#             right = i + (1 + p[i])
#
#             # left >= 0 and right < t_len 保证不越界
#             # t[left] == t[right] 表示可以扩散 1 次
#             while left >= 0 and right < t_len and t[left] == t[right]:
#                 p[i] += 1
#                 left -= 1
#                 right += 1
#
#             # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
#             # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
#             if i + p[i] > max_right:
#                 # max_right 和 center 需要同时更新
#                 max_right = i + p[i]
#                 center = i
#
#             if p[i] > max_len:
#                 # 记录最长回文子串的长度和相应它在原始字符串中的起点
#                 max_len = p[i]
#                 start = (i - max_len) // 2
#         return s[start: start + max_len]