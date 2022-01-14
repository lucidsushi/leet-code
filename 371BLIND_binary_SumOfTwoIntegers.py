'''
https://leetcode.com/problems/sum-of-two-integers/
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''

"""
32 16 8 4 2 1

&	Bitwise AND	x & y         Returns 1 if both the bits are 1 else 0.
|	Bitwise OR	x | y         Returns 1 if either of the bits is 1 else 0.
~	Bitwise NOT	~x            Returns the complement of x.
^	Bitwise XOR	x ^ y         Returns 1 if only one of the bits is 1, else 0.
>>	Bitwise right shift	x>>   Shift x to the right by y positions.
<<	Bitwise left shift	x<<   Shift x to the left by y positions.
"""

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    bit_mask32 = 0xFFFFFFFF
    while b:
        a, b = (a ^ b) & bit_mask32, ((a & b) << 1) & bit_mask32
    print(bin(a))
    print(a)
    return a


assert getSum(-1, -2) == -3
# assert getSum(1, 2) == 3

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is