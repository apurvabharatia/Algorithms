#Partition
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        low = ListNode(-1)
        low_copy = low
        high = ListNode(-1)
        high_copy = high

        while head:
            if head.val < x:
                low.next = ListNode(head.val)
                low = low.next
            else:
                high.next = ListNode(head.val)
                high = high.next
            head = head.next
        low_copy2 = low_copy
        while low_copy.next:
            low_copy = low_copy.next
        low_copy.next = high_copy.next
        return low_copy2.next