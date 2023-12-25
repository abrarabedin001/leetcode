# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        newHead = None
        while current!=None:
            temp = current.next
            current.next = newHead
            newHead = current
            current = temp
        return newHead