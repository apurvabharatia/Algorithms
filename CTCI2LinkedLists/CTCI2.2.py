#Return kth to last
"""
Implement an algorithm to find the kth to last element of a singly linked list
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        start = head
        end = head
        cnt = 0
        p1 = ListNode(-1)
        p1.next = end
        while cnt < n:
            p1 = p1.next
            end = end.next
            cnt += 1
        prev = ListNode(-1)
        prev.next = head
        if start.next:
            nex = start.next
        if not end:
            return head.next
        while end:
            prev = prev.next
            start = start.next
            nex = nex.next
            end = end.next
        prev.next = nex
        return head


