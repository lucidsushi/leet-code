# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    
    a, b = c, a
    temp = (c, a)
    a, b = temp
    b gets assigned old a and a is new a
    """
    l1s = []
    l2s = []
    carry = 0
    lsum_head = None

    while l1:
        l1s.append(l1.val)
        l1 = l1.next

    while l2:
        l2s.append(l2.val)
        l2 = l2.next

    while l1s or l2s or carry:
        total = carry
        if l1s:
            total += l1s.pop()
        if l2s:
            total += l2s.pop()
        carry, num = divmod(total, 10)
        lsum_head, lsum_head.next = ListNode(num), lsum_head
    return lsum_head
    
