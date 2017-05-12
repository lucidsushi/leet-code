#https://leetcode.com/problems/reverse-linked-list/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList_recursion(head):
    if not head or not head.next:
        return head
    p = reverseList_(head.next)
    head.next.next = head
    head.next = None
    return p

def reverseList_iteration(head):
    prev = None
    while head:
        next_head, head.next = head.next, prev
        prev = head
        head = next_head
    return prev

class Solution(object):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def reverseList(self, head):
        return reverseList_recursion(head)
        #return reverseList_iteration(head)
