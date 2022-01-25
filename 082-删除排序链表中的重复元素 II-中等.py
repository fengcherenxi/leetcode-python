# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 注意终止条件
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return 
        if not head.next:return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
                pre = pre.next
            else:
                # print(cur.val)
                # print(cur.next.val)
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
                
        return dummy.next
