# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 这道题难点是nxt、prev、cur的作用以及相互之间的交换逻辑
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        cur = head
        prev = dummy
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
