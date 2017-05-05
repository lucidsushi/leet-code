# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        heads = []
        reverse_root = reverse = ListNode(0)
        while head:
            heads.append(head.val)
            head = head.next
        while heads:
            reverse.next = reverse = ListNode(heads.pop())
        return reverse_root.next
