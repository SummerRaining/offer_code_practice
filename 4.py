# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head!=None:
            result = []
            self.helper(head,result)
            return result
    def helper(self,head,result):
        if head.next != None:
            helper(head.next,result)
        result.append(head.val)