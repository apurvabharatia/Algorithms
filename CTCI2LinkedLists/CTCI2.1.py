#Remove Dups

"""
Write code to remove duplicates from an unsorted linked list.

FOLLOW UP: How would you solve this if a temporary buffer is not allowed?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_copy = head
        if not head:
            return head
        if head.next is None:
            return head
        diff = head.next
        while head and diff:
            while head.val == diff.val:
                if diff.next:
                    diff = diff.next
                else:
                    head.next = None
                    return head_copy
                    break
            head.next = diff
            head = diff
            diff = diff.next

        return head_copy