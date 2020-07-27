# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # 2. 两数相加
#     # 示例：
#     # 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#     # 输出：7 -> 0 -> 8
#     # 原因：342 + 465 = 807
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         start0 = ListNode(0)  # 初始化链表头节点为0
#         node = start0
#         carry = 0  # 传递进位
#         s = 0
#         while (l1 or l2):
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             # 对应位数字相加并加进位
#             s = val1 + val2 + carry
#             # 更新进位，整除10
#             carry = s // 10
#             val = s % 10
#             node.next = ListNode(val)
#
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#             node = node.next
#
#         # 循环完后检查最后一位是否有进位
#         if carry != 0:
#             node.next = ListNode(1)
#         return start0.next
# ListNode(0)
# Solution().addTwoNumbers(123,1)



# #第二种
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = p = ListNode(None)
#         s = 0
#         while l1 or l2 or s:
#             s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
#             p.next = ListNode(s % 10)
#             p = p.next
#             s //= 10
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next
# ListNode(0)
# c=Solution().addTwoNumbers(ListNode(123),ListNode(5))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
dummy = p = ListNode(None)
print(dir(dummy))