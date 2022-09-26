

"""

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i =0
        j = 0
        maximum = float("-inf")
        while i < len(nums):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[j] == 0:
                    k += 1
                j += 1
            maximum = max(maximum,i-j+1)
            
            i += 1
        return maximum