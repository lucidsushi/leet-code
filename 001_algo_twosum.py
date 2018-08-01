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


# using while loop
def twoSum(nums, target):
    i1 = 0
    while i1 < len(nums):
        for i2 in range(i1 + 1, len(nums)):
            if nums[i1] + nums[i2] == target:
                return i1, i2
        i1 += 1


# using two for loops instead  o(n^2)
def twoSum(nums, target):
    nums_size = len(nums)
    for i in range(nums_size - 1):
        for j in range(i+1, nums_size):
            if nums[i] + nums[j] == target:
                return i, j


# first realization of O(n)
def twoSum(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        counter_part = target - num
        if counter_part in nums_dict:
            return (index, nums_dict[counter_part])
        else:
            nums_dict[num] = index


# rejection until match exist with less conditional checking
def twoSum(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        try:
            return index, nums_dict[target-num]
        except KeyError:
            nums_dict[num] = index


# jake's mention of using sorted list, O(n log n)? . that doesn't work yet.
def twoSum(nums, target):
    nums = sorted(nums)  # this messed up the indices though
    index_small = 0
    index_big = len(nums) - 1

    # move towards answer from both sides
    for _ in range(index_big):
        result = nums[index_small] + nums[index_big]
        if result > target:
            index_big -= 1

        elif result < target:
            index_small += 1

        else:
            return (index_small, index_big)


# print twoSum([3, 2, 4], 6)
# print twoSum([3, 3], 6)
# print twoSum([2, 7, 11, 15], 9)
