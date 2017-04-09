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
    solution = []
    index_count = 0
    other_value = None
    indices = {i:num for i, num in enumerate(nums)}
    while len(solution) < 2:
        item = indices.pop(index_count)
        if item == other_value or target - item in indices.values():
            other_value = target - item 
            solution.append(index_count)
        index_count += 1
    return solution

print twoSum([2, 7, 11, 15], 9)
