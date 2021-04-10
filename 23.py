# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dumphead = ListNode(0)
        while head != None:
            pnext = head.next
            head.next = dumphead.next
            dumphead.next = head
            head = pnext
        return dumphead.next

