# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l = 0
        c = head
        while c:
            l += 1
            c = c.next
        if l == n:
            return head.next

        p = head
        for _ in range(l - n - 1):
            p = p.next
        
        p.next = p.next.next
            
        return head
        