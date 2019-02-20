# https://leetcode.com/problems/add-two-numbers/#/description
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8



# Definition for singly-linked list.
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


# Did it again in 2019 but looks pretty much the same as previous attempt
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l0 = ListNode(None)
    next_previous_node = None
    carry = 0

    while l1 or l2:

        if not next_previous_node:
            next_previous_node, carry, l1, l2 = add_one_digit(l0, l1, l2, carry)
        else:
            next_previous_node, carry, l1, l2 = add_one_digit(next_previous_node, l1, l2, carry)

    if carry:
      next_previous_node.next = ListNode(carry)

    return l0.next

def add_one_digit(previous_node, l1, l2, carry):
    """Add a digit of l1 and l1 and return the newly linked node location representing the sum"""

    if l1:
      l1_val = l1.val
      l1 = l1.next
    else:
      l1_val = 0
    
    if l2:
      l2_val = l2.val
      l2 = l2.next
    else:
      l2_val = 0

    sum_total = l1_val + l2_val + carry
    sum_digit = sum_total % 10
    sum_carry = sum_total // 10
    previous_node.next = ListNode(sum_digit)

    return previous_node.next, sum_carry, l1, l2


# l1 = ListNode(1)
# l1.next = ListNode(8)

# l2 = ListNode(0)

# result = addTwoNumbers(l1, l2)

# print result.val
# print result.next.val
