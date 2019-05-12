# Definition for singly-linked list.

#Sum of lists

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        res_copy = res
        carry = 0
        while l1 and l2:
            res.next = ListNode((l1.val + l2.val + carry)%10)
            res = res.next
            carry = (l1.val + l2.val + carry)/10
            l1 = l1.next
            l2 = l2.next
        if not l1:
                while l2:
                    res.next = ListNode(( l2.val + carry)%10)
                    res = res.next
                    carry = (l2.val + carry)/10
                    l2 = l2.next
        if not l2:
                while l1:
                    res.next = ListNode(( l1.val + carry)%10)
                    res = res.next
                    carry = (l1.val + carry)/10
                    l1 = l1.next
        if carry != 0:
            res.next = ListNode(carry)
        return res_copy.next