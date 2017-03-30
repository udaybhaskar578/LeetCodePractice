'''
Author: Sai Uday Bhaskar Mudivarty
Question: https://leetcode.com/problems/add-two-numbers
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)
        carry=0 
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            carry,val = divmod(carry,10)
            n.next = ListNode(val)
            n = n.next
        return root.next
        


        


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        isRoot = True
        carry=0 
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            carry,val = divmod(carry,10)
            
            if isRoot:
                root = n = ListNode(val)
                isRoot =False
                continue
            else:
                n.next = n = ListNode(val)
                print(n.val)
        
        return root
        