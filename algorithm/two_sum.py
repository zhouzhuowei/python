"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.You may assume that
each input would have exactly one solution, and you may not use
the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(length-i-1):
                if (nums[i] + nums[i+j+1]) == target:
                    rtype = [i, i+j+1]
                    return rtype
