# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


def findDuplicates(nums):
    """ given num cannot be largeer than len(nums) and are all positive,
        use them as indexs and mark with unary minus operator """
    nums_duplicate = []
    for num in nums:
        nums[abs(num)-1] *= -1
        if nums[abs(num)-1] > 0:
            nums_duplicate.append(abs(num))
    return nums_duplicate



