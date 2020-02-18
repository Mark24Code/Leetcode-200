# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        x = head
        y = head.next
        while x != None and y != None and y.next != None :
            if x == y:
                return True
            x = x.next
            y = y.next.next
        return False

