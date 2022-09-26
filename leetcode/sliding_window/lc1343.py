
"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
"""
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        i = 0
        j = 0
        res = 0
        total=0
        while i < len(arr):
            total += arr[i]
            if i + 1 >= k:
                avg = total // k
                if avg >= threshold:
                    res += 1
                total -= arr[j]
                j += 1
                    
            i += 1
        
        return res