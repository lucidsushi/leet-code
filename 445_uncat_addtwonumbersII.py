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
    """
    lsum_root = lsum = ListNode(0)
    carry = 0
    l1s = []
    l2s = []
    lsums = []

    while l1 or l2:
        if l1 and l1.val is not None:
            l1s.append(l1.val)
            l1 = l1.next
        if l2 and l2.val is not None:
            l2s.append(l2.val)
            l2 = l2.next

    while l1s or l2s or carry:
        try:
            val1 = l1s.pop()
        except IndexError:
            val1 = 0
        try:
            val2 = l2s.pop()
        except IndexError:
            val2 = 0
        carry, num = divmod(val1+val2+carry, 10)
        lsums.append(num)

    while True:
        try:
            lsum.next = lsum = ListNode(lsums.pop())
        except IndexError:
            return lsum_root.next
