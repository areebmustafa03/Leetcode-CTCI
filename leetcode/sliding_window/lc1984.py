
"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

LC #1984 - Easy
"""

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        j = 0
        minimum = float("inf")
        while i < len(nums):
            if i + 1 >= k:
                diff = nums[i] - nums[j]
                j += 1
                minimum = min(minimum,diff)
                
            i += 1
        return minimum