# https://leetcode.com/problems/reverse-linked-list/#/description

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return reverseList_recursion(head)
        # return reverseList_iteration(head)


# reverse(A B C D E F):
# head = A
# second = head.next = B
# reversed_rest = reverse(second) = F E D C B
# what do we do with B now?
# what do we do with A now?

"""
in the recursive strategy, you save a reference to B as second
and call reverse from B onwards
which gives you back a reference to F
so since you still have a reference to B, you can then do B.next = A
"""

# head = A
# head_next = head.next = B

# head_dummy = head
# second_ = head.next
# return reverse(head_dummy, head, second_)
# def reverse(head):
#     second = head.next
#     if not second:
#         second_.next = head_dummy
#     second.next = head
#     return reverse(second)

# prev = None
# while head:
#     next_head, head.next = head.next, prev
#     prev = head
#     head = next_head
# return prev


# heads = []
# reverse_root = reverse = ListNode(0)
# while head:
#     heads.append(head.val)
#     head = head.next
# while heads:
#     reverse.next = reverse = ListNode(heads.pop())
# return reverse_root.next
