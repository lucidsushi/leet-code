# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexs = []
    for i, v in enumerate(nums):
        num2 = target - v
        numz = nums[:]
        numz.remove(v)
        if num2 in numz:
            indexs.append(i)
            continue
        try:
            if v == nums[indexs[0]]:
                indexs.append(i)
                break
        except IndexError:
            continue
    return indexs

print twoSum([2, 7, 11, 15], 9)
