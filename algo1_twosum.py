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
    index_count = len(nums)
    first_solution = None
    while len(indexs) < 2:
        index_count -= 1
        last_num = nums.pop()
        target_element = target - last_num
        if target_element == first_solution:
            indexs.append(index_count)
        elif target_element in nums:
            first_solution = last_num
            indexs.append(index_count)
    return indexs

print twoSum([2, 7, 11, 15], 9)
