# https://leetcode.com/problems/add-two-numbers/#/description
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l_sum = None
    l_ret = None
    base = 0
    while True:
        l1_val = 0
        l2_val = 0
        if l1:
            l1_val = l1.val
            l1 = l1.next
        if l2:
            l2_val = l2.val
            l2 = l2.next
        digit = (l1_val + l2_val + base) % 10
        base = (l1_val + l2_val + base)//10
        if not l_sum:
            l_sum = ListNode(digit)
            l_ret = l_sum
        else:
            l_sum.next = ListNode(digit)
            l_sum = l_sum.next
        if not l1 and not l2 and base:
            l_sum.next = ListNode(base)
        if not l1 and not l2:
            break
    return l_ret