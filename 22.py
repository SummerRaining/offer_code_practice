# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        p1,p2 = head,head
        num = 1
        while p1.next != None and num<k:
            p1 = p1.next
            num += 1
        if num<k:
            return None
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2 