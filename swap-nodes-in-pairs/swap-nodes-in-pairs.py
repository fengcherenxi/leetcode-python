# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:# 即终止条件链表中没有结点或者只有一个结点
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
        
# 递归方法，终止条件是：链表中没有节点，或者链表中只有一个节点，此时无法进行交换。