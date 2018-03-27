# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# mchen style
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    _map = {}
    for i, n in enumerate(nums):
        try:
            return [_map[target-n], i]
        except:
            _map[n] = i


# slowest method thought of
def addtwo(nums, target):
    i_to_try = 0
    while i_to_try < len(nums):
        for i, v in enumerate(nums):
            if nums[i_to_try] + v == target and i_to_try != i:
                return i_to_try, i
        i_to_try += 1


# first realization of O(n)
def addtwo(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        if (target-num) in nums_dict and nums_dict[target-num] != index:
            return (index, nums_dict[target-num])
        else:
            nums_dict[num] = index


# rejection until match exist with less conditional checking
def addtwo(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        try:
            return index, nums_dict[target-num]
        except KeyError:
            nums_dict[num] = index


# print twoSum([2, 3, 4], 6)
# print twoSum([3, 3], 6)
# print twoSum([2, 7, 11, 15], 9)
