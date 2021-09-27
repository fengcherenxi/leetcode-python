# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        x = None
        for y in lists:
            x = self.merge(x, y)
        return x
    def merge(self,a:ListNode,b:ListNode):
        prehead=ListNode(-1)
        prev=prehead
        while a and b:
            if a.val < b.val:
                prev.next=a
                a=a.next
            else:
                prev.next=b
                b=b.next
            prev=prev.next
        prev.next= a if a is not None else b
        return prehead.next