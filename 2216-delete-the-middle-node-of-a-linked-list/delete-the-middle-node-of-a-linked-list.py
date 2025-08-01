# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head

        
        