# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return None

        if head.val == val:
            tmp = head.next
            del head
            return tmp
            
        pnode = head
        pnext = head.next
        while pnext!=None and pnext.val != val:
            pnext = pnext.next
            pnode = pnode.next
        if pnext==None:
            return head
        pnode.next = pnext.next
        del pnext
        return head