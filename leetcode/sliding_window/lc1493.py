

"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

LC # 1493 - Medium
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        i = 0
        j = 0
        maximum = float("-inf")
        while i < len(nums):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                
                if nums[j] == 0:
                    k += 1
                j += 1
            maximum = max(maximum,i-j)
            
            i += 1
        
        return maximum