# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = None
        current = None
        while(l1 != None and l2 != None):
            tmp = ListNode()
            if l1.val <= l2.val:
                tmp.val = l1.val
                l1 = l1.next
            else:
                tmp.val = l2.val
                l2 = l2.next
            tmp.next = None
            if r == None:
                r = tmp
                current = r
            else:
                current.next = tmp
                current = tmp
        
        while(l1 != None):
            tmp = ListNode()
            tmp.val = l1.val
            tmp.next = None
            if r == None:
                r = tmp
                current = r
            else:
                current.next = tmp
                current = tmp
            l1 = l1.next
            
        while(l2 != None):
            tmp = ListNode()
            tmp.val = l2.val
            tmp.next = None
            if r == None:
                r = tmp
                current = r
            else:
                current.next = tmp
                current = tmp
            l2 = l2.next
        return r
