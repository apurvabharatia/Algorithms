#Delete middle Node

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(arr):
        head = ListNode(arr[0])
        head_copy = head
        for index in range(1, len(arr)):
            head.next = ListNode(arr[index])
            head = head.next
        #printVals(head_copy)
        return head_copy

def printVals(head):
        while head:
            print (head.val)
            head = head.next

def deleteMiddleNode():
        arr = [1,2,3,4,5,6]
        head = createLinkedList(arr)
        head_copy = head
        slow = head
        fast = head
        prev = ListNode(-1)
        prev.next = slow
        nex = slow.next
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            nex = nex.next
            fast = fast.next.next
        prev.next = nex
        printVals(head_copy)

deleteMiddleNode()
